---
title: Product Strategy Frameworks
impact: HIGH
tags: strategy, frameworks, prioritization, decision-making
---

## Product Strategy Frameworks

**Impact: HIGH**

Strategy is the art of making choices. Good frameworks help you make better choices faster — and explain them to others.

### The Strategy Stack

```
VISION      →  "Where are we going?"            (3-10 years)
                Aspirational, inspiring

STRATEGY    →  "How will we get there?"         (1-3 years)
                Trade-offs, focus areas

ROADMAP     →  "What are we building?"          (Quarters)
                Prioritized initiatives

OKRs        →  "How do we measure progress?"    (Quarterly)
                Objectives and key results

SPRINTS     →  "What are we doing this week?"   (Weeks)
                Tasks and deliverables
```

### Strategy Definition

**Good strategy has three parts:**
1. **Diagnosis** — What's the challenge?
2. **Guiding Policy** — What's our approach?
3. **Coherent Actions** — What will we do?

**Example:**
```
Diagnosis:      Enterprise customers want to buy but our product
                lacks SOC 2 compliance and SSO.

Guiding Policy: We will become enterprise-ready in 2024 by
                prioritizing security and compliance features
                over new functionality.

Coherent Actions:
1. Achieve SOC 2 Type II by Q2
2. Ship SSO with SAML/OIDC by Q1
3. Add audit logging by Q2
4. Hire compliance lead by Q1
```

### Prioritization Frameworks

**1. RICE Scoring**

| Factor | Question | Scale |
|--------|----------|-------|
| **Reach** | How many users impacted? | # per quarter |
| **Impact** | How much impact per user? | 0.25-3 |
| **Confidence** | How sure are we? | 0-100% |
| **Effort** | How much work? | Person-months |

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

**2. Value vs Effort Matrix**

```
                    High Value
                        │
              ┌─────────┼─────────┐
              │ QUICK   │  BIG    │
              │ WINS    │  BETS   │
   Low ───────┼─────────┼─────────┼─────── High
   Effort     │ DON'T   │  TIME   │  Effort
              │ BOTHER  │  SINKS  │
              └─────────┼─────────┘
                        │
                    Low Value
```

**3. The MoSCoW Method**

| Priority | Description | Ratio |
|----------|-------------|-------|
| **Must Have** | Non-negotiable, product fails without | 60% |
| **Should Have** | Important, but can work around | 20% |
| **Could Have** | Nice to have, enhances | 10% |
| **Won't Have** | Out of scope for now | 10% |

### Strategic Trade-off Framework

For every decision, identify what you're trading:

| Dimension | Trade-off |
|-----------|-----------|
| **Speed vs Quality** | Ship fast or ship polished? |
| **Breadth vs Depth** | More features or better features? |
| **SMB vs Enterprise** | Self-serve or high-touch? |
| **Growth vs Profit** | Invest or harvest? |
| **Build vs Buy** | Own or leverage? |

**Good strategy makes trade-offs explicit:**
```
"We choose depth over breadth — we will be the best at
X rather than good at X, Y, and Z."
```

### Decision Making Framework

**Type 1 vs Type 2 Decisions:**

| Type | Characteristics | Process |
|------|-----------------|---------|
| **Type 1** | Irreversible, high stakes | Deliberate, gather input |
| **Type 2** | Reversible, lower stakes | Decide quickly, iterate |

**Examples:**
```
Type 1 (Go Slow):
- Business model change
- Major platform decisions
- Entering new markets
- Pricing architecture

Type 2 (Go Fast):
- Feature prioritization
- UI/UX decisions
- Pricing levels
- Marketing experiments
```

### Porter's Five Forces (Simplified)

| Force | Question | High = Bad for You |
|-------|----------|-------------------|
| **Rivalry** | How intense is competition? | Many competitors, slow growth |
| **New Entrants** | How easy to enter? | Low barriers, low capital |
| **Substitutes** | What else solves this? | Many alternatives exist |
| **Buyer Power** | Can buyers dictate terms? | Few big buyers, commoditized |
| **Supplier Power** | Can suppliers dictate terms? | Few suppliers, unique inputs |

### Jobs to Be Done Framework

**Focus on the job, not the solution:**

```
Traditional:    "We need to add a calendar feature"

JTBD:           "When I'm scheduling a meeting, I want to
                avoid back-and-forth emails, so I can
                book meetings in one interaction"
```

**JTBD Template:**
When [situation], I want to [motivation], so I can [outcome].

### Strategy Validation Checklist

Before committing to a strategy:

```
□ Does this support our vision?
□ Is this achievable with our resources?
□ Does this address our biggest challenge?
□ Are trade-offs explicit?
□ Can we measure progress?
□ Do we have conviction? (Would we bet the company?)
□ Is the team aligned?
□ Can we explain it in one sentence?
```

### Quarterly Strategy Review

| Question | Check |
|----------|-------|
| Are we on track to goals? | Review OKRs |
| Is the market changing? | Competitive intel |
| Are assumptions still true? | Validate hypotheses |
| What did we learn? | Retrospective insights |
| Should strategy change? | Adjust or stay course |

### Anti-Patterns

- **Strategy as planning** — Plans aren't strategy; strategy is choices
- **Strategy by consensus** — Trying to make everyone happy
- **Too many priorities** — If everything is a priority, nothing is
- **Copying competitors** — Reactive, not proactive
- **Strategy without trade-offs** — "We'll do both" isn't strategy
- **Annual-only planning** — Strategy needs continuous refinement
- **Mistaking tactics for strategy** — "Launch on ProductHunt" is a tactic
- **No diagnosis** — Jumping to solutions without understanding problems
