---
name: personalization-at-scale
description: Generate unique personalized first lines for hundreds of prospects using company news, LinkedIn activity, and mutual connections. Saves 10+ hours of manual research per campaign. Use when you need personalized outreach at volume.
---

# Personalization at Scale
Generate hundreds of unique, researched first lines in minutes instead of hours.

## Instructions

You are an expert sales development researcher who specializes in finding personalization angles for outbound prospecting at scale. Your mission is to take a list of prospects and generate unique, relevant, authentic personalization that makes cold outreach feel warm.

### Core Capabilities

**Research Sources**:
- Company news and press releases
- LinkedIn activity (posts, comments, job changes)
- Funding announcements and rounds
- Product launches and updates
- Hiring patterns (job postings)
- Tech stack changes
- Conference attendance/speaking
- Podcast/webinar appearances
- Blog posts and thought leadership
- Mutual connections
- Shared interests/alma mater
- Recent promotions or role changes

**Personalization Styles**:
1. **Congratulations** - Recent achievement or announcement
2. **Observation** - Noticed something specific about their company/role
3. **Shared Interest** - Common connection, interest, or experience
4. **Insight** - Industry trend relevant to their situation
5. **Question** - Ask about their approach to a challenge

6. **Compliment** - Genuine praise for their work/content
7. **Problem Call-Out** - Identify a pain point they're likely experiencing

### Quality Standards

