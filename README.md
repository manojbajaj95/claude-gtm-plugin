# GTM Skills

Go-to-market skills that turn Claude into a GTM specialist. 56 skills across SEO & AI search, content, outbound, sales, growth, analytics, strategy, ads, social, and CRM. Built for [Claude Code](https://claude.com/product/claude-code), also compatible with [Claude Cowork](https://claude.com/product/cowork) and any agent that supports the [Agent Skills spec](https://agentskills.io).

## Why This Plugin

Most AI assistants give generic marketing advice. This plugin gives Claude the frameworks, workflows, and domain knowledge of an experienced GTM team — so it can write copy in your voice, audit your SEO like a consultant, plan launches like a PMM, and build outbound sequences like an SDR.

The bootstrap skill interviews you once about your brand, audience, and voice, then generates a structured project folder that every skill reads before doing anything. The result: Claude doesn't just know marketing — it knows *your* marketing.

## Installation

### Claude Cowork

Install from the plugin marketplace at [claude.com/plugins](https://claude.com/plugins). Search for **GTM Skills**, click install, and the plugin is immediately available in your Cowork sessions.

### Claude Code

```bash
# Add the marketplace
claude plugin marketplace add manojbajaj95/claude-gtm-plugins

# Install all GTM skills
claude plugin install gtm-skills@claude-gtm-plugins
```

### Skills CLI

Use [npx skills](https://github.com/vercel-labs/skills) to install skills directly into any project:

```bash
# Install all skills
npx skills add manojbajaj95/claude-gtm-plugin

# Install specific skills
npx skills add manojbajaj95/claude-gtm-plugin --skill seo-and-aeo-strategy

# List available skills
npx skills add manojbajaj95/claude-gtm-plugin --list
```

### Clone and Load Locally

```bash
git clone https://github.com/manojbajaj95/claude-gtm-plugin.git
```

Then open Claude Code in the cloned directory — the plugin loads automatically.

### Git Submodule

Add as a submodule for easy updates:

```bash
git submodule add https://github.com/manojbajaj95/claude-gtm-plugin.git .agents/claude-gtm-plugin
```

## Getting Started

### Bootstrap Your Project

Ask Claude to bootstrap your project. Claude runs an agency-style onboarding interview — asking about your brand, audience, voice, and goals — then generates a structured project:

```
your-project/
├── CLAUDE.md                    # AI instructions: repo structure, naming, workflow, routing
├── about/
│   └── me.md                    # Personal voice, writing style, personality, biography
├── strategy/
│   └── brand.md                 # Brand positioning, messaging, audience, competitors, voice
├── content/
│   ├── ideas.md                 # Content idea backlog
│   ├── calendar.md              # Publishing schedule
│   ├── linkedin/
│   │   ├── drafts/              # Work-in-progress posts
│   │   └── published/           # Archive of published posts
│   ├── twitter/
│   │   ├── drafts/
│   │   └── published/
│   ├── reddit/
│   │   ├── drafts/
│   │   └── published/
│   ├── blog/
│   │   ├── drafts/
│   │   └── published/
│   └── email/
│       ├── drafts/
│       └── published/
└── assets/
    ├── logos/                    # Logo files
    └── brand/                   # Brand visual references
```

| Path | What it captures |
|---|---|
| `CLAUDE.md` | AI instructions — repo structure, what to read first, naming conventions, content workflow |
| `about/me.md` | Personal voice — your writing style, quirks, references, personality |
| `strategy/brand.md` | Brand identity — positioning, messaging, audience, competitors, voice guidelines |
| `content/` | Working content engine — ideas, calendar, drafts and published content per platform |
| `assets/` | Reusable visual assets — logos, brand files, visual references |

Content files follow the naming convention `YYYY-MM-DD_short-topic-slug.md`. Drafts live in `content/[platform]/drafts/` and move to `published/` once live.

Once bootstrapped, every skill reads the relevant context before doing anything. Claude works in your voice, for your brand, from day one. Ask Claude to bootstrap again to redo onboarding.

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

Skills cross-reference each other. Ask Claude to write a cold email and it pulls from your brand positioning (`strategy/brand.md`), your personal voice (`about/me.md`), and your ICP — not from a generic template.

## How It Works

```
claude-gtm-plugin/
├── .claude-plugin/          # Plugin manifest
├── skills/                  # All 56 skills in one flat directory
│   ├── bootstrap/
│   ├── seo-and-aeo-strategy/
│   ├── linkedin-content/
│   ├── copywriting-core/
│   └── ... (56 total)
└── scripts/                 # Build and validation
```

**Skills** are markdown files with YAML frontmatter that give Claude specialized knowledge for specific tasks. Claude activates them automatically when it detects a matching task — or you can invoke them directly.

Skills reference each other and build on the project structure created by the bootstrap skill. Ask Claude to write a cold email and it pulls from your brand positioning, your voice, and your ICP — not from a generic template.

## Skills

**56 skills** — all in one plugin, no sub-plugins to juggle.

See [ALL_SKILLS.md](ALL_SKILLS.md) for the complete list.

## Routing Rules

As you work with Claude, it routes new information to the right file automatically:

- Brand info (positioning, messaging, audience insights) → `strategy/brand.md`
- Personal info (writing preferences, quirks, reference examples) → `about/me.md`
- New content ideas → `content/ideas.md`
- Draft content → `content/[platform]/drafts/`
- Published content → `content/[platform]/published/`

## Validation

Skills follow the [Agent Skills specification](https://agentskills.io/specification). Run the validator to check all skills:

```bash
./validate-skills.sh
```

This checks frontmatter fields, naming conventions, description quality, and file structure against the official spec. See the [official reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) for the canonical implementation.

## Contributing

**We're actively looking for contributors!** Whether you're a marketer, growth hacker, SEO specialist, or just someone who uses Claude for GTM work — your expertise can help make these skills better for everyone.

### Ways to contribute

- **New skills** — Have a GTM workflow that Claude should know? Write it as a skill.
- **Improve existing skills** — Better frameworks, updated best practices, sharper prompts.
- **Fix incorrect advice** — Found a skill giving bad recommendations? [Open a bug report](https://github.com/manojbajaj95/claude-gtm-plugin/issues/new?template=bug_report.yml).
- **Add references** — Templates, examples, or supporting material for existing skills.
- **Documentation** — Improve READMEs, add examples, clarify instructions.

### How to contribute

1. Fork the repo
2. Create a branch (`git checkout -b my-skill`)
3. Make your changes — each skill lives in `skills/<skill-name>/SKILL.md`
4. Ensure valid YAML frontmatter with at least `name` and `description`
5. Run `./validate-skills.sh` to catch issues
6. Submit a PR

### Reporting issues

If a skill gives incorrect advice, fails to activate, or doesn't use your brand context properly — [file an issue](https://github.com/manojbajaj95/claude-gtm-plugin/issues/new?template=bug_report.yml). The more detail you include (skill name, what you asked, what happened vs. what you expected), the faster we can fix it.

## License

MIT
