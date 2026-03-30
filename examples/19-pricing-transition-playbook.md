# The Pricing Transition Playbook

Communicate a pricing change to legacy users with empathy and transparency, then send the sequence in staggered batches so you can catch churn signals before they compound.

## Workflow

### Step 1 — Analyze the pricing change impact

```
Review our recent pricing strategy changes.
For legacy users specifically, identify:
  - Which legacy plan(s) are affected and how (price increase, feature removal,
    tier consolidation, or feature addition)
  - The exact delta: what they currently pay vs. what they will pay (or lose)
  - The added value they receive under the new structure (be specific, not vague)
  - The effective date and any grace period
  - User segments most likely to churn based on usage patterns or plan type

Return a plain-language summary of the change as if explaining it to a customer —
no internal jargon.
```

### Step 2 — Write the email sequence

```
Read strategy/brand.md and about/me.md for brand voice and tone.
Using the impact analysis from Step 1, draft a 3-email sequence following customer
success and retention best practices.

Email 1 — Heads up (send 30 days before effective date):
  - Subject: transparent, not alarming (avoid "Important changes to your account")
  - Open by acknowledging their loyalty as a legacy user
  - Explain the change clearly: what's changing, what's not, and the exact date
  - Lead with the added value they're gaining before mentioning any cost increase
  - Include a direct link to a FAQ page or support chat
  - Under 200 words

Email 2 — Value reinforcement (send 14 days before):
  - Subject: focused on what they now have access to
  - Spotlight one specific new capability or benefit relevant to their usage
  - Include a 1-click "lock in your plan" or "confirm your account" CTA if applicable
  - Social proof: brief mention of what other users are doing with the new tier
  - Under 150 words

Email 3 — Final notice (send 3 days before):
  - Subject: factual, clear timeline ("Your plan updates in 3 days")
  - Recap: what changes on [date], what stays the same
  - Escalation path: link to billing support for anyone who needs to talk
  - Under 100 words
```

### Step 3 — Configure the staggered send plan

```
Design a staggered batch sending plan for the 3-email sequence.
Goal: monitor sentiment and churn signals between batches before sending to the full list.

Batch structure:
  - Batch 1 (5% of affected users): send Email 1 first. Monitor for 48 hours.
    Watch: unsubscribe rate, reply sentiment, support ticket volume.
    If unsubscribe rate exceeds [Insert Churn Threshold]%, pause and review before batch 2.
  - Batch 2 (20% of affected users): send if Batch 1 metrics are within acceptable range.
  - Batch 3 (remaining 75%): send after Batch 2 clears the 48-hour observation window.

For each subsequent email in the sequence, apply the same 3-batch structure.

Deliver:
  - Batch schedule table: batch # | % of list | send date | observation window | go/no-go metric
  - Recommended CRM segment filters to build each batch
  - Alert thresholds: the specific numbers that should trigger a pause and review
```

## Output

- `content/email/drafts/YYYY-MM-DD_pricing-transition-sequence.md` — 3-email sequence
- `content/briefs/drafts/YYYY-MM-DD_pricing-staggered-send-plan.md` — batch schedule and CRM segment spec

