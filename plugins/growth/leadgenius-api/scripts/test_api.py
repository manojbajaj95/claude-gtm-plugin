#!/usr/bin/env python3
"""
LeadGenius Pro API — End-to-End Test Script
============================================
Tests authentication, client CRUD, and lead CRUD against the live API.

Usage:
  python3 scripts/test_api.py --username EMAIL --password PASSWORD [--base-url URL]

The script runs through:
  1. Auth — POST /api/auth to get Cognito JWT tokens
  2. Clients — List, Create, Update, Delete
  3. Leads — Create (single + batch), List, Update, Delete (single + batch)

All test data is cleaned up at the end.
"""

import argparse
import json
import os
import sys
import time
import requests

# ─── Defaults ───────────────────────────────────────────────────────────────
DEFAULT_BASE_URL = "https://last.leadgenius.app"
AUTH_FILE = os.path.expanduser("~/.leadgenius_auth.json")

# ─── Colors ─────────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def ok(msg):    print(f"  {GREEN}✓{RESET} {msg}")
def fail(msg):  print(f"  {RED}✗{RESET} {msg}")
def info(msg):  print(f"  {CYAN}ℹ{RESET} {msg}")
def warn(msg):  print(f"  {YELLOW}⚠{RESET} {msg}")
def header(msg): print(f"\n{BOLD}{CYAN}{'═'*60}\n  {msg}\n{'═'*60}{RESET}")
def subheader(msg): print(f"\n{BOLD}  ── {msg} ──{RESET}")

# ─── Helpers ────────────────────────────────────────────────────────────────
class APIClient:
    """Thin wrapper around requests with JWT auth."""
    
    def __init__(self, base_url, access_token=None, id_token=None):
        self.base_url = base_url.rstrip("/")
        self.access_token = access_token
        self.id_token = id_token
    
    def _headers(self):
        h = {"Content-Type": "application/json"}
        if self.access_token:
            h["Authorization"] = f"Bearer {self.access_token}"
        return h
    
    def _cookies(self):
        """Build cookies dict that mimics what the Next.js app sets for Cognito auth."""
        # The API routes use runWithAmplifyServerContext which reads cookies
        # We need to provide the tokens as cookies, not just headers
        cookies = {}
        if self.access_token:
            cookies["accessToken"] = self.access_token
        if self.id_token:
            cookies["idToken"] = self.id_token
        return cookies if cookies else None
    
    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        r = requests.get(url, headers=self._headers(), params=params, cookies=self._cookies(), timeout=30)
        return r.status_code, self._parse(r)
    
    def post(self, path, data=None):
        url = f"{self.base_url}{path}"
        r = requests.post(url, headers=self._headers(), json=data, cookies=self._cookies(), timeout=30)
        return r.status_code, self._parse(r)
    
    def put(self, path, data=None):
        url = f"{self.base_url}{path}"
        r = requests.put(url, headers=self._headers(), json=data, cookies=self._cookies(), timeout=30)
        return r.status_code, self._parse(r)
    
    def delete(self, path, params=None, data=None):
        url = f"{self.base_url}{path}"
        r = requests.delete(url, headers=self._headers(), params=params, json=data, cookies=self._cookies(), timeout=30)
        return r.status_code, self._parse(r)
    
    def _parse(self, r):
        try:
            return r.json()
        except:
            return {"raw": r.text}

# ─── Test Result Tracking ───────────────────────────────────────────────────
results = {"passed": 0, "failed": 0, "skipped": 0}

def assert_ok(condition, test_name, detail=""):
    if condition:
        ok(test_name)
        results["passed"] += 1
    else:
        fail(f"{test_name} — {detail}")
        results["failed"] += 1
    return condition

def skip(test_name, reason=""):
    warn(f"SKIP: {test_name} — {reason}")
    results["skipped"] += 1

