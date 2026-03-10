# GTM Skills

Go-to-market skills that turn Claude into a GTM specialist. 183 skills across SEO & AI search, content, outbound, sales, growth, analytics, strategy, ads, social, and CRM — plus a `/bootstrap` command that onboards Claude to your brand, voice, and goals. Built for [Claude Code](https://claude.com/product/claude-code), also compatible with [Claude Cowork](https://claude.com/product/cowork) and any agent that supports the [Agent Skills spec](https://agentskills.io).

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
    ├── seo/                 # 20 skills (includes AI search & GEO)
    ├── content/             # 19 skills
    ├── social/              # 24 skills
    ├── outbound/            # 12 skills
    ├── sales/               # 9 skills
    ├── growth/              # 45 skills
    ├── analytics/           # 14 skills
    ├── strategy/            # 29 skills
    ├── ads/                 # 7 skills
    └── crm/                 # 5 skills
```

**Skills** are markdown files with YAML frontmatter that give Claude specialized knowledge for specific tasks. Claude activates them automatically when it detects a matching task — or you can invoke them directly.

**Commands** are explicit actions you trigger. Currently: `/bootstrap`.

Skills reference each other and build on the context files created by `/bootstrap`. Ask Claude to write a cold email and it pulls from your brand positioning, your voice, and your ICP — not from a generic template.

## Skills

### Ads & Paid (7)

├── `ad-copy-generator`
├── `ad-creative`
├── `landing-page-copywriter`
├── `landing-page-guide-v2`
├── `landing-page-vercel`
├── `landing-page`
└── `paid-ads`

### Analytics & Data (8)

├── `analytics-interpretation`
├── `analytics-tracking`
├── `app-store-optimization`
├── `competitive-ads-extractor`
├── `product-analytics`
├── `qr-code-generator`
├── `roi-analyzer`
└── `utm-builder`

### Content & Copywriting (19)

├── `blog-post-writer`
├── `blog-writer`
├── `blog-writing-specialist`
├── `blog-writing`
├── `content-brief`
├── `content-creation-and-marketing`
├── `content-optimizer`
├── `content-research`
├── `content-strategy-and-planning`
├── `copy-editing`
├── `copy`
├── `copywriting`
├── `newsletter-curation`
├── `newsletter`
├── `ph-content-recycling`
├── `technical-blog-writing`
├── `twitter-algorithm-optimizer`
├── `webinar-content-and-events`
└── `writing-linkedin-posts`

### CRM & Automation (2)

├── `crm-integration`
└── `marketing-automation`

### Growth & Conversion (22)

├── `ab-test-setup`
├── `challenge-funnel`
├── `conversion-rate-optimization`
├── `customer-success-and-retention`
├── `executive-dashboard-generator`
├── `free-tool-strategy`
├── `funnel-analysis`
├── `funnel-validator`
├── `growth-strategy`
├── `launch-gtm-execution`
├── `launch-marketing`
├── `lead-generation-and-demand`
├── `marketing-campaign-management`
├── `personalization-at-scale`
├── `ph-community-outreach`
├── `pr-specialist`
├── `product-hunt-launch`
├── `product-market-fit-analysis`
├── `producthunt`
├── `referral-program`
├── `skill-navigator`
└── `user-onboarding`

### Email & Outbound (3)

├── `cold-outreach-generator`
├── `email-design`
└── `outbound-email-strategy`

### Sales (4)

├── `revops`
├── `sales-compensation`
├── `sales-strategy-and-enablement`
└── `startup-icp-definer`

### SEO & AI Search (20)

├── `aeo-optimization`
├── `aeo-scorecard`
├── `ai-search-optimization`
├── `ai-seo`
├── `backlink-analyzer`
├── `competitor-alternatives`
├── `geo-aeo-optimization`
├── `keyword-cluster-builder`
├── `keyword-expansion`
├── `keyword-research`
├── `programmatic-seo`
├── `project-aeo-monitoring-tools`
├── `schema-markup`
├── `seo-audit`
├── `seo-backlink-strategy`
├── `seo-geo`
├── `seo-optimizer`
├── `seo`
├── `serp-analysis`
└── `site-architecture`

### Social Media (24)

├── `ai-social-media-content`
├── `community-architect`
├── `community-builder`
├── `community-building-strategist`
├── `community-building`
├── `linkedin-automation`
├── `linkedin-content`
├── `linkedin-personal-branding`
├── `linkedin-post-optimizer`
├── `linkedin`
├── `social-community`
├── `social-content`
├── `social-graphics`
├── `social-media-analyzer`
├── `social-media`
├── `social-repurposer`
├── `twitter-x`
├── `writing-linkedin-posts`
├── `x-impact-checker`
├── `youtube-plan-new-video`
├── `youtube-research-video-topic`
├── `youtube-video-analyst`
├── `youtube-video-hook`
└── `youtube`

### Strategy & Positioning (29)

├── `brand-messaging-architecture`
├── `branding`
├── `business-competitor-analysis`
├── `buyer-persona-generator`
├── `competitor-analysis`
├── `competitor-price-tracker`
├── `competitor-teardown`
├── `design-branding`
├── `go-to-market-planner`
├── `growth-product-manager`
├── `gtm-pricing`
├── `launch-strategy`
├── `market-research-reports`
├── `market-researcher`
├── `marketing-strategy-pmm`
├── `pitch-deck-visuals`
├── `pitch-deck`
├── `positioning-messaging`
├── `prd-v09-gtm-strategy`
├── `pricing-strategist`
├── `pricing-strategy`
├── `product-marketing-context`
├── `product-strategist`
├── `product-strategy`
├── `startup-go-to-market`
├── `storybrand-messaging`
├── `technical-launch-planner`
├── `webconsulting-branding`
└── `working-backwards`

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
