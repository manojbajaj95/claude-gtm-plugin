# The YouTuber's SEO Loop

Use your own retention data to write better hooks for future videos, then optimize existing titles and descriptions with AEO keywords to improve Suggested Video and search rankings.

## Workflow

### Step 1 — Analyze retention drop-off points

```
Analyze the retention graphs of our last 3 YouTube videos.
For each video identify:
  - The exact timestamp(s) where the sharpest audience drop-off occurs
  - What content was happening at that moment (describe from the transcript or notes)
  - A hypothesis for why viewers left (pacing, topic shift, no payoff signal, etc.)
Return a summary table: video title | drop-off timestamp | content at that moment | hypothesis
```

### Step 2 — Write new hooks that prevent those exits

```
Using the drop-off hypotheses from Step 1, write 3 video hooks for future scripts.
Each hook should:
  - Address the most common exit reason identified (e.g., "no payoff signal early enough")
  - Be 30–45 seconds when read aloud at a natural pace
  - Follow the structure: pattern interrupt → problem acknowledgment → payoff promise
Topic for the hooks: [Insert Upcoming Video Topic]
```

### Step 3 — Rewrite titles and descriptions with AEO keywords

```
Take the titles and descriptions of the same 3 videos from Step 1.
Rewrite each using AEO-optimized keywords:
  - Title: under 60 characters, front-load the primary keyword, human-readable
  - Description: first 2 sentences answer the video's core question directly
    (optimized for AI answer extraction), followed by a chapter list and CTA
  - Tags: 8–10 tags mixing exact-match and related long-tail phrases
Goal: improve ranking in YouTube search and "Suggested Video" placements.
```

## Output

- `content/youtube/drafts/YYYY-MM-DD_hooks-<topic-slug>.md` — 3 new video hooks
- `content/youtube/drafts/YYYY-MM-DD_seo-updates-<date>.md` — revised titles, descriptions, and tags for 3 videos

