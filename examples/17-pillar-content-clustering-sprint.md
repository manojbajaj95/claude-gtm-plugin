# The Pillar Content Clustering Sprint

Map a full topic cluster around a broad subject — one pillar page and five supporting sub-topics with internal linking planned — then draft the pillar article's introduction and all H2 outlines.

## Workflow

### Step 1 — Research and cluster keywords

```
Conduct deep keyword research around [Insert Broad Topic].
Return:
  - 1 central pillar keyword: highest volume, broadest intent, covers the full topic
  - 5 supporting cluster keywords: narrower, longer-tail, each answering a specific
    sub-question a reader of the pillar page would also have
  - For each keyword: estimated monthly search volume, search intent
    (informational / commercial / navigational), and the ideal content format

Cluster rules:
  - No two keywords should target the same search intent
  - Each cluster keyword should naturally link TO the pillar and FROM the pillar
  - Prioritize AEO-friendly phrasing (how people ask AI assistants, not just Google)
```

### Step 2 — Build the content strategy brief

```
Using the keyword cluster from Step 1, develop a content strategy and planning brief.
Include:
  - Pillar page title (H1): keyword-forward, under 65 characters
  - Internal linking map: a table showing which cluster page links to the pillar
    and which section of the pillar links back to each cluster page
  - Publishing order recommendation: which piece to publish first for maximum
    topical authority build-up
  - Content gap note: any cluster sub-topic where we already have existing content
    that should be updated rather than created fresh
```

### Step 3 — Draft the pillar article

```
Write the introduction and full H2 outline for the main pillar piece.
Target length: 2,000 words (this step covers the scaffold, not the full draft).

Deliver:
  Introduction (150–200 words):
    - Hook: open with a stat, provocative question, or specific scenario
    - Problem framing: what the reader is struggling with
    - Promise: what they will know or be able to do by the end
    - Primary keyword included naturally in the first 100 words

  H2 outline (all sections of the 2,000-word piece):
    - 6–8 H2 headings
    - Under each H2: 2–3 bullet points summarizing the key points to cover
    - Note which H2 should contain an internal link to each cluster page
    - Flag one H2 as the AEO target section (structured to be extracted as a
      featured snippet or AI answer)

Read strategy/brand.md for voice and audience before drafting the intro.
```

## Output

- `content/blog/drafts/YYYY-MM-DD_pillar-<topic-slug>-outline.md` — intro + H2 outline
- `content/briefs/drafts/YYYY-MM-DD_content-cluster-brief-<topic-slug>.md` — keyword cluster and internal linking map

