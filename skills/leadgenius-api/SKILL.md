---
name: leadgenius-api
description: Comprehensive toolset for interacting with LeadGenius Pro APIs. Use for managing B2B leads, clients, companies, enrichment settings, AI-driven lead processing (enrichment, copyright, SDR AI), search history, webhooks, territory analysis, email services, and integrations. Supports Cognito JWT (cookies + Bearer) and API key authentication with multi-tenant data isolation.
---

# LeadGenius Pro API — Skill Reference

This skill provides a comprehensive interface for interacting with the **LeadGenius Pro API v1.1**.

> **Base URL:** `https://last.leadgenius.app/api`  
> **Full Reference:** See [docs/API_REFERENCE.md](../../../docs/API_REFERENCE.md)

---

## Authentication

LeadGenius supports three authentication methods, tried in order by `getAuthContext`:

| Priority | Method | How It Works | Use Case |
|----------|--------|--------------|----------|
| 1 | **Cognito Cookies** | Automatic via browser session (`next/headers` cookies) | Web app (frontend) |
| 2 | **Bearer JWT** ✨ | `Authorization: Bearer <accessToken>` header; JWT `sub` claim extracted as owner | **External scripts, agents, CLI tools** |
| 3 | **API Key** | `x-api-key: <key>` + `x-user-id: <sub>` headers | Bulk data extraction, service-to-service |

### Getting a JWT Token

```bash
# Option 1: Use the test/auth script
python3 scripts/auth.py --email your@email.com

# Option 2: Direct API call
curl -X POST https://last.leadgenius.app/api/auth \
  -H "Content-Type: application/json" \
  -d '{"username": "your@email.com", "password": "YourPassword"}'
```

**Response:**
```json
{
  "success": true,
  "tokens": {
    "accessToken": "eyJra...",
    "idToken": "eyJra...",
    "refreshToken": "eyJj...",
    "expiresIn": 3600
  }
}
```

Use `tokens.accessToken` as the Bearer token for all subsequent API calls. Tokens expire after 1 hour.

### Using Bearer JWT in API Calls

```bash
# All API calls use the accessToken in the Authorization header
curl -H "Authorization: Bearer <accessToken>" \
     -H "Content-Type: application/json" \
     https://last.leadgenius.app/api/clients
```

The `getAuthContext` middleware (`src/utils/apiAuthHelper.ts`) decodes the JWT, extracts the `sub` claim as the `owner`, and resolves the `company_id` for multi-tenant isolation — all automatically.

### Auth Credentials Storage

Tokens are saved to `~/.leadgenius_auth.json` by the auth scripts:
```json
{
  "token": "<accessToken>",
  "id_token": "<idToken>",
  "refresh_token": "<refreshToken>",
  "email": "your@email.com",
  "base_url": "https://last.leadgenius.app"
}
```

---

## Core Workflows (E2E Tested ✅)

The following operations have been validated end-to-end with the test suite.

### 1. Client Management ✅

All client operations are scoped by `company_id` (resolved from JWT).

| Operation | Method | Endpoint | Status |
|-----------|--------|----------|--------|
| List all clients | `GET` | `/api/clients` | ✅ Tested |
| Get single client | `GET` | `/api/clients?clientId=<id>` | ✅ Tested |
| Create client | `POST` | `/api/clients` | ✅ Tested (201) |
| Update client | `PUT` | `/api/clients` | ✅ Tested |
| Delete client | `DELETE` | `/api/clients?id=<id>` | ✅ Tested |
| Purge client + leads | `DELETE` | `/api/clients?id=<id>&purge=true` | Documented |

#### Create Client Payload
```json
{
  "clientName": "Acme Corp",
  "companyURL": "https://acme.com",
  "description": "Enterprise client for B2B leads"
}
```

**Response (201):**
```json
{
  "success": true,
  "client": {
    "id": "edd5c738-...",
    "client_id": "5b9cb5db-...",
    "clientName": "Acme Corp",
    "companyURL": "https://acme.com",
    "description": "Enterprise client for B2B leads",
    "owner": "4428a4f8-...",
    "company_id": "company-177..."
  }
}
```

> **Note:** `id` is the DynamoDB record ID. `client_id` is the unique business identifier used in lead operations.

#### Update Client Payload
```json
{
  "id": "<dynamodb-id>",
  "clientName": "Updated Name",
  "description": "Updated description"
}
```

---

### 2. Lead Management ✅

Leads are stored as `EnrichLeads` in DynamoDB and are scoped by `client_id` and `company_id`.