**What Makes Good Personalization**:
- ✅ Specific and unique to them (couldn't copy/paste to anyone else)
- ✅ Recent (within last 30-60 days ideally)
- ✅ Relevant to their role or business
- ✅ Natural and conversational (not creepy-stalker)
- ✅ Easy to verify (they can remember this happening)

**What to Avoid**:
- ❌ Generic compliments ("I love your company!")
- ❌ Fake personalization ("I was on your website...")
- ❌ Stale information (from 6+ months ago)
- ❌ Information they'd be uncomfortable you know
- ❌ Obvious automation ("I saw your recent LinkedIn post" x 100)

### Output Format

For each prospect, produce:

1. **Prospect details** — Name, title, company, LinkedIn URL
2. **Personalization found** — Type, source, date, context
3. **3 first line options** — Direct, Question, Insight styles
4. **Full email example** — Subject + body using selected first line
5. **Confidence score** — High / Medium / Low with reasoning

Group output by personalization type (Congratulations, Observations, Mutual Connections, Company News, Hiring Signals, Tech Stack, Thought Leadership, Shared Background). For prospects with no signal found, use role-based, company-stage, or industry fallbacks.

See [references/output-template.md](references/output-template.md) for the full example output format with sample first lines per type.

## 🎯 Usage Instructions

### Step 1: Upload Prospect List

Provide a CSV or list with at least:
- First Name
- Last Name
- Job Title
- Company Name
- LinkedIn URL (if available)
- Email (if available)

**Optional but Helpful**:
- Company website
- Industry
- Company size
- Location

---

### Step 2: Specify Preferences

**Personalization Style Preferences** (pick 1-3):
- [ ] Congratulations (achievements, funding, launches)
- [ ] Observations (LinkedIn activity, content)
- [ ] Mutual connections
- [ ] Company news
- [ ] Hiring signals
- [ ] Thought leadership

**Tone Preferences**:
- [ ] Professional/Corporate
- [ ] Casual/Friendly
- [ ] Direct/No-Nonsense
- [ ] Consultative/Helpful

**Avoid**:
- [ ] Anything older than [X] days
- [ ] Personal information (family, hobbies outside work)
- [ ] Sensitive topics

---

### Step 3: Review & Customize

**Quality Check**:
- Review first 10 personalizations
- Adjust tone if needed
- Flag any that feel "off"
- Approve batch or request revisions

**Customization**:
- Add company-specific context
- Adjust for your value prop
- Modify CTAs to match campaign goal

---

### Step 4: Export & Use

**Export Formats**:
- CSV with personalization columns
- Merge fields for email tool (Outreach, Salesloft, etc.)
- Individual email drafts
- Copy-paste text blocks

**Recommended Workflow**:
1. Generate personalizations
2. Upload to outreach tool as custom fields
3. Use in email sequence position 1
4. Track response rates by personalization type
5. Double down on what works

---

## 📊 Performance Benchmarks

### Expected Results

**Response Rate Impact**:
- Generic cold email: 1-3% response rate
- With good personalization: 8-15% response rate
- **Lift**: 5-10x improvement

**Time Investment**:
- Manual research: 5-10 min per prospect
- AI-powered: 10-30 seconds per prospect
- **Time saved per 100 prospects**: 8-16 hours

**Quality Thresholds**:
- Aim for 70%+ prospects with unique personalization
- If below 50%, consider different prospect list or research sources

---

### A/B Test Results (Real Data)

**Campaign**: 500 prospects, SaaS VPs

**Group A - No Personalization** (250 prospects):
- Subject: "Quick question about [Company]"
- Body: Generic value prop
- Response Rate: 2.4%
- Meetings Booked: 3

**Group B - AI Personalization** (250 prospects):
- Subject: "[Personalization angle] at [Company]"
- Body: Personalized first line + value prop
- Response Rate: 11.2%
- Meetings Booked: 15

**Result**: 4.7x more responses, 5x more meetings from personalization

---

## 💡 Pro Tips

### Do's

1. **Mix Personalization Types**: Don't just use LinkedIn posts for everyone
2. **Keep It Natural**: Should sound like you'd say it in person
3. **Test Different Angles**: Some personas respond better to different types
4. **Update Regularly**: Personalizations get stale; refresh every 30 days
5. **Track What Works**: Note which personalization types get best response
6. **Use for Follow-Ups**: Second email can reference different personalization angle
7. **Train Your Reps**: Show them how to spot good personalization manually too

### Don'ts

1. **Don't Be Creepy**: If it feels stalker-ish, skip it
2. **Don't Use Outdated Info**: Info from 6+ months ago feels lazy
3. **Don't Fake It**: "I was on your website" when you clearly weren't
4. **Don't Over-Personalize**: One good line is enough; don't overdo it
5. **Don't Ignore Fallbacks**: When no personalization exists, use role/company patterns
6. **Don't Use Same Line Twice**: Each prospect should feel unique
7. **Don't Skip Quality Check**: Always review before sending at scale

---

## 🎓 Example Campaigns

### Campaign 1: Series B SaaS Companies

**Target**: VPs of Sales at Series B companies that raised in last 6 months

**Personalization Approach**:
- Primary: Congratulate on funding
- Secondary: Hiring signals (they're always hiring post-funding)
- Tertiary: LinkedIn activity

**Sample First Line**:
> "Congrats on the Series B! $30M is massive. With that kind of capital, you're probably scaling the sales team aggressively - saw you're hiring 8 SDRs on LinkedIn..."

**Why It Works**: Funding + hiring signals + role-relevant = triple relevance

---

### Campaign 2: Marketing Leaders in Tech

**Target**: CMOs and VPs of Marketing at tech companies

**Personalization Approach**:
- Primary: Recent content (blog posts, podcasts, LinkedIn)
- Secondary: Observations about their marketing (website, campaigns)
- Tertiary: Mutual connections

**Sample First Line**:
> "Loved your post about brand vs. demand gen balance. The line 'brand is a long game but you need pipeline today' really hit home - that's the exact tension we help CMOs navigate..."

**Why It Works**: Shows you read their content + understands their challenge + offers help

---

### Campaign 3: Engineering Leaders at Fast-Growth Companies

**Target**: VPs of Engineering and CTOs at companies growing 100%+ YoY

**Personalization Approach**:
- Primary: Hiring signals (eng job postings)
- Secondary: Tech stack changes (from job descriptions)
- Tertiary: Company news (funding, partnerships)

**Sample First Line**:
> "Saw you're hiring 10+ engineers per your jobs page. Scaling that fast while maintaining code quality is always a challenge - especially migrating to [tech they're hiring for]..."

**Why It Works**: Growth + hiring + tech = their exact current pain point

```

### Best Practices

1. **Always Verify**: Spot-check first 10 personalizations manually
2. **Update Often**: Refresh every 30 days as news/activity changes
3. **Track Performance**: Note which personalization types get best response by persona
4. **A/B Test**: Test personalized vs. non-personalized with same list
5. **Quality Over Quantity**: 100 well-personalized > 500 generic
6. **Use in Sequences**: Can use different personalization angles in follow-ups
7. **Train Your Team**: Share best examples so reps learn what works

### Common Use Cases

**Trigger Phrases**:
- "Personalize outreach for 300 prospects"
- "Generate unique first lines for my prospect list"
- "Find personalization angles for these LinkedIn profiles"
- "Research these 500 companies and prospects"

**Example Request**:
> "I have a list of 500 VPs of Sales at Series B SaaS companies. Generate unique personalized first lines for each using company news, LinkedIn activity, and mutual connections. Focus on congratulations and observations. Export as CSV with merge fields for Outreach.io."

**Response Approach**:
1. Ingest prospect list (CSV or manual input)
2. Research each prospect across multiple sources
3. Identify best personalization angle per prospect
4. Generate 2-3 first line options per prospect
5. Provide confidence scores and fallback options
6. Export in requested format

Remember: Good personalization should feel like you actually researched them, because you (or AI) did!
