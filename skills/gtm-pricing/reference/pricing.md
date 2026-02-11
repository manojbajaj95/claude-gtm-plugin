# Pricing Reference

Deep-dive on pricing models, strategies, and services pricing.

---

## Pricing Models Deep Dive

### Per-Seat Pricing

```yaml
per_seat_model:
  pros:
    - "Easy to understand"
    - "Scales with organization size"
    - "Predictable revenue"

  cons:
    - "Discourages adoption"
    - "Gaming (shared logins)"
    - "Hard to price for varying usage"

  best_practices:
    - "Offer viewer/editor tiers"
    - "Volume discounts at thresholds"
    - "Annual commitment discounts"

  example_tiers:
    starter: "$15/seat/month (up to 5)"
    professional: "$25/seat/month (5-50)"
    enterprise: "Custom (50+)"
```

### Usage-Based Pricing

```yaml
usage_model:
  pros:
    - "Aligns cost with value"
    - "Low barrier to start"
    - "Scales naturally"

  cons:
    - "Unpredictable revenue"
    - "Complex billing"
    - "Customer budget anxiety"

  common_metrics:
    - "API calls"
    - "Compute time"
    - "Storage"
    - "Active users"
    - "Transactions processed"

  best_practices:
    - "Include free tier/credits"
    - "Provide usage dashboards"
    - "Alert before overage"
    - "Offer committed use discounts"
```

### Tiered Pricing

```yaml
tiered_model:
  structure:
    free:
      purpose: "Land, qualify, viral growth"
      limits: "Core features, limited usage"

    starter:
      purpose: "Individuals, small teams"
      price: "$X/month"
      features: "Essential features"

    professional:
      purpose: "Growing teams"
      price: "$Y/month"
      features: "Full features + integrations"

    enterprise:
      purpose: "Large orgs, compliance needs"
      price: "Custom"
      features: "SSO, SLA, dedicated support"

  psychology:
    - "3-4 tiers optimal"
    - "Middle tier most popular (anchor)"
    - "Enterprise tier prices pro tier down"
```

---

## Pricing Page Best Practices

```markdown
## Pricing Page Checklist

### Above the Fold
- [ ] Clear tier names
- [ ] Prices visible immediately
- [ ] "Most Popular" badge on target tier
- [ ] CTA buttons for each tier

### Tier Details
- [ ] Feature comparison table
- [ ] Check marks for included features
- [ ] Expansion for feature details
- [ ] Clear upgrade path

### Trust Elements
- [ ] Money-back guarantee
- [ ] Customer logos
- [ ] Security badges
- [ ] "No credit card required" (if free trial)

### Conversion Optimization
- [ ] FAQ section
- [ ] "Compare plans" toggle
- [ ] Annual/monthly toggle
- [ ] Enterprise "Contact us" CTA
```

---

## Price Increase Strategy

### Planning a Price Increase

```yaml
price_increase_playbook:
  preparation:
    - "Analyze customer value delivered"
    - "Review competitive pricing"
    - "Segment by price sensitivity"
    - "Prepare value justification"

  communication:
    timing: "60-90 days notice minimum"
    channel: "Email from executive"
    messaging:
      - "Lead with value added"
      - "Be transparent about increase"
      - "Offer annual lock-in at current rate"

  execution:
    - "Grandfather best customers if needed"
    - "Prepare for some churn"
    - "Train support on objections"
    - "Monitor churn closely"

  typical_increase:
    annual: "3-5% inflation adjustment"
    strategic: "10-20% with value adds"
    catch_up: "25%+ if underpriced"
```

---

## Services Pricing

### Consulting/Services Rates

```yaml
services_pricing:
  hourly:
    junior: "$100-150/hr"
    mid: "$150-250/hr"
    senior: "$250-400/hr"
    executive: "$400-600/hr"

  project_based:
    method: "Estimate hours x 1.2 buffer x rate"
    include: "Scope change process"

  retainer:
    discount: "10-20% vs hourly"
    minimum: "40 hours/month"
    benefit: "Predictable, priority access"

  value_based:
    method: "% of value delivered"
    range: "10-30% of documented savings"
    risk: "Tie to measurable outcome"
```

### Productized Service Model

```yaml
productized_service:
  offering:
    name: ""
    description: ""
    price: 0
    delivery_time: ""

  capacity:
    max_per_month: 0
    hours_per_delivery: 0

  economics:
    monthly_revenue_max: 0  # max x price
    monthly_hours_max: 0  # max x hours
    effective_hourly: 0  # revenue / hours

  scaling:
    can_delegate: bool
    delegation_cost: 0
    margin_after_delegation: 0
```

---

## Discount Framework

### Discount Types

| Type | Trigger | Range | Example |
|------|---------|-------|---------|
| Volume | Commitment to scale | 10-30% | 20% off for 100+ seats |
| Term | Annual commitment | 15-25% | 2 months free on annual |
| Competitive | Switching from competitor | 20-40% | Match remaining contract |
| Strategic | Reference customer, logo value | Up to 50% | Name brand + case study |

### Protect Your Pricing

**Never Discount When:**
- Customer hasn't articulated value
- No competitive pressure
- Early in negotiation
- Customer is price shopping
- Deal doesn't meet minimum size

**Alternatives to Discounting:**
- Extended payment terms
- Additional services/training
- Extended trial
- Success milestones unlock features
- Multi-year lock-in

---

## Revenue Model Analysis

### Model 1: Subscription (SaaS/MRR)

```yaml
subscription_economics:
  pricing:
    tier_1:
      name: "Starter"
      price_monthly: 0
      price_annual: 0
      features: []
      target: ""

    tier_2:
      name: "Pro"
      price_monthly: 0
      price_annual: 0
      features: []
      target: ""

    tier_3:
      name: "Enterprise"
      price_monthly: 0
      price_annual: 0
      features: []
      target: ""

  metrics:
    arpu: 0  # Average Revenue Per User
    conversion_free_to_paid: 0.0  # %
    monthly_churn: 0.0  # %
    expansion_rate: 0.0  # % revenue expansion from existing
```

**Key formulas:**
```python
# Customer Lifetime Value
LTV = ARPU / monthly_churn

# Months to recover CAC
payback_months = CAC / ARPU

# Net Revenue Retention
NRR = (starting_mrr + expansion - contraction - churn) / starting_mrr
```

### Model 2: Marketplace / Transaction Fee

```yaml
marketplace_economics:
  transaction_model:
    take_rate: 0.0  # % of GMV
    minimum_fee: 0

  volume_projections:
    transactions_month_1: 0
    avg_transaction_value: 0
    gmv_month_1: 0
    revenue_month_1: 0  # GMV x take_rate

  growth:
    monthly_transaction_growth: 0.0  # %

  costs:
    payment_processing: 0.029  # typical 2.9%
    hosting_per_transaction: 0
    support_per_transaction: 0
```

---

## Key Metrics Dashboard

### SaaS Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| MRR | | | |
| MRR Growth | >10%/mo | | |
| Churn Rate | <5%/mo | | |
| LTV | >3x CAC | | |
| CAC Payback | <12 mo | | |
| NRR | >100% | | |

### Services Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Monthly Revenue | | | |
| Utilization | >70% | | |
| Effective Rate | >$100/hr | | |
| Client Retention | >80% | | |
| Profit Margin | >40% | | |
