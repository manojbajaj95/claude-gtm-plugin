---
name: ph-content-recycling
description: Repurpose Product Hunt launch content across channels. Use this skill to maximize the value of your launch assets by adapting them for blog posts, documentation, social media, and more.
---

# Product Hunt Content Recycling

## Workspace Context

Read bootstrap context before asking questions: `strategy/brand.md` for brand, audience, offer, channels, tools, constraints, and metrics; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` for content planning. Use legacy product-marketing context files only as fallback. Save generated drafts to `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md`, and route durable learnings back to `strategy/brand.md`, `about/me.md`, or `content/ideas.md`.

## Operating Contract

This skill is self-contained for its frontmatter scope: use its local instructions, references, scripts, and assets as the playbook; ask only for missing task-specific inputs; hand off to adjacent skills instead of expanding scope; and return an actionable artifact, decision, plan, draft, or diagnostic.



This skill helps you repurpose Product Hunt launch content across multiple channels to extend your launch impact.

## When to Use This Skill

- After your PH launch
- Maximizing content ROI
- Building your content library
- Extending launch visibility
- Creating evergreen materials

## The Content Recycling Framework

### What You Created for PH

```
LAUNCH ASSETS:
├── Tagline
├── Description (short + long)
├── Maker comment
├── Gallery images (4-6)
├── Video demo
├── Thumbnail/GIF
├── Email templates
├── Social posts
└── Supporter materials
```

### Where to Repurpose

```
DESTINATION CHANNELS:
├── Website (landing page, about, features)
├── Blog (launch story, learnings, how-to)
├── Documentation (README, quickstart)
├── Social media (ongoing posts)
├── Email marketing (sequences)
├── Other platforms (directories, communities)
├── Sales materials (decks, one-pagers)
└── PR/Media (press releases, pitches)
```

## Channel-by-Channel Guide

### 1. Website Updates

**Landing Page:**
- Tagline → Headline
- Description → Value proposition section
- Gallery images → Feature screenshots
- Video → Hero or features section
- Maker comment → About section

**Features Page:**
- Gallery images → Feature highlights
- Demo video → Embedded walkthrough
- Description points → Feature list

**About Page:**
- Origin story from maker comment
- Mission/vision from description
- Team info (if mentioned)

**Homepage Badge:**
```html
<!-- Product Hunt Badge -->
<a href="https://www.producthunt.com/posts/your-product">
  <img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=YOUR_ID" />
</a>
```

---

### 2. Blog Content

**Launch Announcement Post:**
```
Title: "Introducing [Product]: [Tagline]"

Contents:
- What we launched (description)
- Why we built it (maker comment story)
- Key features (from gallery)
- Getting started (CTA)
```

**Launch Retrospective:**
```
Title: "What We Learned Launching on Product Hunt"

Contents:
- Our results (numbers)
- What worked
- What didn't
- Advice for others
```

**Feature Deep-Dive (from each gallery image):**
```
Title: "How [Feature] Helps You [Benefit]"

Contents:
- The problem (from description)
- Our solution (from demo)
- How to use it (new content)
- Results/examples
```

---

### 3. Documentation

**README.md:**
```markdown
# [Product Name]

> [Tagline]

[Description - first paragraph]

![Product Screenshot](gallery-image-1.png)

## Features

- [Feature 1 from gallery]
- [Feature 2 from gallery]
- [Feature 3 from gallery]

## Getting Started

[Adapted from demo script]

## Support

[From maker comment closing]

---

🏆 Featured on Product Hunt: [Badge/Link]
```

**Quick Start Guide:**
- Adapted from demo video script
- Screenshots from gallery
- Step-by-step from description

---

### 4. Social Media (Ongoing)

**Thread Formats:**

*Origin Story Thread:*
```
1/ Just launched [Product] on Product Hunt! 🚀

Here's the story of why we built it...

[Maker comment story, broken into tweets]

n/ Try it here: [link]
```

*Lessons Learned Thread:*
```
1/ We launched on Product Hunt and got [X upvotes].

Here are [X] things we learned:

[List of lessons]

n/ Full details: [blog link]
```

*Feature Highlight Posts:*
```
[Gallery image]

[Feature name] makes [benefit] easy.

Here's how:
[Demo or explanation]

