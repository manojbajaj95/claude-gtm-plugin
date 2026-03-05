---
name: startup-go-to-market
description: Use when designing go-to-market strategy, selecting GTM motion (PLG/sales-led), defining ICP, planning product launches, or implementing AI-powered GTM automation. Covers channel selection, growth loops, RevOps alignment, and market entry execution.
---

# Startup Go-to-Market

Systematic workflow for designing and executing market entry, launch, and growth.

**Modern Best Practices (Jan 2026)**: Start from ICP + positioning, pick 1-2 channels to sequence, instrument the funnel end-to-end, use AI for execution (not strategy), align RevOps across sales/marketing/CS.

---

## When to Use

- Designing go-to-market strategy for new product
- Choosing between PLG and sales-led motion
- Planning product launches (soft, beta, ProductHunt, full)
- Defining ICP and channel strategy
- Implementing AI-powered GTM automation

## When NOT to Use

- Positioning and messaging deep dive -> [marketing-content-strategy](../marketing-content-strategy/) (use [startup-competitive-analysis](../startup-competitive-analysis/) for differentiation inputs)
- Competitive intelligence -> [startup-competitive-analysis](../startup-competitive-analysis/)
- Fundraising strategy -> [startup-fundraising](../startup-fundraising/)
- Pricing and revenue models -> [startup-business-models](../startup-business-models/)

---

## Quick Start (Inputs)

Ask for the smallest set of inputs that makes decisions meaningful:

- Stage: pre-PMF, early PMF, growth, scale
- Product and category: what it is, who uses it, and what "first value" looks like
- ICP and buyer: firmographics, pains, procurement constraints, economic buyer vs champion
- Pricing and economics: current/target ACV/ARPA, COGS drivers (include variable compute), payback constraints
- Motion constraints: self-serve possible, sales cycle expectations, implementation/onboarding complexity
- Channel constraints: budget, time, audience access (communities, lists, partnerships), geo, compliance limits
- Baseline metrics: traffic, signup/demo rate, activation, retention, win rate, sales cycle length, pipeline
- Team and tooling: who executes (founder/marketing/sales/CS), CRM + analytics stack

If numbers are missing, proceed with ranges + explicit assumptions and list what to measure next.

## Workflow

1) Define ICP and the buying path
- Primary/secondary ICP, anti-ICP, trigger events, and an "activation" definition.
- Use `assets/icp-definition.md` to draft.

2) Align on positioning and proof
- If positioning is unclear, use [startup-competitive-analysis](../startup-competitive-analysis/) to map alternatives + differentiation, then [marketing-content-strategy](../marketing-content-strategy/) to express it as messaging.

3) Choose the motion (PLG / sales-led / hybrid)
- Use the decision tree below for a fast cut.
- For details: `references/plg-implementation.md` and `references/sales-motion-design.md`.

4) Pick 1-2 channels to sequence (not parallelize)
- Use a bullseye-style test plan: quick tests, measure, double down.
- For execution details: `references/channel-playbooks.md`.

5) Define measurement and RevOps alignment
- Define shared lifecycle stages and the "one source of truth" for metrics (product + CRM).
- Ensure handoffs are measurable (e.g., PQL -> SQL routing rules and SLAs for hybrid).

6) Produce deliverables + operating cadence
- Draft GTM plan (`assets/gtm-strategy.md`) and launch plan (`assets/launch-playbook.md`).
- Run a weekly GTM review: 30 minutes on pipeline + funnel, 30 minutes on experiments, 30 minutes on decisions.

---

## Decision Tree

```
GTM QUESTION
  |-- "How do I reach customers?" -> Channel Strategy
  |-- "PLG or Sales-led?" -> Motion Selection
  |-- "How do I launch?" -> Launch Planning
  |-- "Who is my ICP?" -> Segmentation
  `-- "How do I scale?" -> Growth Loops
```

---

## GTM Motion Types

| Motion | Description | Best For | Examples |
|--------|-------------|----------|----------|
| **PLG** | Product drives acquisition, conversion, expansion | SMB, developers | Slack, Figma |
| **Hybrid (PLG + Sales-Assist)** | Product drives acquisition; sales assists conversion/expansion | Mid-market, higher ACV PLG | Atlassian, Notion |
| **Sales-Led** | Reps drive deals through outbound/inbound | Enterprise, complex sales | Salesforce |
| **Community-Led** | Community drives awareness and adoption | Developer tools, OSS | MongoDB |
| **Partner-Led** | Partners drive distribution | Enterprise, geographic expansion | Microsoft |

### Motion Selection Framework

```
ACV < $5K and self-serve possible?
  - yes: PLG (add sales-assist for expansion)
  - no: is buyer technical?
      - yes: developer/community-led (bottom-up)
      - no: sales-led
