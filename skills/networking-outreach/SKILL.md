---
name: networking-outreach
description: Relationship-first networking skill for identifying the right people to connect with and drafting value-add outreach — not sales, not referral asks. Use when building a network for a job search, career pivot, partnership, or industry access. Covers target identification by purpose, deep LinkedIn + web research on a specific person, brainstorming 10 value-add angles, and drafting three outreach formats: cold networking email (max 200 words), LinkedIn connection request (max 300 characters), and hiring manager follow-up email (120–160 words). Never drafts generic openers or referral asks — always leads with a specific observation and genuine value.
---

# Networking Outreach

Relationship-first outreach built on research and value. The goal is to start a conversation by giving something, not asking for something.

## Quick Start

**Mode 1 — Identify targets:**
1. Tell me your networking purpose (e.g. "break into AI safety", "find hiring managers at fintech startups")
2. I'll build a target persona matrix and suggest 5–10 specific people to reach

**Mode 2 — Draft outreach for a specific person (cold networking):**
1. Share their LinkedIn URL (or screenshot if profile is private)
2. I'll research them + their company via the web
3. We'll pick the best value-add angle together
4. I'll draft: email (≤200 words) + LinkedIn connection request (≤300 chars)

**Mode 3 — Hiring manager follow-up:**
1. Share their LinkedIn URL + the role you applied for
2. Tell me any referral context and your core proof points
3. I'll draft a personal follow-up email that leads with a specific reference to their work, states your value clearly, and ends with a soft CTA

---

## Mode 1: Identify Targets

### Intake Questions

Before generating targets, establish:

| Question | Why It Matters |
|----------|----------------|
| What's your goal? | Job, partnership, learning, visibility |
| What's your current context? | Title, company, background |
| What industry/function? | Narrows the search |
| Do you have any warm connections? | Starting point for introductions |
| What's your timeline? | Urgency affects strategy |

### Target Persona Matrix

| Dimension | Options |
|-----------|---------|
| **Seniority** | Peer / +1 level / +2 levels (max) |
| **Accessibility** | Active on LinkedIn, writes publicly, open profiles |
| **Relevance** | Working on what you want to learn/join/partner with |
| **Warmth** | Shared community, school, company, mutual connection |

### Target Prioritization

Rank targets by:
1. **Warm path** — mutual connection, shared community, same alumni network
2. **Content match** — they've written or spoken about your exact interest
3. **Accessibility** — they respond publicly, actively post, have open DMs
4. **Seniority fit** — close enough to relate, senior enough to open doors

### Output Format

For each target:
- Name + LinkedIn URL
- Why they're relevant
- Best angle to approach
- LinkedIn search query to find similar people

---

## Mode 2: Research & Draft Cold Outreach

### Step 1: Pull Their LinkedIn Profile

Use browser tools to read the full profile (expand all sections):

| Tool | MCP Name | Use For |
|------|----------|---------|
| Screenshot | `mcp__computer-use__screenshot` | Full page capture |
| Navigate | `mcp__Claude_in_Chrome__navigate` | Go to LinkedIn URL |
| Get page text | `mcp__Claude_in_Chrome__get_page_text` | Extract full profile text |
| Playwright fallback | `mcp__plugin_compound-engineering_pw__browser_snapshot` | Accessibility tree |

**Extraction steps:**
1. Navigate to the LinkedIn URL
2. Screenshot or get_page_text the full profile
3. Note: headline, current role, recent posts, skills, education, shared connections

### Step 2: Web Research

Search for additional context beyond LinkedIn:

- `[Name] [Company] interview OR podcast OR talk`
- `[Company] goals challenges [current year]`
- `[Name] article OR newsletter OR writing`
- `[Company] funding hiring news`

Capture:
- What they've said publicly (opinions, priorities)
- Their company's current focus (fundraise, launch, hiring push)
- Anything they're building or working toward

### Step 3: Brainstorm Value-Add Angles

Generate 5–10 ideas. Every angle must answer: **"What's in it for them?"**

| # | Angle | Example |
|---|-------|---------|
| 1 | Share a resource they'd genuinely care about | Article on a problem they mentioned |
| 2 | React to something they published — specific insight | "Your take on X made me think of Y" |
| 3 | Extend or challenge their public work | "I tried your framework, here's what I found" |
| 4 | Offer a skill/perspective they don't have | Fresh context from a different industry |
| 5 | Introduce them to someone useful | Connector play |
| 6 | Flag an opportunity they might not know about | Event, grant, community, tool |
| 7 | Share a relevant win related to their challenge | "We solved X, happy to share what worked" |
| 8 | Give feedback on something they're building | Beta test, review, honest take |
| 9 | Ask a specific expert question that's flattering to their depth | Shows you've done the homework |
| 10 | Surface a shared interest or community | Common ground, not flattery |

