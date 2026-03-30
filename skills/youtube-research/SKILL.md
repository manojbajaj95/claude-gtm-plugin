---
name: youtube-research
description: Research YouTube topics, analyze competitor videos, deconstruct viral content, and query the YouTube Data API. Use when researching a video topic before planning, analyzing video transcripts for viral patterns, searching competitor channels, or fetching video and channel stats via the YouTube Data API v3.
allowed-tools: Bash, WebSearch, WebFetch
---

# YouTube Research

Three modes in one skill:

1. **Topic Research** — competitive landscape, content gaps, strategic insights before planning a video
2. **Video Analysis** — forensic deconstruction of transcripts to extract viral formulas and retention mechanics
3. **API Queries** — direct YouTube Data API v3 access for search, stats, comments, and channel info

---

## When to Use

- Researching a video topic before planning production
- Analyzing a competitor video to extract what makes it work
- Fetching channel stats, video metrics, or comments via the API
- Identifying content gaps and opportunities in a niche

---

## YouTube Data API Setup

### 1. Get an API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/) → APIs & Services → Library
2. Enable **YouTube Data API v3**
3. Create Credentials → API Key

```bash
export YOUTUBE_API_KEY="your-api-key-here"
```

> **Important:** When piping curl output, wrap the command in `bash -c '...'` to preserve env vars:
> ```bash
> bash -c 'curl -s "https://..." -H "..." | jq .'
> ```

### 2. Key API Commands

**Search Videos:**
```bash
bash -c 'curl -s "https://www.googleapis.com/youtube/v3/search?part=snippet&q=YOUR_QUERY&type=video&maxResults=10&order=viewCount&key=${YOUTUBE_API_KEY}"' | jq '.items[] | {videoId: .id.videoId, title: .snippet.title, channel: .snippet.channelTitle}'
```

**Get Video Details (stats, duration):**
```bash
bash -c 'curl -s "https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id=VIDEO_ID&key=${YOUTUBE_API_KEY}"' | jq '.items[0] | {title: .snippet.title, views: .statistics.viewCount, likes: .statistics.likeCount, duration: .contentDetails.duration}'
```

**Get Channel by Handle:**
```bash
bash -c 'curl -s "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&forHandle=@HANDLE&key=${YOUTUBE_API_KEY}"' | jq '.items[0] | {id: .id, title: .snippet.title, subscribers: .statistics.subscriberCount, videos: .statistics.videoCount}'
```

**Get Video Comments:**
```bash
bash -c 'curl -s "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=VIDEO_ID&maxResults=20&order=relevance&key=${YOUTUBE_API_KEY}"' | jq '.items[] | {author: .snippet.topLevelComment.snippet.authorDisplayName, text: .snippet.topLevelComment.snippet.textDisplay, likes: .snippet.topLevelComment.snippet.likeCount}'
```

**Get Trending Videos:**
```bash
bash -c 'curl -s "https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode=US&maxResults=10&key=${YOUTUBE_API_KEY}"' | jq '.items[] | {title: .snippet.title, channel: .snippet.channelTitle, views: .statistics.viewCount}'
```

**Quota:** 10,000 units/day. Search = 100 units. Most others = 1 unit.

