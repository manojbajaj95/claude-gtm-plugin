# Opportunity Evaluation Reference

Scorecards, unit economics, build vs partner decisions, and evaluation frameworks.

---

## Opportunity Scorecard Template

### Opportunity Overview

```yaml
opportunity:
  name: ""
  type: ""  # business_idea, partnership, job, consulting, investment
  source: ""  # how discovered
  date_identified: ""
  evaluation_deadline: ""

  one_liner: ""  # Explain in one sentence

  decision_maker: ""  # Who decides if this moves forward
  next_action: ""
```

---

## Section 1: Market Fit (25 points)

### Problem Clarity (10 pts)

| Score | Criteria |
|-------|----------|
| 10 | Urgent, painful problem I've experienced or deeply understand |
| 7-9 | Clear problem with evidence (complaints, spend, alternatives) |
| 4-6 | Probable problem, needs validation |
| 1-3 | Vague problem, solution looking for problem |
| 0 | No clear problem |

### Market Size (8 pts)

| Score | Criteria |
|-------|----------|
| 8 | Large market ($1B+), growing, accessible segment |
| 6-7 | Good market ($100M+), clear path to customers |
| 3-5 | Niche market, but profitable |
| 1-2 | Very small or declining market |
| 0 | No real market |

### Timing (7 pts)

| Score | Criteria |
|-------|----------|
| 7 | Perfect timing - market ready, tech mature, trend rising |
| 5-6 | Good timing - some tailwinds |
| 3-4 | Neutral - no particular advantage |
| 1-2 | Early or late - fighting headwinds |
| 0 | Wrong time entirely |

---

## Section 2: Technical Fit (20 points)

### Can I Build It? (10 pts)

| Score | Criteria |
|-------|----------|
| 10 | Fully within my skills, can ship in days/weeks |
| 7-9 | Mostly within skills, small learning curve |
| 4-6 | Significant learning required but achievable |
| 1-3 | Would need to hire/partner for core tech |
| 0 | Beyond my technical reach |

### Infrastructure Fit (5 pts)

| Score | Criteria |
|-------|----------|
| 5 | Uses my standard stack (RunPod, Supabase, Vercel, etc.) |
| 3-4 | Minor additions to stack |
| 1-2 | Significant new infrastructure |
| 0 | Completely different stack required |

### Maintenance Burden (5 pts)

| Score | Criteria |
|-------|----------|
| 5 | Low maintenance, runs itself |
| 3-4 | Moderate maintenance, predictable |
| 1-2 | High maintenance, unpredictable |
| 0 | Would consume all my time |

---

## Section 3: GTM Fit (20 points)

### Sales Complexity (8 pts)

| Score | Criteria |
|-------|----------|
| 8 | Simple sale I've done 100x before |
| 6-7 | Familiar sale with minor variations |
| 4-5 | New but adjacent to my experience |
| 1-3 | Complex enterprise sale requiring heavy process |
| 0 | Sales motion I can't execute |

### Channel Access (7 pts)

| Score | Criteria |
|-------|----------|
| 7 | Direct access to buyers (network, current role, etc.) |
| 5-6 | Indirect but clear path to buyers |
| 3-4 | Need to build channel from scratch |
| 1-2 | No clear channel |
| 0 | Can't reach buyers |

### Competition (5 pts)

| Score | Criteria |
|-------|----------|
| 5 | Blue ocean or clear differentiation |
| 3-4 | Competitive but winnable with positioning |
| 1-2 | Crowded, hard to differentiate |
| 0 | Dominated by well-funded incumbents |

---

## Section 4: Personal Fit (20 points)

### Interest & Energy (8 pts)

| Score | Criteria |
|-------|----------|
| 8 | Genuinely excited, would do for fun |
| 6-7 | Interested, aligns with curiosity |
| 4-5 | Neutral, professional interest |
| 1-3 | Meh, doing for money only |
| 0 | Actively disinterested |

### Growth Potential (7 pts)

| Score | Criteria |
|-------|----------|
| 7 | Significant skill/network/reputation growth |
| 5-6 | Good learning opportunity |
| 3-4 | Some growth, mostly lateral |
| 1-2 | Limited growth |
| 0 | Would stagnate or regress |

