#!/usr/bin/env python3
import argparse
import json
import os
import requests
import sys
from getpass import getpass
from datetime import datetime

DEFAULT_BASE_URL = "https://last.leadgenius.app"
AUTH_FILE = os.path.expanduser("~/.leadgenius_auth.json")

class LeadGeniusCLI:
    def __init__(self, base_url=None):
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip('/')
        self.token = self._load_token()

    def _load_token(self):
        # 1. Prefer Environment Variable (API Key)
        api_key = os.environ.get("LGP_API_KEY")
        if api_key:
            return api_key
            
        # 2. Check Auth File
        if os.path.exists(AUTH_FILE):
            try:
                with open(AUTH_FILE, "r") as f:
                    data = json.load(f)
                    # Prefer API Key if stored (future proofing), else JWT
                    return data.get("api_key") or data.get("token")
            except:
                pass
        return None

    def _request(self, method, endpoint, data=None, params=None):
        if not self.token:
            print("Error: Not authenticated. Set LGP_API_KEY or run 'lgp auth'.")
            sys.exit(1)

        url = f"{self.base_url}/api/{endpoint.lstrip('/')}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        # If token is JWT (long), it might need different handling if backend strict about X-API-Key vs Bearer
        # Current backend implementation expects X-API-Key to be the API Key (lgp_...).
        # If user is using JWT (from lgp auth), `validateApiKey` will fail because it expects a hashable key.
        #
        # CRITICAL: `validateApiKey` in backend expects an API Key, NOT a JWT.
        # So `lgp auth` (which gets JWT) is now ONLY useful for generating an API Key.
        # Operations referencing `api/agent/*` now REQUIRE an API Key.
        #
        # Exception: `generate-key` endpoint itself must be accessible via JWT.
        
        try:
            response = requests.request(method, url, headers=headers, json=data, params=params)
            if response.status_code == 401 or response.status_code == 403:
                print(f"Auth Error ({response.status_code}): {response.text}")
                print("Make sure LGP_API_KEY is set to a valid API Key.")
                return None
            if response.status_code >= 400:
                print(f"Error ({response.status_code}): {response.text}")
                return None
            return response.json()
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

    def auth(self, email=None, password=None):
        email = email or input("Email: ")
        password = password or getpass("Password: ")
        
        url = f"{self.base_url}/api/auth"
        try:
            response = requests.post(url, json={"username": email, "password": password})
            if response.status_code == 200:
                data = response.json()
                tokens = data.get("tokens", {})
                jwt_token = tokens.get("accessToken") or data.get("jwt_token")
                # But wait, we want to encourage API Keys.
                # We save JWT strictly to allow `generate-key` to work next.
                with open(AUTH_FILE, "w") as f:
                    json.dump({"token": jwt_token, "email": email, "base_url": self.base_url}, f)
                print(f"Successfully authenticated as {email}")
                print("IMPORTANT: Most commands now require an API Key.")
                print("Run 'lgp generate-key' to create one.")
            else:
                print(f"Auth Failed: {response.text}")
        except Exception as e:
            print(f"Auth Error: {e}")

    def generate_key(self, name=None, description=None):
        # This requires JWT token (from auth), not API Key.
        # We need to manually load JWT from file because self.token might be empty or API Key.
        jwt_token = None
        if os.path.exists(AUTH_FILE):
             try:
                with open(AUTH_FILE, "r") as f:
                    data = json.load(f)
                    jwt_token = data.get("token")
             except:
                 pass
        
        if not jwt_token:
            print("Error: You must run 'lgp auth' first to generate a key.")
            return

        url = f"{self.base_url}/api/agent-api-keys"
        headers = {
            "Authorization": f"Bearer {jwt_token}", # Standard Bearer for this endpoint
            "Content-Type": "application/json"
        }
        payload = {
            "name": name or f"CLI Key {datetime.now().isoformat()}",
            "description": description or "Generated via lgp CLI"
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                api_key = data.get("apiKey")
                print("\nSUCCESS: API Key Generated!")
                print(f"Key: {api_key}")
                print("\nTo use this key:")
                print(f"export LGP_API_KEY={api_key}")
                print("\n(You should save this key securely, it will not be shown again)")
                
                # Optional: Save to file for convenience?
                # Best practice: User sets env var. But for UX, we can save it.
                # Let's verify if user wants to save it? No interactive prompt defined in requirements.
                # Let's save it to auth file as 'api_key' to allow immediate usage without export.
                if os.path.exists(AUTH_FILE):
                    with open(AUTH_FILE, "r+") as f:
                        file_data = json.load(f)
                        file_data["api_key"] = api_key
                        f.seek(0)
                        json.dump(file_data, f)
                        f.truncate()
                else:
                     with open(AUTH_FILE, "w") as f:
                        json.dump({"api_key": api_key}, f)
                print("Key has been saved to ~/.leadgenius_auth.json for immediate use.")

            else:
                print(f"Failed to generate key: ({response.status_code}) {response.text}")
        except Exception as e:
            print(f"Error: {e}")

    # Leads
    def list_leads(self, limit=20):
        data = self._request("GET", "leads", params={"pageSize": limit})
        if data:
            print(json.dumps(data, indent=2))

    def find_lead(self, first_name=None, last_name=None, full_name=None, email=None, company=None):
        params = {"pageSize": 100}
        if first_name:
            params["firstName"] = first_name
        if last_name:
            params["lastName"] = last_name
        if full_name:
            params["fullName"] = full_name
        if email:
            params["email"] = email
        if company:
            params["companyName"] = company
        data = self._request("GET", "leads", params=params)
        if data:
            leads = data.get("data", [])
            if not leads:
                print("No leads found matching criteria.")
                return
            print(f"Found {len(leads)} lead(s):\n")
            for lead in leads:
                print(f"  ID:       {lead.get('id')}")
                print(f"  Name:     {lead.get('fullName') or lead.get('contactName', 'N/A')}")
                print(f"  Title:    {lead.get('title', 'N/A')}")
                print(f"  Company:  {lead.get('companyName', 'N/A')}")
                print(f"  Email:    {lead.get('email', 'N/A')}")
                print(f"  LinkedIn: {lead.get('linkedinUrl', 'N/A')}")
                print(f"  Location: {lead.get('city', 'N/A')}, {lead.get('country', 'N/A')}")
                print(f"  Status:   {lead.get('status', 'N/A')}")
                print()

    def enrich_leads(self, lead_ids, type="technographic"):
        payload = {"leadIds": lead_ids, "enrichmentType": type}
        data = self._request("POST", "enrichment/trigger", data=payload)
        if data:
            print(f"Enrichment triggered: Job ID {data.get('jobId')}")

    # Campaigns
    def list_campaigns(self):
        data = self._request("GET", "campaigns")
        if data:
            for c in data.get("campaigns", []):
                print(f"[{c.get('id')}] {c.get('name')} ({c.get('status')})")

    def create_campaign(self, name, type="abm"):
        payload = {"name": name, "campaignType": type, "status": "active"}
        data = self._request("POST", "campaigns", data=payload)
        if data:
            print(f"Campaign created: {data.get('id')}")

    # Analytics
    def show_pipeline(self, start_date=None, end_date=None):
        params = {"startDate": start_date, "endDate": end_date}
        data = self._request("GET", "analytics/pipeline", params=params)
        if data:
            print("--- Pipeline Metrics ---")
            print(json.dumps(data, indent=2))

    # Maintenance
    def list_bugs(self):
        data = self._request("GET", "maintenance/bugs")
        if data:
            print(json.dumps(data, indent=2))

    def report_bug(self, description, email=None):
        payload = {"description": description, "userEmail": email}
        data = self._request("POST", "maintenance/bugs", data=payload)
        if data:
             # Handle structure { bug: {...} }
             bug = data.get('bug', {})
             print(f"Bug reported: ID {bug.get('id')}")

    def list_enhancements(self):
        data = self._request("GET", "maintenance/enhancements")
        if data:
            print(json.dumps(data, indent=2))

    def request_enhancement(self, description, email=None):
        payload = {"description": description, "userEmail": email}
        data = self._request("POST", "maintenance/enhancements", data=payload)
        if data:
             # Handle structure { enhancement: {...} }
             enh = data.get('enhancement', {})
             print(f"Enhancement requested: ID {enh.get('id')}")
    
    # Admin
    def list_all_companies(self):
         # Admin endpoint call attempt
        print("Warning: Admin endpoints require session cookies. This might fail with API Key.")
        url = f"{self.base_url}/api/admin/companies"
        headers = {
            "Content-Type": "application/json",
             # Try passing API Key anyway, maybe backend changes later
            "X-API-Key": self.token
        }
        try:
             response = requests.get(url, headers=headers)
             print(f"Status: {response.status_code}")
             print(response.text)
        except Exception as e:
            print(f"Error: {e}")

    def list_all_users(self):
        print("Warning: Admin endpoints require session cookies. This might fail with API Key.")
        url = f"{self.base_url}/api/admin/users"
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.token
        }
        try:
             response = requests.get(url, headers=headers)
             print(f"Status: {response.status_code}")
             print(response.text)
        except Exception as e:
            print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="LeadGenius Pro Agent CLI")
    parser.add_argument("--base-url", help="Override base URL")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Auth
    auth_parser = subparsers.add_parser("auth", help="Authenticate (Login)")
    auth_parser.add_argument("--email", help="Account email")
    
    # Generate Key
    gen_key_parser = subparsers.add_parser("generate-key", help="Generate a new API Key")
    gen_key_parser.add_argument("--name", help="Name for the key")
    gen_key_parser.add_argument("--desc", help="Description for the key")

    # Leads
    leads_parser = subparsers.add_parser("leads", help="Manage leads")
    leads_parser.add_argument("action", choices=["list", "find", "enrich"])
    leads_parser.add_argument("--ids", nargs="+", help="Lead IDs for enrichment")
    leads_parser.add_argument("--first-name", help="First name filter (for find)")
    leads_parser.add_argument("--last-name", help="Last name filter (for find)")
    leads_parser.add_argument("--full-name", help="Full name search (for find)")
    leads_parser.add_argument("--email", help="Email filter (for find)")
    leads_parser.add_argument("--company", help="Company name filter (for find)")

    # Campaigns
    camp_parser = subparsers.add_parser("campaigns", help="Manage campaigns")
    camp_parser.add_argument("action", choices=["list", "create"])
    camp_parser.add_argument("--name", help="Campaign name")

    # Analytics
    pipeline_parser = subparsers.add_parser("pipeline", help="Show pipeline analytics")
    pipeline_parser.add_argument("--start", help="Start date (YYYY-MM-DD)")
    pipeline_parser.add_argument("--end", help="End date (YYYY-MM-DD)")

    # Maintenance
    maint_parser = subparsers.add_parser("maintenance", help="Maintenance bugs/enhancements")
    maint_sub = maint_parser.add_subparsers(dest="mtype", help="Type")
    
    # Bugs
    bugs_parser = maint_sub.add_parser("bugs", help="Manage bugs")
    bugs_parser.add_argument("action", choices=["list", "report"])
    bugs_parser.add_argument("--desc", help="Description for report")
    bugs_parser.add_argument("--email", help="Contact email")

    # Enhancements
    enh_parser = maint_sub.add_parser("enhancements", help="Manage enhancements")
    enh_parser.add_argument("action", choices=["list", "request"])
    enh_parser.add_argument("--desc", help="Description for request")
    enh_parser.add_argument("--email", help="Contact email")

    # Admin
    admin_parser = subparsers.add_parser("admin", help="Admin functions")
    admin_parser.add_argument("resource", choices=["companies", "users"])

    args = parser.parse_args()
    cli = LeadGeniusCLI(base_url=args.base_url)

    if args.command == "auth":
        cli.auth(email=args.email)
    elif args.command == "generate-key":
        cli.generate_key(name=args.name, description=args.desc)
    elif args.command == "leads":
        if args.action == "list":
            cli.list_leads()
        elif args.action == "find":
            if not any([args.first_name, args.last_name, args.full_name, args.email, args.company]):
                print("Error: provide at least one filter: --first-name, --last-name, --full-name, --email, or --company")
                return
            cli.find_lead(
                first_name=args.first_name,
                last_name=args.last_name,
                full_name=args.full_name,
                email=args.email,
                company=args.company,
            )
        elif args.action == "enrich":
            if not args.ids:
                print("Error: --ids required for enrichment")
                return
            cli.enrich_leads(args.ids)
    elif args.command == "campaigns":
        if args.action == "list":
            cli.list_campaigns()
        elif args.action == "create":
            if not args.name:
                print("Error: --name required")
                return
            cli.create_campaign(args.name)
    elif args.command == "pipeline":
        # Check for --start and --end from pipeline_parser (need to add them)
        start_date = getattr(args, 'start', (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
        end_date = getattr(args, 'end', datetime.now().strftime('%Y-%m-%d'))
        cli.show_pipeline(start_date=start_date, end_date=end_date)
    elif args.command == "maintenance":
        if args.mtype == "bugs":
            if args.action == "list":
                cli.list_bugs()
            elif args.action == "report":
                if not args.desc:
                    print("Error: --desc required")
                    return
                cli.report_bug(args.desc, email=args.email)
        elif args.mtype == "enhancements":
            if args.action == "list":
                cli.list_enhancements()
            elif args.action == "request":
                if not args.desc:
                    print("Error: --desc required")
                    return
                cli.request_enhancement(args.desc, email=args.email)
    elif args.command == "admin":
        if args.resource == "companies":
            cli.list_all_companies()
        elif args.resource == "users":
            cli.list_all_users()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
