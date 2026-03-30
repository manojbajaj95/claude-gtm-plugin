# The Conversion Audit Sprint

Pinpoint your worst-performing funnel page and immediately brief an A/B test — one focused on gain, one on loss aversion — ready for deployment.

## Workflow

### Step 1 — Find the drop-off page

```
Pull the last 30 days of funnel data for [Insert Campaign].
Identify the page with the highest drop-off rate.
Return: page URL, drop-off percentage, and the previous step in the funnel.
```

### Step 2 — Audit the landing page

```
Perform a landing page optimization audit of [page from Step 1].
Focus on:
  - Above the fold content: headline, subheadline, hero image/video
  - Primary CTA: copy, placement, visual contrast
  - Trust signals present or missing
Return: top 3 friction points with a severity rating (High / Medium / Low).
```

### Step 3 — Brief the A/B test

```
Create an A/B test brief for the page audited in Step 2.
Hypothesis: fixing the highest-severity friction point will lift conversion.
Deliver:
  - Variation A headline: focused on user gain (what they get)
  - Variation B headline: focused on loss aversion (what they risk missing)
  - Success metric (primary KPI)
  - Minimum sample size recommendation
  - Suggested test duration
Format as a ready-to-hand-off brief.
```

## Output

- `content/briefs/drafts/YYYY-MM-DD_ab-test-<campaign-slug>.md` — A/B test brief