```

---

## ICP Components

| Component | Questions | Example |
|-----------|-----------|---------|
| **Firmographics** | Size, industry, geography | 50-500 employees, B2B SaaS, US |
| **Technographics** | Tech stack, tools | Uses Salesforce, modern data stack |
| **Pain indicators** | Symptoms of problem | Growing support tickets |
| **Success indicators** | Signs of good fit | Strong product-market alignment |

### ICP Scoring

| Factor | Weight |
|--------|--------|
| Budget available | 20% |
| Problem severity | 25% |
| Technical fit | 15% |
| Decision timeline | 15% |
| Champion identified | 15% |
| Expansion potential | 10% |

---

## Channel Strategy

| Category | Channels | Best For |
|----------|----------|----------|
| **Organic** | SEO, content, social, community | Long-term |
| **Paid** | SEM, paid social, display | Fast, scalable |
| **Outbound** | Email, cold calls, LinkedIn | Enterprise, high ACV |
| **Product** | Viral, freemium, PLG | Self-serve |

### Channel Sequencing by Stage

| Stage | Primary Channels |
|-------|------------------|
| Pre-PMF | Founder sales, communities |
| Early | Content, outbound, founder network |
| Growth | Paid, SEO, partnerships |
| Scale | All channels optimized |

---

## Measurement (Minimum Viable GTM Analytics)

- Prefer lifecycle + cohorts over vanity metrics. Always break down by ICP/segment + channel.
- Define a single funnel per motion (PLG vs sales-led) with clear stage definitions and owners.
- Track leading indicators (activation/retention, PQL, win rate) before "scale" decisions.

**PQL (Product Qualified Lead) Score**:
```
PQL = (Engagement * 0.4) + (Fit * 0.3) + (Intent * 0.3)
```

### Product-Led Sales (Sales-Assist) Basics

Use when PLG brings users in, but conversion/expansion benefits from a human touch.

**PQL -> SQL routing checklist**:
- [ ] Define PQL triggers (events) and thresholds (e.g., 3 key actions in 7 days)
- [ ] Define disqualifiers (students, competitors, tiny companies, unsupported geo)
- [ ] Set an SLA for first touch (e.g., <24 hours for high-intent PQLs)
- [ ] Define handoff criteria to AE (PQL -> meeting booked, security/procurement requested)
- [ ] Instrument outcomes (PQL->meeting->pipeline->won) and review weekly

---

## Launch Types

| Type | Goal | Timeline |
|------|------|----------|
| **Soft launch** | Test, iterate | 2-4 weeks |
| **Beta launch** | Build waitlist, feedback | 4-8 weeks |
| **ProductHunt** | Awareness, early adopters | 1 day + prep |
| **Full launch** | Maximum awareness | 1-2 weeks |

---

## Growth Loops

| Loop | Mechanism | Example |
|------|-----------|---------|
| **Viral** | User invites users | Dropbox referrals |
| **Content** | Content -> SEO -> Users | HubSpot |
| **UGC** | Users create content | YouTube |
| **Paid** | Revenue -> Ads -> Users | Performance marketing |
| **Sales** | Pipeline -> close -> revenue -> hiring -> more pipeline | Sales-led SaaS |
| **Partner** | Enable partners -> referrals -> deals -> partner revenue -> more partners | Cloud marketplaces |

---

## Do / Avoid

### Do

- Define activation as concrete "first value moment"
- Track leading indicators (activation, PQL, retention)
- Use AI for execution while humans own strategy
- Tier ICP based on fit + intent signals

### Avoid

- Content spam without measurement
- "Do all channels" in parallel
- Vanity metrics without retention context
- Over-automating without human oversight
- Scaling paid before activation/retention is stable
- Treating benchmarks as targets without segmenting by ICP/channel

---

## Resources

| Resource | Purpose |
|----------|---------|
| [channel-playbooks.md](references/channel-playbooks.md) | Detailed channel execution |
| [sales-motion-design.md](references/sales-motion-design.md) | Sales process + RevOps |
| [plg-implementation.md](references/plg-implementation.md) | PLG execution + PQL frameworks |
| [ai-gtm-automation.md](references/ai-gtm-automation.md) | AI-powered GTM tools |

## Templates

| Template | Purpose |
|----------|---------|
| [gtm-strategy.md](assets/gtm-strategy.md) | Full GTM strategy document |
| [launch-playbook.md](assets/launch-playbook.md) | Launch planning |
| [icp-definition.md](assets/icp-definition.md) | ICP documentation |

## Data

| File | Purpose |
|------|---------|
| [sources.json](data/sources.json) | GTM resources |

---

## Related Skills

| Skill | Use For |
|-------|---------|
| [startup-competitive-analysis](../startup-competitive-analysis/) | Market mapping, battlecards |
| [startup-business-models](../startup-business-models/) | Pricing, unit economics |
| [marketing-ai-search-optimization](../marketing-ai-search-optimization/) | GEO/AI search visibility for content-led GTM |
| [marketing-social-media](../marketing-social-media/) | Social channel execution |
| [marketing-leads-generation](../marketing-leads-generation/) | Lead acquisition |

---

## What Good Looks Like

- One primary ICP with clear anti-ICP and measurable triggers (signals) for targeting.
- A motion decision with explicit economics (ACV, payback, touch model) and defined handoffs.
- One primary channel with a test plan, success metrics, and stop/pivot triggers.
- Instrumented funnel from source -> activation/value -> revenue/expansion (by segment + channel).
- A weekly operating cadence with a backlog of experiments and a written decision log.
