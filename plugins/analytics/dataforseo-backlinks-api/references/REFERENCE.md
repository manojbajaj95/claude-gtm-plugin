# DataForSEO Core Integration Reference

This file contains shared, language-agnostic integration guidance for DataForSEO API v3.

## Base URLs

- Production: `https://api.dataforseo.com/` (all endpoints are under `/v3/...`)
- Sandbox: `https://sandbox.dataforseo.com/` (test most endpoints for free)

Sandbox note:
- Sandbox uses a dynamic path pattern: `POST https://sandbox.dataforseo.com/v3/$path`
- Docs: https://docs.dataforseo.com/v3/appendix/sandbox/

## Authentication (HTTP Basic)

- Use HTTP Basic Auth with your DataForSEO credentials (API Access): https://app.dataforseo.com/api-access
- Header format: `Authorization: Basic base64(login:password)`
- Docs: https://docs.dataforseo.com/v3/auth/

## Standard Response Envelope and Error Handling

- Do not rely on HTTP status alone. Many endpoints return HTTP `200` even for application-level errors.
- Always validate:
  - top-level `status_code` and `status_message`
  - each `tasks[]` item `status_code` and `status_message`
- Treat any `status_code != 20000` as a failure.
- Surface errors with:
  - `status_code`, `status_message`
  - task identifier (`tasks[].id`) when present

Docs:
- Status codes: https://docs.dataforseo.com/v3/appendix/status/
- Errors: https://docs.dataforseo.com/v3/appendix/errors/

## Live vs Task-based Endpoints

- Live endpoints return results in one call (synchronous).
- Task-based endpoints are asynchronous and typically follow:
  1) `task_post`
  2) `tasks_ready` (poll until ready)
  3) `task_get` (fetch final results)

Implementation guidance:
- Store `tasks[].id` so results can be retrieved later.
- Prefer task-based endpoints for scheduled or high-volume workloads.

## Webhooks (postback_url / pingback_url)

- Many task endpoints support webhook callbacks.
- Use callbacks to avoid polling when possible.
- Treat callbacks as signals; fetch the canonical final data via `task_get`.

## AI-optimized Responses (.ai)

- Many endpoints support appending `.ai` to the end of the endpoint URL.
- This returns a cropped response optimized for LLM usage.
- Docs: https://docs.dataforseo.com/v3/appendix/ai_optimized_response/

## Reliability

- Implement retries with exponential backoff on transient failures (timeouts, connection resets, 429/5xx).
- Use idempotency by storing task IDs and not re-posting tasks unnecessarily.
- Log the raw request/response (redacting credentials) for debugging.

## Data Handling and Compliance

- Avoid collecting unnecessary personal data.
- Store only what you need and apply reasonable retention.
- Respect customer and platform terms.