| Operation | Method | Endpoint | Status |
|-----------|--------|----------|--------|
| List leads | `GET` | `/api/leads?client_id=<client_id>&limit=100` | ✅ Tested |
| Create single lead | `POST` | `/api/leads` | ✅ Tested (201) |
| Create batch leads | `POST` | `/api/leads` (with `leads` array) | ✅ Tested (201) |
| Update single lead | `PUT` | `/api/leads` | ✅ Tested |
| Batch update leads | `PUT` | `/api/leads` (with `leads` array) | ✅ Tested |
| Delete single lead | `DELETE` | `/api/leads?id=<id>` | ✅ Tested |
| Batch delete leads | `DELETE` | `/api/leads` (with `ids` array body) | ✅ Tested |

#### Create Single Lead Payload
```json
{
  "client_id": "5b9cb5db-...",
  "firstName": "John",
  "lastName": "Smith",
  "email": "john.smith@example.com",
  "companyName": "Acme Corp",
  "companyDomain": "acme.com",
  "title": "VP Engineering",
  "linkedinUrl": "https://linkedin.com/in/johnsmith"
}
```

#### Create Batch Leads Payload
```json
{
  "leads": [
    {
      "client_id": "5b9cb5db-...",
      "firstName": "Jane",
      "lastName": "Doe",
      "email": "jane@example.com",
      "companyName": "BatchCorp",
      "title": "CTO"
    },
    {
      "client_id": "5b9cb5db-...",
      "firstName": "Bob",
      "lastName": "Wilson",
      "email": "bob@example.com",
      "companyName": "BatchCorp",
      "title": "VP Sales"
    }
  ]
}
```

**Batch Response (201):**
```json
{
  "success": true,
  "created": 2,
  "skipped": []
}
```

#### Update Single Lead Payload
```json
{
  "id": "<lead-dynamodb-id>",
  "title": "Senior VP Engineering",
  "notes": "Updated via API"
}
```

#### Batch Update Payload
```json
{
  "leads": [
    { "id": "<id-1>", "notes": "Updated lead 1" },
    { "id": "<id-2>", "notes": "Updated lead 2" }
  ]
}
```

#### Batch Delete Payload (body)
```json
{
  "ids": ["<id-1>", "<id-2>"]
}
```

#### List Leads Query Parameters
- `client_id` (**required**) — The `client_id` field from Client (not the DynamoDB `id`)
- `limit` — 1 to 1000 (default: 100)
- `nextToken` — Pagination token

---

### 3. Bulk Data Extraction

High-volume extraction bypasses standard auth for raw GSI performance.

| Operation | Endpoint | Auth |
|-----------|----------|------|
| Bulk EnrichLeads | `GET /api/enrich-leads/list` | API Key |
| Bulk SourceLeads | `GET /api/source-leads/list` | API Key |

#### Bulk List Query Parameters
- `companyId` (required) — Multi-tenant isolation
- `clientId` (optional) — Filter by client. Use `ALL`/`DEFAULT` or omit for all
- `limit` (optional) — Default 1000, max 5000
- `nextToken` (optional) — Pagination token
- `fields` (optional) — Comma-separated field projection (reduces payload)

---

### 4. Company Management

| Operation | Endpoint | Auth |
|-----------|----------|------|
| Get Company | `GET /api/company` | JWT |
| Create Company | `POST /api/company` | JWT |
| Update Company | `PUT /api/company` | JWT (Owner/Admin) |

---

### 5. Search History

Track and manage lead search operations (e.g., Apify scraping runs).

| Operation | Endpoint | Auth |
|-----------|----------|------|
| Create Search History | `POST /api/search-history` | JWT / API Key |
| List Search History | `GET /api/search-history` | JWT |
| Update Search History | `PUT /api/search-history` | JWT |

#### List Query Parameters
- `client_id`, `status` (initiated/running/completed/failed), `icpId`, `category`, `limit`, `cursor`

#### Create Payload
```json
{
  "searchName": "Tech Companies in SF",
  "searchDescription": "Looking for SaaS companies",
  "searchCriteria": { "industry": "Technology", "location": "San Francisco" },
  "searchFilters": { "companySize": "50-200" },
  "client_id": "client-123",
  "clientName": "Acme Corp",
  "icpId": "icp-456",
  "icpName": "Enterprise SaaS",
  "apifyActorId": "actor-789",
  "category": "prospecting",
  "tags": ["enterprise", "saas"]
}
```

---

### 6. Webhook Management

Create and manage inbound webhooks for third-party integrations.

| Operation | Endpoint | Auth |
|-----------|----------|------|
| List Webhooks | `GET /api/webhook-workbench` | JWT / API Key |
| Create Webhook | `POST /api/webhook-workbench` | JWT / API Key |

**Supported Platforms:** `heyreach`, `woodpecker`, `lemlist`, `generic`

