# SEO Checklist

Comprehensive SEO guide for B2B content.

## Keyword Research

### Finding Keywords
```yaml
tools:
  free:
    - Google Search Console (what you rank for)
    - Google Trends (seasonal trends)
    - AnswerThePublic (question keywords)
    - AlsoAsked (related questions)
    - Google autocomplete

  paid:
    - Ahrefs (competitor keywords)
    - SEMrush (keyword difficulty)
    - Clearscope (content optimization)
```

### Keyword Intent
```yaml
intent_types:
  informational:
    signals: "how to", "what is", "guide", "tutorial"
    content: Blog posts, guides, videos
    example: "how to write cold emails"

  commercial:
    signals: "best", "vs", "review", "comparison"
    content: Comparison posts, reviews
    example: "best email outreach tools"

  transactional:
    signals: "buy", "pricing", "demo", "trial"
    content: Landing pages, product pages
    example: "email automation software pricing"

  navigational:
    signals: Brand names, specific products
    content: Homepage, product pages
    example: "Apollo.io login"
```

### Keyword Selection Criteria
```yaml
good_keywords:
  search_volume: ">100/month for niche B2B"
  difficulty: "<40 for new sites, <60 for established"
  intent_match: "Matches your content type"
  relevance: "Your audience actually searches this"

red_flags:
  - All top results are big brands
  - SERP is all ads
  - Results don't match your content type
  - Too broad (e.g., "sales")
```

## On-Page SEO Checklist

### Title Tag
- [ ] Primary keyword included
- [ ] Keyword front-loaded (first 60 chars)
- [ ] Under 60 characters
- [ ] Compelling (includes number, power word, or question)
- [ ] Unique across site

### Meta Description
- [ ] Primary keyword included
- [ ] 150-160 characters
- [ ] Includes call to action
- [ ] Summarizes content value
- [ ] Unique across site

### URL Structure
- [ ] Short and clean (/topic-keyword)
- [ ] Primary keyword included
- [ ] No dates (evergreen URLs)
- [ ] Hyphens between words
- [ ] Lowercase only

### Headings
- [ ] H1 contains primary keyword
- [ ] Only one H1 per page
- [ ] H2s contain secondary keywords
- [ ] Logical hierarchy (H1 > H2 > H3)
- [ ] Scannable (reader can skim headings)

### Content Body
- [ ] Primary keyword in first 100 words
- [ ] Natural keyword density (1-2%)
- [ ] LSI keywords included
- [ ] Questions answered (from "People Also Ask")
- [ ] Minimum 1,500 words for competitive topics

### Images
- [ ] Descriptive file names (topic-keyword.jpg)
- [ ] Alt text with keywords
- [ ] Compressed (<100KB where possible)
- [ ] WebP format preferred
- [ ] Lazy loading enabled

### Internal Links
- [ ] 2-3 internal links minimum
- [ ] Descriptive anchor text (not "click here")
- [ ] Link to relevant, high-value pages
- [ ] Update old posts to link to new ones

### External Links
- [ ] 1-2 authoritative external links
- [ ] Opens in new tab
- [ ] Supports claims with evidence
- [ ] No competitor links

## Technical SEO

### Page Speed
```yaml
targets:
  largest_contentful_paint: "<2.5s"
  first_input_delay: "<100ms"
  cumulative_layout_shift: "<0.1"
  time_to_first_byte: "<600ms"

quick_wins:
  - Compress images (TinyPNG, Squoosh)
  - Enable browser caching
  - Minify CSS/JS
  - Use CDN
  - Remove unused plugins
```

### Mobile Optimization
- [ ] Mobile-responsive design
- [ ] Tap targets >48px
- [ ] No horizontal scrolling
- [ ] Font size >16px
- [ ] Mobile-first indexing ready

### Schema Markup
```yaml
recommended_schema:
  articles:
    - Article
    - BlogPosting
    - HowTo (for tutorials)
    - FAQ (for Q&A content)

  business:
    - Organization
    - LocalBusiness
    - Product
    - Review

  events:
    - Event
    - Webinar
```

### Indexing
- [ ] Page is indexable (no noindex)
- [ ] Submitted to Google Search Console
- [ ] XML sitemap includes page
- [ ] No duplicate content issues
- [ ] Canonical tags set correctly

## Content Quality Signals

### E-E-A-T (Experience, Expertise, Authority, Trust)
```yaml
experience:
  - First-person accounts
  - Real examples and case studies
  - Screenshots and proof

expertise:
  - Author credentials visible
  - Technical accuracy
  - Up-to-date information

authority:
  - Backlinks from relevant sites
  - Brand mentions
  - Social proof

trust:
  - Contact information visible
  - Privacy policy
  - Secure site (HTTPS)
  - Accurate claims with sources
```

### Content Freshness
- [ ] Publication date visible
- [ ] Last updated date (for evergreen content)
- [ ] Regular updates to key pages
- [ ] Outdated content removed or updated

## Post-Publish Checklist

### Indexing
- [ ] Request indexing in Search Console
- [ ] Share on social (generates initial traffic)
- [ ] Internal link from high-traffic pages

### Monitoring
- [ ] Set up rank tracking for target keyword
- [ ] Monitor Search Console for impressions/clicks
- [ ] Check for crawl errors

### Iteration
- [ ] Review rankings after 2-4 weeks
- [ ] Update content based on SERP changes
- [ ] Add missing sections competitors have
- [ ] Improve weak sections

## Quick Reference: SEO Copy Formulas

### Title Formulas
```
[Number] [Adjective] Ways to [Desired Outcome]
How to [Achieve Goal] in [Timeframe]
[Topic]: The Complete Guide for [Year]
[Topic] vs [Topic]: Which is Better for [Use Case]?
What is [Topic]? [Benefit]-Focused Guide
```

### Meta Description Formulas
```
Learn [what they'll learn]. This guide covers [topics] so you can [benefit]. [CTA].

[Pain point]? Discover [number] proven [solutions] that [benefit]. [CTA].

[Question]? This [content type] shows you [what] with [proof point]. [CTA].
```
