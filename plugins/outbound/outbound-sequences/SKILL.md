---
name: outbound-sequences
description: Templates and frameworks for cold outreach sequences. Email templates, cold call scripts, LinkedIn messages, subject lines, and response handling.
allowed-tools: Read, Write, Edit, WebSearch
---

# Outbound Sequences

Design high-response cold outreach sequences for email, phone, and LinkedIn.

## Input Context

Expect structured context from orchestrator:

```yaml
current_metrics:
  open_rate: percent
  reply_rate: percent
  meeting_rate: percent
diagnosed_problem: subject_lines | copy | targeting | CTA
target_persona:
  title: string
  industry: string
  company_size: string
channels: [email, phone, linkedin]
value_prop: string
social_proof: string
current_best: string  # sample copy
tool: Apollo | Outreach | Lemlist | etc.
```

## Sequence Architecture

### Multi-Channel Sequence (7 touches)

```
Day 1:  Email #1 (Initial) ──→ Day 3: LinkedIn Connect
Day 4:  Email #2 (Value-add) ──→ Day 6: LinkedIn Message
Day 7:  Phone Call ──→ Day 8: Email #3 (Insight)
Day 10: LinkedIn Engage ──→ Day 12: Email #4 (Case Study)
Day 15: Email #5 (Breakup)

RESPONSE BRANCHES:
Positive → Discovery call booking sequence
Objection → Objection handler sequence
"Not Now" → Nurture sequence (30-day follow-up)
```

## Channel Templates

| Channel | Resource |
|---------|----------|
| Email | [resources/email-outreach.md](resources/email-outreach.md) |
| Cold Calling | [resources/cold-call-scripts.md](resources/cold-call-scripts.md) |
| LinkedIn | [resources/linkedin-outreach.md](resources/linkedin-outreach.md) |

## Response Handling

### Positive Response

```
{{first_name}}, great to hear from you!

I have {{day}} at {{time}} or {{day}} at {{time}} available.

Here's my calendar if easier: {{link}}

Looking forward to it.

{{sender_name}}
```

### Objection Response

```
{{first_name}}, appreciate the candid response.

Totally understand {{their_objection}}.

Quick question: {{question_uncovering_real_concern}}

Either way, happy to {{lower_commitment_offer}}.

{{sender_name}}
```

### "Not Now" Response

```
{{first_name}}, completely understand - timing is everything.

When would be a better time to revisit this?

Happy to reach back out in {{timeframe}} if that works.

{{sender_name}}
```

### "Send More Info" Response

```
{{first_name}}, happy to share more.

Here's {{one_specific_asset}}: {{link}}

Quick question: What specifically prompted the interest?

That'll help me tailor what I send next.

{{sender_name}}
```

## Personalization Framework

| Tier | Time/Prospect | What to Include |
|------|---------------|-----------------|
| Tier 1 (Basic) | 30 sec | Name, company, industry |
| Tier 2 (Researched) | 2-3 min | News, LinkedIn content, job postings |
| Tier 3 (Deep) | 10-15 min | Podcast quotes, custom video, mutual connections |

### Research Sources

- LinkedIn posts and activity
- Company news/press releases
- Job postings (indicate priorities)
- Podcast appearances
- Conference presentations
- Mutual connections

## Timing Optimization

### Sequence Spacing

- Email to email: 3-4 days
- Email to LinkedIn: 1-2 days
- LinkedIn to phone: 1 day
- After no response: wait 3 days
- Breakup email: day 14-15

## Output Format

```markdown
# OUTBOUND SEQUENCE: {{Company Name}}

## Target Persona
{{title}}, {{industry}}, {{company_size}}

## Sequence Architecture
[Visual flow diagram]

## Email Sequence
### Email 1: Initial (Day 1)
**Subject:** [3 options]
**Preview:** [preview text]
**Copy:** [full email]
**Personalization:** [variables used]

### Email 2: Follow-up (Day 4)
...

## LinkedIn Sequence
### Touch 1: Connection (Day 3)
...

## Cold Call Script
[Opening + structure + objection handling]

## Response Playbook
[Templates for each response type]

## A/B Test Variants
[Specific tests for diagnosed problem area]
```

## Anti-Patterns

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Generic opener | "Hope you're well" ignored | Specific observation |
| Feature dump | They don't care yet | Lead with their pain |
| Multiple CTAs | Confusion, lower response | Single clear ask |
| Long emails | Won't be read on mobile | Under 75 words |
| Same angle each email | No reason to reply | New value per touch |
| No personalization | Feels like spam | Add {{variables}} |
