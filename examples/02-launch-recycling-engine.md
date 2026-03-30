# The Launch Recycling Engine

Squeeze maximum value from a Product Hunt launch by converting the most-upvoted feature into newsletter content and a PH Community update — fully tracked with UTM links.

## Workflow

### Step 1 — Identify the top feature

```
Review our last Product Hunt launch post. Extract the "Top Features" list and
identify the single most upvoted or most-commented feature.
Return: feature name, its original technical description, and the top 2–3 pieces of
community feedback about it.
```

### Step 2 — Build UTM links

```
URL: [Feature Landing Page URL]
Campaigns to tag:
  - newsletter (medium: email, campaign: ph-recycling)
  - ph-community-update (medium: community, campaign: ph-recycling)
Return both tagged URLs.
```

### Step 3 — Write newsletter segment

```
Feature: [output from Step 1]
Goal: Rewrite the technical description as a "benefit-first" story — lead with the
user outcome, not the mechanism.
Format: 150-word newsletter segment
Include: the UTM-tagged newsletter link from Step 2 as the CTA
Read strategy/brand.md for voice and audience before drafting.
```

### Step 4 — Write PH Community update

```
Source: the newsletter segment from Step 3
Target: Product Hunt Community update section
Adapt tone for PH's maker-community context (first-person, transparent, grateful)
Include: UTM-tagged PH community link from Step 2
Keep it under 200 words.
```

## Output

- `content/email/drafts/YYYY-MM-DD_ph-feature-<slug>.md` — newsletter segment
- `content/ph-community/drafts/YYYY-MM-DD_ph-update-<slug>.md` — PH community post
