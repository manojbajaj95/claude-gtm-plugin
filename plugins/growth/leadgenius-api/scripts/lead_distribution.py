#!/usr/bin/env python3
import argparse
import requests
import json
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="LeadGenius Pro: Aggregate Leads per Client")
    parser.add_argument("--url", default="https://ugdmgjyxenhipk74b5swx4xvuy.appsync-api.us-east-1.amazonaws.com/graphql", help="GraphQL API URL")
    parser.add_argument("--key", help="AppSync API Key (defaults to LGP_APPSYNC_KEY env var)")
    parser.add_argument("--company-id", help="Company ID (defaults to LGP_COMPANY_ID env var)")

    args = parser.parse_args()

    api_key = args.key or os.environ.get("LGP_APPSYNC_KEY")
    company_id = args.company_id or os.environ.get("LGP_COMPANY_ID")

    if not api_key:
        print("Error: API Key is required. Use --key or set LGP_APPSYNC_KEY.")
        sys.exit(1)
    if not company_id:
        print("Error: Company ID is required. Use --company-id or set LGP_COMPANY_ID.")
        sys.exit(1)

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    # 1. Fetch all clients
    client_query = """
    query ListClients {
        listClients(limit: 1000) {
            items {
                id
                client_id
                clientName
            }
        }
    }
    """

    print("Fetching clients...")
    try:
        response = requests.post(args.url, headers=headers, json={"query": client_query})
        clients_data = response.json().get('data', {}).get('listClients', {})
        clients = clients_data.get('items', [])
    except Exception as e:
        print(f"Failed to fetch clients: {e}")
        sys.exit(1)

    client_map = {c['id']: c['clientName'] for c in clients}
    client_id_str_map = {c['client_id']: c['clientName'] for c in clients if c.get('client_id')}

    # 2. Fetch all leads
    leads_query = """
    query ListLeadsByCompany($company_id: String!, $nextToken: String) {
        listEnrichLeadsByCompanyId(company_id: $company_id, nextToken: $nextToken, limit: 1000) {
            items {
                id
                client_id
            }
            nextToken
        }
    }
    """

    print(f"Fetching leads for company {company_id}...")
    all_leads = []
    next_token = None

    while True:
        payload = {
            "query": leads_query,
            "variables": {
                "company_id": company_id,
                "nextToken": next_token
            }
        }
        try:
            response = requests.post(args.url, headers=headers, json=payload)
            data = response.json().get('data', {}).get('listEnrichLeadsByCompanyId', {})
            all_leads.extend(data.get('items', []))
            next_token = data.get('nextToken')
            if not next_token:
                break
        except Exception as e:
            print(f"Failed to fetch leads: {e}")
            break

    # 3. Aggregate
    stats = {}
    for lead in all_leads:
        cid = lead.get('client_id')
        stats[cid] = stats.get(cid, 0) + 1

    # 4. Results
    print("\n--- Leads per Client ---")
    print(f"{'Client Name':<40} | {'Client ID':<30} | {'Leads':<5}")
    print("-" * 80)

    for cid, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        name = client_id_str_map.get(cid) or client_map.get(cid) or "Unknown/Unassigned"
        cid_display = cid if cid else "N/A"
        print(f"{name:<40} | {cid_display:<30} | {count:<5}")

    # Clients with 0 leads
    zero_lead_clients = []
    for cid_id, name in client_map.items():
        if cid_id not in stats:
            client_obj = next((c for c in clients if c['id'] == cid_id), {})
            cid_str = client_obj.get('client_id')
            if cid_str not in stats:
                zero_lead_clients.append((name, cid_str or cid_id))

    if zero_lead_clients:
        print("\n--- Clients with 0 Leads ---")
        for name, cid in zero_lead_clients:
            print(f"{name:<40} | {cid:<30} | 0")

    print(f"\nTotal Leads analyzed: {len(all_leads)}")

if __name__ == "__main__":
    main()
