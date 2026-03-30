# The Frictionless Bug-Reporting Loop

Identify the highest-friction setup screen in your onboarding, build an automated idle-trigger feedback prompt, and follow up instantly with a troubleshooting email that feels helpful rather than automated.

## Workflow

### Step 1 — Identify the friction point in onboarding

```
Review our current user onboarding flow for new sign-ups.
Pinpoint the step(s) where new users experience the most:
  - Technical friction (errors, unclear instructions, required integrations)
  - Drop-off (users exit or go idle without completing the step)
  - Support tickets (common themes in early-stage help requests)

For each friction point return:
  - Step name and position in the onboarding sequence
  - Type of friction (technical, cognitive, motivational)
  - Average time users spend on this step before dropping or idling
  - The single most common reason users get stuck here
```

### Step 2 — Set up the idle-trigger feedback protocol

```
Define an automated issue reporting protocol that triggers a feedback prompt when a
user has been idle on a setup screen for more than 3 minutes.

Deliver:
  Trigger specification:
    - Event: user idle on [setup screen name] for 180 seconds without completing
      the required action
    - Delivery method: in-app tooltip or modal (not a new page)
    - Prompt copy (under 30 words): friendly, non-accusatory, offers a path forward
      Example tone: "Stuck here? You're not alone — here's what usually helps."
    - Options presented: [Quick Fix guide] | [Chat with support] | [Skip for now]

  CRM/tracking action on prompt display:
    - Tag user: onboarding-idle-[screen-slug]
    - Log timestamp and screen name
    - If user clicks "Skip for now": enroll in troubleshooting email (Step 3)
    - If user clicks "Chat with support": tag support-escalation-onboarding
      and alert support queue

Return the trigger spec as an engineering handoff brief.
```

### Step 3 — Write the follow-up troubleshooting email

```
Write the marketing automation email that fires immediately (within 5 minutes) when
a user triggers the idle prompt and chooses "Skip for now" or does not interact with
the prompt within 10 minutes.

Read about/me.md for brand voice.

Email spec:
  - Trigger: idle-trigger tag applied (Step 2) + user did not resolve the step
  - Send delay: 5 minutes after trigger
  - Subject line: helpful and specific to the screen they were stuck on
    (use dynamic variable: {{screen_name}})
  - Opening: acknowledge they may have hit a snag — normalize it
  - Body:
      1. The single most common fix for this screen (specific steps, under 5 lines)
      2. Link to the relevant help doc or video walkthrough
      3. Direct support contact option (not a generic "contact us" link)
  - CTA: "Back to setup" button that deep-links to the exact screen
  - Tone: peer-to-peer, not corporate support ticket
  - Under 150 words
```

## Output

- `content/briefs/drafts/YYYY-MM-DD_idle-trigger-spec-<screen-slug>.md` — engineering handoff for the idle trigger
- `content/email/drafts/YYYY-MM-DD_troubleshooting-followup-<screen-slug>.md` — follow-up email
