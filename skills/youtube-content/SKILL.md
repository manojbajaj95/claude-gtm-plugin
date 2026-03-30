---
name: youtube-content
description: Plan new YouTube videos with optimized titles, thumbnails, and hooks. Use when planning a video, writing or reviewing opening hooks, generating title and thumbnail concepts, or creating a production-ready video plan backed by research.
---

# YouTube Content Planning

Two modes in one skill:

1. **Hook Creation** — Design or review the opening 5–30 seconds for maximum retention
2. **Video Planning** — Orchestrate title, thumbnail, and hook into a complete production-ready plan

---

## When to Use

- Planning a new YouTube video (title, thumbnail, hook, outline)
- Writing or reviewing an opening hook for retention
- Generating multiple title/thumbnail options for a user to choose from
- Creating a complete video plan after research is done

---

## Mode 1: Hook Creation

The opening seconds are the highest-leverage part of any YouTube video. Design them with precision.

### Core Principle

**The opening MUST extend the curiosity from the title/thumbnail — never repeat it.**

The viewer already clicked based on the promise. The opening must add new intrigue and make them MORE interested, not restate what they know.

### Forbidden Patterns (Instant Failure)

These cause immediate abandonment and must never appear before the hook:

**1. Repeating the title**
- ❌ Title: "5 Photography Mistakes" → Opening: "Today I'm showing you 5 photography mistakes"
- Why: The viewer already has this info. Repetition drains attention.

**2. Welcoming the viewer first**
- ❌ "Hi guys, welcome back to the channel! Thanks for being here..."
- Why: Friendly but not engaging. Doesn't build on title/thumbnail momentum.
- Exception: Greetings are fine AFTER the hook (after first 15 seconds).

**3. Starting with unrelated content**
- ❌ Title: "Cat Tricks Tutorial" → Opening: 90-second story about a new car
- Why: Viewer confusion → abandonment → YouTube suppresses the video.

### Proven Hook Patterns

**Pattern A: Preview/Teaser** — Show a brief glimpse of the payoff
> Quick montage of the 5 cat tricks in action → "I need to know how to do that!"

**Pattern B: Intrigue Escalation** — Add surprising context that makes the promise MORE compelling
> "What I'm about to show you took professionals years to discover, but you'll learn it in 60 seconds"

**Pattern C: Problem Amplification** — Immediately validate why the viewer needs this
> "If you're still doing X, you're losing Y every single day"

**Pattern D: Immediate Value Demonstration** — Jump straight into delivering on the promise
> No preamble, just start teaching/showing results

### Timing Requirements

- Hook must land within **5–15 seconds** (optimal: 3–8s)
- After hook: brief intro acceptable (5–10s max)
- Main promised content must begin **within 30 seconds**

### Hook Checklist

Before finalizing any opening hook:

- [ ] Non-Repetition: Does NOT repeat the title
- [ ] Curiosity Extension: Makes viewers MORE curious than the title alone
- [ ] Direct Connection: Immediately related to what title/thumbnail promised
- [ ] No Welcome First: Avoids greetings before the hook
- [ ] Attention Increase: Increases attention, doesn't drain it
- [ ] Hook Timing: Occurs within 5–15 seconds

### Content Type Guidance

**Educational/How-To:** Open with result preview or immediate demonstration. Never "In this tutorial I'm going to teach you..."

**Entertainment/Vlogs:** Open with the most exciting/surprising moment. Start in the middle of the action.

**List Videos:** Tease the most interesting items without naming them. Create urgency: "Wait until you see number 3..."

---

## Mode 2: Video Planning

Generate a complete, production-ready video plan: titles, thumbnail concepts, hook strategies, and a high-level outline.

**MANDATORY prerequisite:** Research must be completed first. Either:
- Research file exists at `./youtube/episode/[episode_number]_[topic_short_name]/research.md`, OR
- Run `youtube-research` skill (Topic Research mode) first

### Planning Workflow

**Step 0: Load research**

Read `./youtube/episode/[episode_number]_[topic_short_name]/research.md`. All planning decisions must be grounded in research findings.

**Step 1: Create plan file**

Create `./youtube/episode/[episode_number]_[topic_short_name]/plan.md`. If it exists, read it and continue from where it left off.

**Step 2: Generate 3 title options**

Invoke `youtube-title` skill if available; otherwise generate manually. For each title include:
- Title text
- Rationale (why it's predicted to perform, how it uses research insights)
- Star rating ⭐ to ⭐⭐⭐ (⭐⭐⭐ = top pick)

**Step 3: Generate thumbnail concepts**

For each title, create 2 thumbnail concepts. Each concept includes:
- Which title it pairs with
- Visual description
- Rationale (CTR prediction, research alignment, title complement)
- Star rating for your top 3 across all concepts

**Step 4: Present options and get user selection**

Present all title + thumbnail combinations. Highlight your top 3 pairings. Ask the user to select one to proceed with. Mark their selection with ✅ User Selection in the plan file.

**Step 5: Generate hook strategies**

For the user's selected title + thumbnail, generate 3 hook options using Hook Creation mode (above). Each includes:
- Hook script (actual wording)
- Hook type/pattern used
- Rationale for why it works with the selected title + thumbnail
- Star rating

Ask user to select. Mark with ✅ User Selection.

**Step 6: High-level content outline**

Structure the video into sections (Hook, Intro, Main Content, Outro). List key points and estimated durations. Keep it strategic — structure and key points only, no detailed scripts. Do not assume what specific content to demonstrate; that's the creator's job.

**Step 7: Finalize with AB testing thumbnails**

Generate 3 actual thumbnail images for AB testing (using `thumbkit` or `youtube-thumbnail` skill if available):
- Thumbnail A: Based on user's selected concept
- Thumbnails B & C: Visual style variations of A

Embed in the plan file:
```markdown
- ![Thumbnail A](/path/to/thumbnail_a.png) — [description]
- ![Thumbnail B](/path/to/thumbnail_b.png) — [description]
- ![Thumbnail C](/path/to/thumbnail_c.png) — [description]
```

### Plan File Template

```markdown
# [Episode]: [Topic] - Video Plan

## Research Summary
[Key insights from research that informed decisions]

## Titles
[3 options with rationale and ⭐ ratings]

## Thumbnails
[2 concepts per title with rationale and ⭐ ratings for top 3]

## Hooks
[3 options for selected title+thumbnail with scripts and ⭐ ratings]

## High-Level Content Outline
[Sections, key points, estimated durations]

## Final Plan
**Title**: [Selected]
**Thumbnails**: [3 AB test images embedded]
**Hook**: [Selected strategy]
**Rationale**: [Why this combination works]
```

### Quality Checklist

- [ ] Research loaded and decisions grounded in findings
- [ ] 3 title options with rationale and ratings
- [ ] 2 thumbnail concepts per title
- [ ] User-selected title + thumbnail marked ✅
- [ ] 3 hook options generated for selected pairing
- [ ] User-selected hook marked ✅
- [ ] High-level outline complete
- [ ] 3 AB-test thumbnails generated and embedded

### Critical Rules

- **Always provide all options** — never pick one and present only that
- **Never generate hooks that repeat the title** — see Hook Creation mode
- **Back every recommendation with research** — cite specific content gaps and competitor insights
- **Verify complementarity** — title, thumbnail, and hook must work together as a system
