---
name: newsletter-management
description: Create, curate, and grow email newsletters across all formats and strategies. Use when working on newsletters, email newsletters, weekly digests, link roundups, curated content, audience building, subscriber engagement, or content distribution. Covers 6 newsletter formats (curated/link roundup, story-driven, educational, interview, data-driven, personal update), editorial issue structure, content sourcing via inference.sh CLI, commentary writing, sending cadence, subject line optimization, subscriber growth, and engagement metrics. Trigger keywords: newsletter curation, curated newsletter, newsletter writing, newsletter format, newsletter strategy, newsletter template, content curation, subscriber growth.
---

# Newsletter Management

Build, curate, and grow recurring newsletters that create genuine value for subscribers.

## Quick Start (inference.sh CLI)

```bash
curl -fsSL https://cli.inference.sh | sh && infsh login

# Find content to curate
infsh app run tavily/search-assistant --input '{
  "query": "[your niche] most important developments this week"
}'

# Generate newsletter header image
infsh app run infsh/html-to-image --input '{
  "html": "<div style=\"width:600px;height:200px;background:linear-gradient(135deg,#1e293b,#334155);display:flex;align-items:center;padding:40px;font-family:system-ui;color:white\"><div><h1 style=\"font-size:32px;margin:0;font-weight:800\">The Weekly Signal</h1><p style=\"font-size:16px;opacity:0.7;margin-top:8px\">Issue #47 — January 15, 2025</p></div></div>"
}'
```

## The 6 Newsletter Formats

### 1. Curated / Link Roundup

Share 5–15 curated links with commentary per link.

**Structure**:
- Opening: Personal note or insight
- 5–10 curated links with your take (not just a description)
- Closing: Personal sign-off

```markdown
## This Week's Top Picks

### [Article Title](url)
One to three sentences on why this matters and what the reader
will get from it. Add your take — don't just describe.
```

**Best for**: Building authority, staying top-of-mind | **Time**: 30–45 min

---

### 2. Story-Driven

Tell a personal story that teaches a lesson.

**Structure**: Hook → Story → Lesson → Application → Closing

**Best for**: Building connection, teaching through narrative | **Time**: 45–60 min

**Example**: "How I learned the hard way about delegation"

---

### 3. Educational / Deep Dive

Teach a specific concept, framework, or analysis (300–1,000 words).

**Structure**: Hook (why this matters) → Concept/Analysis → Examples → Application → Closing

```markdown
## The Big Story

[300-500 word analysis of the week's most important topic]

## Also Worth Reading

- **[Title](url)** — One sentence commentary
```

**Best for**: Establishing authority, providing value | **Time**: 60–90 min

---

### 4. Interview / Q&A

Feature a customer, expert, or practitioner.

**Structure**: Introduction → Q&A (5–10 questions) → Key Takeaway → Closing

**Best for**: Social proof, diverse perspectives | **Time**: 90–120 min (including interview)

---

### 5. Data-Driven / Trends

Share data, research, or trend analysis.

**Structure**: Surprising finding → Data presentation → Analysis → Application → Closing

**Best for**: Establishing authority, providing insights | **Time**: 60–90 min

**Example**: "2024 Remote Work Trends: What the Data Shows"

---

### 6. Personal Update

Share what you're working on, learning, and thinking about.

**Structure**:
- What I'm working on
- What I'm learning
- What I'm thinking about
- A recommendation (resource, tool, article)
- Closing

**Best for**: Authenticity, personal connection | **Time**: 30–45 min

---

## Issue Structure (Full Template)

```markdown
# [Newsletter Name] — Issue #[N]

## 👋 Hello

[2-3 sentences of personal intro — what's on your mind,
what this issue covers, why it matters right now]

## 🔥 The Big Story

[Featured content — your deepest analysis or most important
curated piece with commentary]

## 📚 Worth Reading

### [Title 1](url)
[2-3 sentence commentary with your take]

### [Title 2](url)
[2-3 sentence commentary]

## 💡 Quick Hits

- [One-liner + link](url)
- [One-liner + link](url)

## 📊 Stat of the Week

[One compelling data point with context]

## 💬 From the Community

[Reader reply, question, or discussion point]

---

That's it for this week. If you found this useful, forward
it to a colleague who'd enjoy it.

[Your name]

P.S. [Relevant insight, question, or recommendation]
```

