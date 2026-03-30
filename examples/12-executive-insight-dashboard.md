# The Executive Insight Dashboard

Aggregate 30 days of campaign data into a one-page executive summary that leads with revenue impact — not vanity metrics — and names the single biggest growth lever for the month ahead.

## Workflow

### Step 1 — Gather and normalize the data

```
Pull the last 30 days of marketing campaign performance data across all active channels.
For each channel collect:
  - Total spend
  - Cost Per Acquisition (CPA)
  - Revenue attributed (or pipeline value if pre-revenue)
  - Customer Lifetime Value (CLV) of acquired customers where available
  - Conversion rate at each funnel stage
Exclude vanity metrics (impressions, follower counts, raw clicks) from the primary view.
```

### Step 2 — Calculate revenue impact per channel

```
Using the data from Step 1, calculate for each channel:
  - Revenue ROI: (revenue attributed ÷ spend) × 100
  - CPA vs. average CLV ratio: is each channel acquiring customers profitably?
  - Month-over-month trend: improving, flat, or declining?
Rank channels by revenue ROI.
```

### Step 3 — Generate the executive dashboard

```
Generate a 1-page executive dashboard summary in a format suitable for a Monday
leadership review.
Structure:
  - 3-number headline: total spend | total revenue attributed | blended ROI
  - Channel performance table: channel | spend | CPA | revenue | ROI | trend arrow
  - Top insight (1 sentence): what's working and why
  - Bottom insight (1 sentence): what's underperforming and the likely cause
  - #1 Growth Lever for next month: one specific, actionable recommendation
    — name the channel, the change, and the expected impact
Keep the entire summary scannable in under 2 minutes.
```

## Output

- `content/reports/drafts/YYYY-MM-DD_exec-dashboard.md` — executive dashboard ready for leadership review