### Lifestyle Fit (5 pts)

| Score | Criteria |
|-------|----------|
| 5 | Perfect fit - remote, flexible, timezone compatible |
| 3-4 | Minor friction with lifestyle |
| 1-2 | Significant friction |
| 0 | Incompatible with current life |

---

## Section 5: Economics (15 points)

### Revenue Potential (8 pts)

| Score | Criteria |
|-------|----------|
| 8 | High revenue, clear path ($10K+/month realistic) |
| 6-7 | Good revenue ($5-10K/month realistic) |
| 4-5 | Moderate revenue ($2-5K/month) |
| 1-3 | Low revenue (<$2K/month) |
| 0 | No clear revenue |

### Time to Revenue (4 pts)

| Score | Criteria |
|-------|----------|
| 4 | Immediate (<30 days) |
| 3 | Short (1-3 months) |
| 2 | Medium (3-6 months) |
| 1 | Long (6-12 months) |
| 0 | Very long (12+ months) |

### Risk/Reward (3 pts)

| Score | Criteria |
|-------|----------|
| 3 | Asymmetric upside, limited downside |
| 2 | Balanced risk/reward |
| 1 | High risk, moderate reward |
| 0 | High risk, low reward |

---

## Final Score Interpretation

| Score | Recommendation |
|-------|----------------|
| 80-100 | **STRONG PURSUE** - Prioritize this |
| 60-79 | **EXPLORE** - Worth time investment |
| 40-59 | **CONDITIONAL** - Only if specific factor changes |
| 0-39 | **PASS** - Opportunity cost too high |

---

## Decision Summary Template

```yaml
final_decision:
  score: 0
  recommendation: ""  # PURSUE, EXPLORE, CONDITIONAL, PASS

  top_3_reasons_for:
    - ""
    - ""
    - ""

  top_3_concerns:
    - ""
    - ""
    - ""

  what_would_change_my_mind: ""

  next_steps:
    - action: ""
      deadline: ""
    - action: ""
      deadline: ""

  revisit_date: ""  # When to re-evaluate if not pursuing now
```

---

## Unit Economics Template

### Quick Viability Check

```markdown
## 5-Minute Viability Test

1. How much will one customer pay? $____/month
2. How many customers can I realistically get in 6 months? ____
3. What does it cost to serve one customer? $____/month
4. How many hours/week will this take me? ____

Quick math:
- Monthly revenue (6 months): #2 x #1 = $____
- Monthly costs: #2 x #3 = $____
- Monthly margin: Revenue - Costs = $____
- Hourly rate equivalent: Margin / (hours x 4) = $____/hr

Is hourly rate > $100?
[ ] Yes -> Continue analysis
[ ] No -> Needs rethink
```

### Cost Structure Analysis

#### Fixed Costs

```yaml
fixed_costs_monthly:
  infrastructure:
    hosting: 0  # Vercel, RunPod, etc.
    database: 0  # Supabase
    domains: 0

  tools:
    development: 0  # Cursor, GitHub, etc.
    marketing: 0
    operations: 0

  services:
    accounting: 0
    legal: 0
    insurance: 0

  total_fixed: 0
```

#### Variable Costs

```yaml
variable_costs_per_unit:
  api_costs:
    llm_per_request: 0  # Average LLM cost
    other_apis: 0

  payment_processing: 0.029  # 2.9% + $0.30 typical

  support:
    time_per_customer_monthly: 0  # hours
    cost_per_hour: 0

  infrastructure_scaling:
    cost_per_1000_users: 0

  total_variable_per_unit: 0
```

### Break-Even Analysis

```python
def calculate_break_even(
    fixed_costs: float,
    price_per_unit: float,
    variable_cost_per_unit: float
) -> dict:
    contribution_margin = price_per_unit - variable_cost_per_unit
    break_even_units = fixed_costs / contribution_margin

    return {
        'contribution_margin': contribution_margin,
        'break_even_units': break_even_units,
        'break_even_revenue': break_even_units * price_per_unit
    }

# Example
result = calculate_break_even(
    fixed_costs=500,      # monthly
    price_per_unit=50,    # per customer
    variable_cost_per_unit=5  # API costs, etc.
)
# break_even_units = 500 / (50-5) = 11.1 customers
```

