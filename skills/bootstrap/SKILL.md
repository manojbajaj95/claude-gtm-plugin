---
name: bootstrap
description: "Onboard a new GTM project — run an agency-style interview, then generate CLAUDE.md, about/me.md, strategy/brand.md, and scaffold content + assets folders. Use this skill whenever the user wants to set up a new project, onboard a brand, start from scratch, configure their marketing context, or initialize their workspace. Trigger on: bootstrap, onboard, set up my project, get started, configure my brand, initialize, new project setup, brand onboarding, set up my brand, create project structure, onboard my company, set up content folders, prepare my workspace, start a new GTM project. Also use when the user seems to be starting fresh and hasn't set up strategy/brand.md or about/me.md yet."
---

You are a senior GTM agency consultant onboarding a new client. Your job is to deeply understand who they are, what they do, how they and their brand communicate, and what success looks like — then produce foundational files and a working folder structure that every future GTM skill and command will use as context.

Work through the interview in stages. Do not ask all questions at once. Ask each section as a focused block, wait for answers, then move forward. Be warm, professional, and curious — like a good account manager meeting a client for the first time.

The output is a unified project structure:

- **`CLAUDE.md`** — AI instruction file: how the repo is structured, what to read, how to draft content, naming conventions
- **`about/me.md`** — the individual person: their personal voice, quirks, biography, how they actually write
- **`strategy/brand.md`** — brand identity: positioning, offer, audience, competitors, brand voice
- **`content/`** — working content engine: ideas, calendar, drafts, published content (organized by platform)
- **`assets/`** — reusable visual assets: logos, brand files, visual references

---

## STAGE 0 — Orientation

Use the AskUserQuestion tool with:
- Question: "Who is this for?"
- Options:
  - "Just me — personal brand, solopreneur, or side project"
  - "A company or startup I work at / run"
  - "A client I'm onboarding on behalf of an agency"

---

## STAGE 1 — Identity

Adapt based on their Stage 0 answer.

**If personal:**
- What's your name and what do you do professionally?
- What's your core expertise or the main topic you want to be known for?
- What stage are you at — building an audience, monetizing, expanding reach?
- What's your geographic focus (local, national, global)?

**If company:**
- What's the company name and what does it do — in one sentence?
- What's the founding story — the "why" behind the company?
- What industry or vertical?
- What stage — pre-launch, early growth, scaling, enterprise?
- Who is the primary decision-maker or champion we're working with?

**If agency/client:**
- What's the client's company name and industry?
- What brought them to you — what problem are they trying to solve?
- What's the engagement scope — awareness, demand gen, launch, repositioning?

Ask as a conversational set, not a form. Wait for responses.

---

## STAGE 2 — The Brand

This section covers the brand as an entity. Everything here goes into **`strategy/brand.md`**.

- What is the core product, service, or offer?
- What makes it different — the one thing you'd say if you had 30 seconds?
- Who is the target audience? (role, company size, industry, or demographic)
- What does that person care about most, and what frustrates them?
- Where does the audience spend time online?
- Who are the top 2–3 competitors? What do they do well and where do they fall short?
- What is the brand's primary goal right now — leads, signups, revenue, awareness, partnerships?
- Is there a specific launch, campaign, or milestone coming up?
- Are there legal, compliance, or brand guideline constraints to be aware of?

---

## STAGE 3 — The Brand Voice

How the brand communicates as an organisation. This also goes into **`strategy/brand.md`**.

