# The Viral Loop Referral Setup

Design a "Give $X, Get $Y" referral program for power users, map the automation flow, and write the full triggered email sequence — ready to hand off to engineering and CRM.

## Workflow

### Step 1 — Design the incentive structure

```
Design a "Give $X, Get $Y" referral program for our current power users.
Define:
  - Who qualifies as a power user (usage threshold or subscription tier)
  - The referrer reward: what they get when a referred user converts
  - The referee reward: what the new user gets for signing up via referral
  - Expiry rules for rewards (if any)
  - Any cap on referral credits per user
Base the incentive on our unit economics — the reward should cost less than our
current Cost Per Acquisition. Reference strategy/brand.md for pricing context.
```

### Step 2 — Map the automation flow

```
Map out the full marketing automation flow for the referral program.
Include these trigger points:
  1. Referral program invite: triggered after a user's 3rd login
  2. Referral link share confirmation: sent when user generates their referral link
  3. Referred user signed up: notification to referrer
  4. Reward delivery: triggered when referred user converts (define "converts")
  5. Reminder nudge: sent to users who have a referral link but haven't shared it (Day 7)
For each trigger: event condition → email or in-app action → delay (if any)
Output as a flow diagram description and a trigger table.
```

### Step 3 — Write the email sequence

```
Read strategy/brand.md and about/me.md for brand voice.
Write the copy for the automated email sequence from Step 2.
Deliver:
  Email 1 (Invite, after 3rd login):
    - Subject line
    - Body: introduce the program, explain the Give/Get, prominent CTA to generate link
    - Under 150 words
  Email 2 (Reward delivery confirmation):
    - Subject line
    - Body: congratulate, confirm reward, CTA to use reward or share again
    - Under 100 words
  Email 3 (Nudge, Day 7 no share):
    - Subject line
    - Body: soft reminder, re-state the value, low-friction CTA
    - Under 100 words
```

## Output

- `content/briefs/drafts/YYYY-MM-DD_referral-program-brief.md` — incentive structure and automation flow
- `content/email/drafts/YYYY-MM-DD_referral-email-sequence.md` — 3-email sequence copy
