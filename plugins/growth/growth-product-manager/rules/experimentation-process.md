---
title: Growth Experimentation Process
impact: HIGH
tags: experimentation, ab-testing, growth, process, iteration
---

## Growth Experimentation Process

**Impact: HIGH**

Growth is a discipline of systematic experimentation. The best growth teams run 10-20x more experiments than average teams — and learn 10-20x faster.

### The Growth Experimentation Mindset

```
Two types of product work:

BUILD MODE:                    GROWTH MODE:
─────────────────              ──────────────────
Big bets                       Small experiments
Months of work                 Days to weeks
High conviction                High velocity
Ship and iterate               Test and learn
"We believe..."                "We'll test..."
```

### The Growth Experiment Lifecycle

```
┌──────────────────────────────────────────────────────────────┐
│                EXPERIMENT LIFECYCLE                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  IDEATE → PRIORITIZE → DESIGN → BUILD → RUN → ANALYZE → LEARN
│     │                                                   │    │
│     └───────────────── LEARN & ITERATE ←───────────────┘    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Experiment Prioritization: ICE Framework

```
ICE Score = Impact × Confidence × Ease

Impact (1-10):     How much will this move the metric?
Confidence (1-10): How sure are we of the impact?
Ease (1-10):       How easy is this to implement?

