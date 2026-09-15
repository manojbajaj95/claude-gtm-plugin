---
name: vibe-prospecting-enrichment
description: Build ICP prospect lists and enrich B2B companies or contacts with Vibe Prospecting / Explorium data inside Claude. Use when the user asks to find prospects, build a lead list, enrich firmographics or contacts, research accounts before outbound, or connect Explorium or Vibe Prospecting for GTM workflows.
---

# Vibe Prospecting Enrichment

## Workspace Context

Read bootstrap context before asking questions: `strategy/brand.md` for brand, audience, offer, channels, tools, constraints, and metrics; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` for content planning. Use legacy product-marketing context files only as fallback. Save generated drafts to `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md`, and route durable learnings back to `strategy/brand.md`, `about/me.md`, or `content/ideas.md`. Update `PROGRESS.md` each session.

## Operating Contract

This skill is self-contained for its frontmatter scope: use its local instructions, references, scripts, and assets as the playbook; ask only for missing task-specific inputs; hand off to adjacent skills instead of expanding scope; and return an actionable artifact, decision, plan, draft, or diagnostic.

---

Use live B2B data from **Vibe Prospecting** (Explorium) to turn ICP briefs into previewable lists and enriched account or contact tables — then hand off to `outbound-email-strategy`, `lead-generation-and-demand`, or `personalization-at-scale`.

## Prerequisites

- Vibe Prospecting remote MCP connected in the session: `https://vibeprospecting.explorium.ai/mcp` (OAuth browser sign-in; no API key in this skill).
- If missing, point the user to https://vibeprospecting.ai or https://www.explorium.ai install docs, then retry.

## Quick Start

1. **ICP from workspace** — Prefer `strategy/brand.md` audience and ICP; ask only for gaps.
2. **Sample preview** — Pull 5–10 rows; confirm filters before full export.
3. **Export / enrich** — Materialize the approved list; email enrichment by default, phone only when asked.
4. **Handoff** — Pass the table into outbound sequence or personalization skills; log outcomes in `PROGRESS.md`.

## Workflows

### A. List build

Parse titles, seniority, industry, size, geo, tech, and events. Combine title + seniority for people lists. Restate the audience definition after the user approves the preview.

### B. Company enrichment

Resolve by domain when possible. Append firmographics, technographics, funding, and growth signals. Never invent missing fields.

### C. Contact enrichment / shortlist

Rank decision-makers at target accounts. Default to email and profile fields; add phone only for dialer workflows.

## Adjacent skills

- `lead-generation-and-demand` — channel and funnel strategy around the list
- `outbound-email-strategy` — sequences once contacts are enriched
- `personalization-at-scale` — first-line personalization from enrichment signals
- `crm-integration` — push cleaned rows into CRM

## Output checklist

- [ ] Preview shown and filters confirmed
- [ ] Full list or enrichment table delivered
- [ ] Fill-rate / gaps called out honestly
- [ ] `PROGRESS.md` updated with next steps
