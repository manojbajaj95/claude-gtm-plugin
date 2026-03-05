---
title: Strategic Roadmap Planning
impact: HIGH
tags: roadmap, planning, strategy, prioritization
---

## Strategic Roadmap Planning

**Impact: HIGH**

A roadmap is strategy made visible. It's not a commitment to ship specific features — it's a communication tool that shows how you'll achieve your strategy.

### Roadmap Types

| Type | Audience | Time Horizon | Detail Level |
|------|----------|--------------|--------------|
| **Vision** | Board, investors | 2-5 years | Themes only |
| **Strategic** | Leadership | 1-2 years | Initiatives |
| **Product** | Team, customers | 3-12 months | Epics, features |
| **Release** | Engineering | 1-3 months | Stories, tasks |

### Roadmap Anatomy

```
VISION (2-5 years)
"Where we're going"
├── THEME 1: Become enterprise-ready
├── THEME 2: Expand to new verticals
└── THEME 3: Build platform ecosystem

STRATEGIC (1 year)
"Major bets for the year"
├── Q1-Q2: Security & compliance features
├── Q2-Q3: Healthcare vertical launch
└── Q3-Q4: API & integrations platform

PRODUCT (Quarters)
"What we're building"
├── Now: SSO/SAML, audit logging
├── Next: HIPAA compliance, healthcare templates
└── Later: Public API, developer portal
```

### Theme-Based Roadmapping

**Why themes over features:**
- Allows flexibility in execution
- Communicates intent without commitment
- Enables customer feedback on direction
- Avoids the "feature factory" trap

**Good Themes:**
```
✓ "Enterprise-ready security"
✓ "Self-serve onboarding excellence"
✓ "Mobile-first experience"
✓ "Platform extensibility"
```

**Bad Themes (Too Specific):**
```
✗ "Build SSO with SAML support"
✗ "Add dark mode and 10 new integrations"
✗ "Migrate to new database"
```

### Roadmap Pillars

**Balance roadmap across dimensions:**

| Pillar | Purpose | Typical % |
|--------|---------|-----------|
| **New Value** | New features, capabilities | 40-50% |
| **Improve Existing** | Quality, performance, UX | 20-30% |
| **Technical Foundation** | Infrastructure, scale | 15-25% |
| **Risk Reduction** | Security, compliance | 10-15% |

### Now/Next/Later Framework

| Horizon | Time | Confidence | Detail |
|---------|------|------------|--------|
| **Now** | Current quarter | High (80%+) | Specific features |
| **Next** | Next quarter | Medium (50%) | Initiatives |
| **Later** | Future quarters | Low (30%) | Themes only |

```
NOW (This Quarter)
├── SSO with SAML/OIDC
├── Audit logging for compliance
└── Self-serve team management

NEXT (Next Quarter)
├── SOC 2 Type II certification
├── Role-based access controls
└── Security dashboard

LATER (Future)
├── Enterprise security suite
├── Advanced compliance features
└── Security integrations
```

### Roadmap Inputs

**Balanced input framework:**

| Input | Weight | Source |
|-------|--------|--------|
| **Strategy alignment** | 30% | Company OKRs, vision |
| **Customer requests** | 25% | Support, CS, surveys |
| **Market/competitive** | 20% | Competitors, analysts |
| **Technical debt** | 15% | Engineering assessment |
| **Team input** | 10% | Internal ideas, research |

### Customer Feedback Integration

**How to process feature requests:**

```
Feedback Funnel:

All Requests (1000)
      │
      ▼
Validated Requests (200)  ← "Would they pay for this?"
      │
      ▼
Strategic Fit (50)        ← "Does this align with vision?"
      │
      ▼
Prioritized (10)          ← "What's the impact/effort?"
      │
      ▼
Roadmap (5)              ← "What makes the cut?"
```

### Stakeholder Communication

**What different audiences need:**

| Audience | Show Them | Don't Show |
|----------|-----------|------------|
| **Board** | Vision themes, strategic bets | Feature details |
| **Customers** | Value delivered, timing ranges | Technical details |
| **Sales** | What to sell, rough timing | Exact dates |
| **Engineering** | Clear priorities, context | Marketing spin |
| **Marketing** | Narrative, differentiators | Technical debt |

### Roadmap Artifacts

**External Roadmap (Customers):**
```
Theme-based, quarter-level, no specific dates
"In Q2, we're focused on enterprise security"
```

**Internal Roadmap (Team):**
```
Feature-level, milestone-based, clear owners
"SSO ships March 15, owned by Platform team"
```

**Board Roadmap:**
```
Strategic themes, annual view, metrics
"Enterprise segment = 40% of 2024 focus"
```

### Roadmap Review Cadence

| Meeting | Frequency | Focus |
|---------|-----------|-------|
| **Sprint planning** | Weekly/bi-weekly | What's shipping now |
| **Product review** | Monthly | Progress on current quarter |
| **Roadmap review** | Quarterly | Adjust next 2-4 quarters |
| **Strategy review** | Annually | Annual themes, vision update |

### Roadmap vs Backlog

| Roadmap | Backlog |
|---------|---------|
| Strategic, themed | Tactical, specific |
| Quarter/year horizon | Sprint horizon |
| "What" and "why" | "How" |
| PM owns | Team owns |
| Customer-facing | Internal |

### Saying No

**How to decline roadmap requests:**

```
Good: "That's not on our roadmap for the next two quarters
       because we're focused on [strategic priority]. We'll
       revisit in Q3 when we plan the second half."

Bad:  "We can't do that."
Bad:  "Maybe someday."
Bad:  "Let me add it to the backlog." (and forget it)
```

### Roadmap Anti-Patterns

- **Date-driven roadmap** — Commitments to dates, not outcomes
- **Feature factory** — List of features without strategic context
- **Customer-driven only** — Building whatever loudest customers want
- **Static roadmap** — Never updating as you learn
- **Secret roadmap** — Team doesn't know the plan
- **Overcommitted roadmap** — 200% of capacity planned
- **No roadmap** — Purely reactive, no proactive direction
- **Competitor roadmap** — Just copying competitor features
- **Roadmap as promise** — Treating themes as commitments
- **Kitchen sink** — Everything on roadmap, no prioritization