# ═══════════════════════════════════════════════════════════════════════════
#  1. AUTH
# ═══════════════════════════════════════════════════════════════════════════
def test_auth(base_url, username, password):
    header("1. AUTHENTICATION")
    
    subheader("POST /api/auth — Login with Cognito credentials")
    
    url = f"{base_url}/api/auth"
    payload = {"username": username, "password": password}
    
    try:
        r = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        status = r.status_code
        body = r.json() if r.status_code != 500 else {"raw": r.text}
    except Exception as e:
        fail(f"Auth request failed: {e}")
        return None
    
    if not assert_ok(status == 200, "Auth returns 200", f"Got {status}: {json.dumps(body, indent=2)[:300]}"):
        return None
    
    assert_ok(body.get("success") == True, "Response has success=true")
    
    tokens = body.get("tokens", {})
    access_token = tokens.get("accessToken")
    id_token = tokens.get("idToken")
    refresh_token = tokens.get("refreshToken")
    
    assert_ok(bool(access_token), "Access token received")
    assert_ok(bool(id_token), "ID token received")
    assert_ok(bool(refresh_token), "Refresh token received")
    
    info(f"Token expires in: {tokens.get('expiresIn', '?')}s")
    info(f"Access token length: {len(access_token) if access_token else 0} chars")
    
    # Save tokens for future use
    auth_data = {
        "token": access_token,
        "id_token": id_token,
        "refresh_token": refresh_token,
        "email": username,
        "base_url": base_url,
    }
    with open(AUTH_FILE, "w") as f:
        json.dump(auth_data, f, indent=2)
    info(f"Tokens saved to {AUTH_FILE}")
    
    return APIClient(base_url, access_token=access_token, id_token=id_token)