#### Create Webhook Payload
```json
{
  "name": "My Webhook",
  "platform": "heyreach",
  "description": "Webhook for lead capture",
  "platformConfig": "{\"field_mapping\": {}}",
  "client_id": "client-123"
}
```
Returns: `webhookUrl` with embedded secret key for the external platform to call.

---

### 7. Territory Workbench

Aggregated company-level analytics for territory planning.

| Operation | Endpoint | Auth |
|-----------|----------|------|
| List Companies | `GET /api/territory-workbench/companies` | JWT |
| Create/Update Company | `POST /api/territory-workbench/companies` | JWT |

#### List Query Parameters
- `client_id` (required), `sortBy`, `sortDirection`, `industry`, `minLeads`, `maxLeads`, `search`, `startDate`, `endDate`

---

### 8. Settings Management ⚙️

**Settings drive all Lead Processing endpoints.** Configure settings first, then trigger processing.

All settings endpoints require **JWT auth** and are scoped by `company_id`.

#### URL Settings (Enrichment Service URLs)
| Operation | Endpoint |
|-----------|----------|
| Get | `GET /api/settings/url` |
| Create | `POST /api/settings/url` |
| Update | `PUT /api/settings/url` |

Available URL/key pairs: `companyUrl`, `emailFinder`, `enrichment1` through `enrichment10` (each with `_Apikey`).

#### Agent Settings (EpsimoAI Agent IDs for Copyright)
| Operation | Endpoint |
|-----------|----------|
| Get | `GET /api/settings/agent` |
| Create | `POST /api/settings/agent` |
| Update | `PUT /api/settings/agent` |

Available fields: `projectId`, `enrichment1AgentId` through `enrichment10AgentId`.

#### SDR AI Settings (EpsimoAI Agent IDs for SDR AI)
| Operation | Endpoint |
|-----------|----------|
| Get | `GET /api/settings/sdr-ai` |
| Create | `POST /api/settings/sdr-ai` |
| Update | `PUT /api/settings/sdr-ai` |

Available fields: `projectId`, plus `<fieldName>AgentId` for all SDR fields.

---

### 9. Lead Processing 🚀

Settings-driven execution routes that trigger enrichment, copyright, and SDR AI processing on individual leads.

| Processing Type | Endpoint | Settings Source |
|-----------------|----------|-----------------|
| Enrichment | `POST /api/leads/process/enrich` | URL Settings |
| Copyright AI | `POST /api/leads/process/copyright` | Agent Settings |
| SDR AI | `POST /api/leads/process/sdr` | SDR AI Settings |

#### Enrichment Processing
```json
{
  "leadId": "enrich-lead-id",
  "services": ["companyUrl", "enrichment1", "enrichment3"],
  "overwrite": false
}
```

#### Copyright Processing
```json
{
  "leadId": "enrich-lead-id",
  "processes": [1, 3, 5],
  "overwrite": false
}
```

#### SDR AI Processing
```json
{
  "leadId": "enrich-lead-id",
  "fields": ["message1", "aiLeadScore", "aiQualification"],
  "overwrite": false
}
```

#### Response Format (all three)
```json
{
  "success": true,
  "runIds": ["run-abc-123", "run-def-456"],
  "batchTag": "enrich-process-1707654321-x8k2m1",
  "triggered": ["companyUrl", "enrichment1"],
  "skipped": ["enrichment3"],
  "leadId": "enrich-lead-id"
}
```

#### Processing Workflow
1. **Configure** (one-time per company): `POST /api/settings/url`, `POST /api/settings/agent`, `POST /api/settings/sdr-ai`
2. **Trigger** (per lead): `POST /api/leads/process/enrich`, `.../copyright`, `.../sdr`
3. **Track**: Use `runIds` → `GET /api/trigger-task-status?runId=...`

---

### 10. Background Tasks (Trigger.dev)

| Operation | Endpoint |
|-----------|----------|
| Submit Task | `POST /api/trigger` |
| Check Status | `GET /api/trigger-task-status?runId=...` |
| List Recent Runs | `GET /api/trigger-recent-runs?limit=20` |

---

### 11. Email Services

| Operation | Endpoint |
|-----------|----------|
| Validate Email | `POST /api/email-validate` |
| Verify Email (deep) | `POST /api/email-verify` |

---

### 12. Integration APIs

| Operation | Endpoint |
|-----------|----------|
| Start Apify Scrape | `POST /api/start-lead-scrape-complete` |
| Check Scrape Status | `GET /api/lead-generation-status?runId=...` |
| Epsimo AI Chat | `POST /api/epsimo-chat` |
| Unipile Accounts | `GET /api/unipile-accounts` |

---

## Data Architecture