Example:
┌─────────────────────────────────────────────────────────────┐
│ Experiment              │ Impact │ Conf │ Ease │ ICE Score │
├─────────────────────────────────────────────────────────────┤
│ Simplify signup flow    │   8    │  7   │  9   │   504     │
│ Add social proof        │   5    │  6   │  8   │   240     │
│ Redesign onboarding     │   9    │  5   │  3   │   135     │
│ New referral program    │   7    │  4   │  4   │   112     │
└─────────────────────────────────────────────────────────────┘
```

### The Experiment Document

**Every experiment needs:**

```
┌─────────────────────────────────────────────────────────────┐
│                    EXPERIMENT BRIEF                         │
├─────────────────────────────────────────────────────────────┤
│ EXPERIMENT NAME: [Clear, descriptive name]                  │
│                                                             │
│ HYPOTHESIS:                                                 │
│ If we [change], then [metric] will [improve] because        │
│ [rationale].                                                │
│                                                             │
│ METRICS:                                                    │
│ - Primary: [The metric this aims to move]                   │
│ - Secondary: [Related metrics to watch]                     │
│ - Guardrail: [Metrics that shouldn't degrade]               │
│                                                             │
│ AUDIENCE:                                                   │
│ - Who: [User segment]                                       │
│ - Sample: [% of traffic]                                    │
│ - Duration: [Expected runtime]                              │
│                                                             │
│ SUCCESS CRITERIA:                                           │
│ - Minimum detectable effect: [X%]                           │
│ - Statistical significance: [95%]                           │
│                                                             │
│ VARIANTS:                                                   │
│ - Control: [Current experience]                             │
│ - Treatment: [New experience]                               │
└─────────────────────────────────────────────────────────────┘
```

### Writing Good Hypotheses

**Bad Hypothesis:**
```
"Let's test a new onboarding flow"
- No expected outcome
- No rationale
- Can't be proven wrong
```

**Good Hypothesis:**
```
"If we show a personalized checklist during onboarding
(instead of a generic welcome screen),
then day-7 activation rate will increase by 15%
because users will have clear next steps tailored to their use case."

Components:
- Specific change
- Measurable outcome
- Rationale/belief
```

### Statistical Rigor

**Sample Size Calculation:**

```
Minimum Sample Size per Variant:

n = (Z² × p × (1-p)) / E²

Where:
Z = 1.96 (for 95% confidence)
p = baseline conversion rate
E = minimum detectable effect

Example:
- Baseline: 5% conversion
- Want to detect: 10% relative lift (5% → 5.5%)
- Need: ~30,000 users per variant

Use: https://www.evanmiller.org/ab-testing/sample-size.html
```

**Running Time:**

```
Never stop early based on results!

Common mistake:
Day 3: Treatment winning by 20%! → Ship it!
Day 14: Treatment actually -5% → Oops.

Why: Early results are noisy. Statistical power requires full sample.

Minimum: 1-2 full business cycles (usually 2+ weeks)
```

### Experiment Types

| Type | When to Use | Example |
|------|-------------|---------|
| **A/B Test** | Clear change, measurable outcome | Button color, copy |
| **Multivariate** | Multiple changes, interactions | Page layout + copy + CTA |
| **Holdout** | Measure cumulative impact | Feature launch impact |
| **Sequential** | Quick iteration, rolling changes | Onboarding flow steps |
| **Fake Door** | Validate demand before building | "Coming soon" feature |
| **Painted Door** | Test interest without building | Click to gauge interest |

### The Growth Experiment Cadence

**Weekly Growth Sprint:**

```
Monday:    Review last week's results
           Prioritize this week's experiments

Tuesday-   Design and build experiments
Thursday:  Launch when ready

Friday:    Review early data
           Plan next week's experiments
           Document learnings
```

**Experiment Velocity Benchmarks:**

| Stage | Experiments/Quarter | Why |
|-------|---------------------|-----|
| Early Stage | 20-30 | Finding what works |
| Growth Stage | 50-100 | Optimizing loops |
| Scale Stage | 100-200 | Marginal gains |

### Analyzing Results

**Decision Framework:**

```
                Statistical Significance
                  Yes              No
            ┌─────────────┬─────────────┐
    Positive│   SHIP IT   │   EXTEND    │
    Result  │             │   TEST      │
            ├─────────────┼─────────────┤
    Negative│   LEARN &   │   CALL IT   │
    Result  │   ITERATE   │   (Neutral) │
            └─────────────┴─────────────┘
```

**Analysis Checklist:**

```
□ Did we reach required sample size?
□ Did we run for full business cycles?
□ Is the result statistically significant (p < 0.05)?
□ Is the effect size practically meaningful?
□ Did guardrail metrics hold?
□ Are there segment-level differences?
□ Can we explain the result?
```

### Learning Documentation

**After every experiment:**

```
┌─────────────────────────────────────────────────────────────┐
│                EXPERIMENT RESULTS                           │
├─────────────────────────────────────────────────────────────┤
│ RESULT: [Win / Loss / Neutral]                              │
│                                                             │
│ DATA:                                                       │
│ - Control: [X% conversion]                                  │
│ - Treatment: [Y% conversion]                                │
│ - Lift: [Z%]                                                │
│ - Significance: [p-value]                                   │
│                                                             │
│ DECISION: [Ship / Iterate / Kill]                           │
│                                                             │
│ LEARNINGS:                                                  │
│ - What did we learn about users?                            │
│ - What hypotheses does this generate?                       │
│ - What should we test next?                                 │
│                                                             │
│ NEXT STEPS: [Follow-up experiments]                         │
└─────────────────────────────────────────────────────────────┘
```

### Common Experiment Areas

| Area | Experiments to Try |
|------|-------------------|
| **Acquisition** | Landing page copy, CTA, social proof, form fields |
| **Activation** | Onboarding flow, welcome emails, feature discovery |
| **Retention** | Notification timing, re-engagement emails, feature adoption |
| **Monetization** | Pricing page, upgrade prompts, trial length |
| **Referral** | Invite flow, incentives, share mechanics |

### Anti-Patterns

- **HiPPO decisions** — Highest Paid Person's Opinion overrides data
- **Peeking** — Looking at results before sample size reached
- **P-hacking** — Running until you get significance
- **No guardrails** — Improving one metric while breaking another
- **Ship and forget** — Not monitoring post-ship
- **No documentation** — Same failed experiments repeated
- **Too many variants** — Diluting sample size
- **Testing tiny changes** — Button color when activation is broken
- **Experimentation theater** — Tests without rigor or learnings
