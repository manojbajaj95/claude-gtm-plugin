# SEO Implementation Checklist

## Per-Page Requirements

- [ ] Unique `<title>` (50-60 chars, keyword first)
- [ ] Unique `<meta name="description">` (150-160 chars)
- [ ] Canonical URL: `<link rel="canonical" href="...">`
- [ ] Single H1 tag with primary keyword
- [ ] Heading hierarchy (H1 > H2 > H3, no skipping)
- [ ] Image alt text (descriptive, not stuffed)
- [ ] Internal links to related pages

## Technical SEO

- [ ] robots.txt configured
- [ ] XML sitemap submitted
- [ ] HTTPS everywhere
- [ ] Mobile responsive
- [ ] Core Web Vitals passing
- [ ] No duplicate content
- [ ] 301 redirects for moved pages

## Structured Data (JSON-LD)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": { "@type": "Person", "name": "Author" },
  "datePublished": "2024-01-01"
}
</script>
```
