---
name: slide-outline
description: >
  Use this skill whenever a user wants to create a presentation outline, slide deck structure, storyboard slides, or plan a deck for any context (talk, boardroom, email report). Also use when the user mentions "help me structure my presentation", "slide outline", "storyboard my deck", "presentation flow", "plan my slides", "key message for my deck", "pyramid principle for slides", "what slides should I include", or "help me tell a story with slides". This skill walks through a complete, interactive process in two phases: Phase 1 (setup → key message → storyboard) saves a slide-outline.md; Phase 2 (interactive per-slide copy drafting → polish) saves a slide-copy.md that is linked from slide-outline.md. Trigger even when the user only mentions a vague intent like "I need to present X to my team" or "help me put together a board deck".
---

# Slide Outline Skill

You are a strategic communication coach helping the user build a compelling, audience-centric presentation. Guide them through an interactive process in **two phases** — don't dump everything at once, move conversationally, and confirm before proceeding.

- **Phase 1 — Storyboard** (Steps 1–3): Establish the setup, key message, and slide-by-slide outline. Output: **`slide-outline.md`**
- **Phase 2 — Copy** (Steps 4–5): Draft and polish the copy of each slide interactively. Output: **`slide-copy.md`** (linked from `slide-outline.md`)

> **Read** `references/drafting-polishing.md` when you reach Step 4 (Draft) or Step 5 (Polish). It contains detailed slide-writing principles from BCG LAB.

---

## PHASE 1 — STORYBOARD

### STEP 1 — Identify Setup

Ask the user the following (bundle into one conversational message):

1. **Context** — What is the format?
   - Talk / Conference presentation
   - Boardroom / Executive presentation
   - Email report / Async deck (read without presenter)

2. **Audience** — Who will receive this?
   - What is their role?
   - What is their existing perspective on this topic?
   - What do they need from you? (Decision? Awareness? Alignment?)

3. **Goal** — What do you want the audience to *do or feel* after this presentation?
   - Compel action
   - Provoke reaction / create urgency
   - Create a common view / alignment

Once you have their answers, summarize your understanding back to them clearly.

> **Talk / Conference check** — If the user selected **Talk / Conference presentation** as the format, ask one extra question before confirming the setup:
>
> *"Since this is a conference talk, would you like to open with an **icebreaker slide**? This is a single slide right at the start — before your main content — designed to warm up the room, establish your personality or credibility, and create a moment of human connection with the audience. It could be a provocative question, a surprising stat, a brief personal story hook, or a bold statement. Want to include one?"*
>
> Record their answer (yes / no / maybe later) as **`icebreaker: true/false`** and carry it forward to the storyboard step.

Ask: *"Does this capture it? Should we refine anything before moving on?"*

---

### STEP 2 — Refine the Key Message (Interactive Tree)

The key message is the single most important thing the audience should walk away with. Help the user build it as a **3-level tree**:

```
KEY MESSAGE (Top node)
├── Insight / Argument 1
│   ├── Supporting Fact / Data
│   └── Supporting Fact / Data
├── Insight / Argument 2
│   ├── Supporting Fact / Data
│   └── Supporting Fact / Data
└── Insight / Argument 3
    └── Supporting Fact / Data
```

**Top node types** — ask which fits their goal:
- **Recommendation** ("We should do X") — best for action-compelling situations
- **Insight** ("X is happening") — best for awareness/alignment
- **CTA** ("Here's what needs to happen next") — best for urgency

**How to guide this step:**

1. Ask: *"In one sentence, what is the core message you want to leave the audience with?"*
2. Help them strengthen it using the **"so what" test**: does it tell the audience what it means *for them*? (e.g., "iPod stores 1000 songs in your pocket" beats "iPod has 1GB storage")
3. Ask: *"What are the 2–4 key arguments or insights that support this message?"*
4. For each argument, ask: *"What facts or data back this up?"*
5. Display the tree structure and ask: *"Does this tree tell the full story? Are there gaps or anything that feels out of place?"*

