---
title: North Star Metrics & Growth Measurement
impact: MEDIUM-HIGH
tags: metrics, north-star, measurement, kpis, growth
---

## North Star Metrics & Growth Measurement

**Impact: MEDIUM-HIGH**

What you measure determines what you optimize. A clear North Star metric aligns the entire company around what matters most — value delivered to customers.

### What Is a North Star Metric?

```
A North Star Metric is the single metric that best captures
the core value your product delivers to customers.

Characteristics:
✓ Measures value delivered (not captured)
✓ Leading indicator of revenue
✓ Actionable by product/growth teams
✓ Easy to understand company-wide
✓ Reflects your product strategy
```

### North Star Metric Examples

| Company | North Star | Why It Works |
|---------|------------|--------------|
| Airbnb | Nights booked | Directly measures value exchange |
| Slack | Daily Active Users sending messages | Measures engagement with core value |
| Spotify | Time spent listening | Measures content consumption |
| Amplitude | Weekly Learning Users | Measures users getting insights |
| Figma | Weekly Active Editors | Measures design collaboration |
| Dropbox | Files synced | Measures core utility |
| HubSpot | Weekly Active Teams | Measures business value |
| Notion | Weekly Active Users | Measures regular engagement |

### Finding Your North Star

**Step 1: Identify Core Value**

```
Questions to answer:
1. What job does our product do for users?
2. When do users say "this is valuable"?
3. What action indicates they got value?
4. What predicts they'll stay and pay?
```

**Step 2: Test Candidate Metrics**

```
For each candidate metric, check:

□ Does it measure VALUE delivered (not just activity)?
□ Does it CORRELATE with revenue?
□ Can teams INFLUENCE it?
□ Is it SIMPLE to explain?
□ Does it ALIGN with strategy?

Score each 1-5. Highest total = best candidate.
```

**Step 3: Validate with Data**

```
Correlation analysis:
- Does higher metric → higher retention?
- Does higher metric → higher revenue?
- Does higher metric → higher referral?

If yes to all three, you have a strong North Star.
```

### The Input Metrics Framework

```
                    NORTH STAR METRIC
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   INPUT 1            INPUT 2            INPUT 3
   (Breadth)          (Depth)            (Frequency)
        │                  │                  │
   Sub-metrics        Sub-metrics        Sub-metrics
```

**Example: Spotify**

```
                Time Spent Listening
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   Total Users      Sessions/User    Time/Session
   (Breadth)         (Frequency)       (Depth)
        │               │               │
   • New users      • Push opens     • Playlist quality
   • Reactivated    • Home screen    • Skip rate
                    • Recommendations • Completion rate
```

### Metric Hierarchy

**Level 1: North Star (Company)**
```
Single metric everyone knows
Example: Weekly Active Users
```

**Level 2: Health Metrics (Leadership)**
```
4-6 metrics that feed the North Star
Example: New users, Activation rate, Retention, ARPU
```

**Level 3: Team Metrics (Product Teams)**
```
Specific metrics each team owns
Example: Onboarding completion, Feature adoption, Support tickets
```

**Level 4: Experiment Metrics (Growth Team)**
```
Granular metrics for experiments
Example: CTA click rate, Form completion, Time on page
```

### The AARRR Framework (Pirate Metrics)

```
Stage        │ Definition              │ Example Metrics
─────────────┼─────────────────────────┼──────────────────────
ACQUISITION  │ User discovers product  │ Visitors, signups, CAC
ACTIVATION   │ User experiences value  │ Activation rate, TTV
RETENTION    │ User keeps coming back  │ D7/D30 retention, churn
REVENUE      │ User pays money         │ Conversion, ARPU, LTV
REFERRAL     │ User brings others      │ K-factor, NPS, referrals
```

### Growth Accounting

**Tracking Where Growth Comes From:**

```
New Users This Period =
  + New signups (acquisition)
  + Resurrected users (win-back)
  - Churned users (retention)

Growth Accounting Table:
┌──────────────────────────────────────────────────────────┐
│ Month      │ Start │ +New │ +Resur │ -Churn │ End    │
├──────────────────────────────────────────────────────────┤
│ January    │ 1000  │ +200 │ +30    │ -80    │ 1150   │
│ February   │ 1150  │ +250 │ +40    │ -90    │ 1350   │
│ March      │ 1350  │ +280 │ +50    │ -100   │ 1580   │
└──────────────────────────────────────────────────────────┘
```

### Metric Definitions Matter

**Be Precise:**

```
"Monthly Active Users" could mean:
- Logged in at least once
- Performed any action
- Performed core action
- Performed core action on X days
- Paid users who logged in

Define exactly what counts, document it, don't change it.
```

**Good Definition Example:**

```
Metric: Weekly Active Users (WAU)

Definition:
"Unique users who completed at least one [core action]
in the trailing 7-day period, excluding:
- Internal/test accounts
- Users in trial who never activated
- Bot/automated accounts"

Why: This measures users receiving value, not just logging in.
```

### Dashboard Design

**Growth Dashboard Essentials:**

```
┌─────────────────────────────────────────────────────────────┐
│                    GROWTH DASHBOARD                         │
├─────────────────────────────────────────────────────────────┤
│ NORTH STAR                                                  │
│ Weekly Active Users: 12,450 (+8% WoW)                       │
├─────────────────────────────────────────────────────────────┤
│ ACQUISITION          │ ACTIVATION      │ RETENTION          │
│ Signups: 2,100       │ Rate: 34%       │ D7: 42%           │
│ CAC: $45             │ TTV: 8 min      │ D30: 28%          │
├─────────────────────────────────────────────────────────────┤
│ REVENUE              │ REFERRAL        │ EXPERIMENTS        │
│ MRR: $125K           │ K-factor: 0.3   │ Active: 4          │
│ Conversion: 5.2%     │ NPS: 52         │ Last win: +12%     │
└─────────────────────────────────────────────────────────────┘
```

### Metric Reviews

**Weekly Growth Review:**

```
Agenda (30-60 min):
1. North Star trend (5 min)
2. Input metric review (10 min)
3. Experiment results (15 min)
4. Anomalies and insights (10 min)
5. Priorities for next week (10 min)
```

**Monthly Deep Dive:**

```
Agenda (2 hours):
1. Month-over-month trends
2. Cohort analysis
3. Channel performance
4. Experiment portfolio review
5. Roadmap alignment check
```

### Avoiding Vanity Metrics

| Vanity Metric | Why It's Vanity | Better Alternative |
|---------------|-----------------|-------------------|
| Total signups | Includes churned users | Active users |
| Page views | Activity, not value | Time on page, conversions |
| Total downloads | Doesn't mean usage | Activated users |
| Follower count | Doesn't mean engagement | Engagement rate |
| Feature launches | Output, not outcome | Feature adoption rate |

### Metric Red Flags

```
Warning Signs:
⚠ Metric going up but revenue flat
⚠ Metric looks good but customers churning
⚠ Teams gaming the metric
⚠ Metric impossible to move
⚠ Different teams measuring differently
⚠ No one can explain what the metric means
```

### Anti-Patterns

- **Multiple North Stars** — If everything is the priority, nothing is
- **Vanity over value** — Measuring activity instead of value delivered
- **Changing definitions** — Makes trends incomparable
- **Dashboard overload** — 50 metrics = 0 focus
- **Lagging-only metrics** — Revenue tells you what happened, not what's coming
- **Gaming metrics** — Optimizing metric without delivering value
- **Ignoring cohorts** — Aggregate hides user behavior
- **No input metrics** — North Star without levers to pull
