# GTM Reference

ICP templates, launch playbooks, channel strategy, and competitive intelligence.

---

## ICP Development Templates

### Full ICP Worksheet

#### Section 1: Firmographics

```yaml
company_profile:
  size:
    employees_min:
    employees_max:
    revenue_min:
    revenue_max:

  industry:
    primary: []
    secondary: []
    excluded: []

  geography:
    regions: []
    countries: []
    excluded: []

  company_type:
    - [ ] Startup (seed-Series A)
    - [ ] Growth (Series B-D)
    - [ ] Enterprise (public/PE-backed)
    - [ ] SMB (bootstrapped)
```

#### Section 2: Technographics

```yaml
tech_profile:
  required_stack:
    must_have: []
    nice_to_have: []
    incompatible: []

  tech_maturity:
    - [ ] Early adopter (bleeding edge)
    - [ ] Early majority (proven tech)
    - [ ] Late majority (conservative)
    - [ ] Laggard (legacy-bound)

  current_solutions:
    crm: ""
    erp: ""
    industry_specific: ""

  integration_requirements: []
```

#### Section 3: Psychographics

```yaml
buyer_profile:
  awareness_stage:
    - [ ] Unaware (doesn't know problem)
    - [ ] Problem-aware (feels pain)
    - [ ] Solution-aware (researching)
    - [ ] Product-aware (evaluating us)

  buying_committee:
    economic_buyer: ""
    technical_buyer: ""
    user_buyer: ""
    champion: ""
    blocker: ""

  decision_criteria:
    primary: []
    secondary: []

  risk_factors:
    - [ ] Budget concerns
    - [ ] Implementation risk
    - [ ] Change management
    - [ ] Vendor stability
```

#### Section 4: Behavioral Signals

```yaml
intent_signals:
  high_intent:
    - "Searched for [competitor] alternatives"
    - "Visited pricing page 3+ times"
    - "Downloaded buyer's guide"

  medium_intent:
    - "Attended webinar"
    - "Engaged with case study"
    - "Connected on LinkedIn"

  low_intent:
    - "Blog subscriber"
    - "Social follower"
    - "Newsletter open"
```

---

## ICP Validation Checklist

```markdown
## Validate Your ICP

### Market Size Check
- [ ] TAM: Total addressable market calculated
- [ ] SAM: Serviceable addressable market defined
- [ ] SOM: Realistic obtainable market estimated
- [ ] Minimum 1000 companies in ICP

### Win Rate Check
- [ ] Historical win rate against ICP: >30%
- [ ] Average deal size meets targets
- [ ] Sales cycle length acceptable

### Customer Success Check
- [ ] ICP customers have lowest churn
- [ ] Highest NPS scores from ICP
- [ ] Most expansions/upsells from ICP

### Qualitative Check
- [ ] Sales team agrees on ICP
- [ ] Customer success validates fit
- [ ] Product roadmap serves ICP
```

---

## Example ICP: MEP Contractors

```yaml
icp_mep_contractor:
  firmographics:
    employees: "50-500"
    revenue: "$10M-$100M"
    trades: ["Electrical", "Plumbing", "HVAC", "Fire Protection"]
    geography: "US, primarily Sun Belt"

  technographics:
    current_tools:
      - "QuickBooks or Sage"
      - "Spreadsheets for project tracking"
      - "Paper or basic mobile for field"
    pain_indicators:
      - "Manual data entry between systems"
      - "No real-time job costing"
      - "Field-office communication gaps"

  psychographics:
    champions: ["Operations Manager", "CFO", "Owner"]
    pain_points:
      - "Can't see project profitability until job ends"
      - "Billing delays due to paperwork"
      - "Losing bids due to slow estimates"

  disqualifiers:
    - "Under $5M revenue (can't afford)"
    - "Union-only shops (different workflow)"
    - "Already on ServiceTitan (entrenched)"
```

---

## Channel Strategy

### GTM Motion Selection

| Motion | Best For | CAC | Sales Cycle | Team |
|--------|----------|-----|-------------|------|
| Product-Led | Low ACV (<$5K), self-serve | Low | Days | Growth |
| Sales-Assisted | Mid ACV ($5-50K) | Medium | Weeks | SDR+AE |
| Enterprise | High ACV ($50K+) | High | Months | AE+SE |
| Partner/Channel | Geographic expansion | Variable | Variable | Partner Mgr |

### Channel Mix Framework

```
Primary Channel (60-70% of pipeline)
└── [Selected motion based on ACV and complexity]

Secondary Channel (20-30%)
└── [Supporting motion for different segments]

Experimental (10%)
└── [New channel being tested]
```