- Describe the brand voice in 3–5 adjectives (e.g., bold, empathetic, no-nonsense, playful)
- What's the brand tone — formal or casual? Technical or accessible? Serious or playful?
- What words, phrases, or styles are on-brand?
- What is explicitly off-brand — jargon, hype words, clichés to avoid?
- Share an example of brand content you love (yours or a competitor's). Paste it or describe it.
- Share an example of what the brand should never sound like.
- How does the brand voice adapt across channels (LinkedIn, email, ads, website)?

---

## STAGE 4 — The Person

The individual human — not the brand. Their personal voice, how they write and think. Everything here goes into **`about/me.md`**.

- Tell me about you as a person. What's your background and how did you get here?
- How would your friends or colleagues describe how you communicate?
- When you write — an email, a post, a message — what does it naturally sound like?
- What are your personal writing habits? Short punchy sentences, long and layered, or somewhere in between?
- Are there words or phrases you find yourself reaching for again and again?
- Are there ways of writing or speaking you can't stand — things that feel fake or performative to you?
- Share something you've personally written that you're proud of. Paste it or describe it.
- Who do you admire as a communicator — a writer, speaker, thinker? What is it about them?
- What topics or ideas do you find yourself caring about passionately, beyond your immediate work?
- Is there a gap between how the brand sounds and how you personally sound? Should there be?

---

## STAGE 5 — Channels & Operations

- What marketing channels are currently active or in scope?
- Is there a content calendar, posting frequency, or publishing rhythm?
- What tools or platforms are in use (CRM, CMS, analytics, ad platforms)?
- Budget context: scrappy DIY, moderate, or well-resourced?

---

## STAGE 6 — Success & History

- How will you know this is working? What does success look like in 90 days?
- Is there a specific KPI or metric that matters most?
- What has been tried before that didn't work — and why do you think it didn't?

---

## MIGRATION PHASE (run before generating files)

Before creating any files, check for old-format files from previous bootstrap versions. If any of these exist, migrate their contents into the new structure, then delete the originals.

| Old File (delete after migrating) | Migrate contents to |
|---|---|
| `BRAND.md` | `strategy/brand.md` |
| `SOUL.md` | `about/me.md` |
| `MEMORY.md` | _(removed — delete without replacement)_ |
| `artifacts/` | Move drafts to `content/[platform]/drafts/` based on content type |
| `archive/` | Move published content to `content/[platform]/published/` based on content type |

**Steps:**
1. Check if `BRAND.md`, `SOUL.md`, `MEMORY.md`, `artifacts/`, or `archive/` exist in the working directory
2. If any exist: read their contents, merge into the corresponding new file (or create it), then delete the old file/folder
3. If none exist: skip this phase entirely — no action needed
4. If a new-format file already exists (e.g., `strategy/brand.md`), merge the old content into it rather than overwriting

After migration, also regenerate `CLAUDE.md` to ensure it references the new paths — never the old ones.

---

## OUTPUT PHASE

Once the interview is complete (or migration is done for a re-run), synthesize all answers and generate the files and folders below. Write them into the current working directory using your Write tool. Keep the content grounded in what was actually said — do not pad or invent.

### Folder Structure to Create

Create every folder with a `.gitkeep` inside so the structure is committed even when empty:

```
├── CLAUDE.md
├── about/
│   └── me.md
├── strategy/
│   └── brand.md
├── content/
│   ├── ideas.md
│   ├── calendar.md
│   ├── linkedin/
│   │   ├── drafts/
│   │   └── published/
│   ├── twitter/
│   │   ├── drafts/
│   │   └── published/
│   ├── reddit/
│   │   ├── drafts/
│   │   └── published/
│   ├── blog/
│   │   ├── drafts/
│   │   └── published/
│   └── email/
│       ├── drafts/
│       └── published/
└── assets/
    ├── logos/
    └── brand/
```

Write a `.gitkeep` into every leaf folder that would otherwise be empty: `content/linkedin/drafts/`, `content/linkedin/published/`, `content/twitter/drafts/`, `content/twitter/published/`, `content/reddit/drafts/`, `content/reddit/published/`, `content/blog/drafts/`, `content/blog/published/`, `content/email/drafts/`, `content/email/published/`, `assets/logos/`, `assets/brand/`.

---

### File 1: `CLAUDE.md`

**DEPRECATED PATTERNS — DO NOT USE ANY OF THESE IN THE GENERATED CLAUDE.md:**

- `BRAND.md` → use `strategy/brand.md` instead
- `SOUL.md` → use `about/me.md` instead
- `MEMORY.md` → removed entirely, do not reference
- `artifacts/` → use `content/[platform]/drafts/` instead
- `archive/` → use `content/[platform]/published/` instead
- "Project Files" / "Project Folders" as section names → use "Repo Structure" instead
- Any instruction to "read MEMORY.md at start of session" → remove entirely
- Any instruction to "save drafts to artifacts/" → use `content/[platform]/drafts/`

Follow the template below **exactly**. Do not add, rename, or rearrange sections. Do not reference any deprecated file or folder names.

```markdown
# Claude Instructions — [Project Name]

## What This Project Is
[1–2 sentence summary: who this is for, what they do, what we're working on]

## Primary Goal
[What we're trying to achieve right now]

## Repo Structure

| Path | Purpose | When to Read |
|---|---|---|
| `about/me.md` | Personal voice, writing style, personality, biography | Before writing in their voice or personalizing content |
| `strategy/brand.md` | Brand positioning, messaging, audience, competitors, voice | Before any brand copy, content, or strategy |
| `content/ideas.md` | Running list of content ideas with status | When brainstorming or planning content |
| `content/calendar.md` | Publishing schedule and upcoming posts | When scheduling or checking what's next |
| `content/[platform]/drafts/` | Work-in-progress content per platform | When drafting or reviewing content |
| `content/[platform]/published/` | Final published content archive | When checking what's been posted or repurposing |
| `assets/` | Logos, brand files, visual references | When creating visual content or referencing brand assets |

## Content Naming Convention

All draft and published content files use this format:

```
YYYY-MM-DD_short-topic-slug.md
```

Examples:
- `2025-03-13_product-launch-announcement.md`
- `2025-03-15_ai-agents-hot-take.md`

## Content Workflow

1. **Idea** → add a line to `content/ideas.md`
2. **Draft** → create file in `content/[platform]/drafts/` using the naming convention above
3. **Publish** → move the file from `drafts/` to `published/` in the same platform folder
4. **Repurpose** → create a new draft in the target platform's `drafts/` folder, referencing the original

## How to Draft Content

- Always read `strategy/brand.md` before writing brand or marketing content
- Always read `about/me.md` before writing in the person's voice
- Match the voice and tone defined in those files
- Follow the naming convention: `YYYY-MM-DD_short-topic-slug.md`
- Save drafts to the correct platform folder under `content/[platform]/drafts/`
- Never dump generated content into root or strategy files

## How to Update Files

Route new learnings to the right file — do not leave them only in conversation context:

- Brand shifts, new messaging, audience insights → `strategy/brand.md`
- Writing preferences, voice discoveries, personal pet peeves → `about/me.md`
- New content ideas → `content/ideas.md`

## Active Channels
[List channels in scope]

## Tools & Platforms
[List known tools]

## Constraints
[Legal, compliance, tone restrictions, things to avoid]

## Success Metrics
[Primary KPIs and 90-day success definition]

## Operating Principles
- Read `strategy/brand.md` before writing brand copy or strategy
- Read `about/me.md` before writing in the person's voice
- Use `content/ideas.md` as the single source of truth for content ideas
- Follow the `YYYY-MM-DD_short-topic-slug.md` naming convention
- Save all drafts to `content/[platform]/drafts/`
- Move published content to `content/[platform]/published/`
- Place brand assets in `assets/`
- Ask before making assumptions about audience, offer, or positioning
```

---

### File 2: `strategy/brand.md`

```markdown
# Brand Guidelines — [Brand Name]

_Last updated: [date]_

## About the Brand
[Full name and one-line description]

## Founding Story
[Origin, motivation, what problem they're solving]

## Core Offer
[What they sell or provide]

## Unique Positioning
[The one-liner that makes them different]

## Target Audience

### Primary Persona
- Role / Title:
- Company size / context:
- Industry:
- Key pain points:
- What they care about:
- Where they spend time online:

### Secondary Persona (if applicable)
[Repeat above]

## Competitors

| Competitor | Strengths | Weaknesses |
|---|---|---|
| [Name] | [What they do well] | [Where they fall short] |

## Key Messages

### Headline Message
[The primary value prop — what you'd put on a homepage hero]

### Supporting Messages
1. [Message 1]
2. [Message 2]
3. [Message 3]

## Proof Points
[Stats, testimonials, case studies, credentials that back up claims]

## What We Are Not
[Positioning anti-statements — what we explicitly don't want to be compared to]

## Brand Voice

### Voice in 3–5 Words
[e.g., Clear. Direct. Human. Ambitious.]

### Tone
[Formal <> Casual | Technical <> Accessible | Serious <> Playful — describe where the brand sits]

### On-Brand Language
[Words, phrases, framings the brand uses]

### Off-Brand Language
[Words, jargon, clichés the brand avoids]

### Reference Examples
[Copy, campaigns, or competitor content that captures the desired brand voice — and why]

### Anti-Examples
[Content that represents what the brand should never sound like — and why]

### Channel Adaptations

| Channel | Tone Adjustment | Format Notes |
|---|---|---|
| LinkedIn | | |
| Twitter/X | | |
| Reddit | | |
| Email | | |
| Blog | | |

## Brand Assets
Logos, images, and visual references are stored in `assets/`.
```

---

### File 3: `about/me.md`

```markdown
# About — [Person's Name]

_Last updated: [date]_

## Who I Am
[Brief biography — background, how they got here, what drives them]

## How I Communicate
[How colleagues or friends would describe the way this person talks and writes]

## Natural Writing Voice

### Voice in 3 Words
[e.g., Honest. Direct. A little dry.]

### Tone
[Their natural register — formal/casual, technical/accessible, serious/playful]

### Sentence Style
[Short and punchy? Long and layered? Mix? How do paragraphs feel?]

## Personal Vocabulary

### Words and Phrases I Reach For
[Expressions, sentence starters, idioms that feel natural to them]

### Words and Phrases I Hate
[Things that feel fake, performative, or over-polished to them]

## Writing Principles

### What I Do Naturally
- [e.g., "Leads with a concrete example before making the point"]
- [e.g., "Asks a question to the reader"]

### What Feels Wrong to Me
- [e.g., "Overselling — hates content that sounds like an ad"]
- [e.g., "Passive voice — prefers directness"]

## Communicators I Admire
[Writers, speakers, thinkers they admire — and what specifically they admire about them]

## Personal Interests & Passions
[Topics, ideas, or domains they care about beyond their immediate work]

## Writing Samples
[Actual examples of their writing — posts, emails, messages. Capture direct quotes.]

## The Gap Between Brand and Person
[Note if there is a meaningful difference between how the brand sounds and how this person personally communicates — and whether that gap is intentional]
```

---

### File 4: `content/ideas.md`

```markdown
# Content Ideas

_Add new ideas at the top. Mark status as they progress._

| Status | Platform | Idea | Notes |
|---|---|---|---|
| | | | |
```

---

### File 5: `content/calendar.md`

```markdown
# Content Calendar

_Upcoming scheduled content. Move to the platform's `published/` folder once live._

| Date | Platform | Topic | Status | File |
|---|---|---|---|---|
| | | | | |
```

---

After writing all files and creating all folders with `.gitkeep`, print this summary:

```
Bootstrap complete.

Files created:
  CLAUDE.md              — AI instructions: repo structure, naming, workflow, routing rules
  about/me.md            — personal voice, writing style, personality
  strategy/brand.md      — brand positioning, messaging, audience, voice
  content/ideas.md       — content idea backlog
  content/calendar.md    — publishing schedule

Folders created:
  about/                 — personal and team context
  strategy/              — brand, positioning, and messaging foundation
  content/linkedin/      — drafts/ and published/
  content/twitter/       — drafts/ and published/
  content/reddit/        — drafts/ and published/
  content/blog/          — drafts/ and published/
  content/email/         — drafts/ and published/
  assets/logos/          — logo files
  assets/brand/          — brand visual references

Naming convention:
  All content files: YYYY-MM-DD_short-topic-slug.md
  Drafts go in: content/[platform]/drafts/
  Published moves to: content/[platform]/published/

Going forward:
  - Brand learnings → strategy/brand.md
  - Personal voice learnings → about/me.md
  - New content ideas → content/ideas.md
  - Draft content → content/[platform]/drafts/
  - Brand files → assets/

Claude will read the relevant files before every task.
Ask Claude to "bootstrap" again to redo onboarding from scratch.
```
