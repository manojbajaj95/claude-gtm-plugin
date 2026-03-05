# AI Crawlers & Bot Management Guide

## Table of Contents
1. [AI Crawler Overview](#ai-crawler-overview)
2. [robots.txt Configuration](#robotstxt-configuration)
3. [Crawler Characteristics](#crawler-characteristics)
4. [Strategic Decisions](#strategic-decisions)
5. [Implementation Guide](#implementation-guide)

---

## AI Crawler Overview

### Major AI Crawlers (2025)

| Crawler | Company | Purpose | Recommendation |
|---------|---------|---------|----------------|
| GPTBot | OpenAI | Training data | Block if concerned about training |
| OAI-SearchBot | OpenAI | ChatGPT Search | Allow for AI search visibility |
| ChatGPT-User | OpenAI | User-requested fetching | Allow for user experience |
| Google-Extended | Google | Gemini training | Block if concerned, Allow for AI Search |
| Googlebot | Google | Search indexing | Always Allow |
| PerplexityBot | Perplexity | Search & answers | Allow for visibility |
| ClaudeBot | Anthropic | Claude features | Allow for visibility |
| Bytespider | ByteDance | TikTok/Training | Consider blocking |
| CCBot | Common Crawl | Dataset collection | Consider blocking |
| FacebookBot | Meta | AI training | Consider blocking |

### Key Distinction: Search vs Training

```
SEARCH CRAWLERS (Allow for visibility):
├── Googlebot          → Traditional search
├── OAI-SearchBot      → ChatGPT Search results
├── ChatGPT-User       → User asks ChatGPT to read a page
├── PerplexityBot      → Perplexity answers
└── ClaudeBot          → Claude features

TRAINING CRAWLERS (Block if data protection matters):
├── GPTBot             → OpenAI model training
├── Google-Extended    → Gemini training
├── CCBot              → Common Crawl datasets
├── Bytespider         → ByteDance training
└── FacebookBot        → Meta AI training
```

---

## robots.txt Configuration

### Recommended Configuration (Balanced)

```txt
# ===========================================
# AI SEARCH CRAWLERS - ALLOW
# ===========================================

# OpenAI Search (ChatGPT Search feature)
User-agent: OAI-SearchBot
Allow: /

# ChatGPT when users ask it to read a page
User-agent: ChatGPT-User
Allow: /

# Perplexity AI search
User-agent: PerplexityBot
Allow: /

# Claude AI
User-agent: ClaudeBot
Allow: /

# ===========================================
# AI TRAINING CRAWLERS - BLOCK
# ===========================================

# OpenAI training (not search)
User-agent: GPTBot
Disallow: /

# Google Gemini training
User-agent: Google-Extended
Disallow: /

# Common Crawl
User-agent: CCBot
Disallow: /

# ByteDance
User-agent: Bytespider
Disallow: /

# Meta AI training
User-agent: FacebookBot
Disallow: /

# ===========================================
# TRADITIONAL SEARCH - ALLOW
# ===========================================

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

### Maximum Visibility Configuration

```txt
# Allow all AI crawlers for maximum reach
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

### Maximum Protection Configuration

```txt
# Block all AI crawlers except traditional search
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Disallow: /

User-agent: OAI-SearchBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: *
Disallow: /
```

---

## Crawler Characteristics

### Crawl Behavior Comparison

| Crawler | Respects robots.txt | Crawl Rate | JavaScript Rendering |
|---------|---------------------|------------|---------------------|
| Googlebot | Yes | Adaptive | Yes (2nd wave) |
| GPTBot | Yes | Unknown | Limited |
| OAI-SearchBot | Yes | Unknown | Limited |
| PerplexityBot | Yes | Moderate | Limited |
| ClaudeBot | Yes | Unknown | Limited |
| CCBot | Generally yes | Heavy | No |

### What AI Crawlers Index

```
Typically Indexed:
├── Main body content
├── Headers (H1-H6)
├── Meta descriptions
├── Alt text
├── Structured data (JSON-LD)
├── Tables
└── Lists

Often Missed:
├── JavaScript-rendered content
├── Content behind tabs/accordions
├── Lazy-loaded images
├── PDF content
├── Video transcripts (unless in HTML)
└── Content in iframes
```

---

## Strategic Decisions

### Decision Matrix

| Business Type | Strategy | Reasoning |
|---------------|----------|-----------|
| Publisher/Blog | Allow search, Block training | Maintain traffic, protect content |
| E-commerce | Allow all | Maximum product visibility |
| SaaS | Allow search, Consider training | Brand visibility, protect docs |
| Enterprise B2B | Selective allow | Control information flow |
| Personal brand | Allow all | Maximum reach |
| Research/Academic | Allow all | Citation and reach |

### Questions to Ask

1. **Is being cited by AI chatbots valuable to you?**
   - Yes → Allow search crawlers
   - No → Block all AI crawlers

2. **Are you concerned about AI training on your content?**
   - Yes → Block training crawlers (GPTBot, Google-Extended)
   - No → Allow all

3. **Do users ask AI to read your pages?**
   - Yes → Allow ChatGPT-User
   - No → Can block

4. **Is your content time-sensitive or frequently updated?**
   - Yes → Allow all search crawlers for freshness
   - No → Selective blocking okay

---

## Implementation Guide

### Step 1: Audit Current Configuration

```bash
# Check current robots.txt
curl -s https://yoursite.com/robots.txt

# Test specific bot access
curl -A "GPTBot" -I https://yoursite.com/
curl -A "OAI-SearchBot" -I https://yoursite.com/
```

### Step 2: Monitor Crawler Activity

**In server logs, look for:**
```
User-Agent patterns:
- "GPTBot/1.0"
- "OAI-SearchBot"
- "ChatGPT-User"
- "PerplexityBot"
- "ClaudeBot"
```

**Log analysis command:**
```bash
grep -E "GPTBot|OAI-SearchBot|ChatGPT-User|PerplexityBot|ClaudeBot" access.log | \
  awk '{print $1, $7}' | sort | uniq -c | sort -rn
```

### Step 3: Implement WAF Rules (if needed)

**Cloudflare example:**
```
# Block specific bots at WAF level
(cf.client.bot and http.user_agent contains "GPTBot")
```

### Step 4: Verify Implementation

```bash
# Test that robots.txt is being served correctly
curl -s https://yoursite.com/robots.txt | grep -A2 "GPTBot"

# Verify bot can/cannot access
curl -A "GPTBot" -s -o /dev/null -w "%{http_code}" https://yoursite.com/
```

### Step 5: Monitor Impact

Track these metrics after changes:
- AI referral traffic (from Perplexity, ChatGPT, etc.)
- Brand mentions in AI responses (manual testing)
- Overall organic traffic (ensure no negative impact)

---

## Emerging Crawlers to Watch

| Bot | Company | Status | Notes |
|-----|---------|--------|-------|
| MistralBot | Mistral AI | Emerging | European AI |
| DeepSeekBot | DeepSeek | Emerging | Chinese AI |
| GrokBot | xAI | Expected | Elon Musk's AI |
| MetaAI-SearchBot | Meta | Expected | Meta AI search |

**Recommendation**: Monitor industry news and update robots.txt quarterly.
