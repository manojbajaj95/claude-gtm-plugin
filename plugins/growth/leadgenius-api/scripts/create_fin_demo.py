import requests
import json

url = "https://ugdmgjyxenhipk74b5swx4xvuy.appsync-api.us-east-1.amazonaws.com/graphql"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "da2-5u4a7hbhvbb2fdsj2ys2h2pljy"
}

company_id = "company-1769080774403-0fbkihn"
owner = "2498a4e8-5071-70f7-987b-cc3e1d6ffc51"
client_name = "Premier Financial Services"
client_id_str = "client_fin_services"

def run_query(query, variables=None):
    payload = {"query": query, "variables": variables}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 1. Create/Verify Client
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
    "companyURL": "https://finance.example.com",
    "description": "Mock client for Financial Services demo",
    "owner": owner,
    "company_id": company_id
}

print(f"Creating client: {client_name}...")
res = run_query(create_client_mutation, {"input": client_input})
# We don't worry about duplicate client_id errors for now as we just need the campaign to link to the string ID
print(f"Client Processed.")

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
    "name": "Banking & Fintech Outreach 2026",
    "description": "Global outreach campaign for top-tier financial institutions",
    "campaignType": "abm",
    "status": "active",
    "client_id": client_id_str,
    "company_id": company_id,
    "owner": owner
}

print("Creating campaign...")
res = run_query(create_campaign_mutation, {"input": campaign_input})
campaign_id = res.get('data', {}).get('createABMCampaign', {}).get('id')
print(f"Campaign Created. ID: {campaign_id}")

# 3. Define 20 Leads
mock_leads = [
    {"first": "Mark", "last": "Stevens", "email": "m.stevens@goldmansachs.com", "company": "Goldman Sachs", "title": "Managing Director, Investment Banking"},
    {"first": "Angela", "last": "Wong", "email": "a.wong@jpmorgan.com", "company": "JP Morgan Chase", "title": "Head of Fintech Innovation"},
    {"first": "Christopher", "last": "Bell", "email": "c.bell@morganstanley.com", "company": "Morgan Stanley", "title": "VP Wealth Management"},
    {"first": "Jessica", "last": "Lange", "email": "j.lange@hsbc.com", "company": "HSBC", "title": "Chief Compliance Officer"},
    {"first": "Andrew", "last": "Foster", "email": "a.foster@barclays.com", "company": "Barclays", "title": "Head of Digital Transformation"},
    {"first": "Michelle", "last": "Ross", "email": "m.ross@citigroup.com", "company": "Citigroup", "title": "Global Risk Manager"},
    {"first": "Patrick", "last": "Murphy", "email": "p.murphy@wellsfargo.com", "company": "Wells Fargo", "title": "VP Consumer Lending"},
    {"first": "Sandra", "last": "Bullock", "email": "s.bullock@bankofamerica.com", "company": "Bank of America", "title": "Director of Strategy"},
    {"first": "Kevin", "last": "Hart", "email": "k.hart@fidelity.com", "company": "Fidelity Investments", "title": "Portfolio Manager"},
    {"first": "Rachel", "last": "Green", "email": "r.green@vanguard.com", "company": "Vanguard", "title": "Head of Client Experience"},
    {"first": "Monica", "last": "Geller", "email": "m.geller@blackrock.com", "company": "BlackRock", "title": "Managing Director, ESG"},
    {"first": "Chandler", "last": "Bing", "email": "c.bing@ubs.com", "company": "UBS", "title": "Head of Private Banking"},
    {"first": "Joey", "last": "Tribbiani", "email": "j.tribbiani@allianz.com", "company": "Allianz", "title": "VP Marketing"},
    {"first": "Phoebe", "last": "Buffay", "email": "p.buffay@axa.com", "company": "AXA", "title": "HR Director"},
    {"first": "Ross", "last": "Geller", "email": "r.geller@prudential.com", "company": "Prudential Financial", "title": "Chief Data Officer"},
    {"first": "William", "last": "Shatner", "email": "w.shatner@metlife.com", "company": "MetLife", "title": "VP Enterprise Sales"},
    {"first": "Leonard", "last": "Nimoy", "email": "l.nimoy@statestreet.com", "company": "State Street", "title": "Head of Custody Services"},
    {"first": "Hiroshi", "last": "Tanaka", "email": "h.tanaka@bnymellon.com", "company": "BNY Mellon", "title": "Director of Operations"},
    {"first": "Elena", "last": "Petrova", "email": "e.petrova@nomura.com", "company": "Nomura Holdings", "title": "Investment Strategist"},
    {"first": "Sven", "last": "Gunnar", "email": "s.gunnar@ubs.com", "company": "UBS", "title": "Senior Portfolio Analyst"}
]

# 4. Insert Leads
create_lead_mutation = """
mutation CreateEnrichLeads($input: CreateEnrichLeadsInput!) {
    createEnrichLeads(input: $input) {
        id
    }
}
"""

print(f"Inserting 20 leads for {client_name}...")
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
    res = run_query(create_lead_mutation, {"input": lead_input})
    print(f"Inserted: {full_name} ({lead['company']})")

print("\nAll 20 leads for Financial Services completed successfully!")