See [YouTube Data API docs](https://developers.google.com/youtube/v3) for full reference.

---

## Mode 1: Topic Research

Conduct research before planning a new video. Focus on insights and big levers — not data dumping.

### Workflow

**Step 0: Create research file**

Save all research to: `./youtube/episode/[episode_number]_[topic_short_name]/research.md`

If it already exists, read it and continue from where it left off.

**Step 1: Understand the topic**
- What problem does this video solve?
- Why would someone click on it?
- What makes it relevant now?

**Step 2: Research your own channel**

Use the API to find related videos you've already published. Document:
- Related videos (title, video ID, URL, key metrics)
- What's already been covered and how to differentiate

**Step 3: Competitor research**

Search for 5–8 top videos on the topic. For each:
- Get video details (views, likes, duration)
- Note the title, angle, and what makes it successful
- Synthesize common patterns and approaches

**Step 4: Content gap analysis**

Document:
- **What's saturated** — 3–5 over-covered angles
- **Gaps (Opportunities)** — rated ⭐⭐⭐ high / ⭐⭐ medium / ⭐ low
- **Recommended focus** — specific angle + unique value proposition

Rating criteria:
- ⭐⭐⭐ High: Significant gap, strong demand, clear differentiation
- ⭐⭐ Medium: Moderate gap, some competition, good potential
- ⭐ Low: Minor gap, heavily competed

### Research File Template

```markdown
# [Episode]: [Topic] - Research

## Episode Overview
**Topic**: [Brief description]
**Target Audience**: [Who this is for]
**Goal**: [What viewers will learn/gain]

## YouTube Research
### Your Previous Videos
[Related videos with metrics]

### Top Competing Videos
[5-8 videos: title, channel, views, angle, what works]

### Key Insights
[Patterns and findings synthesized]

## Content Gap Analysis
### What's Already Well-Covered
[List]

### Content Gaps (Opportunities)
[Rated list with ⭐ ratings]

### Recommended Focus
[Specific angle and unique value proposition]

## Production Notes
**Status**: Research Complete
**Created**: [Date]
```

### Subagents for Parallel Research

Use the `Task` tool to run research tasks in parallel for faster results. Each task should have a focused, specific objective (e.g., "Search for top 8 videos on X and get their stats"). Synthesize findings after all tasks complete.

### Pitfalls

- **Data dumping** — Limit to 5–8 competitors, synthesize patterns instead of listing every video
- **Vague gaps** — "Not much content on this" → identify the specific missing angle
- **Long reports** — Focus on insights and big levers

**Next step:** Use `youtube-content` skill to plan the video based on this research.

---

## Mode 2: Video Analysis

Forensic deconstruction of video transcripts to extract viral formulas, hooks, and retention mechanics.

### Getting the Transcript

**Auto-fetch:**
```bash
python skills/youtube-research/scripts/fetch_transcript.py "YOUTUBE_URL_OR_VIDEO_ID"
```

**Manual paste:** YouTube's built-in transcript (click "..." → "Show transcript") or ytscribe.ai.

### Analysis Framework

Approach the transcript like a crime scene — extract everything systematically. See `reference/analysis-framework.md` for the full checklist and templates.

Analyze these 11 dimensions:

1. **Hook Architecture** — Primary hook (first 3–8s), hook type, secondary hooks, fill-in-blank templates
2. **Structural Blueprint** — Content framework (PAS, Story-Lesson-CTA, List-Depth-Summary), beat map, pacing
3. **Retention Mechanics** — Open loops, pattern interrupts, curiosity gaps, payoff points
4. **Emotional Engineering** — Emotional arc, trigger words, identity hooks, Us vs. Them dynamics
5. **Storytelling Elements** — Narrative framework, character positioning, conflict/stakes, specificity
6. **Linguistic Patterns** — Power phrases, sentence rhythm, repetition, conversational triggers
7. **Algorithm Signals** — Watch time optimizers, engagement bait, share/save triggers
8. **CTA Architecture** — Primary CTA, soft CTAs, timing, value exchange
9. **Viral Coefficient** — Shareability score (1–10), comment bait density, crossover potential
10. **Reusable Templates** — Fill-in-blank opening hooks (3 variations), section templates, transition library
11. **Implementation Playbook** — Top 10 steal-this elements, niche adaptation, A/B test suggestions

### Before Analysis, Collect Context

- Your niche/topic
- Your content style (casual, educational, hype, etc.)
- Target platform and video length goal

### Output Format

Structure output with all 11 sections. End with a **Quick Reference Cheatsheet** — one-page summary of all extracted patterns for rapid implementation.

---

## Tools

- **YouTube API**: `bash -c 'curl ...'` with `$YOUTUBE_API_KEY`
- **MCP (if available)**: `mcp__plugin_yt-content-strategist_youtube-analytics__search_videos`, `get_video_details`, `get_channel_details`
- **Web**: `WebSearch` and `WebFetch` for industry trends and context
