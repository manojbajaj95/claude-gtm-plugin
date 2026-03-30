---
name: webinar-content-and-events
description: This skill covers two related use cases: (1) Creating high-converting webinar registration and event landing pages, and (2) Repurposing webinar recordings into multiple content assets including blog posts, social media, email sequences, and sales materials. Use when users need to build webinar pages or convert webinar content into multi-channel marketing materials.
---

# Webinar Content & Events

This skill combines two capabilities:
1. **Webinar Registration Pages** - Creating high-converting event/webinar landing pages
2. **Content Repurposing** - Transforming webinar recordings into multiple content assets

---

## Part 1: Webinar Registration Pages

Write high-converting webinar registration landing pages using successful webinar marketing principles from Mike Filsaime (Webinar Control), Andy Jenkins (Webinar Genesis), Russell Brunson (Perfect Webinar), and Jason Fladlien (One-To-Many).

### Core Objectives

- Maximize registrations and show-up rate
- Build anticipation for transformation delivered
- Clearly articulate reason to register now
- Position host as authority and mentor
- Create momentum to attend live

### Registration Page Structure

#### 1. Above-the-Fold Section

**Headline:**
- Focus on transformation
- Problem solved or secret revealed
- Specific outcome promise

**Subheadline:**
- Preview core benefit of attending
- Why this matters now

**Date/Time Widget:**
- Clear date and time
- Time zone converter
- Calendar reminder option

**Primary CTA:**
- "Reserve My Spot Now"
- "Join the Free Training"
- High-contrast button

**Visual:**
- [Hero Image or Presenter Headshot]

#### 2. What You'll Learn Section

**3-5 Value-Driven Promises:**
- Secrets revealed in webinar
- Jason Fladlien method: ONE core idea, MULTIPLE hooks
- Feature → Outcome framing

**Examples:**
- Secret #1: How to [specific outcome] without [common pain]
- Secret #2: The [counterintuitive approach] that [result]
- Secret #3: Why [common belief] is wrong and what to do instead

#### 3. Meet Your Host Section

**Authority Building:**
- Experience and credentials
- Backstory (struggle → discovery → success)
- Media mentions and recognition
- [Presenter Image]

#### 4. Why This Webinar Is Different

**Andy Jenkins "Contrarian Hook":**
- Dismantle myths or assumptions
- Bold claims or polarizing truths
- Create tension and intrigue

#### 5. Social Proof Section

**Testimonials:**
- Past webinar attendees
- Client success stories
- Transformation moments
- Video or quote-based

#### 6. Urgency & Scarcity Layer

**Elements:**
- Countdown timer
- "Seats are limited"
- Bonus for live attendance
- Registration deadline

#### 7. Call-to-Action (Repeating)

**CTA Placement:**
- Every scroll/section
- Sticky or floating option

**CTA Copy:**
- "Yes, Save My Seat"
- "Unlock My Spot Now"
- "Claim My Free Training"

**Form Fields:**
- First name + email (minimal)
- [Trust Badge]

### Copywriting Style

- Conversational and benefit-rich
- Urgency-aware
- Open loops and ellipses for anticipation
- Fladlien's logical close + Filsaime's emotional close
- Break up text every 2-4 lines

### Visual & UX Best Practices

- Vibrant CTA button contrast
- Mobile-first layout
- Thumb-friendly spacing
- Video thumbnail with play overlay
- Countdown visible above-fold

### Optional Enhancements

- Calendar integration (Google/Apple)
- Short teaser video (<90 seconds)
- Workbook/checklist bonus for live attendance
- SMS reminder opt-in
- Replay access promise

### Post-Registration Elements

**Thank You Page:**
- Confirmation message
- Add to calendar buttons
- What to expect
- Bridge offer (optional)
- Social sharing

**Confirmation Email:**
- Registration confirmed
- Date/time/timezone
- Join link
- What to prepare

**Reminder Sequence:**
- 24 hours before
- 1 hour before
- "Starting now"

### Slide Deck Output Format

When generating webinar slides (slide deck assets), output using this JSON structure.

**CRITICAL: Use the advanced slide types (`split_image`, `big_number`, `full_image_overlay`, `grid_features`) to create a World Class visual experience.**

