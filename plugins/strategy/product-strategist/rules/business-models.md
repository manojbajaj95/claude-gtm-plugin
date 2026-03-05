---
title: Business Model Design
impact: HIGH
tags: business-model, revenue, pricing, monetization
---

## Business Model Design

**Impact: HIGH**

Your business model is how you create, deliver, and capture value. Get it right and everything else gets easier. Get it wrong and you'll struggle no matter how good your product is.

### Business Model Canvas

```
┌─────────────────┬─────────────────┬─────────────────┐
│   KEY           │   VALUE         │   CUSTOMER      │
│   PARTNERS      │   PROPOSITION   │   RELATIONSHIPS │
│                 │                 │                 │
│   Who helps us  │   What unique   │   How do we     │
│   deliver?      │   value?        │   acquire and   │
│                 │                 │   retain?       │
├─────────────────┼─────────────────┼─────────────────┤
│   KEY           │                 │   CHANNELS      │
│   ACTIVITIES    │   [VALUE]       │                 │
│                 │                 │   How do we     │
│   What do we    │                 │   reach         │
│   do?           │                 │   customers?    │
├─────────────────┼─────────────────┼─────────────────┤
│   KEY           │                 │   CUSTOMER      │
│   RESOURCES     │                 │   SEGMENTS      │
│                 │                 │                 │
│   What do we    │                 │   Who do we     │
│   need?         │                 │   serve?        │
├─────────────────┴─────────────────┼─────────────────┤
│        COST STRUCTURE             │ REVENUE STREAMS │
│                                   │                 │
│   What are our major costs?       │ How do we make  │
│                                   │ money?          │
└───────────────────────────────────┴─────────────────┘
```

### SaaS Business Models

| Model | How It Works | Best For | Example |
|-------|-------------|----------|---------|
| **Subscription** | Monthly/annual recurring fee | Predictable value | Netflix, Slack |
| **Usage-Based** | Pay for what you use | Variable consumption | AWS, Twilio |
| **Freemium** | Free tier + paid upgrades | Viral products | Spotify, Notion |
| **Per-Seat** | Price per user | Team collaboration | Salesforce, Figma |
| **Tiered** | Feature-gated pricing | Diverse segments | HubSpot, GitHub |
| **Hybrid** | Base + usage | Complex value delivery | Snowflake |

### Revenue Model Spectrum

```
Fixed Recurring ─────────────────────────────── Variable/Usage
       │                                               │
   Subscription                                    Usage-Based
   Per-seat                                        Per-transaction
   Platform fee                                    Consumption
       │                                               │
   Predictable                                     Scalable
   Easy to plan                                    Aligns with value
   May limit growth                                Hard to forecast
```

### Choosing Your Revenue Model

| Factor | Subscription Better | Usage-Based Better |
|--------|---------------------|-------------------|
| **Value delivery** | Consistent over time | Variable by usage |
| **Customer type** | Budget-conscious | Value-focused |
| **Sales cycle** | Simple, self-serve | Complex, negotiated |
| **Cost structure** | Fixed costs | Variable costs |
| **Competition** | Commoditized market | Differentiated value |

### Freemium Strategy

**When freemium works:**
- Large TAM (need volume)
- Low marginal cost per user
- Network effects present
- Clear upgrade trigger

**Freemium conversion funnel:**

```
Free Users:          100,000
Active (monthly):    30,000   (30%)
Engaged (weekly):    10,000   (10%)
Power Users:         3,000    (3%)
Paid Converts:       1,500    (1.5%)
```

**Free vs Paid Feature Splits:**

| Keep Free | Gate for Paid |
|-----------|---------------|
| Core value prop | Advanced features |
| Individual use | Team features |
| Basic limits | Higher limits |
| Community support | Priority support |

### Unit Economics

**Key Metrics:**

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| **CAC** | Sales + Marketing / New Customers | Varies by ACV |
| **LTV** | ARPU × Gross Margin × (1/Churn) | > 3× CAC |
| **Payback** | CAC / (ARPU × Gross Margin) | < 12 months |
| **Gross Margin** | (Revenue - COGS) / Revenue | > 70% |
| **Net Revenue Retention** | (MRR + Expansion - Churn) / MRR | > 100% |

**The Golden Ratio:**
```
LTV : CAC > 3:1
(If LTV is $3,000, CAC should be < $1,000)
```

### Pricing Architecture

**Build pricing that scales:**

```
            ENTERPRISE
           ┌──────────┐
           │ Custom   │  ← High-touch, negotiated
           │ pricing  │
           └────┬─────┘
         BUSINESS
        ┌────────────┐
        │ $XXX/month │  ← Self-serve, annual option
        └────┬───────┘
       PRO/TEAM
      ┌──────────────┐
      │ $XX/month    │  ← Entry point for paid
      └────┬─────────┘
     FREE/STARTER
    ┌────────────────┐
    │ $0             │  ← Lead generation
    └────────────────┘
```

### Value-Based Pricing Framework

**Price = Value Delivered × Willingness to Pay**

| Step | Action |
|------|--------|
| 1 | Calculate customer's problem cost |
| 2 | Estimate value your solution provides |
| 3 | Price at 10-20% of value delivered |
| 4 | Validate with customer interviews |

**Example:**
```
Customer problem cost:     $100,000/year (lost productivity)
Your solution value:       $60,000/year saved (60%)
Price at 15% of value:     $9,000/year
```

### Monetization Timing

| Stage | Monetization Strategy |
|-------|----------------------|
| **Pre-PMF** | Don't optimize pricing; focus on PMF |
| **Early PMF** | Simple pricing, learn from customers |
| **Growth** | Tier pricing, expand segments |
| **Scale** | Optimize pricing, usage-based expansion |

### Business Model Innovation Examples

**Disruption Patterns:**

| From | To | Example |
|------|-----|---------|
| One-time purchase | Subscription | Adobe Creative Suite → Creative Cloud |
| Per-seat | Usage-based | Traditional licensing → Snowflake |
| Product | Platform | Salesforce CRM → Salesforce Platform |
| License | Freemium | Oracle → MongoDB |
| Custom pricing | Transparent | Enterprise software → Stripe |

### Anti-Patterns

- **Monetizing too early** — Charging before value is proven
- **Monetizing too late** — Free forever, can't convert
- **Complex pricing** — Customers can't understand/estimate
- **Value misalignment** — Charging for things customers don't value
- **One-size-fits-all** — Same price for SMB and Enterprise
- **Per-seat when value isn't per-person** — Analytics tools charging per seat
- **Ignoring unit economics** — Growing at negative margins
- **Pricing by cost** — Instead of by value delivered
- **Never changing pricing** — Markets and value evolve