---

## GTM Complexity Matrix

### Complexity Levels

| Level | Buyer | Company Size | ACV | Cycle | Decision |
|-------|-------|--------------|-----|-------|----------|
| 1: PLG | Individual | 1-50 | <$2K | Days | User = buyer |
| 2: Low-Touch | Manager | 10-200 | $2-15K | 1-4 weeks | Light demo |
| 3: Mid-Market | Director/VP | 200-2K | $15-100K | 1-3 months | Committee |
| 4: Enterprise | C-suite | 2K+ | $100K-1M | 6-18 months | RFP/security |
| 5: Complex | Board | Global | $1M+ | 12-36 months | Transformation |

### Matching Complexity to Resources

#### Solo Founder

```yaml
optimal_complexity: Level 1-2
max_complexity: Level 3 (with constraints)

constraints:
  - 20 hrs/week available for side projects
  - No sales team
  - Limited marketing budget

strategies:
  - Focus on PLG or low-touch
  - Productize consulting
  - Partner for enterprise deals
  - Leverage existing networks
```

#### With Co-founder/Partner

```yaml
optimal_complexity: Level 2-3
max_complexity: Level 4 (with investment)

enables:
  - Split technical/GTM
  - Higher touch sales
  - More accounts in parallel
  - Extended hours coverage
```

### Complexity Reduction Tactics

1. **Target smaller segment**: Enterprise -> Mid-market, Company-wide -> Department
2. **Simplify pricing**: Custom -> Standard tiers, Annual -> Monthly option
3. **Reduce stakeholders**: Find single budget holder, Start with pilot/POC
4. **Eliminate friction**: Self-serve trial, No-contract option
5. **Partner for complexity**: Reseller handles procurement, SI handles implementation

---

## Launch Playbook

### Comprehensive Launch Checklist

```markdown
## Pre-Launch (T-30 days)
- [ ] ICP documented and validated
- [ ] Positioning finalized
- [ ] Messaging hierarchy complete
- [ ] Battle cards created
- [ ] Sales enablement materials ready
- [ ] Pricing approved
- [ ] Website content ready
- [ ] Demo environment stable
- [ ] Customer references committed

## Launch Week
- [ ] Press release distributed
- [ ] Website updated
- [ ] Sales team trained
- [ ] Customer references lined up
- [ ] Outbound sequences activated
- [ ] Social media campaign live
- [ ] Partner notifications sent
- [ ] Internal all-hands communication

## Post-Launch (T+30 days)
- [ ] Win/loss analysis started
- [ ] Messaging refinement based on feedback
- [ ] Pipeline review
- [ ] Competitive response documented
- [ ] Customer feedback collected
- [ ] Metrics dashboard active
- [ ] Lessons learned documented
```

---

## Battle Card Template

```markdown
## Competitor: [Name]

### Overview
- Founded: YYYY | HQ: Location | Funding: $XXM
- Target market: [description]
- Pricing: [model and range]
- Key customers: [list notable logos]

### Strengths (acknowledge honestly)
- [Strength 1]
- [Strength 2]
- [Strength 3]

### Weaknesses (our opportunities)
- [Weakness 1] -> Our advantage: [...]
- [Weakness 2] -> Our advantage: [...]
- [Weakness 3] -> Our advantage: [...]

### Common Objections When We Compete
| Objection | Response |
|-----------|----------|
| "They're cheaper" | [Value-based response] |
| "They have feature X" | [Alternative or roadmap] |
| "They're bigger/more established" | [Agility, support, focus] |

### Win Strategy
1. Lead with [differentiator]
2. Demonstrate [proof point]
3. Reference [customer story]

### Key Talking Points
- [Point 1]
- [Point 2]
- [Point 3]

### Questions to Ask Prospect
- "What's driving you to evaluate alternatives?"
- "What would make this project a success?"
- "What's your timeline for implementation?"
```

---

## Positioning Examples

### B2B SaaS Positioning Statement

```
For [mid-market MEP contractors] who [struggle with disconnected systems and manual processes],
[Product Name] is a [unified project management platform]
that [provides real-time visibility into job costs and field operations].
Unlike [spreadsheets and legacy software],
our product [was built for modern mobile-first field teams with native integration to accounting].
```

### Competitive Positioning Framework

| Axis | Our Position | Why It Matters |
|------|--------------|----------------|
| Feature completeness | Focused | Do one thing extremely well |
| Price | Value | Pay for outcomes, not seats |
| Support | High-touch | Real humans, fast response |
| Integration | Native | Not bolted on, built in |
| Industry focus | Specialist | Deep domain expertise |
