---
title: Market Opportunity Sizing (TAM/SAM/SOM)
impact: CRITICAL
tags: market, tam, sam, som, opportunity, sizing
---

## Market Opportunity Sizing (TAM/SAM/SOM)

**Impact: CRITICAL**

Market sizing isn't about impressing investors with big numbers. It's about understanding where you can realistically win and how big the opportunity truly is.

### The TAM/SAM/SOM Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                            TAM                                  │
│                  Total Addressable Market                       │
│        "If we had 100% market share, how big?"                  │
│                                                                 │
│    ┌───────────────────────────────────────────────────┐       │
│    │                       SAM                          │       │
│    │            Serviceable Addressable Market          │       │
│    │       "Segment we can actually reach & serve"      │       │
│    │                                                    │       │
│    │    ┌────────────────────────────────────┐         │       │
│    │    │              SOM                    │         │       │
│    │    │      Serviceable Obtainable Market  │         │       │
│    │    │    "Realistic capture in 3-5 years" │         │       │
│    │    └────────────────────────────────────┘         │       │
│    └───────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
```

### TAM Calculation Methods

**1. Top-Down (Quick, less accurate)**
Start with industry reports, narrow down.

```
Example: Project Management Software

Global software market:           $500B
× Enterprise software %:          × 20%   = $100B
× Productivity software %:        × 15%   = $15B
× Project management %:           × 25%   = $3.75B TAM
```

**2. Bottom-Up (More work, more accurate)**
Build from unit economics up.

```
Example: Project Management Software

Companies with 50+ employees:         500,000 globally
× Avg seats per company:              × 50
= Total potential seats:              25,000,000
× Price per seat per year:            × $120
= TAM:                                $3B
```

**3. Value-Theory (Best for new categories)**
Calculate based on value delivered.

```
Example: AI Code Assistant

Developer hours saved per week:       5 hours
× Developer hourly cost:              × $75
× Weeks per year:                     × 50
= Value per developer per year:       $18,750
× Developers globally:                × 30M
× Willingness to pay (10%):           × 10%
= TAM:                                $56B
```

### SAM Refinement

**SAM = TAM × Filters**

| Filter | Question | Example |
|--------|----------|---------|
| **Geography** | Where can we sell? | North America only = 40% |
| **Company size** | Who's our ICP? | Mid-market 100-1000 = 25% |
| **Vertical** | Which industries? | Tech + Finance = 30% |
| **Budget** | Can they afford us? | >$5k budget = 60% |
| **Technology** | Compatible stack? | Cloud-native = 50% |

```
SAM Calculation Example:

TAM:                    $3B
× Geography (NA):       × 40%    = $1.2B
× Company size:         × 25%    = $300M
× Has budget:           × 60%    = $180M SAM
```

### SOM Reality Check

**SOM answers:** "What can we realistically capture in 3-5 years?"

| Factor | Question | Typical Range |
|--------|----------|---------------|
| **Market share** | What % can a leader achieve? | 10-30% |
| **Competition** | How fragmented is market? | Adjust down if concentrated |
| **Sales capacity** | How much can you sell? | Based on team size |
| **Product readiness** | How complete is product? | Adjust down if early |

```
SOM Calculation Example:

SAM:                    $180M
× Realistic share (15%): × 15%
= SOM:                  $27M in 3-5 years
```

### Market Sizing Sanity Checks

**The "So What?" Tests:**

| Check | Calculation | Red Flag |
|-------|-------------|----------|
| **VC Math** | SOM × 10 = viable exit? | SOM < $50M |
| **Bootstrap Math** | Can SOM support lifestyle? | SOM < $5M |
| **Growth Math** | Can you 10x in 5 years? | TAM < 20× current |
| **Share Math** | Is 10% share achievable? | Requires >50% share |

### Good vs Bad Market Sizing

**Good Sizing (Investor-Ready):**
```
TAM: $15B
- Global enterprise communication tools
- Source: Gartner 2024, growing 12% CAGR

SAM: $3B
- Mid-market companies (100-1000 employees)
- North America and Europe
- Technology and professional services verticals

SOM: $150M (Year 5)
- 5% of SAM
- Based on comparable company trajectories
- Assumes $50M ARR current → $150M ARR
```

**Bad Sizing (Red Flags):**
```
TAM: $500B
- "If every company in the world uses us..."

SAM: $100B
- "Everyone who uses computers..."

SOM: $10B
- "We just need 2% of the market"
```

### Market Dynamics to Consider

**Growing vs Shrinking Markets:**

| Market Type | Strategy Implication |
|-------------|---------------------|
| **Growing 20%+ CAGR** | Land grab, first-mover advantage |
| **Growing 5-20% CAGR** | Sustainable, focus on differentiation |
| **Flat 0-5%** | Zero-sum, must steal share |
| **Declining** | Avoid, or find growing sub-segment |

**Fragmented vs Concentrated:**

| Market Type | Opportunity |
|-------------|-------------|
| **Fragmented** (no leader >10%) | Category creation opportunity |
| **Concentrated** (1-2 leaders >50%) | Niche or disruption required |
| **Consolidating** | M&A target potential |

### Adjacent Market Expansion

```
            ┌─────────────────┐
            │   CORE MARKET   │
            │   (Start Here)  │
            └────────┬────────┘
                     │
         ┌──────────┴──────────┐
         │                      │
    ┌────▼────┐           ┌────▼────┐
    │ ADJACENT │           │ ADJACENT │
    │ MARKET A │           │ MARKET B │
    │ (Geo)    │           │ (Product)│
    └────┬────┘           └────┬────┘
         │                      │
         └──────────┬──────────┘
                    │
              ┌─────▼─────┐
              │  ADJACENT  │
              │  MARKET C  │
              │  (Segment) │
              └────────────┘
```

**Expansion Types:**
- **Geographic:** NA → Europe → APAC
- **Segment:** SMB → Mid-market → Enterprise
- **Product:** Core → Adjacent features → Platform

### Investor-Ready Market Analysis

**What investors want to see:**

```
1. Bottom-up TAM with clear assumptions
2. SAM that matches your current product
3. SOM that's achievable in 3-5 years
4. Clear path from SOM → SAM (expansion story)
5. Growing market (10%+ CAGR)
6. Credible data sources cited
```

### Anti-Patterns

- **TAM theater** — Using absurdly large numbers to impress
- **Top-down only** — "It's a $100B market, we just need 1%"
- **Ignoring competition** — Sizing without competitive context
- **Static sizing** — Not accounting for market growth/decline
- **One-time sizing** — Markets change; re-assess annually
- **SAM = TAM** — No meaningful segmentation
- **SOM optimism** — Assuming unrealistic market share
- **Category confusion** — Mixing categories to inflate numbers
