---
name: linkedin
description: LinkedIn profile optimization and content creation. Use when auditing or optimizing a LinkedIn profile, writing LinkedIn posts, developing thought leadership content, building personal brand on LinkedIn, analyzing SSI score, improving profile visibility, or crafting hooks and engagement strategy for LinkedIn.
---

# LinkedIn

Two modes — often used together:

1. **Profile Audit** — analyze and optimize your LinkedIn profile (photo, headline, About, experience, skills, SSI, engagement rate)
2. **Content Creation** — write high-engagement posts, build thought leadership, grow your audience

Check for `strategy/brand.md` and `about/me.md` before starting. If they exist, use them to calibrate voice, audience, and positioning.

---

## Mode 1: Profile Audit

### Analysis Types

- **Full Profile Audit** — all elements, complete report with scores
- **Quick Profile Review** — priority action items and quick wins only
- **Visibility Optimization** — keyword/SEO discoverability
- **Content Strategy Analysis** — posting frequency, engagement performance

### Accessing LinkedIn via Chrome DevTools

Requires LinkedIn profile open in Chrome, user logged in.

| Tool | MCP Name | Use For |
|------|----------|---------|
| List Pages | `mcp__chrome-devtools__list_pages` | Find LinkedIn tab |
| Select Page | `mcp__chrome-devtools__select_page` | Focus tab |
| Snapshot | `mcp__chrome-devtools__take_snapshot` | Accessibility tree with UIDs |
| Screenshot | `mcp__chrome-devtools__take_screenshot` | Photo and banner analysis |
| Navigate | `mcp__chrome-devtools__navigate_page` | Go to URLs |
| Click/Hover | `mcp__chrome-devtools__click` / `hover` | Interact with elements |

**Workflow:** `list_pages` → find `linkedin.com/in/` → `select_page` → `take_snapshot` → `take_screenshot` → hover lazy-loaded sections → re-snapshot.

**Playwright fallback:** If Chrome DevTools unavailable, use `mcp__playwright__browser_*` equivalents.

**Sections to analyze:** photo, banner, headline, About, custom URL, experience, education, skills/endorsements, recommendations, featured section, activity/posts, followers/connections, groups.

**Common errors:**

| Error | Recovery |
|-------|----------|
| LinkedIn tab not found | Ask user to open LinkedIn in Chrome |
| Content not loading | Scroll, increase timeout, refresh |
| Rate limited/CAPTCHA | Pause 30+ seconds, proceed slowly |
| SSI requires Sales Navigator | Note unavailable, provide estimation |

### Profile Scoring

| Category | Weight | Key Factors |
|----------|--------|-------------|
| Visual Identity | 15% | Photo quality, banner, consistency |
| Headline | 15% | Value proposition, keywords, memorability |
| About Section | 15% | Story, keywords, CTA |
| Experience | 20% | Completeness, achievements, metrics |
| Skills & Endorsements | 10% | Relevance, count, endorsements |
| Recommendations | 10% | Quality, diversity, recency |
| Activity & Content | 15% | Posting frequency, engagement rate |

**Score guide:** 90–100 Elite · 80–89 Excellent · 70–79 Good · 60–69 Average · <60 Needs Work

### Mandatory Metrics

**Engagement Rate:**
```
(Reactions + Comments + Shares) / Impressions × 100
```
Target: 3%+. Example: (15+1+0)/1,376×100 = 1.16% → below target.

**SSI Score (target: 70+/100):**
- User visits `linkedin.com/sales/ssi` to share actual score, OR
- Estimate: All-Star + active + engaged network → 70–85; complete + regular posting → 55–70; basic + occasional → 40–55

### Profile Element Best Practices

**Photo:** 400×400px min, professional attire, approachable expression, face 60–70% of frame, clean background.

**Banner (1584×396px):** Branded, value proposition text, no small text or clutter.

