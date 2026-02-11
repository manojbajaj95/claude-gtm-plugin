# Pre-Publish Checklist

Run through this checklist before using `/publish_blog`.

## Frontmatter Validation

### Core Fields
- [ ] `title`: Present and compelling
- [ ] `slug`: Kebab-case, no special characters
- [ ] `publishedAt`: Valid ISO date (YYYY-MM-DD)
- [ ] `category`: One of `technology`, `company`, `product`
- [ ] `contentType`: Valid content type

### AEO Fields
- [ ] `excerpt`: Present, max 300 chars
- [ ] `tldr`: 80-100 words, self-contained

### SEO Fields
- [ ] `seo.metaDescription`: 150-160 characters
- [ ] `seo.focusKeyword`: Present
- [ ] `seo.secondaryKeywords`: 2-4 keywords
- [ ] `seo.faq`: 3-5 Q&A pairs

## Category-Specific Checks

### Technology Posts
- [ ] Word count: 800-1,500 words
- [ ] At least 1 code example per major section
- [ ] Technical metrics/benchmarks included
- [ ] "Why we built" section or equivalent
- [ ] 5-10 external citations

### Company Posts
- [ ] Word count: 300-800 words
- [ ] Bold reframing statement in opening
- [ ] "Shift from/to" narrative present
- [ ] Executive quote included
- [ ] Forward-looking close
- [ ] 3-5 external citations

### Product Posts
- [ ] Word count: 500-1,000 words
- [ ] Pain point identified in opening
- [ ] Feature breakdown with bullets
- [ ] Use cases section
- [ ] Availability statement
- [ ] 3-5 external citations

## Content Quality

### Structure
- [ ] TL;DR immediately after frontmatter
- [ ] FAQ section present with 3-5 questions
- [ ] Internal links: 3-5 to docs
- [ ] External links: 5+ authoritative sources
- [ ] Author bio reference

### Style
- [ ] No passive voice ("Users are able to" -> "You can")
- [ ] No marketing buzzwords without substance
- [ ] No emoji
- [ ] Professional tone
- [ ] Active, direct language

### Forbidden Patterns
- [ ] No "Coming soon" without conditional
- [ ] No vague feature names (be specific)
- [ ] No unverified claims
- [ ] No `excerpt` = `metaDescription` (must differ)

## Red Flags (Automatic Rejection)

| Red Flag | Detection |
|----------|-----------|
| Missing TL;DR | `tldr` field undefined |
| TL;DR too short | Word count < 80 |
| Missing FAQ | `seo.faq` empty or undefined |
| No code examples | Technology post without code blocks |
| Over length | Exceeds category word limit |
| Under length | Below category minimum |