### Multi-Tenant Isolation
All data is strictly isolated. Three isolation layers are enforced:
1. **Owner-based** — Data filtered by authenticated user's `owner` ID (JWT `sub`)
2. **Company-based** — Data filtered by user's `company_id` (resolved from CompanyMember table)
3. **Client-based** — Data filtered by `client_id`

### Key ID Fields
- **Client `id`** — DynamoDB record ID (used for update/delete)
- **Client `client_id`** — Business identifier (used in lead operations as `client_id`)
- **Lead `id`** — DynamoDB record ID (used for update/delete)
- **`owner`** — Cognito user `sub` (UUID), set automatically from JWT

### Data Operations Auth Mode
After `getAuthContext` resolves the owner, all data queries use `generateClient<Schema>({ authMode: 'apiKey' })` — meaning the Amplify API key handles DynamoDB access while the JWT provides identity and isolation.

---

## Error Handling

All errors follow a consistent format:
```json
{
  "success": false,
  "error": "Error message",
  "errorType": "authentication_error",
  "details": "Additional error details",
  "recommendation": "Suggested action"
}
```

### Common Error Types
- **Authentication** — `no_valid_credentials`, `token_expired`, `federated_jwt`, `no_valid_tokens`
- **Authorization** — `insufficient_permissions`, `owner_mismatch`
- **Validation** — `missing_required_field`, `invalid_format`, `invalid_value`
- **Resource** — `not_found`, `already_exists`, `conflict`

---

## Rate Limits & Pagination

### Rate Limits
| Tier | Limit |
|------|-------|
| Standard | 100 requests/minute |
| Premium | 1,000 requests/minute |

### Pagination
- **Standard API**: Cursor-based (`limit` + `nextToken`)
- **Bulk API**: Token-based (`limit` default 1000, max 5000 + `nextToken`)

---

## Helper Scripts

| Script | Description |
|--------|-------------|
| [`scripts/test_api.py`](scripts/test_api.py) | **E2E test suite** — tests auth, client CRUD, lead CRUD with cleanup |
| [`scripts/lgp.py`](scripts/lgp.py) | Unified CLI for all common operations |
| [`scripts/api_call.py`](scripts/api_call.py) | Low-level utility for custom raw API requests |
| [`scripts/auth.py`](scripts/auth.py) | Standalone auth utility |

### Running the E2E Test Suite
```bash
python3 scripts/test_api.py \
  --username your@email.com \
  --password YourPassword \
  --base-url https://last.leadgenius.app
```

Options:
- `--base-url` — Override base URL (default: `https://last.leadgenius.app`)
- `--skip-cleanup` — Keep test data after run

The test creates a temporary client and leads, exercises all CRUD operations, and cleans up automatically.

---

## CLI Usage (`lgp.py`)

```bash
# Auth
python3 scripts/lgp.py auth --email your@email.com

# Leads
python3 scripts/lgp.py leads list
python3 scripts/lgp.py leads find --full-name "Hugo Sanchez"
python3 scripts/lgp.py leads enrich --ids lead_1 lead_2

# Campaigns
python3 scripts/lgp.py campaigns list
python3 scripts/lgp.py campaigns create --name "Q3 Expansion"

# Pipeline analytics
python3 scripts/lgp.py pipeline --start 2026-01-01 --end 2026-02-08

# Maintenance
python3 scripts/lgp.py maintenance bugs list
python3 scripts/lgp.py maintenance bugs report --desc "Enrichment fails on LinkedIn URLs"
python3 scripts/lgp.py maintenance enhancements list
python3 scripts/lgp.py maintenance enhancements request --desc "Add support for Google Maps leads"

# API Key generation
python3 scripts/lgp.py generate-key --name "Production Agent" --desc "Key for main auto-agent"

# Admin (admin only)
python3 scripts/lgp.py admin companies
python3 scripts/lgp.py admin users
```

---

## Quick Start

```bash
# 1. Authenticate and get JWT
python3 scripts/auth.py --email your@email.com

# 2. Run the full E2E test suite
python3 scripts/test_api.py --username your@email.com --password YourPassword

# 3. Or make individual API calls
python3 scripts/api_call.py GET /clients
python3 scripts/api_call.py GET /leads?client_id=your-client-id
python3 scripts/api_call.py POST /leads --data '{"client_id": "...", "firstName": "Test", "lastName": "User"}'
```

## Reference Material

- **API Reference**: See [docs/API_REFERENCE.md](../../../docs/API_REFERENCE.md) for detailed endpoint descriptions, payloads, and response schemas
- **Auth Helper**: See `src/utils/apiAuthHelper.ts` for the 3-layer auth implementation
- **OpenAPI Spec**: See [references/openapi.json](references/openapi.json) for machine-readable schemas
