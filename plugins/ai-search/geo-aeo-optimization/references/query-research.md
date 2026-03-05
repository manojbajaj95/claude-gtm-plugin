# Query Research Methods for GEO/AEO

## Table of Contents
1. [Conversational Query Discovery](#conversational-query-discovery)
2. [Question Clustering](#question-clustering)
3. [Intent Classification](#intent-classification)
4. [AI Platform Testing](#ai-platform-testing)
5. [Competitive Intelligence](#competitive-intelligence)

---

## Conversational Query Discovery

### Tools & Methods

| Tool | Best For | Output |
|------|----------|--------|
| AnswerThePublic | Question discovery | Visual question maps |
| AlsoAsked | PAA question chains | Hierarchical questions |
| Semrush Keyword Magic | Volume + questions | Data-rich queries |
| Ahrefs Questions | Question filter | Search volume data |
| Google Autocomplete | Real-time trends | Suggested queries |
| Reddit/Quora | Authentic questions | User language patterns |

### Process: Building Question Maps

```
1. Start with seed topic
   └── Example: "email marketing"

2. Generate question variations
   ├── What questions: "what is email marketing"
   ├── How questions: "how to do email marketing"
   ├── Why questions: "why email marketing works"
   ├── When questions: "when to send marketing emails"
   ├── Where questions: "where to learn email marketing"
   ├── Who questions: "who needs email marketing"
   └── Which questions: "which email marketing tool"

3. Expand with modifiers
   ├── For beginners
   ├── In 2025
   ├── vs [alternative]
   ├── examples
   ├── best practices
   └── mistakes to avoid

4. Mine "People Also Ask"
   └── Click through 3+ levels to discover chains
```

### Conversational Query Patterns

**AI chatbots receive queries like:**

```
Traditional Search:
"best email marketing software"

Conversational Equivalent:
"What's the best email marketing software for a small 
e-commerce business with less than 10,000 subscribers 
that integrates with Shopify?"
```

**Optimize for:**
- Long-tail, specific queries
- Context-rich questions
- Multi-part queries
- Scenario-based questions

---

## Question Clustering

### Cluster Framework

```
Topic: [Main Topic]
│
├── Cluster 1: Definitions & Basics
│   ├── What is [topic]?
│   ├── What does [topic] mean?
│   ├── [Topic] definition
│   └── [Topic] explained simply
│
├── Cluster 2: How-To & Process
│   ├── How to [action] with [topic]
│   ├── How does [topic] work?
│   ├── Steps to [achieve outcome]
│   └── [Topic] tutorial
│
├── Cluster 3: Comparisons
│   ├── [Topic] vs [Alternative]
│   ├── Difference between [A] and [B]
│   ├── [Topic] alternatives
│   └── Best [topic] options
│
├── Cluster 4: Problems & Solutions
│   ├── [Topic] not working
│   ├── Common [topic] mistakes
│   ├── How to fix [problem]
│   └── [Topic] troubleshooting
│
├── Cluster 5: Cost & Value
│   ├── How much does [topic] cost?
│   ├── Is [topic] worth it?
│   ├── [Topic] pricing
│   └── Free vs paid [topic]
│
└── Cluster 6: Advanced & Specific
    ├── [Topic] for [specific audience]
    ├── Advanced [topic] techniques
    ├── [Topic] best practices
    └── [Topic] examples
```

### Prioritization Matrix

| Cluster | Search Volume | AI Citation Potential | Priority |
|---------|--------------|----------------------|----------|
| Definitions | High | Very High | 1 |
| How-To | High | High | 2 |
| Comparisons | Medium | High | 3 |
| Problems | Medium | Medium | 4 |
| Cost/Value | Medium | Medium | 5 |
| Advanced | Low | Low | 6 |

---

## Intent Classification

### The 4 Intent Types

```
1. INFORMATIONAL (Know)
   Signal words: what, why, how, guide, tutorial, learn
   AI behavior: Synthesizes answers from multiple sources
   Optimization: Comprehensive, authoritative content

2. NAVIGATIONAL (Go)
   Signal words: [brand name], login, official, website
   AI behavior: Directs to specific destinations
   Optimization: Brand presence, clear site structure

3. COMMERCIAL (Compare)
   Signal words: best, top, vs, review, comparison
   AI behavior: Provides options with analysis
   Optimization: Comparison content, honest reviews

4. TRANSACTIONAL (Do)
   Signal words: buy, price, discount, download, sign up
   AI behavior: Often defers to websites
   Optimization: Clear CTAs, product pages
```

### Intent-to-Content Mapping

| Intent | Content Type | Schema | Snippet Format |
|--------|--------------|--------|----------------|
| Informational | Guide, Explainer | Article, FAQPage | Paragraph, List |
| Navigational | Landing page | Organization, WebSite | Sitelinks |
| Commercial | Comparison, Review | Product, Review | Table |
| Transactional | Product page | Product, Offer | Rich product |

---

## AI Platform Testing

### Manual Testing Protocol

```
For each target query, test across:
□ ChatGPT (free and Plus)
□ Perplexity
□ Google (AI Overview)
□ Claude
□ Bing Copilot
□ Google Gemini

Document:
1. Is your brand/site mentioned?
2. Is your content cited?
3. What sources are cited?
4. How is the answer structured?
5. What's missing from the answer?
```

### Testing Queries Template

```
Base query: "[Your topic]"

Test variations:
1. "What is [topic]?"
2. "How do I [action related to topic]?"
3. "Best [topic] for [use case]"
4. "[Your brand] vs [competitor]"
5. "[Topic] in [current year]"
6. "Explain [topic] simply"
7. "[Topic] examples"
8. "Is [topic] worth it?"
```

### Competitor Citation Analysis

```python
# Pseudocode for tracking citations
queries = load_target_queries()
for query in queries:
    for platform in [ChatGPT, Perplexity, Google]:
        response = query_platform(platform, query)
        citations = extract_citations(response)
        
        record({
            'query': query,
            'platform': platform,
            'our_site_cited': our_domain in citations,
            'competitors_cited': [c for c in citations if c in competitor_domains],
            'citation_position': get_position(our_domain, citations)
        })
```

---

## Competitive Intelligence

### Citation Gap Analysis

**Step 1: Identify who's being cited**
```
Query your target topics across AI platforms
Record all cited domains
Tally citation frequency by domain
```

**Step 2: Analyze cited content**
```
For top-cited competitors:
├── Content structure (headers, formatting)
├── Content depth (word count, comprehensiveness)
├── Authority signals (author, sources, data)
├── Freshness (last updated date)
└── Technical factors (speed, schema, crawlability)
```

**Step 3: Gap identification**
```
Questions to answer:
├── What topics do they cover that we don't?
├── What formats are they using?
├── What unique data/research do they have?
├── How recent is their content?
└── What E-E-A-T signals are present?
```

### Competitive Content Audit Template

| Factor | Competitor A | Competitor B | Your Site | Gap |
|--------|--------------|--------------|-----------|-----|
| Topic coverage | | | | |
| Content depth | | | | |
| Freshness | | | | |
| Author authority | | | | |
| Source citations | | | | |
| Schema markup | | | | |
| FAQ sections | | | | |
| Original research | | | | |

### Action Planning

```
Priority actions based on gaps:
1. QUICK WINS: Easy to implement, high impact
   - Add FAQ sections
   - Update publish dates
   - Add author bios
   
2. MEDIUM EFFORT: Moderate effort, solid impact
   - Expand thin content
   - Add original data/statistics
   - Implement schema markup
   
3. LONG-TERM: High effort, transformative impact
   - Original research
   - Thought leadership content
   - Building topical authority
```
