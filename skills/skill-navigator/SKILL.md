---
name: skill-navigator
description: Use this skill when you need guidance on which skill to use for any task. Recommends the perfect skill, creates skill combinations, and helps you discover capabilities you didn't know you had.
---

# Skill Navigator

## Workspace Context

Read bootstrap context before asking questions: `strategy/brand.md` for brand, audience, offer, channels, tools, constraints, and metrics; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` for content planning. Use legacy product-marketing context files only as fallback. Save generated drafts to `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md`, and route durable learnings back to `strategy/brand.md`, `about/me.md`, or `content/ideas.md`.

## Operating Contract

This skill is self-contained for its frontmatter scope: use its local instructions, references, scripts, and assets as the playbook; ask only for missing task-specific inputs; hand off to adjacent skills instead of expanding scope; and return an actionable artifact, decision, plan, draft, or diagnostic.


Guide users to the right GTM plugin skill for the task at hand. Recommend one primary skill, optional supporting skills, and copy-paste prompts that fit this repository's actual skill set.

## Instructions

When a user describes what they want to accomplish:

1. Identify the best primary skill from the local `skills/` directory.
2. Suggest at most 2 supporting skills for multi-step workflows.
3. Explain the handoff order in plain language.
4. Provide one copy-paste prompt for the recommended next step.
5. Avoid recommending skills that are not present in this plugin.

Use the current plugin vocabulary: `marketing-strategy`, `brand-messaging-and-positioning`, `go-to-market-strategy`, `content-strategy-and-planning`, `content-creation-and-marketing`, `seo-and-aeo-strategy`, `keyword-research-and-clustering`, `copywriting-core`, `linkedin`, `newsletter-management`, `outbound-email-strategy`, `marketing-automation`, `lead-generation-and-demand`, `sales-and-revenue-operations`, `pricing-strategy`, `conversion-rate-optimization`, `ab-test-setup`, `data-and-funnel-analytics`, `customer-success-and-retention`, `community-building`, `product-market-fit-analysis`, `product-hunt-launch`, `ph-community-outreach`, `ph-content-recycling`, `youtube-research`, `youtube-content`, `webinar-content-and-events`, `pitch-deck-creation`, `slide-outline`, `issue-reporting`, and adjacent local skills.

### Output Format

```markdown
# Skill Navigator Output

## Recommended Skill
[primary skill and why]

## Supporting Skills
[0-2 supporting skills and when to use them]

## Suggested Workflow
[ordered steps]

## Copy-Paste Prompt
[one prompt the user can run next]

```

### Best Practices

1. **Be Specific**: Focus on concrete, actionable outputs
2. **Use Templates**: Provide copy-paste ready formats
3. **Include Examples**: Show real-world usage
4. **Add Context**: Explain why recommendations matter
5. **Stay Current**: Use latest best practices for meta

### Common Use Cases

**Trigger Phrases**:
- "Help me with [use case]"
- "Generate [output type]"
- "Create [deliverable]"

**Example Request**:
> "[Sample user request here]"

**Response Approach**:
1. Understand user's context and goals
2. Generate comprehensive output
3. Provide actionable recommendations
4. Include examples and templates
5. Suggest next steps

Remember: Focus on delivering value quickly and clearly!