### Step 4: Draft Two Formats

#### Cold Email (max 200 words)

**Structure:**
```
Subject: [2–4 words, lowercase, looks internal — not a pitch]

[Specific hook — one observation about them, their work, or their company]

[One sentence connecting it to why you're reaching out]

[Your value offer — what you're giving, not asking for]

[Soft CTA — "Worth a look?" / "Thought you'd find this useful" / "Happy to share more if helpful"]

[Name]
```

**Rules:**
- No "hope this finds you well"
- No "I'm reaching out because"
- "You/your" outnumbers "I/me" 2:1
- One ask max — low-friction (share, reply, yes/no)
- Never ask for a referral or coffee chat in the first message

#### LinkedIn Connection Request (max 300 characters)

**Structure:**
```
[Specific observation about their work] + [one-line reason to connect] + [optional: soft opener]
```

**Examples:**
- "Your post on [X] was the clearest take I've seen on [Y]. I work on [related thing] — would love to be connected."
- "Loved the piece on [X]. I'm building [Y] and ran into the same problem — would value being in your network."
- "You spoke at [event] about [topic]. I'm [context]. Your work on [specific thing] is exactly what I'm exploring."

**Rules:**
- No "I came across your profile"
- No "I'd love to pick your brain"
- Must fit in 300 characters — count before sending
- Specific > flattering

---

## Mode 3: Hiring Manager Follow-Up

Use when you've applied for a role and want to reach out personally to the hiring manager. This is not a cold pitch — it's a human note that shows you did the homework and know why you specifically fit.

### When to Use

- You've already submitted an application
- You have a name and some public context on the hiring manager
- You want to stand out from the applicant pile without being pushy

### Structure

```
Subject: [role name] — a specific note

[One concrete reference to something they've written, built, or said publicly —
connect it directly to the problem you'd solve in the role]

[One paragraph: who you are + your most relevant proof point + a link]

[Optional: honest acknowledgment of any prior attempt at this company —
honesty + persistence reads well]

[Soft CTA — 15 minutes / calendar link]

[Name]
```

### Rules

- Lead with THEIR work, not your credentials
- One specific reference beats three generic ones
- Include a concrete proof point (project, demo, portfolio, event with numbers)
- If you've applied or interviewed before and didn't make it — say so
- No "I'm excited about this opportunity" — show it instead
- CTA: calendar link or "15 minutes" — never "let me know if you're interested"
- Target length: 120–160 words

### Key Principle

**Admit the obvious about yourself** — state the thing that's been true all along that makes you the right fit, as if you're finally saying it out loud. Don't hide behind credentials. Open with identity, not job title.

Example opening pattern:
> "Your piece on [X] is exactly the problem I've been working on from [the other side / a different angle]."

Then: who you are in one line → one proof point with a link → honest context → soft ask.

---

## Research Checklist

Before drafting any format, verify you have:

- [ ] Current role + company + headline
- [ ] 2–3 recent posts, articles, or public content (themes, opinions)
- [ ] Company's current priority (launch, hiring, raise, expansion)
- [ ] Career trajectory (what they're moving toward)
- [ ] Any external writing, interviews, or talks
- [ ] Shared connections, communities, schools, or past companies
- [ ] Something they're building or publicly excited about

---

## Authenticity Rules

- Sound like yourself, not a template
- Lead with their world, not your pitch
- Personalization must connect to a real point — not filler
- No flattery without specifics ("Your work is impressive" = delete)
- One CTA, low friction — share, reply, or yes/no
- Tweak the draft to match your voice before sending

---

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Generic opener | Ignored immediately | Specific observation about their work |
| Asking for coffee chat | Too much friction, too early | Share something useful first |
| Multiple asks | Confusing | Pick one: share, reply, or simple yes/no |
| Long cold email | Won't be read | Under 200 words, ideally under 100 |
| Flattery without substance | Feels like a template | Cite the specific thing you liked |
| No value offer | It's a take, not a give | Always lead with what they get |
| Mentioning referral in first message | Kills rapport before it starts | Build relationship first |
| Credentials dump to hiring manager | Reads like a cover letter | Lead with their work, then one proof point |

---

## Related Skills

- [outbound-email-strategy](../outbound-email-strategy/SKILL.md) — when the relationship converts to a sales conversation
- [linkedin-personal-branding](../linkedin-personal-branding/SKILL.md) — optimize your own profile before outreach
- [linkedin-content](../linkedin-content/SKILL.md) — attract inbound so people reach out to you
