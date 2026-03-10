---
name: pitch-deck-creation
description: Create professional investor pitch decks with structured content and visual design. Use when users need help with pitch deck, investor deck, fundraising deck, startup pitch, deck design, slide design, pitch presentation, pitch deck visuals, investor presentation, Series A deck, seed deck, or VC deck. Covers the full workflow: gathering company info, structuring narrative, generating a PowerPoint via script, and applying visual best practices.
---

# Pitch Deck Creation

Generate professional investor-ready pitch decks. This skill covers both the narrative structure (what goes on each slide) and the visual design rules (how it should look), then produces a `.pptx` file via a bundled Python script.

## Deck Structure

Use the **12-slide framework** — total ~6 minutes. Never exceed 20 slides.

| # | Slide | Duration | Key Question to Answer |
|---|-------|----------|------------------------|
| 1 | **Title** | 15s | Who are you? |
| 2 | **Problem** | 45s | Is this a real problem people pay to solve? |
| 3 | **Solution** | 45s | Is this 10x better than the status quo? |
| 4 | **Demo/Product** | 60s | What does it actually look like? |
| 5 | **Market Size** | 30s | Is this big enough to matter? |
| 6 | **Business Model** | 30s | How do you make money? |
| 7 | **Traction** | 45s | Is this actually working? |
| 8 | **Competition** | 30s | Why you, not them? |
| 9 | **Team** | 30s | Can these people execute? |
| 10 | **Financials** | 30s | Revenue projections, unit economics |
| 11 | **The Ask** | 15s | How much, what for, timeline |
| 12 | **Contact** | 10s | Email, next steps |

**Detailed slide guidance:** consult `references/pitch_deck_best_practices.md` for content rules, examples, and common mistakes for each slide type.

## Step-by-Step Workflow

### Step 1: Gather Information

Ask the user conversationally. Probe for specific metrics and data.

**Required:**
- Company name and tagline (one sentence)
- Problem being solved (with data/stats if available)
- Solution and key features

**Recommended (include if available):**
- Market size (TAM/SAM/SOM) and growth rate
- Traction: revenue, users, growth %, milestones
- Business model: pricing, revenue streams, unit economics
- Competition: competitors and your differentiators
- Team: founders and key hires with relevant background
- Financials & Ask: amount, use of funds, runway, milestones

For missing info, offer placeholder slides that can be updated later.

### Step 2: Create pitch_data.json

Format collected information as JSON for the generation script:

```json
{
  "company_name": "Company Name",
  "tagline": "One-line description",
  "problem": [
    "Problem statement with data",
    "Impact/urgency statement"
  ],
  "solution": [
    "How the product solves the problem",
    "Key feature 1 and its benefit",
    "Unique value proposition"
  ],
  "market": [
    "TAM: $X total addressable market",
    "SAM: $X serviceable market",
    "SOM: $X obtainable market"
  ],
  "product": ["Feature 1", "Feature 2", "Tech highlights"],
  "traction": ["Revenue: $X (YY% growth)", "Users: X,XXX active", "Key milestone"],
  "business_model": ["Revenue model", "Pricing: $XX/month", "CAC, LTV, margins"],
  "competition": {
    "our_advantages": ["Advantage 1", "Unfair advantage"],
    "competitors": ["Competitor 1", "Competitor 2"]
  },
  "team": [
    "CEO: Name - relevant experience",
    "CTO: Name - built X at Y"
  ],
  "financials": [
    "Raising: $X seed/Series A",
    "Use of funds: XX% eng, XX% sales",
    "Milestones with this funding"
  ]
}
```

Notes: all fields are optional except `company_name`; `competition` can be an object (two-column layout) or a plain array.

### Step 3: Generate the PowerPoint

```bash
python3 scripts/create_pitch_deck.py pitch_data.json output_filename.pptx
```

Requires `python-pptx`: `pip3 install python-pptx`

The script produces a `.pptx` with consistent formatting, color scheme, and typography — ready for presentation or manual customization.

### Step 4: Review and Iterate

- User updates `pitch_data.json` with new info, re-runs the script
- For design beyond the script, advise manual editing in PowerPoint
- PDF export: File → Save As → PDF (for sharing)
- Presentation timing: ~10–15 minutes for 10–12 slides

## Visual Design Rules

### Typography

| Element | Size (1920×1080) | Rule |
|---------|-----------------|------|
| Slide title | 48–72px | Max 6 words |
| Key stat | 96–144px | One per slide max |
| Body text | 24–32px | Max 6 bullet points |
| Caption/source | 16–20px | Always cite data |
| Font | Sans-serif only | Inter, Helvetica, SF Pro |

### The 1-6-6 Rule

- **1** idea per slide
- **6** words max per bullet
- **6** bullets max per slide

If you need more text, you need more slides.

### Color

| Element | Guideline |
|---------|-----------|
| Background | Dark navy/charcoal OR clean white — pick one, commit |
| Accent | ONE brand color for emphasis |
| Text | White on dark; dark grey (#333) on light |
| Charts | 2–3 colors max; brand color = your company |
| Avoid | Gradients on text, neon, more than 3 colors |

The bundled script defaults: Primary #2962FF (titles), Secondary #646464 (body), white background.

### Layout

| Rule | Why |
|------|-----|
| Consistent margins (80–100px) | Professional, clean |
| Left-align body text | Easier to scan |
| One visual per slide | Focus attention |
| Slide numbers visible | Investors can reference specific slides |
| Logo in corner | Subtle brand reinforcement |

## Chart Type Guide

| Chart | Use For | Never Use For |
|-------|---------|--------------|
| Line chart | Growth over time (traction) | Category comparisons |
| Bar chart | Comparing amounts | Time series |
| Concentric circles | TAM/SAM/SOM | Anything else |
| 2×2 matrix | Competitive positioning | Feature comparison |
| Single big number | Key metric highlight | Multiple metrics |
| Pie chart | **Never** | Anything — hard to read, unprofessional |

For competition slides: use a 2×2 positioning map, not a feature matrix against competitors.

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| 20+ slides | Max 12–15 |
| Wall of text | Apply 1-6-6 rule |
| Feature matrix vs competitors | Use 2×2 positioning map |
| Pie charts | Use bar or single big number |
| No data source citations | Always cite |
| Team slide with 8+ people | Max 4, most relevant only |
| Vanity metrics | Show revenue, active users, retention |
| Missing "The Ask" slide | State amount + use of funds + timeline |
| Inconsistent design | Same colors/fonts/margins throughout |

## Tailoring for Audience

**Seed/early-stage investor deck:** emphasize problem, solution, market size, and team; show early traction; clear funding ask.

**Growth-stage / Series A deck:** lead with traction and revenue metrics; detailed unit economics; strong competitive moat story.

**Sales / BD deck:** de-emphasize fundraising; focus on customer ROI, case studies, and testimonials.

**Product launch deck:** highlight product features and market need; include demo screenshots; emphasize innovation.

## Resources

- `scripts/create_pitch_deck.py` — generates PowerPoint from `pitch_data.json`
- `references/pitch_deck_best_practices.md` — comprehensive guide: slide-by-slide content rules, design best practices, audience tailoring, pre-pitch checklist
