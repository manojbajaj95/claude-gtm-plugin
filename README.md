# GTM Skills

Go-to-market skills that turn Claude into a GTM specialist. 62 skills across SEO & AI search, content, outbound, sales, growth, analytics, strategy, ads, social, and CRM — plus a `/bootstrap` command that onboards Claude to your brand, voice, and goals. Built for [Claude Code](https://claude.com/product/claude-code), also compatible with [Claude Cowork](https://claude.com/product/cowork) and any agent that supports the [Agent Skills spec](https://agentskills.io).

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
    ├── seo/                 # 2 skills
    ├── content/             # 9 skills
    ├── social/              # 15 skills
    ├── outbound/            # 1 skill
    ├── sales/               # 1 skill
    ├── growth/              # 18 skills
    ├── analytics/           # 4 skills
    ├── strategy/            # 8 skills
    ├── ads/                 # 2 skills
    └── crm/                 # 2 skills
```

**Skills** are markdown files with YAML frontmatter that give Claude specialized knowledge for specific tasks. Claude activates them automatically when it detects a matching task — or you can invoke them directly.

**Commands** are explicit actions you trigger. Currently: `/bootstrap`.

Skills reference each other and build on the context files created by `/bootstrap`. Ask Claude to write a cold email and it pulls from your brand positioning, your voice, and your ICP — not from a generic template.

## Skills

See [ALL_SKILLS.md](ALL_SKILLS.md) for the full 62-skill listing. Regenerate anytime with `scripts/generate-skills-readme.sh`.

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