```json
{
  "slides": [
    {
      "id": "slide-1",
      "type": "full_image_overlay",
      "title": "Webinar Title Here",
      "subtitle": "The Promise or Big Idea",
      "imageUrl": "https://source.unsplash.com/...",
      "notes": "Welcome everyone. Today we are going to cover..."
    },
    {
      "id": "slide-2",
      "type": "split_image",
      "title": "About Your Host",
      "content": [
        "10 years experience in [Industry]",
        "Helped 500+ clients achieve [Result]",
        "Featured in Forbes, Inc, and Entrepreneur"
      ],
      "imageUrl": "https://source.unsplash.com/...",
      "imagePosition": "right",
      "notes": "Let me introduce myself. I started out just like you..."
    },
    {
      "id": "slide-3",
      "type": "big_number",
      "number": "83%",
      "label": "Increase in Revenue",
      "description": "Average result for clients using this method",
      "notes": "Look at this number. This isn't a fluke. This is what happens when..."
    },
    {
      "id": "slide-4",
      "type": "grid_features",
      "title": "What You'll Learn",
      "features": [
        { "title": "Secret #1", "description": "How to [Outcome] without [Pain]", "icon": "🔓" },
        { "title": "Secret #2", "description": "The [Method] for [Result]", "icon": "🚀" },
        { "title": "Secret #3", "description": "Why [Old Way] fails", "icon": "💡" }
      ],
      "notes": "We have three big secrets to cover today. First..."
    },
    {
      "id": "slide-5",
      "type": "value_stack",
      "title": "Everything You're Getting Today",
      "items": [
        { "name": "Main Product", "value": "$997" },
        { "name": "Bonus #1", "value": "$297", "isBonus": true }
      ],
      "totalValue": "$1,294",
      "yourPrice": "$497",
      "notes": "When you join today, you're not just getting the course..."
    }
  ],
  "metadata": {
    "title": "Webinar Presentation Title",
    "theme": "dark",
    "transition": "slide",
    "brandColors": {
      "primary": "#7B61FF",
      "secondary": "#5AC8FA",
      "accent": "#E061FF"
    }
  }
}
```

**Slide Types Available:**
- `full_image_overlay` - **(Preferred for Openers/Breaks)** Text over full-screen background image.
- `split_image` - **(Preferred for Bios/Case Studies)** Text on one side, image on other.
- `big_number` - **(Preferred for Stats)** Massive number focus for data/ROI.
- `grid_features` - **(Preferred for Agendas/Bonuses)** 3-column card grid.
- `value_stack` - Offer pricing presentation.
- `cta` - Call to action slides.
- `quote` - Testimonials with attribution.
- `bullets` - Simple lists (Use sparingly).
- `two_column` - Simple text columns.

**Slide Design Rules:**
1. **Speaker Notes Required:** Every single slide MUST include a `notes` field with 50-100 words of script for the presenter.
2. **Visual Variety:** Do not use the same slide type twice in a row if possible. Mix `split_image`, `big_number`, and `full_image_overlay`.
3. **Imagery:** Provide relevant `imageUrl` or `imagePrompt` for all image slides.
4. **Brief Text:** Slides are for impact. Put the details in the `notes`.

### Registration Page Quality Checklist

- Does headline promise specific transformation?
- Are 3 secrets compelling and specific?
- Is host positioned as authority?
- Is urgency real and believable?
- Would you register for this webinar?

---

## Part 2: Webinar Content Repurposing

Turn one webinar into 20+ pieces of content across multiple channels.

### Core Capabilities

**Input Processing**:
- Accept webinar transcripts, video files, or presentation slides
- Identify key topics, themes, and narrative structure
- Extract timestamps for important moments
- Recognize speaker names, quotes, and expertise areas
- Identify visual aids, demos, and data points

**Content Generation**:

1. **Blog Post Series** (3-5 posts)
   - Main comprehensive post (2000+ words)
   - Deep-dive topic posts
   - FAQ-style posts from Q&A
   - Listicle posts (e.g., "10 Key Takeaways")

2. **Social Media Assets**
   - Twitter/X threads (10-15 tweets)
   - LinkedIn posts (3-5 long-form)
   - Instagram carousel ideas (5-7 slides)
   - TikTok/Reel script ideas (short clips)
   - Quote graphics with speaker attribution

3. **Email Sequence** (5-7 emails)
   - Highlights email
   - Deep-dive topic emails
   - Q&A follow-up
   - Resource roundup
   - CTA-focused conversion email

4. **Sales Enablement**
   - One-pager summary for sales team
   - Key objections handled with timestamps
   - Competitive differentiators mentioned
   - Customer success stories/case studies
   - Demo moments and use cases

5. **Visual Content Ideas**
   - Infographic concepts with data points
   - Slide deck highlights
   - Animated statistic graphics
   - Process diagrams from explanations
   - Before/after comparisons

