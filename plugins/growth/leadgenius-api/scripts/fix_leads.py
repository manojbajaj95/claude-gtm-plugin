import requests
import json

campaign_id = "495dba4f-e39d-4d0d-aefd-54fffd606b3c"
lead_ids = [
    "6d7fdcf9-e561-4faa-8084-6a265c64d923",
    "73c2a359-aae8-4e24-806f-b8131d58c54c",
    "67cb8e2c-d599-44e4-99d4-e84d13ada8ad",
    "311d5d3a-005a-4977-8f0d-bc9cea35cdda",
    "3f31847b-020b-4e9c-b20c-2c8abcae1a81",
    "054b025b-d228-489d-95a5-394430a1e5ae",
    "049a9224-a557-400d-91e2-7c504eb7231d",
    "1c708142-8b9a-4fcd-b05c-9d0ba3410480",
    "3724f074-cb35-4c17-9bb4-bbd5413533db",
    "f41d7d9f-3c9c-458a-beb7-5a4a23f69a13"
]

url = "https://ugdmgjyxenhipk74b5swx4xvuy.appsync-api.us-east-1.amazonaws.com/graphql"
company_id = "company-1769080774403-0fbkihn"
client_id = "client_global_tech_solutions"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "da2-5u4a7hbhvbb2fdsj2ys2h2pljy"
}

# Update Campaign
print(f"Updating campaign {campaign_id}...")
campaign_mutation = """
mutation UpdateABMCampaign($input: UpdateABMCampaignInput!) {
    updateABMCampaign(input: $input) {
        id
    }
}
"""
payload = {
    "query": campaign_mutation,
    "variables": {
        "input": {
            "id": campaign_id,
            "company_id": company_id,
            "client_id": client_id
        }
    }
}
response = requests.post(url, headers=headers, json=payload)
print(f"Updated Campaign: {response.json()}")

# Update Leads
lead_mutation = """
mutation UpdateEnrichLeads($input: UpdateEnrichLeadsInput!) {
    updateEnrichLeads(input: $input) {
        id
    }
}
"""

leads_data = [
    {"id": "6d7fdcf9-e561-4faa-8084-6a265c64d923", "first": "Julia", "last": "Roberts"},
    {"id": "73c2a359-aae8-4e24-806f-b8131d58c54c", "first": "Ian", "last": "McKellen"},
    {"id": "67cb8e2c-d599-44e4-99d4-e84d13ada8ad", "first": "Hannah", "last": "Abbott"},
    {"id": "311d5d3a-005a-4977-8f0d-bc9cea35cdda", "first": "George", "last": "Clooney"},
    {"id": "3f31847b-020b-4e9c-b20c-2c8abcae1a81", "first": "Fiona", "last": "Gallagher"},
    {"id": "054b025b-d228-489d-95a5-394430a1e5ae", "first": "Edward", "last": "Norton"},
    {"id": "049a9224-a557-400d-91e2-7c504eb7231d", "first": "Diana", "last": "Prince"},
    {"id": "1c708142-8b9a-4fcd-b05c-9d0ba3410480", "first": "Charlie", "last": "Davis"},
    {"id": "3724f074-cb35-4c17-9bb4-bbd5413533db", "first": "Bob", "last": "Smith"},
    {"id": "f41d7d9f-3c9c-458a-beb7-5a4a23f69a13", "first": "Alice", "last": "Johnson"}
]

for lead in leads_data:
    full_name = f"{lead['first']} {lead['last']}"
    payload = {
        "query": lead_mutation,
        "variables": {
            "input": {
                "id": lead['id'],
                "lead_id": lead['id'],
                "fullName": full_name,
                "contactName": full_name,
                "company_id": company_id,
                "client_id": client_id,
                "owner": "2498a4e8-5071-70f7-987b-cc3e1d6ffc51"
            }
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"Updated Lead {lead['id']}: {response.json()}")
