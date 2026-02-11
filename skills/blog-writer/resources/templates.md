# Blog Templates

## BaseHub Entry Fields

This frontmatter structure maps to `AIGeneratedPost` type in `@repo/cms-workflows`, enabling publish via `/publish_blog`.

### Core Fields

- **title**: Blog post title (compelling, keyword-rich)
- **slug**: URL slug (kebab-case, no category prefix)
- **publishedAt**: ISO date string (YYYY-MM-DD)
- **category**: One of: `technology`, `company`, `product`
- **contentType**: One of: `tutorial`, `announcement`, `thought-leadership`, `case-study`, `comparison`, `deep-dive`, `guide`

### AEO Fields (Answer Engine Optimization)

- **excerpt**: 2-3 sentences for listings (max 300 chars)
- **tldr**: 80-100 word summary for AI citation. Self-contained paragraph with key benefits.

### SEO Fields (nested under `seo:`)

- **seo.metaDescription**: 150-160 chars with primary keyword
- **seo.focusKeyword**: Primary keyword phrase
- **seo.secondaryKeywords**: Array of 2-4 secondary keywords
- **seo.faq**: Array of 3-5 question/answer pairs

### Author (hardcoded for now)

- **author**: `jeevanpillay`

### Internal Fields (nested under `_internal:`)

Stripped before publishing:

- **_internal.status**: `draft` or `published`
- **_internal.generated**: ISO timestamp
- **_internal.sources**: Array of research URLs
- **_internal.word_count**: Approximate word count
- **_internal.reading_time**: Estimated reading time

### Frontmatter Template

```yaml
---
# Core fields
title: "Blog Post Title"
slug: "blog-post-slug"
publishedAt: "YYYY-MM-DD"
category: "technology" | "company" | "product"
contentType: "deep-dive" | "announcement" | "tutorial" | etc.

# AEO fields
excerpt: "2-3 sentence summary for listings, max 300 chars"
tldr: "80-100 word summary for AI citation. Self-contained paragraph covering key user benefits and main insights."

# SEO nested object
seo:
  metaDescription: "150-160 char meta description with primary keyword"
  focusKeyword: "primary keyword phrase"
  secondaryKeywords:
    - "secondary keyword 1"
    - "secondary keyword 2"
  faq:
    - question: "What is [topic]?"
      answer: "Concise answer optimized for featured snippets."
    - question: "How do I [action]?"
      answer: "Step-by-step answer with specifics."

# Author (hardcoded)
author: "jeevanpillay"

# Internal fields (stripped before publish)
_internal:
  status: draft
  generated: "YYYY-MM-DDTHH:MM:SSZ"
  sources:
    - "https://source1.com"
    - "https://source2.com"
  word_count: 1200
  reading_time: "6 min"
---
```

## Document Structure by Category

### Technology Posts (800-1,500 words)

Note: The `tldr` frontmatter field is rendered automatically in a highlight box on the page. Do NOT include a `## TL;DR` section in the body.

```markdown
## [Technical Problem/Hook]

[1-2 paragraphs introducing the technical challenge or industry controversy]

**Key metrics:**
- [Data point 1]
- [Data point 2]

---

## [Technical Deep-Dive Section]

[Layer 1: Foundation explanation]

```typescript
// Code example
```

[Layer 2: Implementation details]

---

## [Solution/How We Built It]

[Natural product positioning with technical specifics]

**What's included:**
- [Capability 1]
- [Capability 2]

---

## Why We Built It This Way

[1-2 paragraphs on architectural decisions]

---

## Frequently Asked Questions

**Q: [Technical question]?**
A: [Complete, self-contained answer]

**Q: [Implementation question]?**
A: [Step-by-step answer]

---

## Resources

- [Documentation](/docs/relevant-page)
- [API Reference](/docs/api-reference/endpoint)
- [Quick Start](/docs/get-started/quickstart)
```

### Company Posts (300-800 words)

Note: The `tldr` frontmatter field is rendered automatically in a highlight box on the page. Do NOT include a `## TL;DR` section in the body.

```markdown
## [Bold Reframing Statement]

[The internet is no longer... -> it's now...]

---

## [Core Announcement]

[Who, what, when - the news]

**Key highlights:**
- [Highlight 1]
- [Highlight 2]

---

## [Strategic Context]

[Why this matters for the industry]

> "[Executive quote]" -- Name, Title

---

## [Looking Ahead]

[Vision statement, next steps]

---

## Frequently Asked Questions

**Q: [Impact question]?**
A: [Answer with forward-looking vision]

---

## Learn More

- [Careers](/careers)
- [About](/about)
- [Contact](/contact)
```

### Product Posts (500-1,000 words)

Note: The `tldr` frontmatter field is rendered automatically in a highlight box on the page. Do NOT include a `## TL;DR` section in the body.

```markdown
## [Market Shift/Pain Point]

[1-2 paragraphs identifying the problem]

---

## Introducing [Feature Name]

[What it is and high-level purpose]

**Key capabilities:**
- [Capability 1]: [Benefit]
- [Capability 2]: [Benefit]
- [Capability 3]: [Benefit]

---

## How It Works

[Brief explanation or walkthrough]

```yaml
# Example configuration
```

---

## Use Cases

**[Use case 1]**: [How the feature helps]

**[Use case 2]**: [How the feature helps]

---

## Availability

[When and how to access. Availability statement.]

---

## Frequently Asked Questions

**Q: [Pricing/access question]?**
A: [Clear answer]

**Q: [Integration question]?**
A: [Technical answer]

---

## Get Started

- [Quick Start](/docs/get-started/quickstart)
- [Feature Docs](/docs/features/feature-name)
- [Pricing](/pricing)
```
