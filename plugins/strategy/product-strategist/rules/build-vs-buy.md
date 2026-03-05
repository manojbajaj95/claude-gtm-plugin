---
title: Build vs Buy vs Partner
impact: MEDIUM-HIGH
tags: build, buy, partner, make-vs-buy, strategy
---

## Build vs Buy vs Partner

**Impact: MEDIUM-HIGH**

Every feature is a choice: build it yourself, buy a solution, or partner with someone who has it. The right choice depends on strategy, not just cost.

### The Build/Buy/Partner Framework

```
                            STRATEGIC IMPORTANCE
                   Low ──────────────────────────── High
                    │                                │
        ┌───────────┴────────────┬───────────────────┴───────────┐
        │                        │                               │
    BUY/PARTNER              EVALUATE                         BUILD
        │                        │                               │
    Commodity                 Important but                Core to
    Not differentiating       not core                     value prop
        │                        │                               │
    Examples:                 Examples:                    Examples:
    - Auth (Auth0)            - Billing (Stripe)           - Core product
    - Email (SendGrid)        - Analytics (Mixpanel)       - Key differentiators
    - Monitoring (Datadog)    - Search (Algolia)           - Unique algorithms
```

### Decision Matrix

| Factor | Build | Buy | Partner |
|--------|-------|-----|---------|
| **Strategic value** | Core differentiator | Commodity | Complementary |
| **Time to market** | Slow (months) | Fast (days) | Medium (weeks) |
| **Upfront cost** | High (engineering) | Low (subscription) | Variable |
| **Ongoing cost** | Maintenance | Subscription fees | Rev share |
| **Control** | Full | Limited | Shared |
| **Customization** | Unlimited | API constraints | Negotiated |
| **Risk** | Execution | Vendor dependency | Partner alignment |

### When to Build

**Build when:**
```
✓ Core to your value proposition
✓ Sustainable competitive advantage
✓ Unique requirements not met by market
✓ Integration complexity makes buy impractical
✓ Volume economics favor in-house
✓ Strategic IP/data you want to own
```

**Don't build when:**
```
✗ Solved problem with good solutions
✗ Not your core competency
✗ Faster alternatives exist
✗ Opportunity cost too high
✗ Maintenance burden distracts from core
```

### When to Buy

**Buy when:**
```
✓ Commodity/infrastructure need
✓ Market solutions are mature
✓ Speed to market critical
✓ Not a differentiator
✓ Vendor provides ongoing innovation
✓ Compliance/security better outsourced
```

**Don't buy when:**
```
✗ Core to product differentiation
✗ Vendor lock-in unacceptable
✗ Long-term costs exceed build costs
✗ Customization needs are extreme
✗ Vendor stability questionable
```

### When to Partner

**Partner when:**
```
✓ Complementary capabilities needed
✓ Faster market access desired
✓ Distribution channel partnership
✓ Technology integration needed
✓ Credibility/brand association valuable
✓ Shared customer base benefit
```

**Don't partner when:**
```
✗ Misaligned incentives
✗ Core IP at risk
✗ Partner could become competitor
✗ Integration costs high
✗ Dependency creates strategic risk
```

### Total Cost of Ownership (TCO)

**Build TCO:**
```
Year 1:
  Engineering time: $200K (2 engineers × 4 months)
  Infrastructure:   $10K
  Opportunity cost: $100K (what else could they build?)
  Total:            $310K

Years 2-5:
  Maintenance (20%): $40K/year
  Infrastructure:    $15K/year
  Total:             $220K

5-Year TCO: $530K
```

**Buy TCO:**
```
Year 1:
  Subscription:      $24K
  Integration:       $20K (1 engineer × 2 weeks)
  Total:             $44K

Years 2-5:
  Subscription:      $24K/year (may increase)
  Integration maint: $5K/year
  Total:             $116K

5-Year TCO: $160K
```

### Vendor Evaluation Framework

| Criteria | Weight | Score (1-5) | Weighted |
|----------|--------|-------------|----------|
| **Functionality fit** | 25% | | |
| **Integration ease** | 20% | | |
| **Pricing/TCO** | 20% | | |
| **Vendor stability** | 15% | | |
| **Security/compliance** | 10% | | |
| **Support quality** | 10% | | |
| **Total** | 100% | | |

### Common Build/Buy Decisions

| Category | Usually Build | Usually Buy |
|----------|---------------|-------------|
| **Auth** | Custom permissions | User auth (Auth0, Clerk) |
| **Payments** | Custom checkout | Processing (Stripe) |
| **Email** | In-app messaging | Transactional (SendGrid) |
| **Search** | Domain-specific | General search (Algolia) |
| **Analytics** | Product analytics | Web analytics (GA) |
| **Infrastructure** | Custom scaling | Cloud (AWS, GCP) |
| **Monitoring** | Custom dashboards | APM (Datadog) |

### Partnership Types

| Type | Structure | Example |
|------|-----------|---------|
| **Integration** | Technical integration, co-marketing | Zapier integrations |
| **Channel** | Reseller/referral agreement | SI partnerships |
| **Technology** | OEM, white-label | Powered by X |
| **Strategic** | Equity, deep integration | AWS + Slack |
| **Co-development** | Shared R&D | Joint product development |

### Partnership Success Factors

**Good partnership structure:**
```
1. Clear mutual benefit (not one-sided)
2. Aligned incentives (both profit together)
3. Defined boundaries (who does what)
4. Exit clauses (how to unwind if needed)
5. Success metrics (how to measure)
6. Escalation path (how to resolve issues)
```

### Migration Strategy

**From Buy to Build:**
```
Phase 1: Identify limitations of bought solution
Phase 2: Build abstraction layer
Phase 3: Build replacement behind abstraction
Phase 4: Migrate traffic gradually
Phase 5: Deprecate bought solution
```

**From Build to Buy:**
```
Phase 1: Document current functionality
Phase 2: Evaluate vendors against requirements
Phase 3: Build integration with abstraction
Phase 4: Run parallel, validate parity
Phase 5: Deprecate built solution
```

### Anti-Patterns

- **NIH Syndrome** — Building everything, rejecting external solutions
- **Vendor hoarding** — Too many vendors, integration complexity
- **False economy** — Building to save money when time is scarcer
- **Lock-in paranoia** — Avoiding all vendors, building commodity tools
- **Partnership without strategy** — Partnering without clear goals
- **Build then abandon** — Building, but not maintaining
- **Ignoring opportunity cost** — Not considering what else engineers could build
- **One-vendor dependency** — Critical function, single vendor, no plan B
