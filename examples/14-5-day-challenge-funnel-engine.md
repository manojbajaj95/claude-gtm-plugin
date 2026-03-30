# The 5-Day Challenge Funnel Engine

Design a 5-day email challenge for your audience, wire up the CRM tagging flow, and launch it with a community post that drives sign-ups and sets the group's tone from day one.

## Workflow

### Step 1 — Design the challenge structure

```
Design a 5-day email-based challenge funnel for our target audience.
Read strategy/brand.md for ICP, pain points, and brand voice before starting.

The challenge should:
  - Solve one specific early-stage pain point (the kind that stops new users from
    making progress in their first week)
  - Deliver one small, completable win per day that builds on the previous
  - Culminate in Day 5 with a natural bridge into our core product or offer

Deliver:
  - Challenge name
  - Overarching transformation promise (before → after)
  - Day-by-day structure: Day # | Theme | Core task | Win the participant achieves
```

### Step 2 — Write the 5-day email sequence

```
Using the structure from Step 1, write all 5 challenge emails.
For each email:
  - Subject line (curiosity or benefit-driven, under 50 characters)
  - Opening hook (1–2 sentences, acknowledge where they are in the journey)
  - Day's task explained simply (what to do, why it matters)
  - Encouragement or social proof nudge
  - CTA: complete today's task + reply or post their result in the community
  - Under 200 words per email
Day 5 email: add a natural, non-pushy bridge to our product/offer as the logical next step.
```

### Step 3 — Map the CRM integration flow

```
Define the full CRM tagging and automation flow for challenge participants.

Trigger events and tags to apply:
  - Sign-up: tag challenge-enrolled, challenge-[challenge-slug]
  - Email 1 opened: tag challenge-day1-active
  - Day 5 email opened: tag challenge-completed
  - Did not open any email after Day 2: tag challenge-disengaged → trigger re-engagement
  - Clicked Day 5 CTA (product bridge): tag challenge-converted-interest

Post-challenge automation:
  - Completed participants: enroll in product onboarding nurture sequence
  - Disengaged participants: send a "catch-up" digest 48 hours after Day 5
  - All participants: add to segment challenge-alumni for future campaign targeting

Return the flow as a trigger table and a tag glossary.
```

### Step 4 — Write the community launch post

```
Write a social media post to drive initial sign-ups for the challenge.
Read about/me.md for personal voice.
Platform: [Insert Primary Channel — LinkedIn / X / Instagram]

Post structure:
  - Hook: open with the pain point the challenge solves (make it viscerally specific)
  - Body: explain what participants will have at the end of Day 5
  - Rules/expectations: 3 bullet points (e.g., show up daily, share your wins, no lurking)
  - CTA: link to sign-up page or "comment [WORD] to join"
  - Tone: warm, energizing, community-first — not salesy
  Under 250 words.
```

## Output

- `content/email/drafts/YYYY-MM-DD_challenge-sequence-<slug>.md` — 5-day email sequence
- `content/briefs/drafts/YYYY-MM-DD_challenge-crm-flow-<slug>.md` — CRM tagging and automation spec
- `content/<platform>/drafts/YYYY-MM-DD_challenge-launch-post-<slug>.md` — community launch post

