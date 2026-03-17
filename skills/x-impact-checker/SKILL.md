---
name: x-impact-checker
description: >
  Analyze and optimize X (Twitter) posts for viral potential and maximum reach using the actual open-source recommendation algorithm.
  Use when user wants to: (1) Check if a post will go viral, (2) Score a tweet for engagement potential, (3) Optimize or rewrite a tweet for algorithmic reach, (4) Understand why a tweet underperformed, (5) Build audience in a specific niche.
  Triggers: "Check if this will go viral", "Make this post buzz", "Will this tweet perform well?", "Optimize my tweet", "How can I make this viral?", "rewrite this tweet", "improve my tweet engagement", "twitter algorithm", "tweet reach", "debug underperforming tweet",
  "バズるかチェックして", "Xでバズる投稿にして", "伸びるかチェックして", "この投稿を伸ばして", "投稿を改善して", "ツイートを最適化して"
license: AGPL-3.0 (referencing Twitter's open-source algorithm)
---

# X Impact Checker

Analyze X posts for viral potential and optimize them using the open-source recommendation algorithm — both a 19-element scoring system and deep algorithm architecture understanding.

## When to Use

- Score a tweet draft before publishing
- Understand why a tweet underperformed
- Rewrite tweets to align with Twitter's ranking mechanisms
- Build topical authority in a specific niche
- Debug inconsistent engagement rates

---

## Scoring System (100 points)

### Tier 1: Core Engagement (60 points)

| Factor | Max | Scoring Guide |
|--------|-----|---------------|
| Reply Potential | 22 | 22: Direct question/debatable claim, 12: Invites response, 4: Statement only |
| Retweet Potential | 16 | 16: Actionable insight/surprising fact, 8: Interesting but niche, 0: No share value |
| Favorite Potential | 12 | 12: Emotionally resonant/personal story, 6: Useful reference, 0: Low appeal |
| Quote Potential | 10 | 10: Strong opinion inviting commentary, 5: Thought-provoking, 0: No quote value |

### Tier 2: Extended Engagement (25 points)

| Factor | Max | Scoring Guide |
|--------|-----|---------------|
| Dwell Time | 6 | 6: Long-form/detailed content, 3: Medium depth, 0: Skimmable |
| Continuous Dwell Time | 4 | 4: Thread/story arc requiring sustained attention, 2: Medium complexity, 0: Quick read |
| Click Potential | 5 | 5: Compelling link with clear CTA, 3: Link with context, 1: Bare URL, 0: No link |
| Photo Expand Potential | 4 | 4: Multiple images/visual storytelling, 2: Single image reference, 0: No visual content |
| Video View Potential | 3 | 3: Long-form video with hook (>5s), 2: Short clip, 0: No video |
| Quoted Click Potential | 3 | 3: Bold claim inviting verification, 2: Interesting claim, 0: Self-contained |

### Tier 3: Relationship Building (15 points)

| Factor | Max | Scoring Guide |
|--------|-----|---------------|
| Profile Click | 5 | 5: Creates author curiosity, 3: Shows expertise, 0: Generic voice |
| Follow Potential | 4 | 4: Demonstrates ongoing value, 2: Shows potential, 0: One-off content |
| Share Potential | 2 | 2: General sharing value, 1: Limited appeal, 0: No value |
| Share via DM | 2 | 2: Personal/relatable "send to friend" content, 1: Somewhat relatable, 0: Generic |
| Share via Copy Link | 2 | 2: Reference/bookmark worthy, 1: Useful but not evergreen, 0: Ephemeral |

### Penalties (subtract from total)

| Risk | Range | Trigger |
|------|-------|---------|
| Not Interested | -5 to -15 | Clickbait, irrelevant content |
| Mute Risk | -5 to -15 | Repetitive, annoying patterns |
| Block Risk | -10 to -25 | Offensive, aggressive tone |
| Report Risk | -15 to -30 | Policy violations, spam signals |

### Grades

| Score | Grade |
|-------|-------|
| 90-100 | S (Exceptional) |
| 75-89 | A (Strong) |
| 60-74 | B (Good) |
| 45-59 | C (Average) |
| 30-44 | D (Below average) |
| 0-29 | F (Low potential) |

---

## Output Format

### Progress Tracking

Use TodoWrite tool to show analysis progress:
1. **Analyzing post content** (in_progress → completed)
2. **Calculating scores across all elements** (in_progress → completed)
3. **Generating top 5 priority improvements** (in_progress → completed)
4. **Creating optimized version** (in_progress → completed)

### Report Structure

1. **Score**: `🎯 XX/100 (Grade: X)`

2. **Breakdown Table**:
```
| Category | Factor | Score | Max | Assessment |
|----------|--------|-------|-----|------------|
| **💬 Core Engagement** | | | 60 | |
| | 💭 Reply Potential | X/22 | 22 | [reason] |
| | 🔄 Retweet Potential | X/16 | 16 | [reason] |
| | ❤️ Favorite Potential | X/12 | 12 | [reason] |
| | 💬 Quote Potential | X/10 | 10 | [reason] |
| **⏱️ Extended Engagement** | | | 25 | |
| | 👀 Dwell Time | X/6 | 6 | [reason] |
| | ⏳ Continuous Dwell Time | X/4 | 4 | [reason] |
| | 🔗 Click Potential | X/5 | 5 | [reason] |
| | 🖼️ Photo Expand | X/4 | 4 | [reason] |
| | 🎥 Video View | X/3 | 3 | [reason] |
| | 🔍 Quoted Click | X/3 | 3 | [reason] |
| **🤝 Relationship Building** | | | 15 | |
| | 👤 Profile Click | X/5 | 5 | [reason] |
| | ➕ Follow Potential | X/4 | 4 | [reason] |
| | 📤 Share Potential | X/2 | 2 | [reason] |
| | 💌 Share via DM | X/2 | 2 | [reason] |
| | 📋 Share via Link | X/2 | 2 | [reason] |
| **⚠️ Negative Signals** | | | | |
| | 😐 Not Interested Risk | -X | 0 to -15 | [reason] |
| | 🔇 Mute Risk | -X | 0 to -15 | [reason] |
| | 🚫 Block Risk | -X | 0 to -25 | [reason] |
| | 🚨 Report Risk | -X | 0 to -30 | [reason] |
| **🏆 TOTAL** | | **XX/100** | | **Grade: X** |
```

3. **📈 Top 5 Priority Improvements**: Specific, actionable suggestions across different categories

4. **✨ Optimized Version**: Rewritten post with improvements applied (in original language)

---

## Algorithm Architecture

Understanding the underlying models helps explain *why* the scoring works.

### Core Ranking Models

**Real-graph** — Predicts interaction likelihood between users
- Determines if your followers will engage with your content
- Strategy: Make content your specific follower segment will engage with

**SimClusters** — Community detection with sparse embeddings
- Identifies communities with similar interests; your tweet resonates within these clusters
- Strategy: Pick ONE clear topic and serve tight communities deeply

**TwHIN** — Knowledge graph embeddings mapping users and content topics
- Helps Twitter understand if your tweet fits your established identity
- Strategy: Stay in your niche or clearly signal topic shifts

**Tweepcred** — User reputation/authority scoring
- Your past engagement history affects current tweet reach
- Strategy: Build through consistent quality, not engagement bait

### Engagement Signals

**Explicit (high weight):** Likes, replies, retweets, quote tweets

**Implicit (also weighted):** Profile visits, link clicks, dwell time, saves/bookmarks

**Negative:** Block/report (heavily penalized), mute/unfollow, quick scroll-past

### Optimization by Algorithm Layer

| Layer | Strategy |
|-------|----------|
| Real-graph | Ask questions; create debate; post when followers are active |
| SimClusters | One clear topic; use community language; provide niche value |
| TwHIN | Lead with domain expertise; stay consistent; build topical authority |
| Tweepcred | Reply to quality accounts; avoid engagement bait; engage deeply |

---

## Detailed Scoring Criteria

### Reply Potential (22 pts)
- Direct questions, debatable claims, opinion invitations
- ❌ "Just shipped a new feature." → ✅ "Should features ship fast but buggy, or slow but stable? We chose speed—was it the right call?"

### Retweet Potential (16 pts)
- Actionable insights, surprising facts, numbered lists, data-driven content
- ❌ "I learned something today." → ✅ "🧵 3 React patterns that cut my bundle size by 30%: 1. Lazy loading hooks 2. Code splitting by route 3. Tree-shaking unused exports"

### Favorite Potential (12 pts)
- Emotional resonance, personal stories, relatable moments, vulnerability
- ❌ "Debugging is hard." → ✅ "Spent 3 hours debugging a production issue. The fix? A missing semicolon I added during 'quick cleanup' at 2am. Never touching working code past midnight again 😅"

### Quote Potential (10 pts)
- Strong opinions, challenges conventional wisdom, clear stances
- ❌ "TypeScript is useful." → ✅ "TypeScript's biggest value isn't catching bugs—it's documentation. The type errors are just a bonus. Fight me."

### Dwell Time (6 pts)
- Long-form content requiring reading time; detailed explanations; technical depth

### Continuous Dwell Time (4 pts)
- Thread indicators (🧵, "1/"), narrative structure, complexity requiring re-reading
- ❌ "Here's how I built X." → ✅ "🧵 How I went from idea to $10k MRR in 30 days (1/8)\n\nDay 1-7: Validation..."

### Profile Click (5 pts)
- Creates author curiosity; demonstrates expertise; credibility signals
- ❌ "I think React is good." → ✅ "After architecting React apps for Airbnb, Netflix, and 50+ startups, here's what I wish I knew on day one:"

### Follow Potential (4 pts)
- Demonstrates ongoing value; establishes content cadence
- ❌ "Here's a React tip." → ✅ "React tip #47: [insight]\n\nI break down advanced React patterns every Monday."

---

## Score Normalization

```
Final Score = Base Score (0-100) + Penalties (-75 to 0)
Normalized Score = max(0, min(100, Final Score))
```

Penalty capping: total penalties > -20 causes gradual dampening; hard cap at -75.

---

## Text Analysis Limitations

This skill performs heuristic text-based analysis, not ML prediction. It cannot detect actual media presence, real engagement metrics, author follower count, or network graph relationships. Best used for **pre-publishing optimization**, not post-hoc analytics.

---

## Language Handling

Detect input language. Respond in same language. Keep optimized version in original language.

**When input is in Japanese**, display Category and Factor names as: `日本語訳（English Original）`

Japanese translations:
- 💬 Core Engagement → コアエンゲージメント
- ⏱️ Extended Engagement → 拡張エンゲージメント
- 🤝 Relationship Building → 関係構築
- ⚠️ Negative Signals → ネガティブシグナル
- 💭 Reply Potential → 返信潜在力
- 🔄 Retweet Potential → リツイート潜在力
- ❤️ Favorite Potential → いいね潜在力
- 💬 Quote Potential → 引用潜在力
- 👀 Dwell Time → 滞在時間
- ⏳ Continuous Dwell Time → 継続滞在時間
- 🔗 Click Potential → クリック潜在力
- 🖼️ Photo Expand → 写真展開潜在力
- 🎥 Video View → 動画視聴潜在力
- 🔍 Quoted Click → 引用クリック潜在力
- 👤 Profile Click → プロフィールクリック
- ➕ Follow Potential → フォロー潜在力
- 📤 Share Potential → 共有潜在力
- 💌 Share via DM → DM経由共有
- 📋 Share via Link → リンクコピー共有
- 😐 Not Interested Risk → 興味なしリスク
- 🔇 Mute Risk → ミュートリスク
- 🚫 Block Risk → ブロックリスク
- 🚨 Report Risk → 報告リスク

## Algorithm Reference

See [references/algorithm-weights.md](references/algorithm-weights.md) for complete weight details from X's open-source algorithm (19-element system).
