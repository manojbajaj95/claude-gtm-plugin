---
name: growth-strategy
description: Growth strategy for product-led and loop-driven growth systems. Use when building growth strategy, designing growth loops, planning acquisition channels, evaluating network effects, deciding when to scale, or coordinating product, engineering, data, and marketing around growth. For SEO audits use seo-and-aeo-strategy; for page/form CRO use conversion-rate-optimization; for A/B test design use ab-test-setup.
metadata:
  version: 1.0.0
  merged_from:
    - growth
    - growth-strategy
    - growth-loops
---

# Growth Strategy

## Workspace Context

Read bootstrap context before asking questions: `strategy/brand.md` for brand, audience, offer, channels, tools, constraints, and metrics; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` for content planning. Use legacy product-marketing context files only as fallback. Save generated drafts to `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md`, and route durable learnings back to `strategy/brand.md`, `about/me.md`, or `content/ideas.md`.

## Operating Contract

This skill is self-contained for its frontmatter scope: use its local instructions, references, scripts, and assets as the playbook; ask only for missing task-specific inputs; hand off to adjacent skills instead of expanding scope; and return an actionable artifact, decision, plan, draft, or diagnostic.



Growth strategy for compounding growth systems. Use this skill for growth loops, distribution bets, network effects, PLG strategy, and scaling decisions. Route tactical SEO, page/form CRO, and experiment design to the specialist skills.

## Quick Reference

| Situation | Use This Skill For |
|-----------|-------------------|
| SEO, page CRO, or experiment execution | Route to specialist skills |
| Building growth engines | Growth Loops Framework |
| Strategic growth planning | Strategy & Frameworks |
| Distribution strategy | Channel & Platform Strategy |
| Network effects | Product-Led Growth |

---

## Part 1: Core Principles

### Foundational Truths

- Growth follows product-market fit, never precedes it
- Retention is the foundation; acquisition without retention is a leaky bucket
- The best growth is product-driven, not marketing-driven
- Compound effects beat linear efforts
- Every growth channel eventually saturates
- Network effects are the ultimate moat
- Premature growth destroys companies

### Growth Is Not Marketing

Growth is the systematic application of product, engineering, and data to create compounding user acquisition, activation, and retention. It's a mindset, not a department.

---

## Part 2: Growth Loops Framework

### Why Loops, Not Funnels

**Funnels**: Linear. Pour effort in, get results out, start over.
**Loops**: Each cycle generates fuel for the next cycle.

The key shift: Move from "How do we get more users?" to "How does each user we acquire generate more users?"

### Loop Types

| Loop Type | Description |
|-----------|-------------|
| **Content Loops** | Users create content → attracts more users → more content |
| **Viral Loops** | Users invite others → exponential spread |
| **Sales Loops** | Customers generate revenue → fund more acquisition |

### Critical Patterns

| Pattern | Insight |
|---------|---------|
| Funnels vs Loops | Funnels are linear; loops compound |
| Paid ≠ Loop | Paid acquisition doesn't compound — it's buying users |
| Founder-Led First | Can't outsource finding growth model |
| Product Must Own Growth | Can't be marketing-only function |
| One Primary Loop | Others supplement but won't save you |
| Earned Over Paid | Invest 80%+ in earned/owned channels |

### Platform Cycles

New platforms open, then close. Time your bets correctly:
- Early: High reach, low competition
- Mid: Reach peaks, competition grows
- Late: High competition, diminishing returns

---

## Part 3: SEO × SMO × CRO Framework

### SEO Checklist

**Page-Level**
- [ ] `<title>` — unique, 50-60 chars, primary keyword
- [ ] `<meta name="description">` — 150-160 chars
- [ ] `<link rel="canonical">` — self-referencing
- [ ] Single `<h1>` with primary keyword
- [ ] Primary keyword in first 100 words
- [ ] Descriptive `alt` text on all images
- [ ] Internal links to related pages

**Site-Level**
- [ ] `robots.txt` not blocking important resources
- [ ] `sitemap.xml` up to date
- [ ] HTTPS everywhere; mobile-friendly
- [ ] Core Web Vitals passing (LCP < 2.5s, CLS < 0.1, INP < 200ms)

### OGP / Twitter Cards

```html
<meta property="og:type" content="website">
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Description">
<meta property="og:image" content="https://example.com/og-image.png">
<meta property="twitter:card" content="summary_large_image">
```

### CRO Core

| Pillar | Goal | Key Metrics |
|--------|------|-------------|
| **SEO** | Be found | Organic traffic, rankings |
| **SMO** | Be shared | Social CTR, shares |
| **CRO** | Convert | Signup rate, completion |

---

## Part 4: Growth Models

### The LTV Equation

```
LTV = (Average Revenue Per Customer × Average Customer Lifespan) - CAC
```

### Unit Economics

- **LTV:CAC ratio**: 3:1 minimum for sustainable growth
- **Payback period**: < 12 months preferred
- **CAC**: Cost to acquire a customer
- **ARPU**: Average revenue per user

### AARRR Framework

| Metric | Definition |
|--------|------------|
| **Acquisition** | Users come from |
| **Activation** | First meaningful use |
| **Retention** | Users come back |
| **Referral** | Users invite others |
| **Revenue** | Users pay |

---

## Part 5: Network Effects

### Types of Network Effects

| Type | Description |
|------|-------------|
| **Direct** | More users → more value (social networks) |
| **Indirect** | More users → more options → more value (marketplaces) |
| **Two-sided** | Supply and demand sides benefit (platforms) |
| **Data** | More data → better product → more users |

### Building Network Effects

1. **Cross-side presence**: Ensure both sides of marketplace exist
2. **Liquidity thresholds**: Hit critical mass in each segment
3. **Switching costs**: Users invest in platform
4. **Platform stickiness**: Integration with workflows

---

## Part 6: Product-Led Growth (PLG)

### PLG Core Principles

- Product as the main driver of acquisition
- Free trials and freemium models
- In-product virality
- Self-serve onboarding
- Usage-based expansion

### PLG Metrics

| Metric | Target |
|--------|--------|
| Activation rate | > 40% |
| Time to value | < 5 minutes |
| Weekly active ratio | > 20% |
| Expansion revenue | > 20% of total |

---

## Part 7: Growth Experimentation

### ICE Framework

| Factor | Score (1-10) |
|--------|--------------|
| **Impact** | Could this double growth? |
| **Confidence** | How sure will this work? |
| **Ease** | How easy to implement? |

### Test Execution

- Document hypothesis clearly
- Define primary and guardrail metrics
- Calculate required sample size
- Wait for statistical significance (95%)
- Run full business cycle (1-2 weeks minimum)

### What NOT to Test

- Button colors before understanding objections
- Copying competitors blindly
- Optimizing without funnel context

---

## Part 8: Growth Team & Timing

### When to Hire Growth

| Stage | Growth Focus |
|-------|--------------|
| Pre-PMF | Founder-led, iterate on product |
| Finding PMF | First 100 customers, understand channels |
| Validated PMF | First growth hire, build experiments |
| Scaling | Full growth team, channel expansion |

### Growth Team Structure

- **Individual Contributor**: Run experiments
- **Growth Manager**: Prioritize and coordinate
- **Growth Lead**: Strategy and team management

---

## Part 9: Key Frameworks Summary

### Andrew Chen's Wisdom
- Marketplace dynamics
- Network effects as moat
- Platform distribution
- Cold start problem

### Brian Balfour's Frameworks
- Growth loops methodology
- Platform cycles
- Paid ≠ loop insight

### Casey Winters' Playbooks
- Kindle before fire (non-scalable → scalable)
- Product-led sales
- PQA > PQL

---

## Common Mistakes

1. **Premature scaling** — Growth before PMF burns cash
2. **Acquisition without retention** — Leaky bucket
3. **Chasing channels** — Without understanding loops
4. **Vanity metrics** — Focus on leading indicators
5. **One-hit wonders** — Not building compounding systems

---

## Related Skills

- **product-market-fit-analysis**: For PMF assessment
- **conversion-rate-optimization**: For CRO implementation
- **customer-success-and-retention**: For retention strategy
- **ab-test-setup**: For growth experiments
