# The Retention Audit Sprint

Find exactly where new users give up, identify the "Time to Value" moment, and deliver a 3-step fix plan plus a re-engagement welcome email.

## Workflow

### Step 1 — Define the Time to Value moment

```
Review the user onboarding flow for new sign-ups.
Identify:
  - The "Time to Value" (TTV) moment — the first action where a user experiences
    the core benefit of the product (e.g., first report generated, first connection made)
  - How many steps it currently takes to reach that moment from sign-up
  - The median time to reach that moment based on available data
```

### Step 2 — Find the critical exit point

```
Using funnel analytics for the onboarding flow, find the step immediately preceding
the most common exit point.
Return:
  - Step name and position in the flow
  - Drop-off rate at this step
  - Possible friction causes (too many fields, unclear instruction, feature gate, etc.)
  - What percentage of users who pass this step go on to reach the TTV moment
```

### Step 3 — Deliver the fix plan

```
Based on the findings from Steps 1 and 2, deliver a 3-step recommendation plan to
simplify or remove the friction at the critical exit point.
Each recommendation should include:
  - The specific change (what to do)
  - Expected impact (why it should reduce drop-off)
  - Implementation effort: Low / Medium / High
Prioritize by highest impact-to-effort ratio.
```

### Step 4 — Write the re-engagement email

```
Read strategy/brand.md for brand voice and ICP.
Draft a welcome email targeting users who completed sign-up but did not reach the
TTV moment within 48 hours.
Email structure:
  - Subject line: curiosity or benefit-driven (not "You haven't finished setting up")
  - Opening: acknowledge where they are, not what they failed to do
  - Body: one-sentence reminder of the TTV benefit + a single CTA back to the exact step
  - Tone: warm, helpful, low pressure
Under 120 words.
```

## Output

- `content/briefs/drafts/YYYY-MM-DD_retention-fix-plan.md` — 3-step recommendation plan
- `content/email/drafts/YYYY-MM-DD_re-engagement-welcome.md` — re-engagement email
