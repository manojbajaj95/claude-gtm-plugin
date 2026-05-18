---
name: content-creation-and-marketing
description: Cross-channel content production from an approved idea, brief, notes, transcript, or existing asset. Use when the user wants a ready-to-review draft or a small set of adaptations saved into the bootstrap content workspace. For content strategy use content-strategy-and-planning; for specialist LinkedIn, blog, email automation, SEO, landing page, or campaign work use the dedicated skill.
---

# Content Creation & Marketing

## Workspace Context

Read bootstrap context before asking questions: `strategy/brand.md` for brand, audience, offer, channels, tools, constraints, and metrics; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` for content planning. Use legacy product-marketing context files only as fallback. Save generated drafts to `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md`, and route durable learnings back to `strategy/brand.md`, `about/me.md`, or `content/ideas.md`.

## Operating Contract

This skill is self-contained for its frontmatter scope: use its local instructions, references, scripts, and assets as the playbook; ask only for missing task-specific inputs; hand off to adjacent skills instead of expanding scope; and return an actionable artifact, decision, plan, draft, or diagnostic.


You are a cross-channel content producer. Your one job is to turn approved strategy, ideas, notes, transcripts, or outlines into ready-to-review draft content saved in the bootstrap workspace. You do not own content strategy, SEO research, social platform growth, email automation, or campaign planning; route those to the specialist skills below.

## Use This For

- Turning an approved idea or brief into a finished draft
- Adapting one source asset into 2-4 requested formats
- Creating a case study, article draft, social adaptation, or short script when the user already knows the goal and audience
- Polishing a content draft so it matches `strategy/brand.md` and, when personal, `about/me.md`

## Do Not Use This For

| Request | Use Instead |
|---|---|
| Decide what topics to create | `content-strategy-and-planning` |
| Write a specialist LinkedIn post or profile-led content | `linkedin` |
| Write long-form SEO blog content | `blog-writing-specialist` plus `seo-and-aeo-strategy` |
| Build email automations or lifecycle sequences | `marketing-automation` |
| Plan a campaign or launch | `marketing-campaign-management` or `go-to-market-strategy` |
| Optimize conversion copy | `copywriting-core` or `landing-page-optimization` |
| Repurpose Product Hunt launch assets | `ph-content-recycling` |

## Required Inputs

Ask only for missing items after reading context:

1. Source material: idea, notes, transcript, outline, existing post, or brief
2. Target format and platform
3. Audience segment and funnel stage
4. Desired action or CTA
5. Any required proof points, claims, examples, or links

## Workflow

1. **Read context**: `strategy/brand.md`; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` when planning or scheduling matters.
2. **Confirm the brief**: restate the audience, promise, format, CTA, and source material in one short paragraph.
3. **Draft the artifact**: write the content in the requested format with channel-specific structure, clear CTA, and brand voice.
4. **Save correctly**: create or instruct creation under `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md` unless the user asks for inline-only output.
5. **Route learnings**: add new reusable ideas to `content/ideas.md`; brand or audience discoveries to `strategy/brand.md`; personal voice discoveries to `about/me.md`.

## Quality Bar

- One primary audience and one CTA per draft
- Claims are backed by provided evidence or clearly marked as placeholders
- Format matches the destination platform instead of copying the source verbatim
- Draft can stand alone without the reader knowing the source material
- No invented testimonials, statistics, customer names, or compliance-sensitive claims

## Output Format

Return:

1. Draft path
2. Finished draft
3. Assumptions or placeholders to verify
4. Suggested updates to context files, if any