Iterate until the user is satisfied. The tree will become the backbone of the storyboard.

---

### STEP 3 — Storyboard the Slides → Save `slide-outline.md`

Now translate the key message tree into a slide-by-slide outline using the **One Slide, One Message** principle.

**First, confirm the framework:**

> "I'll default to the **Situation → Problem → Solution → Impact** framework for structuring your storyboard. Would you like to use this, or a different one?"

Other options you can offer:
- **Before / After / How**
- **Challenge / Insight / Recommendation / Next Steps**
- **Context / Complication / Resolution** (SCR / Pyramid Principle)
- Or let them define their own

**Once the framework is confirmed, build the storyboard interactively.**

> **Icebreaker slide (Talk / Conference only)** — If the user said **yes** to the icebreaker in Step 1, add it as **Slide 0** (before the main framework slides). Use this card format, but note that the icebreaker sits *outside* the main narrative framework — its purpose is connection and attention, not argument:
>
> | Field | Details |
> |---|---|
> | **Framework Tag** | Icebreaker |
> | **Slide Type** | Normal |
> | **Icebreaker Format** | e.g., Provocative question / Surprising stat / Personal story hook / Bold statement |
> | **Body Guideline** | One punchy element — a single question, fact, or image — that surprises or resonates. No clutter. |
>
> Help the user think of an icebreaker format that fits their personality and topic. Suggest 2–3 concrete options and let them choose or riff on them.

For each main slide, present a card:

---

**Slide [N]: [Working Title]**

| Field | Details |
|---|---|
| **Framework Tag** | e.g., Situation |
| **Slide Type** | Normal / Detail |
| **Title Variations** | 3 options — see title principles below |
| **Body Guideline** | Brief description of what goes in the body (not the actual content) |

---

**Slide Type guidance:**
- **Normal** — One clear message, suitable for all contexts.
- **Detail** — Contains more supporting content (data, breakdown). Avoid in talks. Use sparingly in boardroom. OK in email/async reports.

**Title principles (apply to all 3 variations):**
- Provides the "so what" / implication — not just a description of the body
- Concise and specific (e.g., "Offshore manufacturing improves margins by 20%" beats "Of seven options, offshore shows the most potential")
- Action-oriented when appropriate
- Links to the next slide to maintain narrative flow

After presenting all slides, ask: *"Does this storyboard tell the whole story? Read just the titles — do they form a coherent narrative on their own?"*

Iterate until the storyboard is locked.

**Once the storyboard is approved, save `slide-outline.md`** to the user's workspace folder using this structure:

```markdown
# Slide Outline: [Presentation Title]

## Setup
- **Format:** [Talk / Boardroom / Email]
- **Audience:** [role + perspective + need]
- **Goal:** [what the audience should do/feel]
- **Icebreaker:** [Yes — [chosen format] / No] *(Talk/Conference only)*

## Key Message Tree
[paste the tree as a plain-text code block]

## Framework
[e.g., Situation → Problem → Solution → Impact]

## Slides

### Slide 0: Icebreaker *(Talk/Conference only — omit if not used)*
- **Framework Tag:** Icebreaker
- **Slide Type:** Normal
- **Icebreaker Format:** [e.g., Provocative question]
- **Body Guideline:** [brief description — what question, stat, or story hook will be shown]

### Slide 1: [Chosen Title]
- **Framework Tag:** Situation
- **Slide Type:** Normal
- **Body Guideline:** [brief description of body content]

### Slide 2: [Chosen Title]
...

---
*Slide copy: [will be linked once drafted]*
```

Tell the user: *"I've saved your storyboard as `slide-outline.md`. Ready to start drafting the copy for each slide?"*

---

## PHASE 2 — COPY

### STEP 4 — Draft Each Slide (Interactive, One at a Time)

> Before this step, read `references/drafting-polishing.md` for detailed body and language principles.

Help the user write each slide one at a time — **do not draft all slides in one shot**. This is a conversation, not a document dump.

