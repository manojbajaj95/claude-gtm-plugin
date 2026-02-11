# Schema Markup for AI Optimization

## Table of Contents
1. [Schema Priority for AI](#schema-priority-for-ai)
2. [High-Impact Schema Types](#high-impact-schema-types)
3. [Implementation Patterns](#implementation-patterns)
4. [AI-Specific Considerations](#ai-specific-considerations)

---

## Schema Priority for AI

### Why Schema Matters for AI

AI systems use structured data to:
- Understand content type and context
- Extract specific facts and attributes
- Validate information accuracy
- Determine content authority

### Priority Schema Types for GEO/AEO

| Priority | Schema Type | AI Use Case |
|----------|-------------|-------------|
| 1 | FAQPage | Direct answer extraction |
| 2 | HowTo | Step-by-step instruction |
| 3 | Article/BlogPosting | Content attribution |
| 4 | Product + Review | E-commerce answers |
| 5 | Organization | Brand knowledge |
| 6 | Person | Author authority |
| 7 | LocalBusiness | Location queries |
| 8 | BreadcrumbList | Site structure |

---

## High-Impact Schema Types

### FAQPage (Highest AI Impact)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is [topic]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Complete answer that can stand alone. Include key facts, figures, and context. This entire text may be extracted by AI systems."
      }
    },
    {
      "@type": "Question",
      "name": "How does [topic] work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Step-by-step or explanatory answer. Be comprehensive but concise."
      }
    }
  ]
}
```

**Best practices for AI:**
- Questions should match real user queries
- Answers must be complete and standalone
- Include specific facts, not just fluff
- Keep answers 50-300 words each

### HowTo (High AI Impact)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [Action]",
  "description": "Brief overview of what this guide teaches",
  "totalTime": "PT30M",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Step name (action verb)",
      "text": "Detailed instructions for this step. Be specific and actionable.",
      "image": "https://example.com/step1.jpg"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Next step name",
      "text": "Detailed instructions for this step."
    }
  ]
}
```

**Best practices for AI:**
- Step names should be scannable actions
- Step text should be complete instructions
- Include time estimates when possible
- Each step should be independently understandable

### Article + Author (Authority Signal)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title (max 110 chars)",
  "description": "Meta description - comprehensive summary",
  "image": "https://example.com/image.jpg",
  "datePublished": "2025-01-08T08:00:00Z",
  "dateModified": "2025-01-08T10:00:00Z",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author/name",
    "jobTitle": "Subject Matter Expert",
    "description": "Brief bio establishing expertise",
    "sameAs": [
      "https://linkedin.com/in/authorname",
      "https://twitter.com/authorname"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publisher Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article-url"
  }
}
```

**AI authority signals:**
- Author with credentials and bio
- Publisher organization details
- dateModified shows freshness
- sameAs links validate identity

### Speakable (Voice/AI Extraction)

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Page Title",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".tldr", ".key-takeaway", "#summary"]
  }
}
```

Marks content sections optimized for:
- Voice assistant reading
- AI summary extraction
- Audio content generation

---

## Implementation Patterns

### Combined Schema for Content Pages

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://example.com/page#article",
      "headline": "Complete Guide to [Topic]",
      "author": {"@id": "https://example.com/#author"},
      "publisher": {"@id": "https://example.com/#org"},
      "datePublished": "2025-01-08",
      "dateModified": "2025-01-08"
    },
    {
      "@type": "FAQPage",
      "@id": "https://example.com/page#faq",
      "mainEntity": [...]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://example.com/page#breadcrumb",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/"},
        {"@type": "ListItem", "position": 2, "name": "Category", "item": "https://example.com/category/"},
        {"@type": "ListItem", "position": 3, "name": "Page Title"}
      ]
    },
    {
      "@type": "Organization",
      "@id": "https://example.com/#org",
      "name": "Company Name",
      "url": "https://example.com",
      "logo": "https://example.com/logo.png"
    },
    {
      "@type": "Person",
      "@id": "https://example.com/#author",
      "name": "Author Name",
      "jobTitle": "Expert Title"
    }
  ]
}
```

### E-commerce Product Page

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "name": "Product Name",
      "description": "Detailed product description",
      "image": ["image1.jpg", "image2.jpg"],
      "brand": {"@type": "Brand", "name": "Brand"},
      "offers": {
        "@type": "Offer",
        "price": "99.99",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.5",
        "reviewCount": "127"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is included with [Product]?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Complete list of what's included..."
          }
        }
      ]
    }
  ]
}
```

---

## AI-Specific Considerations

### Schema That AI Systems Prioritize

1. **Factual extraction**
   - FAQPage → Direct Q&A extraction
   - HowTo → Step extraction
   - Product → Spec extraction

2. **Authority signals**
   - Person (author) → Expertise validation
   - Organization → Publisher trust
   - sameAs → Identity verification

3. **Content structure**
   - Article → Content type identification
   - BreadcrumbList → Topic hierarchy
   - WebPage → Page purpose

### Schema That Has Less AI Impact

- Event (unless for event queries)
- Recipe (unless for recipe queries)
- Video (unless for video queries)
- Music (domain-specific)

### Validation for AI Optimization

```
Checklist before publishing:
□ Rich Results Test passes
□ Schema matches visible content exactly
□ No exaggerated claims
□ dateModified is accurate
□ Author has real credentials
□ FAQ questions match real search queries
□ All URLs are absolute and HTTPS
□ Images are accessible and properly sized
```

### Common Mistakes to Avoid

| Mistake | Why It Hurts AI Visibility |
|---------|---------------------------|
| FAQ questions no one searches | AI won't surface irrelevant Q&A |
| Exaggerated ratings | Damages trust signals |
| Missing author info | Reduces E-E-A-T signals |
| Outdated dateModified | AI prefers fresh content |
| Schema not matching content | Validation failures |
| Overly complex nesting | Harder to parse |