6. **Additional Assets**
   - Podcast episode audio clips
   - YouTube chapter markers
   - Speaker quotes for testimonials
   - FAQ document
   - Resource list/links mentioned

### Workflow

1. **Content Analysis**
   - Read through transcript/slides
   - Identify 5-7 key themes
   - Extract notable quotes (10-15)
   - Find data points and statistics
   - Note questions from Q&A section
   - Mark timestamps for video clips

2. **Audience Segmentation**
   - Top-of-funnel content (awareness)
   - Middle-of-funnel (consideration)
   - Bottom-of-funnel (decision)
   - Customer success/retention

3. **Content Mapping**
   ```
   Webinar Topic → Content Types → Distribution Channels → Timeline
   ```

4. **Asset Creation Priority**
   - Immediate: Social snippets, blog post outline
   - Week 1: Full blog post, email sequence
   - Week 2: Infographic, additional blog posts
   - Week 3: Sales assets, video clips
   - Ongoing: Evergreen social posts

### Output Format

Produce a repurposing plan covering:

1. **Blog Posts** (3–5): Main post (2,000+ words), supporting topic posts, FAQ post
2. **Social Media**: Twitter/X thread (10–12 tweets), LinkedIn posts (3), Instagram carousel (7 slides)
3. **Email Sequence** (6 emails): Thank you + highlights → topic deep dives → data → customer story → Q&A → urgency
4. **Sales Enablement**: One-pager with key messages, objections handled with timestamps, competitive differentiators
5. **Visual Content**: Infographic concept, quote graphics (5), slide highlight deck
6. **Video Clips** (3–5): Hook, key insight, demo moment, customer story, Q&A highlight — each with timestamps

See [references/repurposing-templates.md](references/repurposing-templates.md) for full fill-in-the-blank templates for each asset type.

### Distribution Calendar

**Week 1:** Twitter thread + thank you email (Day 1) → LinkedIn post 1 + Instagram carousel (Day 2) → Blog post 1 + Email 2 (Day 3) → Email 3 (Day 5) → TikTok clip + Email 4 (Day 7)

**Week 2:** Blog post 2 (Day 8) → Email 5 + Twitter thread 2 (Day 10) → Infographic (Day 12) → Email 6 + LinkedIn post 3 (Day 14)

**Week 3:** Blog post 3 → Quote graphics series → FAQ post → Video clips to YouTube

**Evergreen:** Repurpose top posts monthly, update blog posts quarterly

## Performance Tracking

**Metrics to Monitor**:
- Blog post traffic and engagement
- Social media reach/engagement by platform
- Email open rates and click-through rates
- Video view duration
- Conversion rates (demo requests, downloads)
- Sales asset usage by team

**Optimization Opportunities**:
- A/B test email subject lines
- Try different social post times
- Experiment with blog post formats
- Test various CTAs
- Repurpose best-performing content

---

## Quick Win Assets (Create First)

1. Twitter thread (1 hour)
2. Thank you email (30 min)
3. 3 quote graphics (1 hour)
4. Main blog post outline (30 min)
5. LinkedIn post (30 min)

**Estimated Total Time**: 3.5 hours for immediate assets
**Total Content Pieces from 1 Webinar**: 25+ assets

---

## Best Practices

1. **Timestamp Everything**: Always include timestamps so video editors can find clips
2. **Maintain Context**: Each piece should standalone, not require watching full webinar
3. **Attribute Quotes**: Always credit speakers for authority
4. **Progressive Disclosure**: Start with teasers, lead to deeper content
5. **Cross-Promote**: Link between assets (blog ↔ email ↔ social)
6. **SEO Optimize**: Blog posts should target keywords from webinar topic
7. **Brand Consistency**: Maintain voice and branding across all assets
8. **Update Links**: Ensure all webinar replay links work and track properly

---

## Trigger Phrases

**For Webinar Registration Pages**:
- "Create webinar registration"
- "Build event pages"
- "Webinar landing page"
- "Event registration"
- "Create a webinar"

**For Content Repurposing**:
- "Repurpose this webinar into content"
- "Turn this transcript into blog posts and social media"
- "Create a content plan from this webinar recording"
- "Extract quotes and insights from this webinar"
- "Build an email sequence from this webinar"
- "Convert webinar to blog post"
- "Extract key quotes from webinar"
- "Create social media from webinar"

---

## Reference Files

- **`references/webinar-formulas.md`** - Proven webinar frameworks