Try it: [link]
```

---

### 5. Email Marketing

**Welcome Sequence:**
- Email 1: Welcome (adapted maker comment)
- Email 2: Feature 1 (gallery image 1)
- Email 3: Feature 2 (gallery image 2)
- Email 4: Success story
- Email 5: CTA

**Newsletter:**
- Launch announcement
- Feature highlights
- User stories

---

### 6. Other Directories

**Platforms to List:**
- BetaList
- SaaSHub
- AlternativeTo
- Capterra/G2
- AppSumo (if applicable)
- Indie Hackers
- Hacker News (Show HN)

**Adapted Content:**
Each platform needs slightly different format, but core content stays same:
- Tagline (may need length adjustment)
- Description (platform-specific)
- Screenshots (gallery images)
- Links

---

### 7. Sales Materials

**One-Pager:**
```
[LOGO]

[Tagline]

THE PROBLEM
[From description]

THE SOLUTION
[From description + demo]

KEY FEATURES
[From gallery]

RESULTS
[From launch metrics or testimonials]

GET STARTED
[CTA]
```

**Pitch Deck Slides:**
- Slide 2: Problem (from description)
- Slide 3: Solution (tagline + demo)
- Slide 4-6: Features (gallery images)
- Slide 7: Traction (PH results + users)

---

### 8. PR/Media

**Press Release:**
```
FOR IMMEDIATE RELEASE

[Tagline] — [Company] Launches [Product]

[City, Date] — [First paragraph of description]

[Key features and benefits]

"[Quote from maker comment]" — [Founder Name], [Title]

[Availability and pricing]

About [Company]:
[Brief company description]

Contact:
[Media contact info]
```

## Content Transformation Matrix

| Original Asset | Blog | Social | Email | Docs | PR |
|----------------|------|--------|-------|------|-----|
| Tagline | Title | Hook | Subject | Header | Headline |
| Description | Body | Threads | Body | Overview | Body |
| Gallery | Images | Posts | Images | Screenshots | Attachments |
| Video | Embed | Clip | GIF | Tutorial | Asset |
| Maker Comment | Story | Thread | Intro | About | Quote |

## Recycling Workflow

### Step 1: Inventory

List all assets created for launch:
- [ ] Tagline
- [ ] Short description
- [ ] Long description
- [ ] Maker comment
- [ ] Gallery image 1
- [ ] Gallery image 2
- [ ] Gallery image 3
- [ ] Gallery image 4
- [ ] Video demo
- [ ] Thumbnail
- [ ] Email templates
- [ ] Social templates

### Step 2: Prioritize Channels

Rank by impact:
1. [Channel] - [Why important]
2. [Channel] - [Why important]
3. [Channel] - [Why important]

### Step 3: Adapt

For each priority channel:
- Review format requirements
- Adapt content to fit
- Maintain core message
- Optimize for platform

### Step 4: Schedule

Create content calendar:
| Date | Channel | Content | Asset Used |
|------|---------|---------|------------|
| [Date] | Blog | Launch post | All |
| [Date] | Twitter | Thread | Story |
| [Date] | LinkedIn | Feature post | Gallery 1 |

## Quick Win Templates

### Twitter Thread from Maker Comment
1. Take maker comment
2. Split into 5-7 logical chunks
3. Add hook as tweet 1
4. Add CTA as final tweet

### Blog Post from Description
1. Use tagline as title
2. Expand each sentence of description into paragraph
3. Add gallery images as illustrations
4. Add demo video embed

### Email from Social Posts
1. Combine 3-4 social posts
2. Add personal greeting
3. Add CTA
4. Send!

## Recycling Checklist

### Week 1 After Launch
- [ ] PH badge added to website
- [ ] Landing page updated with launch assets
- [ ] Blog launch post published
- [ ] README updated

### Week 2-4
- [ ] Feature posts scheduled
- [ ] Email sequence created
- [ ] Other directories submitted
- [ ] Sales materials updated

### Ongoing
- [ ] Social posts from old assets
- [ ] Blog posts from features
- [ ] Email content from results

## Output Format

```
CONTENT RECYCLING PLAN: [Product Name]

ASSETS AVAILABLE:
- [List all launch assets]

PRIORITY CHANNELS:
1. [Channel] - [Reason]
2. [Channel] - [Reason]
3. [Channel] - [Reason]

CONTENT CALENDAR:

Week 1:
- [Date]: [Content] → [Channel]
- [Date]: [Content] → [Channel]

Week 2:
- [Date]: [Content] → [Channel]
- [Date]: [Content] → [Channel]

ADAPTATIONS NEEDED:
- [Asset] → [Channel]: [Changes needed]
- [Asset] → [Channel]: [Changes needed]

QUICK WINS:
- [ ] [Easy recycling task]
- [ ] [Easy recycling task]
- [ ] [Easy recycling task]
```
