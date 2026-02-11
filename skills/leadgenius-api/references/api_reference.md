# LeadGenius Pro API — Endpoint Reference (v1.1)

> **Canonical Reference:** [`docs/API_REFERENCE.md`](../../../../docs/API_REFERENCE.md)  
> **Last Synced:** February 11, 2026

This is a compact endpoint index. For full request/response schemas, see the canonical reference above.

---

## Authentication

Three-layer auth handled by `getAuthContext` (in order):

| Priority | Method | Header / Mechanism | Scope |
|----------|--------|-------------------|-------|
| 1 | Cognito Cookies | Automatic via browser session | Web app (frontend) |
| 2 | **Bearer JWT** | `Authorization: Bearer <accessToken>` | Scripts, agents, CLI |
| 3 | API Key | `x-api-key` + `x-user-id` headers | Bulk endpoints, service-to-service |

### Login Endpoint

| Method | Endpoint | Body | Returns |
|--------|----------|------|---------|
| POST | `/api/auth` | `{"username": "<email>", "password": "<pass>"}` | `tokens.accessToken`, `tokens.idToken`, `tokens.refreshToken` |


## 👤 Lead Management

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/leads` | JWT | List all B2B leads for authenticated user |
| GET | `/api/enrich-leads/{id}` | JWT | Get single enriched lead by ID |
| PUT | `/api/enrich-leads/{id}` | JWT | Update enriched lead (AI scores, enrichment data) |
| GET | `/api/enrich-leads/list` | API Key | Bulk list enriched leads (requires `companyId`) |
| GET | `/api/source-leads/list` | API Key | Bulk list source leads (requires `companyId`) |
| GET | `/api/find-lead` | JWT | Search by `email`, `linkedinUrl`, `client_id` |

### Bulk List Query Params
`companyId` (required), `clientId`, `limit` (default 1000, max 5000), `nextToken`, `fields` (comma-separated)

---

## 🏢 Client Management

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/clients` | JWT | List all clients |
| POST | `/api/clients` | JWT | Create new client |
| PUT | `/api/clients` | JWT | Update existing client |

---

## 🏛️ Company Management

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/company` | JWT | Get current user's company |
| POST | `/api/company` | JWT | Create company |
| PUT | `/api/company` | JWT (Owner/Admin) | Update company name |

---

## 🔍 Search History

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/search-history` | JWT | List search history (filters: `client_id`, `status`, `icpId`, `category`, `limit`, `cursor`) |
| POST | `/api/search-history` | JWT/API Key | Create search history record |
| PUT | `/api/search-history` | JWT | Update status and metrics |

---

## 🔗 Webhook Management

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/webhook-workbench` | JWT/API Key | List inbound webhooks |
| POST | `/api/webhook-workbench` | JWT/API Key | Create inbound webhook |

**Platforms:** `heyreach`, `woodpecker`, `lemlist`, `generic`

---

## 🗺️ Territory Workbench

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/territory-workbench/companies` | JWT | List aggregated company data (requires `client_id`) |
| POST | `/api/territory-workbench/companies` | JWT | Create or update territory company record |

### List Query Params
`client_id` (required), `sortBy`, `sortDirection`, `industry`, `minLeads`, `maxLeads`, `search`, `startDate`, `endDate`

---

## ⚙️ Settings Management

All settings endpoints require **Cognito JWT** and are scoped by `company_id`.

### URL Settings (Enrichment Service URLs & API Keys)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/settings/url` | Get URL settings |
| POST | `/api/settings/url` | Create URL settings |
| PUT | `/api/settings/url` | Update URL settings |

Fields: `companyUrl`, `emailFinder`, `enrichment1`–`enrichment10` (each with `_Apikey`)

### Agent Settings (EpsimoAI Agent IDs — Copyright)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/settings/agent` | Get agent settings |
| POST | `/api/settings/agent` | Create agent settings |
| PUT | `/api/settings/agent` | Update agent settings |

Fields: `projectId`, `enrichment1AgentId`–`enrichment10AgentId`

### SDR AI Settings (EpsimoAI Agent IDs — SDR AI)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/settings/sdr-ai` | Get SDR AI settings |
| POST | `/api/settings/sdr-ai` | Create SDR AI settings |
| PUT | `/api/settings/sdr-ai` | Update SDR AI settings |

Fields: `projectId`, `message1`–`message10` AgentId, `aiLeadScore`, `aiQualification`, `aiNextAction`, `aiColdEmail`, `aiInterest`, `aiLinkedinConnect`, `aiCompetitorAnalysis`, `aiEngagementLevel`, `aiPurchaseWindow`, `aiDecisionMakerRole`, `aiSentiment`, `aiSocialEngagement`, `aiNurturingStage`, `aiBudgetEstimation`, `aiRiskScore`, `aiProductFitScore` (each as `<fieldName>AgentId`)

---

## 🚀 Lead Processing

Settings-driven execution — only `leadId` is required, all config is resolved from Settings.

| Method | Endpoint | Settings Source | Selector |
|--------|----------|-----------------|----------|
| POST | `/api/leads/process/enrich` | URL Settings | `services[]` (e.g., `["companyUrl", "enrichment1"]`) |
| POST | `/api/leads/process/copyright` | Agent Settings | `processes[]` (e.g., `[1, 3, 5]`) |
| POST | `/api/leads/process/sdr` | SDR AI Settings | `fields[]` (e.g., `["message1", "aiLeadScore"]`) |

All three accept: `leadId` (required), selector (optional — omit to run all configured), `overwrite` (optional, default false).

Response shape: `{ success, runIds[], batchTag, triggered[], skipped[], leadId }`

---

## ⏱️ Background Tasks (Trigger.dev)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/trigger` | Submit enrichment task |
| GET | `/api/trigger-task-status` | Check task status (param: `runId`) |
| GET | `/api/trigger-recent-runs` | List recent runs (param: `limit`) |

---

## ✉️ Email Services

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/email-validate` | Validate email format & deliverability |
| POST | `/api/email-verify` | Deep email verification (SMTP, MX, catch-all) |

---

## 🔌 Integration APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/start-lead-scrape-complete` | Start Apify lead generation actor |
| GET | `/api/lead-generation-status` | Check Apify run status (param: `runId`) |
| POST | `/api/epsimo-chat` | Interact with Epsimo AI assistants |
| GET | `/api/unipile-accounts` | List connected social media accounts |

---

## Error Handling

Standard error shape:
```json
{
  "success": false,
  "error": "Error message",
  "errorType": "authentication_error",
  "details": "Additional error details",
  "recommendation": "Suggested action"
}
```

**Error Types:** `federated_jwt`, `no_valid_tokens`, `token_expired`, `insufficient_permissions`, `owner_mismatch`, `missing_required_field`, `invalid_format`, `not_found`, `already_exists`, `conflict`

**HTTP Status Codes:** 200, 201, 400, 401, 403, 404, 500, 503

---

## Rate Limits

| Tier | Limit |
|------|-------|
| Standard | 100 req/min |
| Premium | 1,000 req/min |

Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## Pagination

- **Standard API:** cursor-based (`limit` + `cursor`/`nextToken`)
- **Bulk API:** token-based (`limit` default 1000, max 5000 + `nextToken`)

---

## Data Isolation

1. **Owner-based** — filtered by authenticated user's `owner` ID
2. **Company-based** — filtered by `company_id`
3. **Client-based** — filtered by `client_id`