**Headline (220 chars):** `[Who you are] | [Problems you solve] | [Benefit/result] | [Keywords]`
- ❌ "Marketing Manager"
- ✅ "Marketing Manager | Helping B2B Companies Grow Through Data-Driven Strategies | 45% Revenue Increase Specialist"

**About (2,600 chars):** Hook → story → what you do/who you help → achievements with metrics → skills → CTA. First person, short paragraphs, relevant keywords.

**Experience:** Quantified achievements (%, $, #), scope, key projects demonstrated.

**Featured:** 3–6 curated items — portfolio, case studies, articles, lead magnets.

### Audit Report Structure

1. Executive Summary
2. Classification (Industry, Profile Type, Target Audience)
3. Profile Scorecard
4. Calculated Metrics (Engagement Rate, SSI)
5. Element-by-Element Analysis
6. Quick Wins (high impact, low effort)
7. Strategic Recommendations
8. 30-60-90 Day Action Plan

See `references/scoring_framework.md`, `references/metrics_benchmarks.md`, and `assets/profile_audit_template.md` for detailed criteria, industry benchmarks, and report templates.

**Industry tone calibration:** Conservative industries (Legal, Finance, Healthcare) → formal tone, 2–3x/week, minimal emojis. Progressive industries (Tech, Marketing, Startups) → casual/personal, 4–5x/week, emojis acceptable.

---

## Mode 2: Content Creation

### Core Principles

**Authenticity over performance.** LinkedIn readers instantly spot manufactured vulnerability and engagement bait. What resonates is genuinely useful or genuinely human.

- Real experiences with honest reflection
- Specific insights from your actual work
- Admitting what you don't know
- ❌ Performed vulnerability for engagement
- ❌ Stories that feel too perfectly structured

**One idea per post.** If you have five points, that's five posts.

**Value without strings.** Ask: "Would I find this valuable if a stranger posted it?"

### Post Anatomy

```
[HOOK — first 1-2 lines]          ← Visible before "...see more" (~210 chars)
...see more
[BODY — story or value]
 - Short paragraphs (1-2 sentences)
 - Line breaks for readability
[CTA — last 1-2 lines]
#hashtags (3-5, at the end)
```

**Character limits:**

| Element | Limit |
|---------|-------|
| Post text | 3,000 chars |
| Visible before "see more" | ~210 chars |
| Comment | 1,250 chars |
| Headline | 220 chars |
| About section | 2,600 chars |

### Hook Formulas

| Type | Example |
|------|---------|
| Honest admission | "I've been wrong about remote work." |
| Specific observation | "I've noticed something in every founder who scaled past $10M." |
| Direct challenge | "Most career advice optimizes for the wrong thing." |
| Unexpected angle | "The best hire I made had the worst resume." |
| Contrarian opinion | "Unpopular opinion: code reviews are a waste of time." |
| Personal story | "I got fired on a Tuesday. Best thing that ever happened." |
| List promise | "I've hired 200+ engineers. Here are 5 red flags I look for." |

**Hooks to retire:**
```
❌ "This one thing made me $X"
❌ "The CEO pulled me aside and said..."
❌ "I'm excited to announce..."
❌ "In today's rapidly evolving landscape..."
❌ Starting with a hashtag or emoji
```

See `references/hooks.md` for comprehensive examples.

### Formatting

```
❌ Dense paragraph: "I learned something about leadership last week. My team was
struggling and instead of pushing harder, I removed scope. The result was incredible."

✅ LinkedIn formatted:
"I learned something about leadership last week.

My team was struggling with a deadline.

Instead of pushing harder, I removed scope.

The result?

We shipped faster.
And the quality was BETTER."
```

Rules: one sentence per line, blank lines between paragraphs, numbered lists for tips, 3–5 hashtags at the very end (never inline), one emoji max.

### Post Formats

**Story Post** (personal experiences, lessons):
```
[Honest admission or surprising outcome]
[One sentence of context]
[What happened — the tension]
[The turning point]
[What you learned]
[Question for reader]
```

**List Post** (frameworks, actionable advice):
```
[Hook — clear value promise]
[Why this matters — one sentence]
1. [Point with brief context]
2. [Point with brief context]
3. [Point with brief context]  (3-7 items max)
[Closing insight or question]
```

**Contrarian Post** (challenging conventional wisdom):
```
[Your position, stated directly]
[The common belief you're challenging]
[Your reasoning — why you see it differently]
[Evidence or experience]
[Nuanced conclusion — acknowledge complexity]
[Invite discussion]
```
*Guardrails: Have genuine expertise, argue against ideas not people, offer an alternative, be open to being wrong.*

**Observation Post** (industry insights, trends):
```
[What you've observed]
[Specific evidence or examples]
[Why it matters]
[Your interpretation]
[Question to test if others see it too]
```

### Content Pillars

Rotate through 3–5 pillars:

| Pillar | Example |
|--------|---------|
| **Expertise** | "5 database patterns every engineer should know" |
| **Stories** | "The hardest feedback I ever received" |
| **Opinions** | "AI won't replace engineers. Bad managers will." |
| **Behind the scenes** | "Here's our actual sprint retrospective format" |
| **Curated insights** | "I analyzed 500 job postings. Here's what changed." |

### Algorithm Signals

| Signal | Impact |
|--------|--------|
| Dwell time | Very High — write posts people read fully |
| Comments | Very High — ask questions, create discussion |
| Saves | High — actionable, reference-worthy content |
| "See more" clicks | High — strong hook |
| External links in post | Negative — put links in comments instead |
| Editing within first hour | Negative |
| Posting >1x/day | Negative |

**Link post workaround:** Post without link → add link as first comment → edit post to say "Link in comments."

### Vulnerability Guidelines

**Share when:** The experience taught something others can learn, you've processed it enough to offer perspective, it serves the reader.

**Don't share when:** The wound is still fresh, you're seeking sympathy not providing value.

**Test before posting:** Am I sharing to help others or to process my own feelings? Would I be comfortable if this went viral?

### CTAs

| Type | Example |
|------|---------|
| Genuine question | "What's the worst career advice you've received?" |
| Agreement check | "Agree or disagree?" |
| Experience ask | "Has this happened to you?" |
| Bookmark prompt | "Save this for your next [situation]" |

**Avoid:** "Comment YES if...", "Share this with 3 people", "Follow me for more" — engagement bait destroys trust.

### Engagement Strategy

- **First hour:** Respond to every comment, ask follow-up questions to extend conversations
- **Daily comments on others:** Add insight, not just agreement — "Great post!" without substance builds nothing
- **Posting schedule:** Tue–Thu 7–8 AM, 12 PM, or 5–6 PM; avoid posting >1x/day

### Anti-Patterns

- "I'm excited to announce..." (corporate speak)
- Humblebrags disguised as lessons
- Recycled viral formats (the Uber driver wisdom, the airport conversation)
- Every. Sentence. As. Its. Own. Line. (when overused)
- Hashtag stuffing (>5)
- Engagement pods (LinkedIn detects and penalizes)

### Pre-Posting Checklist

- [ ] Hook: Would this stop MY scroll?
- [ ] Focus: Is there ONE clear idea?
- [ ] Value: Would I find this useful if someone else posted it?
- [ ] Authenticity: Does this sound like me, not "LinkedIn me"?
- [ ] Format: Short paragraphs, scannable with line breaks?
- [ ] CTA: Genuine engagement question (not bait)?
- [ ] Links: External links in comments, not the main post?

---

## References

- `references/hooks.md` — Complete hook patterns with examples
- `references/scoring_framework.md` — Detailed profile scoring criteria
- `references/metrics_benchmarks.md` — Industry benchmarks for SSI, engagement, growth
- `assets/profile_audit_template.md` — Complete audit report template
- `assets/quick_review_template.md` — Rapid assessment checklist
- `assets/action_plan_template.md` — 30-60-90 day roadmap template
