---
name: events-webinars
description: This skill should be used when the user asks to "create webinar registration", "build event pages", "webinar landing page", "event registration", or mentions webinars, events, or live training registration. Creates high-converting event and webinar registration pages.
---

# Events & Webinar Registration

Write high-converting webinar registration landing pages using successful webinar marketing principles from Mike Filsaime (Webinar Control), Andy Jenkins (Webinar Genesis), Russell Brunson (Perfect Webinar), and Jason Fladlien (One-To-Many).

## Core Objectives

- Maximize registrations and show-up rate
- Build anticipation for transformation delivered
- Clearly articulate reason to register now
- Position host as authority and mentor
- Create momentum to attend live

## Registration Page Structure

### 1. Above-the-Fold Section

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

### 2. What You'll Learn Section

**3-5 Value-Driven Promises:**
- Secrets revealed in webinar
- Jason Fladlien method: ONE core idea, MULTIPLE hooks
- Feature → Outcome framing

**Examples:**
- Secret #1: How to [specific outcome] without [common pain]
- Secret #2: The [counterintuitive approach] that [result]
- Secret #3: Why [common belief] is wrong and what to do instead

### 3. Meet Your Host Section

**Authority Building:**
- Experience and credentials
- Backstory (struggle → discovery → success)
- Media mentions and recognition
- [Presenter Image]

### 4. Why This Webinar Is Different

**Andy Jenkins "Contrarian Hook":**
- Dismantle myths or assumptions
- Bold claims or polarizing truths
- Create tension and intrigue

### 5. Social Proof Section

**Testimonials:**
- Past webinar attendees
- Client success stories
- Transformation moments
- Video or quote-based

### 6. Urgency & Scarcity Layer

**Elements:**
- Countdown timer
- "Seats are limited"
- Bonus for live attendance
- Registration deadline

### 7. Call-to-Action (Repeating)

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

## Copywriting Style

- Conversational and benefit-rich
- Urgency-aware
- Open loops and ellipses for anticipation
- Fladlien's logical close + Filsaime's emotional close
- Break up text every 2-4 lines

## Visual & UX Best Practices

- Vibrant CTA button contrast
- Mobile-first layout
- Thumb-friendly spacing
- Video thumbnail with play overlay
- Countdown visible above-fold

## Optional Enhancements

- Calendar integration (Google/Apple)
- Short teaser video (<90 seconds)
- Workbook/checklist bonus for live attendance
- SMS reminder opt-in
- Replay access promise

## Post-Registration Elements

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

## Slide Deck Output Format

When generating webinar slides (slide deck assets), output using this JSON structure. 

**CRITICAL: You MUST use the advanced slide types (`split_image`, `big_number`, `full_image_overlay`, `grid_features`) to create a World Class visual experience. Do NOT rely only on simple bullets.**

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
1.  **Speaker Notes Required:** Every single slide MUST include a `notes` field with 50-100 words of script for the presenter.
2.  **Visual Variety:** Do not use the same slide type twice in a row if possible. Mix `split_image`, `big_number`, and `full_image_overlay`.
3.  **Imagery:** Provide relevant `imageUrl` or `imagePrompt` for all image slides.
4.  **Brief Text:** Slides are for impact. Put the details in the `notes`.

## Quality Checklist

- Does headline promise specific transformation?
- Are 3 secrets compelling and specific?
- Is host positioned as authority?
- Is urgency real and believable?
- Would you register for this webinar?

## Additional Resources

### Reference Files
- **`references/webinar-formulas.md`** - Proven webinar frameworks
