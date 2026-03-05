import requests
import json

url = "https://ugdmgjyxenhipk74b5swx4xvuy.appsync-api.us-east-1.amazonaws.com/graphql"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "da2-5u4a7hbhvbb2fdsj2ys2h2pljy"
}

company_id = "company-1769080774403-0fbkihn"
owner = "2498a4e8-5071-70f7-987b-cc3e1d6ffc51"
client_name = "Global Education Excellence"
client_id_str = "client_global_education"

def run_query(query, variables=None):
    payload = {"query": query, "variables": variables}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 1. Create Client
create_client_mutation = """
mutation CreateClient($input: CreateClientInput!) {
    createClient(input: $input) {
        id
        clientName
    }
}
"""
client_input = {
    "client_id": client_id_str,
    "clientName": client_name,
    "companyURL": "https://education.example.com",
    "description": "Targeting Higher Ed and K-12 for demo",
    "owner": owner,
    "company_id": company_id
}

print(f"Creating client: {client_name}...")
res = run_query(create_client_mutation, {"input": client_input})
client_uuid = res.get('data', {}).get('createClient', {}).get('id')
print(f"Client Created. UUID: {client_uuid}")

# 2. Create Campaign
create_campaign_mutation = """
mutation CreateABMCampaign($input: CreateABMCampaignInput!) {
    createABMCampaign(input: $input) {
        id
        name
    }
}
"""
campaign_input = {
    "name": "Higher Ed Innovation 2026",
    "description": "Strategic outreach for education sector",
    "campaignType": "abm",
    "status": "active",
    "client_id": client_id_str, # Use string ID for dashboard
    "company_id": company_id,
    "owner": owner
}

print("Creating campaign...")
res = run_query(create_campaign_mutation, {"input": campaign_input})
campaign_id = res.get('data', {}).get('createABMCampaign', {}).get('id')
print(f"Campaign Created. ID: {campaign_id}")

# 3. Create 12 Leads
create_lead_mutation = """
mutation CreateEnrichLeads($input: CreateEnrichLeadsInput!) {
    createEnrichLeads(input: $input) {
        id
    }
}
"""

mock_leads = [
    {"first": "Sarah", "last": "Miller", "email": "s.miller@stanford.edu", "company": "Stanford University", "title": "Dean of Engineering"},
    {"first": "James", "last": "Wilson", "email": "j.wilson@harvard.edu", "company": "Harvard University", "title": "IT Director"},
    {"first": "Emily", "last": "Chen", "email": "chen@mit.edu", "company": "MIT", "title": "Head of Admissions"},
    {"first": "Robert", "last": "Taylor", "email": "r.taylor@cps.edu", "company": "Chicago Public Schools", "title": "Superintendent"},
    {"first": "Linda", "last": "Garcia", "email": "lgarcia@nyu.edu", "company": "NYU", "title": "VP Student Affairs"},
    {"first": "David", "last": "Brown", "email": "d.brown@asu.edu", "company": "Arizona State University", "title": "Chief Innovation Officer"},
    {"first": "Susan", "last": "White", "email": "s.white@ox.ac.uk", "company": "Oxford University", "title": "Director of Research"},
    {"first": "Michael", "last": "Davis", "email": "m.davis@yale.edu", "company": "Yale University", "title": "Provost"},
    {"first": "Karen", "last": "Black", "email": "k.black@cam.ac.uk", "company": "University of Cambridge", "title": "Digital Transformation Lead"},
    {"first": "Thomas", "last": "Green", "email": "tgreen@ucla.edu", "company": "UCLA", "title": "Head of EdTech"},
    {"first": "Jennifer", "last": "Adams", "email": "jadams@columbia.edu", "company": "Columbia University", "title": "Registrar"},
    {"first": "Patricia", "last": "King", "email": "p.king@berkeley.edu", "company": "UC Berkeley", "title": "Chancellor"}
]

print(f"Inserting 12 leads for {client_name}...")
for lead in mock_leads:
    full_name = f"{lead['first']} {lead['last']}"
    lead_input = {
        "firstName": lead['first'],
        "lastName": lead['last'],
        "fullName": full_name,
        "contactName": full_name,
        "email": lead['email'],
        "companyName": lead['company'],
        "title": lead['title'],
        "status": "new",
        "campaignId": campaign_id,
        "client_id": client_id_str,
        "company_id": company_id,
        "owner": owner
    }
    # Note: GraphQL create doesn't automatically set lead_id for self-ref usually without custom logic,
    # but we'll let the system handle it or manually set id/lead_id if needed.
    # To be safe and follow visibility rules:
    res = run_query(create_lead_mutation, {"input": lead_input})
    print(f"Inserted: {full_name} ({lead['company']})")

print("\nAll tasks completed successfully!")
