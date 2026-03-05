# GTM Skills

Go-to-market skills that turn Claude into a GTM specialist. 166 skills across SEO, content, outbound, sales, growth, analytics, strategy, ads, social, CRM, and AI search — plus a `/bootstrap` command that onboards Claude to your brand, voice, and goals. Built for [Claude Code](https://claude.com/product/claude-code), also compatible with [Claude Cowork](https://claude.com/product/cowork) and any agent that supports the [Agent Skills spec](https://agentskills.io).

## Why This Plugin

Most AI assistants give generic marketing advice. This plugin gives Claude the frameworks, workflows, and domain knowledge of an experienced GTM team — so it can write copy in your voice, audit your SEO like a consultant, plan launches like a PMM, and build outbound sequences like an SDR.

The `/bootstrap` command interviews you once about your brand, audience, and voice, then generates four context files that every skill reads before doing anything. The result: Claude doesn't just know marketing — it knows *your* marketing.

## Installation

### Claude Cowork

Install from the plugin marketplace at [claude.com/plugins](https://claude.com/plugins). Search for **GTM Skills**, click install, and the plugin is immediately available in your Cowork sessions.

### Claude Code

```bash
# Add the marketplace
claude plugin marketplace add mbajaj/gtm-plugins

# Install all GTM skills
claude plugin install gtm-skills@gtm-plugins
```

You can also install individual domain plugins if you only need specific skills:

```bash
claude plugin install seo@gtm-plugins
claude plugin install content@gtm-plugins
claude plugin install outbound@gtm-plugins
claude plugin install sales@gtm-plugins
claude plugin install growth@gtm-plugins
claude plugin install analytics@gtm-plugins
claude plugin install strategy@gtm-plugins
claude plugin install ads@gtm-plugins
claude plugin install social@gtm-plugins
claude plugin install crm@gtm-plugins
claude plugin install ai-search@gtm-plugins
```

### Skills CLI

Use [npx skills](https://github.com/vercel-labs/skills) to install skills directly into any project:

```bash
# Install all skills
npx skills add mbajaj/gtm-plugin

# Install specific skills
npx skills add mbajaj/gtm-plugin --skill seo-audit copywriting founder-sales

# List available skills
npx skills add mbajaj/gtm-plugin --list
```

### Clone and Load Locally

```bash
git clone https://github.com/mbajaj/gtm-plugin.git
```

Then open Claude Code in the cloned directory — the plugin loads automatically.

### Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/mbajaj/gtm-plugin.git .agents/gtm-plugin
```

## Getting Started

### Bootstrap Your Project

Run `/bootstrap` in any project directory. Claude runs an agency-style onboarding interview — asking about your brand, audience, voice, and goals — then generates four foundational files:

| File | What it captures |
|---|---|
| `CLAUDE.md` | Instructions for Claude: which files to read before which tasks, routing rules for new learnings |
| `BRAND.md` | Brand identity — positioning, messaging, audience, competitors, voice guidelines |
| `SOUL.md` | Personal voice — your writing style, quirks, references, personality |
| `MEMORY.md` | Operational log — campaigns launched, results, decisions, open questions (append-only) |

Once these exist, every skill reads the relevant context before doing anything. Claude works in your voice, for your brand, from day one.

### Using Skills

Skills activate automatically when Claude detects a matching task. Just describe what you need in natural language:

```
"Audit the SEO on my landing page"
→ Activates seo-audit

"Write a cold email sequence for enterprise CTOs"
→ Activates cold-email-sequence-generator + startup-icp-definer

"Plan a Product Hunt launch for next month"
→ Activates product-hunt-launch + launch-marketing

"Create a 5-email onboarding sequence"
→ Activates email-sequence + onboarding-cro

"Help me figure out pricing for my SaaS"
→ Activates pricing-strategy

"Write a LinkedIn post about our new feature"
→ Activates linkedin-content + copywriting
```

Skills cross-reference each other. Ask Claude to write a cold email and it pulls from your brand positioning (`BRAND.md`), your personal voice (`SOUL.md`), and your ICP — not from a generic template.

## How It Works

```
gtm-plugin/
├── .claude-plugin/          # Plugin manifest
├── commands/
│   └── bootstrap.md         # /bootstrap onboarding command
└── plugins/
    ├── seo/                 # 10 skills
    ├── ai-search/           # 5 skills
    ├── content/             # 14 skills
    ├── social/              # 19 skills
    ├── outbound/            # 14 skills
    ├── sales/               # 7 skills
    ├── growth/              # 47 skills
    ├── analytics/           # 21 skills
    ├── strategy/            # 15 skills
    ├── ads/                 # 9 skills
    └── crm/                 # 5 skills
```

**Skills** are markdown files with YAML frontmatter that give Claude specialized knowledge for specific tasks. Claude activates them automatically when it detects a matching task — or you can invoke them directly.

**Commands** are explicit actions you trigger. Currently: `/bootstrap`.

Skills reference each other and build on the context files created by `/bootstrap`. Ask Claude to write a cold email and it pulls from your brand positioning, your voice, and your ICP — not from a generic template.

## Skills

### SEO & Search (10)

`seo` · `seo-audit` · `seo-geo` · `seo-optimizer` · `keyword-research` · `keyword-expansion` · `programmatic-seo` · `backlink-analyzer` · `seo-backlink-strategy` · `serp-analysis`

### AI Search & GEO (5)

`aeo-optimization` · `aeo-scorecard` · `ai-search-optimization` · `geo-aeo-optimization` · `project-aeo-monitoring-tools`

### Content & Copywriting (14)

`copywriting` · `copy` · `content-strategy` · `content-marketing` · `content-research` · `content-marketer` · `content-brief` · `content-optimizer` · `marketing-content-strategy` · `blog-writer` · `blog-writing` · `blog-post-writer` · `technical-blog-writing` · `webinar-to-content-multiplier`

### Social Media (19)

`social-media` · `social-content` · `social-graphics` · `social-media-analyzer` · `social-community` · `social-repurposer` · `ai-social-media-content` · `linkedin` · `linkedin-content` · `linkedin-automation` · `linkedin-personal-branding` · `linkedin-post-optimizer` · `writing-linkedin-posts` · `twitter-x` · `youtube` · `youtube-video-analyst` · `youtube-video-hook` · `youtube-plan-new-video` · `youtube-research-video-topic`

### Email & Outbound (14)

`cold_email` · `cold-email-sequence-generator` · `cold-outreach-generator` · `email-sequence` · `email-template-generator` · `email-design` · `outbound-sequences` · `outbound-plays` · `outbound-optimizer` · `gtm-outbound` · `bd-email` · `newsletter` · `newsletter-curation` · `events-webinars`

### Sales (7)

`founder-sales` · `enterprise-sales` · `sales-qualification` · `product-led-sales` · `building-sales-team` · `sales-compensation` · `startup-icp-definer`

### Growth & Product (47)

`growth` · `growth-strategy` · `growth-loops` · `growth-product-manager` · `product-market-fit` · `measuring-product-market-fit` · `launch-gtm-execution` · `launch-marketing` · `product-hunt-launch` · `producthunt` · `ph-community-outreach` · `ph-content-recycling` · `lead-generation` · `lead-magnet` · `lead-research-assistant` · `leadgenius-api` · `marketing-leads-generation` · `marketing` · `marketing-demand-acquisition` · `marketing-ideas` · `marketing-strategy-pmm` · `running-marketing-campaigns` · `referral-program` · `funnel-analysis` · `funnel-validator` · `challenge-funnel` · `buyer-persona-generator` · `ab-test-setup` · `onboarding-cro` · `personalization-at-scale` · `retain` · `retention-engine` · `customer-success` · `customer-success-manager` · `community-builder` · `community-building` · `community-building-strategist` · `community-architect` · `free-tool-strategy` · `gtm-pricing` · `executive-dashboard-generator` · `webinar-content-repurposer` · `pr-specialist` · `skill-navigator` · `ui-ux-audit` · `user-onboarding` · `x-impact-checker`

### Analytics & Research (21)

`analytics-tracking` · `analytics-interpretation` · `google-analytics` · `posthog-analytics` · `product-analytics` · `competitor-analysis` · `competitor-teardown` · `competitor-price-tracker` · `business-competitor-analysis` · `competitive-ads-extractor` · `market-researcher` · `market-research-reports` · `apify-market-research` · `apify-content-analytics` · `apify-lead-generation` · `app-store-optimization` · `dataforseo-backlinks-api` · `keyword-cluster-builder` · `roi-analyzer` · `utm-builder` · `qr-code-generator`

### Strategy & Positioning (15)

`startup-go-to-market` · `Go-to-Market-Planner` · `positioning-messaging` · `brand-messaging-architecture` · `storybrand-messaging` · `branding` · `design-branding` · `webconsulting-branding` · `pricing-strategy` · `pricing-strategist` · `product-strategy` · `product-strategist` · `prd-v09-gtm-strategy` · `technical-launch-planner` · `working-backwards`

### Ads & Paid (9)

`paid-ads` · `ad-copy-generator` · `landing-page` · `landing-page-copywriter` · `landing-page-guide-v2` · `landing-page-vercel` · `pitch-deck` · `pitch-deck-visuals` · `cro-methodology`

### CRM & Automation (5)

`crm-integration` · `hubspot-crm` · `intercom-crm` · `espocrm-development` · `marketing-automation`

## Routing Rules

As you work with Claude, it routes new information to the right file automatically:

- Brand info (positioning, messaging, audience insights) → `BRAND.md`
- Personal info (writing preferences, quirks, reference examples) → `SOUL.md`
- Operational progress (campaigns launched, results, decisions) → `MEMORY.md` (appended, dated)

## Validation

Skills follow the [Agent Skills specification](https://agentskills.io/specification). Run the validator to check all skills:

```bash
./validate-skills.sh
```

This checks frontmatter fields, naming conventions, description quality, and file structure against the official spec. See the [official reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) for the canonical implementation.

## Contributing

Skills are markdown files. Fork the repo, make your changes, and submit a PR.

Each skill lives in `plugins/<category>/<skill-name>/SKILL.md` and must have valid YAML frontmatter with at least `name` and `description`. Run `./validate-skills.sh` before submitting to catch issues.

## License

MIT
