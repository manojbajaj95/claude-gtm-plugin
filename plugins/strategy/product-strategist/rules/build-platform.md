---
title: Platform vs Product Decisions
impact: MEDIUM-HIGH
tags: platform, product, ecosystem, strategy
---

## Platform vs Product Decisions

**Impact: MEDIUM-HIGH**

The platform vs product decision shapes your company's future. Products solve problems directly. Platforms enable others to solve problems. Each path has different economics, moats, and challenges.

### Product vs Platform Spectrum

```
PRODUCT ─────────────────────────────────────────── PLATFORM
    │                                                   │
 Focused                                            Extensible
 Direct value                                       Enabled value
 Linear scaling                                     Network effects
 Simpler GTM                                        Complex ecosystem
    │                                                   │
 Examples:                                          Examples:
 - Basecamp                                         - Salesforce
 - Linear                                           - Shopify
 - Superhuman                                       - Stripe
```

### Product-Platform Matrix

| | Single Segment | Multiple Segments |
|---|---|---|
| **Single Use Case** | Product | Vertical Platform |
| **Multiple Use Cases** | Product Suite | Horizontal Platform |

### When to Build a Product

**Product is right when:**
```
✓ Focused problem with clear solution
✓ Value is fully realized in your product
✓ No need for third-party extensions
✓ Simpler GTM motion
✓ Limited resources (startup)
✓ Time to market is critical
```

**Product characteristics:**
- Direct value delivery
- Opinionated workflow
- Integrated experience
- Subscription revenue model
- Linear cost scaling

### When to Build a Platform

**Platform is right when:**
```
✓ Problem space has many variations
✓ Third parties can add unique value
✓ Network effects possible
✓ Large enough market for ecosystem
✓ Resources to support developers
✓ Long-term moat building priority
```

**Platform characteristics:**
- Enabled value delivery
- Flexible, extensible
- Ecosystem of solutions
- Multiple revenue streams
- Network effect scaling

### Platform Business Models

| Model | How It Works | Revenue Source |
|-------|-------------|----------------|
| **Take rate** | Transaction fee | % of transactions |
| **API monetization** | Usage-based pricing | Per API call/volume |
| **Marketplace** | Connect buyers/sellers | Commission on sales |
| **App store** | Distribute extensions | % of app revenue |
| **Subscription tiers** | Gate platform features | Subscription fees |
| **Hybrid** | Combination | Multiple streams |

### Platform Flywheel

```
        ┌─────────────────────────────────────┐
        │                                     │
        ▼                                     │
   More Users ──────► More Value ◄────────────┤
        │               for Users             │
        │                                     │
        ▼                                     │
   More Developers ──► More Apps ─────────────┘
        │
        │
        ▼
   More Integration ──► Harder to Leave
```

### Platform Transition Strategy

**From Product to Platform:**

| Phase | Focus | Actions |
|-------|-------|---------|
| **Phase 1** | Product excellence | Nail core product value |
| **Phase 2** | API exposure | Build public APIs |
| **Phase 3** | Developer relations | Attract early developers |
| **Phase 4** | Ecosystem growth | Marketplace, app store |
| **Phase 5** | Platform economics | Monetize ecosystem |

**Warning signs you're too early:**
- Core product not stable
- Less than 1,000 active users
- No demand from customers for extensions
- No budget for developer support

### Platform Metrics

| Metric | What It Measures | Good Benchmark |
|--------|------------------|----------------|
| **# of integrations** | Ecosystem breadth | 50+ for early, 500+ mature |
| **API call volume** | Platform usage | Growing month over month |
| **Developer signups** | Ecosystem interest | 10% of customer count |
| **Active developers** | Ecosystem health | 30%+ of developer signups |
| **App installs** | User adoption | 50%+ of users use apps |
| **Platform revenue** | Monetization | 20%+ of total revenue |

### Minimum Viable Platform

**What you need to launch a platform:**

```
Must Have:
□ Stable, documented APIs
□ Authentication (OAuth)
□ Developer portal/docs
□ Sandbox environment
□ Basic support channel

Should Have:
□ SDKs for major languages
□ Webhooks for events
□ Rate limiting
□ Versioning strategy
□ Sample apps

Nice to Have:
□ Marketplace
□ Partner program
□ Developer community
□ Certification program
□ Revenue sharing
```

### Platform Governance

**Decision framework for platform rules:**

| Dimension | More Open | More Controlled |
|-----------|-----------|-----------------|
| **Who can build** | Anyone | Approved partners |
| **What they can build** | Anything | Within guidelines |
| **How they distribute** | Self-distributed | Through your marketplace |
| **How they monetize** | Keep 100% | Revenue share |
| **API access** | Full access | Tiered access |

### Platform Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Platform leakage** | Developer builds competitor | Core IP protection |
| **Quality control** | Bad apps hurt brand | Review process |
| **Support burden** | Developer support costs | Self-serve resources |
| **Dependency** | Key apps leave | Multi-sourcing |
| **Cannibalization** | Apps compete with you | Clear boundaries |

### Case Studies

**Slack: Product → Platform**
```
2014: Chat product
2015: Basic integrations
2016: App directory
2018: Slack Platform
2020: 2,400+ apps, platform moat
```

**Shopify: Platform from Day 1**
```
2006: E-commerce platform
2009: App store launched
2013: Shopify Payments
2020: Shop app, Fulfillment Network
Today: Platform revenue ~30%
```

**Notion: Product (So Far)**
```
2016: Note-taking product
2020: Still no public API
2021: Limited API beta
Approach: Product excellence first
```

### Platform vs Product Decision Checklist

```
Answer these questions:

□ Can third parties add meaningful value?
  Yes → Platform consideration
  No → Product focus

□ Is there market demand for extensions?
  Yes → Platform consideration
  No → Product focus

□ Do you have resources for developer support?
  Yes → Platform possible
  No → Product focus

□ Will network effects create defensibility?
  Yes → Platform worth investment
  No → Product may be better

□ Is your core product stable and loved?
  Yes → Platform timing may be right
  No → Focus on product first
```

### Anti-Patterns

- **Premature platforming** — Building platform before product works
- **Platform as strategy** — "We're a platform" without clear value
- **Ignored developers** — APIs without support or docs
- **Closed gardens** — Over-restricting what can be built
- **Revenue-first** — Monetizing before ecosystem has value
- **Feature competition** — Building what developers build
- **Platform theater** — APIs no one uses, marketing says "platform"
- **Neglecting core** — Platform investment at expense of core product