---

## Build vs Partner Decision Framework

### Decision Tree

```
START: I need [capability/solution]
|
|-> Is this core to my value proposition?
|   |
|   |-> YES -> Strongly consider BUILD
|   |   |-> Can I build it in <2 weeks?
|   |       |-> Yes -> BUILD
|   |       |-> No -> BUILD anyway (it's core)
|   |
|   |-> NO -> Consider PARTNER or BUY
|       |-> Does a good solution exist?
|           |-> Yes, affordable -> BUY/USE
|           |-> Yes, expensive -> PARTNER or BUILD
|           |-> No -> BUILD or IGNORE
|
|-> What's the opportunity cost?
|   |
|   |-> Building distracts from revenue -> PARTNER/BUY
|   |-> Building enables more revenue -> BUILD
|
|-> What's the maintenance burden?
    |
    |-> High ongoing maintenance -> PARTNER/BUY
    |-> Low/one-time effort -> BUILD
```

### When to BUILD

**Strong signals:**
- Core differentiator for your product
- No good alternatives exist
- You have unique expertise
- Learning is valuable for future
- Control is critical (security, data, UX)
- Existing solutions are overpriced
- You'll use it across multiple projects

**Red flags:**
- Well-maintained open source exists
- Commodity functionality (auth, payments)
- You're building to avoid buying
- Timeline is critical
- It's outside your expertise
- Maintenance would consume you

### When to PARTNER

**Strong signals:**
- Complementary capabilities
- Aligned customer base
- Neither wants to build what other has
- Combined offering is stronger
- Shared go-to-market benefits
- Risk/investment sharing makes sense

**Red flags:**
- Misaligned incentives
- Unclear economics
- Dependency on unreliable party
- Could become competitor
- Cultural mismatch
- Complicated legal/IP issues

### Partnership Types

| Type | Description | Best For |
|------|-------------|----------|
| Referral | Send leads, get commission | Quick revenue, no integration |
| Reseller | Sell their product | When their product fits your customers |
| Integration | Technical connection | When both benefit from connected product |
| White-label | Rebrand their solution | When you need capability fast |
| Joint venture | Shared ownership | Large opportunities, aligned incentives |
| Affiliate | Commission on sales | Low commitment, test market |

### When to BUY

**Strong signals:**
- Commodity functionality
- Time-to-market critical
- Well-established vendors
- Reasonable pricing
- Good documentation/support
- Standard APIs/integration

### Rules of Thumb

1. **If it's an MCP server -> BUILD**: Fast to build, reusable, high learning value
2. **If it's infrastructure -> BUY**: Supabase, Vercel, RunPod
3. **If it's an LLM capability -> BUY via API**: Anthropic, Google, OpenRouter
4. **If it's GTM capability -> PARTNER**: Leverage existing networks
5. **If it doesn't exist and you need it -> BUILD**: Be the first
6. **If in doubt -> START SMALL**: Build MVP, partner on pilot, buy smallest tier

---

## Comparative Analysis Template

### Side-by-Side Comparison

| Factor | Build | Partner | Buy | Ignore |
|--------|-------|---------|-----|--------|
| Time to capability | | | | N/A |
| Upfront cost | | | | $0 |
| Ongoing cost | | | | $0 |
| Control level | High | Medium | Low | N/A |
| Maintenance burden | | | | None |
| Strategic value | | | | |
| Risk level | | | | |

### Scoring Matrix

| Factor | Weight | Build | Partner | Buy | Ignore |
|--------|--------|-------|---------|-----|--------|
| Speed to market | 20% | /5 | /5 | /5 | /5 |
| Total cost (3yr) | 20% | /5 | /5 | /5 | /5 |
| Quality/control | 15% | /5 | /5 | /5 | /5 |
| Strategic fit | 15% | /5 | /5 | /5 | /5 |
| Maintenance | 15% | /5 | /5 | /5 | /5 |
| Risk | 15% | /5 | /5 | /5 | /5 |
| **Weighted Score** | | | | | |