## Content Sourcing

```bash
# Industry news
infsh app run tavily/search-assistant --input '{
  "query": "[your niche] news this week latest developments"
}'

# Research and data
infsh app run exa/search --input '{
  "query": "[your niche] research report statistics 2024"
}'

# Trending discussions
infsh app run tavily/search-assistant --input '{
  "query": "site:reddit.com [your niche] discussion this week"
}'
```

### Source Categories

| Source Type | Best For |
|-------------|----------|
| News (industry press) | Breaking developments |
| Research (papers, reports) | Data-backed insights |
| Blogs (engineering, personal) | Practitioner perspectives |
| Social (Twitter/LinkedIn threads) | Hot takes, discussions |
| Community (Reddit, HN) | Ground-level sentiment |

### Curation Quality Filter

For each piece, ask:
- Would I send this to a colleague 1-on-1?
- Does it teach something actionable?
- Is the source credible?
- Is it timely/relevant this week?
- Can I add commentary that adds genuine value?

If any answer is no, skip or find something better.

## Writing Commentary

Commentary is what makes a newsletter worth reading — not just the links.

```
❌ Describing: "This article talks about React Server Components."
❌ Restating: "React Server Components are here."

✅ Context: "This is the first production teardown I've seen. Key insight:
   they reduced initial JS bundle by 60%, but added build complexity."

✅ Your take: "I'm skeptical about the migration path here. Most teams
   I've talked to are waiting for better tooling."

✅ Connecting dots: "This pairs with Vercel's announcement last month —
   the ecosystem is converging on this pattern."
```

**Formula**: `[What happened] + [Why it matters to the reader] + [Your take or prediction]`

## Sending Cadence

**Weekly is the sweet spot** — same day, same time, every week.

| Frequency | Best For |
|-----------|----------|
| Weekly | Most newsletters — highest open rates |
| Bi-weekly | Deep analysis and essays |
| Monthly | Research roundups |
| Daily | News-focused short formats (high risk) |

**Best days**: Tuesday > Thursday > Wednesday. Avoid Mondays (inbox overload) and Fridays (weekend mode).

## Subject Lines

| Formula | Example |
|---------|---------|
| Issue # + teaser | "#47: The framework nobody's talking about" |
| Number + topic | "5 tools that changed my workflow this month" |
| Question | "Is TypeScript dying?" |
| Direct value | "The SQL optimization guide I wish I had" |

**Keep under 50 characters** — mobile truncates at ~35.

## Growth Strategies

| Strategy | How |
|----------|-----|
| Cross-promotion | Partner with complementary newsletters |
| Social distribution | Post key insights with a subscribe CTA |
| Referral program | "Forward to 3 friends" or formal rewards |
| SEO archive | Publish newsletter issues as blog posts |
| Lead magnet | "Subscribe and get [free resource]" |
| Consistent quality | The most reliable long-term growth lever |

```bash
# Create social teaser for newsletter
infsh app run x/post-create --input '{
  "text": "This week in The Weekly Signal:\n\n→ Why edge computing is eating the backend\n→ 5 tools I discovered this month\n\nJoin 2,000+ engineers: [link]\n\nIssue #47 drops tomorrow."
}'
```

## Metrics That Matter

| Metric | Good | Great | Fix If Low |
|--------|------|-------|------------|
| Open rate | 30–40% | 40%+ | Improve subject lines |
| Click rate | 3–5% | 5%+ | Better curation, stronger CTAs |
| Unsubscribe | < 0.5%/issue | < 0.2% | Check content quality + frequency |
| Reply rate | Any replies | Regular replies | Ask questions, invite conversation |
| Growth rate | 5–10%/mo | 10%+ | More distribution, referral program |

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| No consistent schedule | Same day, same time, every week |
| Links without commentary | Add your take on every piece |
| Too many links (15+) | 5–10 curated picks max |
| Generic subject lines | Tease best content, keep under 50 chars |
| No personal voice | Intro paragraph, opinions, personality |
| Only promotional content | 90% value, 10% promotion |
| No engagement CTA | Ask questions, invite replies |
| No archive/SEO | Publish issues as web pages |

## Related Skills

```bash
npx skills add inferencesh/skills@email-design
npx skills add inferencesh/skills@content-repurposing
npx skills add inferencesh/skills@seo-content-brief
```

Browse all apps: `infsh app list`