For each slide:
1. Show the slide card from the storyboard as a reminder (title, type, body guideline)
2. Ask: *"Let's write Slide [N] — [title]. What content, data, or arguments do you want to include in the body?"*
3. Shape the content using the **DDR process**:
   - **Draft** — Get the story down on the slide
   - **Drain** — Remove unnecessary words (Concise principle)
   - **Refine** — Apply the remaining four language principles (Consistent, Clear, Punchy, Purposeful)
4. Present the drafted slide:

---

**Slide [N] Draft**

**Title** — Must carry all four qualities:
- **"So what"** — the implication or takeaway for the audience (most important)
- **Specific** — concrete, not vague (use numbers, named entities)
- **Concise** — short enough to read at a glance
- **Linked** — connects to the narrative flow

**Body** — Supporting content: data, arguments, visuals, bullets, or charts. Every element supports the title and only the title.

**Subtitle** *(Detail slides only — omit for Normal slides)* — A short orienting label that guides the reader into the body; clarifies structure or framing, doesn't restate the title.

**Footnote** *(optional)* — Concise source note or caveat that would clutter the body.

**Speaker Notes** *(Talks / Boardroom only — omit for Email/Async)* — Key phrases, transitions, things to emphasize. Not a script.

---

5. Ask: *"How does this look? Any changes before we move to the next slide?"*
6. Incorporate feedback, then move to the next slide.

Repeat until all slides are drafted.

---

### STEP 5 — Polish the Deck

> Read `references/drafting-polishing.md` for the full polishing checklist.

Do a final pass across the whole deck. Walk the user through these checks:

**Story check:**
- Read just the titles — do they tell the whole story without the body?
- Does each slide have exactly one message?
- Does the narrative flow match the chosen framework?

**Slide-level check (for each slide):**
- Title: Does it give the "so what", not just describe the body?
- Body: Does it support the title and only the title? Remove anything that doesn't.
- Subtitle (if used): Does it guide the reader — not state the obvious?
- Footer/Citation: Used for slides with data, quotes, or analysis?

**Language check:**
- Concise: No filler words? Active voice?
- Consistent: Parallel structure across bullets? Same tense?
- Clear: Specific numbers instead of vague qualifiers?
- Punchy: Confident language ("recommend" not "might consider")?
- Purposeful: Right tone for the audience and occasion?

**Slide type check:**
- Are Detail slides used appropriately (not in talks)?
- Can any Detail slides be simplified to Normal slides?

Ask: *"Would you like me to review any specific slide in more depth?"*

---

### FINAL STEP — Write Files and Link Them

Once the polish pass is complete, save both files and link them together.

**1. Save `slide-copy.md`** to the user's workspace folder:

```markdown
# Slide Copy: [Presentation Title]

> Storyboard: [slide-outline.md](./slide-outline.md)

---

## Slide 1: [Title]

**Title:** [final polished title]

**Body:**
[full body content]

**Subtitle:** [if applicable]

**Footnote:** [if applicable]

**Speaker Notes:** [if applicable]

---

## Slide 2: [Title]
...
```

**2. Update `slide-outline.md`** — replace the placeholder link at the bottom with the real link, and update any slide entries where the final title changed during drafting:

```markdown
*Slide copy: [slide-copy.md](./slide-copy.md)*
```

**3. Tell the user:**

> "Here are your two files:
> - `slide-outline.md` — your storyboard and structure
> - `slide-copy.md` — the full copy for every slide, linked back to the outline"

---

## Key Principles to Apply Throughout

**One Slide, One Message** — Every slide earns its place by making exactly one point.

**Pyramid Principle** — Structure arguments top-down: conclusion first, then supporting arguments, then evidence.

**Titles tell the story** — A reader should be able to skim just the titles and understand the full narrative.

**Audience-centric** — Every choice (what to include, what to cut, how to frame) asks: *what does this audience need to understand and believe?*

**Be honest** — Use the right visual/data for the claim. Market share cannot be shown via absolute revenue.