# ═══════════════════════════════════════════════════════════════════════════
#  2. CLIENTS
# ═══════════════════════════════════════════════════════════════════════════
def test_clients(api: APIClient):
    header("2. CLIENT MANAGEMENT")
    
    created_client_id = None
    
    # ── List Clients ──
    subheader("GET /api/clients — List all clients")
    status, body = api.get("/api/clients")
    
    if not assert_ok(status == 200, "List clients returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
        info("Skipping remaining client tests due to auth/connection issue")
        return None
    
    assert_ok(body.get("success") == True, "Response has success=true")
    clients = body.get("clients", [])
    info(f"Found {len(clients)} existing client(s)")
    
    if clients:
        first = clients[0]
        info(f"First client: id={first.get('id', 'N/A')}, name={first.get('clientName', 'N/A')}")
    
    # ── Create Client ──
    subheader("POST /api/clients — Create test client")
    test_client_name = f"__TEST_CLIENT_{int(time.time())}"
    create_payload = {
        "clientName": test_client_name,
        "companyURL": "https://test-company.example.com",
        "description": "Automated test client — safe to delete",
    }
    
    status, body = api.post("/api/clients", create_payload)
    
    if assert_ok(status == 201, "Create client returns 201", f"Got {status}: {json.dumps(body)[:300]}"):
        assert_ok(body.get("success") == True, "Response has success=true")
        new_client = body.get("client", {})
        created_client_id = new_client.get("id")
        assert_ok(bool(created_client_id), "Client ID returned", "No id in response")
        assert_ok(new_client.get("clientName") == test_client_name, "Client name matches")
        info(f"Created client: id={created_client_id}, client_id={new_client.get('client_id')}")
    else:
        return None
    
    # ── Update Client ──
    subheader("PUT /api/clients — Update test client")
    updated_name = f"{test_client_name}_UPDATED"
    update_payload = {
        "id": created_client_id,
        "clientName": updated_name,
        "description": "Updated description from automated test",
    }
    
    status, body = api.put("/api/clients", update_payload)
    
    if assert_ok(status == 200, "Update client returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
        assert_ok(body.get("success") == True, "Response has success=true")
        updated_client = body.get("client", {})
        assert_ok(updated_client.get("clientName") == updated_name, "Client name updated")
    
    # ── Verify Update (re-fetch) ──
    subheader("GET /api/clients?clientId=... — Verify update")
    status, body = api.get("/api/clients", params={"clientId": created_client_id})
    
    if assert_ok(status == 200, "Get single client returns 200", f"Got {status}"):
        fetched_clients = body.get("clients", [])
        if fetched_clients:
            assert_ok(fetched_clients[0].get("clientName") == updated_name, "Fetched client reflects updated name")
    
    return created_client_id


# ═══════════════════════════════════════════════════════════════════════════
#  3. LEADS
# ═══════════════════════════════════════════════════════════════════════════
def test_leads(api: APIClient, client_id: str):
    header("3. LEAD MANAGEMENT")
    
    if not client_id:
        skip("All lead tests", "No client ID available (client creation failed)")
        return []
    
    created_lead_ids = []
    
    # We need the client_id field (the UUID), not the DynamoDB id
    # Let's fetch the client to get the client_id field
    subheader("Fetching client_id for lead operations")
    status, body = api.get("/api/clients", params={"clientId": client_id})
    
    if status != 200 or not body.get("clients"):
        skip("All lead tests", "Could not fetch client details")
        return []
    
    client_record = body["clients"][0]
    lead_client_id = client_record.get("client_id", client_id)
    info(f"Using client_id={lead_client_id} for lead operations")
    
    # ── Create Single Lead ──
    subheader("POST /api/leads — Create single lead")
    lead_payload = {
        "client_id": lead_client_id,
        "firstName": "Test",
        "lastName": "LeadOne",
        "email": "test.leadone@example-test.com",
        "companyName": "TestCorp",
        "companyDomain": "testcorp.example.com",
        "title": "VP Engineering",
        "linkedinUrl": "https://linkedin.com/in/test-leadone",
    }
    
    status, body = api.post("/api/leads", lead_payload)
    
    if assert_ok(status == 201, "Create single lead returns 201", f"Got {status}: {json.dumps(body)[:300]}"):
        assert_ok(body.get("success") == True, "Response has success=true")
        new_lead = body.get("lead", {})
        lead_id = new_lead.get("id")
        assert_ok(bool(lead_id), "Lead ID returned")
        info(f"Created lead: id={lead_id}")
        if lead_id:
            created_lead_ids.append(lead_id)
    
    # ── Create Batch Leads ──
    subheader("POST /api/leads — Create batch (2 leads)")
    batch_payload = {
        "leads": [
            {
                "client_id": lead_client_id,
                "firstName": "Test",
                "lastName": "LeadTwo",
                "email": "test.leadtwo@example-test.com",
                "companyName": "BatchCorp",
                "title": "CTO",
            },
            {
                "client_id": lead_client_id,
                "firstName": "Test",
                "lastName": "LeadThree",
                "email": "test.leadthree@example-test.com",
                "companyName": "BatchCorp",
                "title": "VP Sales",
            },
        ]
    }
    
    status, body = api.post("/api/leads", batch_payload)
    
    if assert_ok(status == 201, "Batch create returns 201", f"Got {status}: {json.dumps(body)[:300]}"):
        assert_ok(body.get("success") == True, "Response has success=true")
        created_count = body.get("created", 0)
        assert_ok(created_count == 2, f"Created count is 2", f"Got {created_count}")
        skipped = body.get("skipped", [])
        info(f"Batch result: created={created_count}, skipped={len(skipped)}")
    
    # ── List Leads ──
    subheader("GET /api/leads — List leads for test client")
    status, body = api.get("/api/leads", params={"client_id": lead_client_id, "limit": 50})
    
    if assert_ok(status == 200, "List leads returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
        assert_ok(body.get("success") == True, "Response has success=true")
        leads = body.get("leads", [])
        total = body.get("total", 0)
        info(f"Total leads returned: {total}")
        
        # Collect all lead IDs from the test client for cleanup
        for lead in leads:
            lid = lead.get("id")
            if lid and lid not in created_lead_ids:
                created_lead_ids.append(lid)
        
        if leads:
            first = leads[0]
            info(f"First lead: {first.get('firstName', '')} {first.get('lastName', '')} — {first.get('companyName', 'N/A')}")
    
    # ── Update Single Lead ──
    if created_lead_ids:
        subheader("PUT /api/leads — Update single lead")
        update_lead_id = created_lead_ids[0]
        update_payload = {
            "id": update_lead_id,
            "title": "Senior VP Engineering (Updated)",
            "notes": "Updated by automated test script",
        }
        
        status, body = api.put("/api/leads", update_payload)
        
        if assert_ok(status == 200, "Update lead returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
            assert_ok(body.get("success") == True, "Response has success=true")
            updated_lead = body.get("lead", {})
            assert_ok(updated_lead.get("title") == "Senior VP Engineering (Updated)", "Title updated correctly")
    
    # ── Batch Update ──
    if len(created_lead_ids) >= 2:
        subheader("PUT /api/leads — Batch update (2 leads)")
        batch_update_payload = {
            "leads": [
                {"id": created_lead_ids[0], "notes": "Batch updated lead 1"},
                {"id": created_lead_ids[1], "notes": "Batch updated lead 2"},
            ]
        }
        
        status, body = api.put("/api/leads", batch_update_payload)
        
        if assert_ok(status == 200, "Batch update returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
            assert_ok(body.get("success") == True, "Response has success=true")
            info(f"Batch updated: {body.get('updated', 0)} leads")
    
    # ── Delete Single Lead ──
    if created_lead_ids:
        subheader("DELETE /api/leads?id=... — Delete single lead")
        delete_id = created_lead_ids[0]
        
        status, body = api.delete("/api/leads", params={"id": delete_id})
        
        if assert_ok(status == 200, "Delete single lead returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
            assert_ok(body.get("success") == True, "Response has success=true")
            info(f"Deleted lead: {delete_id}")
            created_lead_ids.remove(delete_id)
    
    # ── Batch Delete ──
    if created_lead_ids:
        subheader(f"DELETE /api/leads — Batch delete ({len(created_lead_ids)} remaining leads)")
        
        status, body = api.delete("/api/leads", data={"ids": created_lead_ids})
        
        if assert_ok(status == 200, "Batch delete returns 200", f"Got {status}: {json.dumps(body)[:300]}"):
            assert_ok(body.get("success") == True, "Response has success=true")
            info(f"Batch deleted: {body.get('deleted', 0)} leads")
            created_lead_ids.clear()
    
    return created_lead_ids


# ═══════════════════════════════════════════════════════════════════════════
#  4. CLEANUP
# ═══════════════════════════════════════════════════════════════════════════
def cleanup(api: APIClient, client_id: str, remaining_lead_ids: list):
    header("4. CLEANUP")
    
    # Delete any remaining leads
    if remaining_lead_ids:
        warn(f"Cleaning up {len(remaining_lead_ids)} remaining lead(s)...")
        status, body = api.delete("/api/leads", data={"ids": remaining_lead_ids})
        if status == 200:
            ok(f"Cleanup: deleted {body.get('deleted', 0)} remaining leads")
        else:
            fail(f"Cleanup: lead deletion failed ({status})")
    
    # Delete the test client
    if client_id:
        info(f"Deleting test client: {client_id}")
        status, body = api.delete("/api/clients", params={"id": client_id})
        if status == 200 and body.get("success"):
            ok("Test client deleted")
        else:
            fail(f"Test client deletion failed ({status}): {json.dumps(body)[:200]}")
    
    ok("Cleanup complete")


# ═══════════════════════════════════════════════════════════════════════════
#  5. SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
def print_summary():
    header("TEST SUMMARY")
    total = results["passed"] + results["failed"] + results["skipped"]
    print(f"  {GREEN}Passed:  {results['passed']}{RESET}")
    print(f"  {RED}Failed:  {results['failed']}{RESET}")
    print(f"  {YELLOW}Skipped: {results['skipped']}{RESET}")
    print(f"  Total:   {total}")
    print()
    
    if results["failed"] == 0:
        print(f"  {GREEN}{BOLD}🎉 ALL TESTS PASSED!{RESET}")
    else:
        print(f"  {RED}{BOLD}❌ {results['failed']} TEST(S) FAILED{RESET}")
    print()


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(
        description="LeadGenius Pro API — End-to-End Test",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/test_api.py --username user@company.com --password MyPass123
  python3 scripts/test_api.py --username user@company.com --password MyPass123 --base-url https://last.leadgenius.app
        """
    )
    parser.add_argument("--username", required=True, help="Cognito username (email)")
    parser.add_argument("--password", required=True, help="Cognito password")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"API base URL (default: {DEFAULT_BASE_URL})")
    parser.add_argument("--skip-cleanup", action="store_true", help="Skip cleanup (leave test data)")
    
    args = parser.parse_args()
    
    print(f"\n{BOLD}{'═'*60}")
    print(f"  LeadGenius Pro API — End-to-End Test Suite")
    print(f"  Base URL: {args.base_url}")
    print(f"  User:     {args.username}")
    print(f"  Time:     {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═'*60}{RESET}\n")
    
    # 1. Auth
    api = test_auth(args.base_url, args.username, args.password)
    if not api:
        fail("Cannot continue without authentication")
        print_summary()
        sys.exit(1)
    
    # 2. Clients
    created_client_id = test_clients(api)
    
    # 3. Leads
    remaining_leads = test_leads(api, created_client_id)
    
    # 4. Cleanup
    if not args.skip_cleanup:
        cleanup(api, created_client_id, remaining_leads or [])
    else:
        warn("Cleanup skipped (--skip-cleanup flag)")
    
    # 5. Summary
    print_summary()
    
    sys.exit(0 if results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
