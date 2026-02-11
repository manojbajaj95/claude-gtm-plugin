# Working Backwards Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Core Insight: Customer Problem First

The fundamental shift in Working Backwards is starting from a different place.

**Working Forward (typical approach):**
```
We have this technology → What can we build? → Who might use it?
```

**Working Backwards (Amazon approach):**
```
Customer has this problem → What's the ideal solution? → How do we build it?
```

Ian McAllister, who spent 12 years at Amazon, describes the key failure mode: "When teams do it wrong, they don't work backwards. They have something they want to build... and if you say 'we could' and it's not grounded in a customer or customer's problem, you're not working backwards."

**The test:** If your project's internal name describes the technology rather than the customer benefit, you're probably working forward, not backward.

- Working forward: "ASIN-to-ASIN linking project"
- Working backwards: "Help customers discover related products they'll love"

## The PR/FAQ Document

The mechanism that enforces Working Backwards is the **internal press release and FAQ**. This is not a real press release — it's a thinking tool.

### The Press Release Structure

**Headline:** One sentence that captures what you're launching and for whom.

**Subheadline:** One sentence expanding on the value proposition.

**Date and Location:** The hypothetical launch date and city. The date signals scope — next month (simple) vs. a year from now (complex).

**First Paragraph:** Brief description of the product and who it's for.

**Problem Paragraph:** What problem does the customer have? This is the most important paragraph. As Jeff Bezos told one PM: "Maybe if you don't have a problem paragraph, there's not really a problem."

**Solution Paragraph:** How does this product solve the problem? Focus on the customer outcome, not the technology.

**Customer Quote:** A hypothetical quote from a customer explaining why they value this. If you can't write a convincing quote, you don't understand the customer.

**How to Get Started:** What does the customer do next?

**Company Quote:** A hypothetical quote from a company leader explaining why this matters.

### The FAQ Structure

The FAQ comes after the press release and is typically longer. It has two sections:

**External FAQ (Customer Questions):**
- How does it work?
- How much does it cost?
- What do I need to get started?
- How is this different from [competitor/alternative]?

**Internal FAQ (Stakeholder Questions):**
- What's the business model?
- What resources do we need?
- What are the key technical challenges?
- What are the dependencies?
- How will we measure success?
- What are the risks?

**The FAQ's purpose:** Surface and address the hard questions early. Bill Carr explains it as the "legitimate plan to succeed" test. A great press release with a weak FAQ means you have an idea, not a product.

## The Three Tests

Jeff Bezos shared three criteria for investing in something new:

### 1. Is it a Big Idea?
Does solving this problem create meaningful value? Small ideas aren't worth the coordination cost.

### 2. Is it Something We Should Be Doing?
An idea can be big but wrong for your company. A new way to extract oil from shale might be big, but it's not something Amazon should do.

### 3. Is There a Legitimate Plan to Succeed?
The FAQ addresses this. You need to have thought through the finances, technical hurdles, dependencies, and path to market. A brilliant concept without a viable path is just a concept.

**You need all three.** Most failed products fail on #3 — they were big ideas that the company should pursue, but there wasn't a realistic plan.

## The Concentric Circle Review

PR/FAQs aren't written once and approved. They go through iterative review:

```
    ┌─────────────────────────────────────────────┐
    │                                             │
    │     ┌─────────────────────────────────┐     │
    │     │                                 │     │
    │     │     ┌───────────────────┐       │     │
    │     │     │                   │       │     │
    │     │     │   Author writes   │       │     │
    │     │     │   first draft     │       │     │
    │     │     │                   │       │     │
    │     │     └─────────┬─────────┘       │     │
    │     │               │                 │     │
    │     │    Small team review            │     │
    │     │    (refine, improve)            │     │
    │     │                                 │     │
    │     └───────────────┬─────────────────┘     │
    │                     │                       │
    │          Wider team review                  │
    │          (cross-functional input)           │
    │                                             │
    └─────────────────────┬───────────────────────┘
                          │
               Leadership review
               (approval to proceed)
```

**Key insight:** Not every PR/FAQ makes it to leadership. Many are "crumpled up and thrown in the trash" after the author realizes the idea isn't compelling on paper, or after small group feedback reveals fatal flaws.

Bill Carr: "You're a product manager and you write 100 PR/FAQs in a year, maybe 20 of those make their way to the CEO. You're really trying to create a product funnel, not a product tunnel."

This is the point. The process is designed to kill weak ideas early, before you've spent engineering resources.

## Writing the Press Release: Guidelines

### Be Specific About the Customer

Don't write for "everyone" or "all businesses." Define exactly who has this problem.

**Weak:** "Amazon announces a new tool for businesses."

**Strong:** "Amazon announces a new tool for e-commerce merchants with 10-100 SKUs who struggle to keep inventory in sync across multiple sales channels."

### Ground the Problem in Reality

The problem paragraph should feel urgent and real. If it sounds like marketing copy, rewrite it.

**Weak:** "Today's businesses need better collaboration tools to thrive in the modern economy."

**Strong:** "Small e-commerce teams waste an average of 12 hours per week manually updating inventory across Amazon, Shopify, and eBay. When they miss an update, they oversell — leading to canceled orders, angry customers, and damaged seller ratings."

### No Jargon, No Hyperbole

Press releases are written as if for external consumption. Use plain language. Avoid superlatives unless you can back them up.

**Avoid:** "Revolutionary," "game-changing," "best-in-class," "leveraging synergies"

**Prefer:** Specific numbers, concrete outcomes, clear before/after comparisons

### One Benefit, One Press Release

If you find yourself listing multiple major benefits, you probably have multiple ideas. Split them into separate PR/FAQs and evaluate each independently.

### Include What You Would Measure

Even in the press release, hint at measurable outcomes: "Customers will save an average of 10 hours per week..." or "Sellers using the tool see a 25% reduction in oversells..."

## Writing the FAQ: Guidelines

### Address the Uncomfortable Questions

The FAQ is where you prove you've thought this through. Include the questions that make you squirm:

- "What if customers don't want to pay for this?"
- "How is this different from the three failed attempts we've already made?"
- "What happens when [big competitor] copies us in 6 months?"
- "Why would the team who owns [dependency] prioritize our integration?"

### Separate External and Internal

External FAQ questions come from customers. Internal FAQ questions come from stakeholders, engineers, finance, and leadership.

External: "How does pricing work?"
Internal: "What's the unit economics at scale?"

### Show the Plan, Not Just the Vision

The internal FAQ should include:
- Resource requirements (headcount, budget, timeline)
- Key technical challenges and proposed approaches
- Dependencies on other teams
- Go-to-market approach
- Success metrics and targets
- Known risks and mitigations

## Common Mistakes

### 1. Writing the PR/FAQ After You've Already Decided
The process only works if you're genuinely open to killing the idea. Writing a PR/FAQ to justify a decision already made is theater.

### 2. Skipping the Problem Paragraph
If you can't articulate the customer problem clearly and compellingly, you probably don't have a product worth building.

### 3. Solution-First Thinking
"We have these two technologies — what if we combined them?" is not Working Backwards. Start with the customer problem, not your capabilities.

### 4. Making the Customer Quote Sound Corporate
The customer quote should sound like something a real person would say. If it sounds like marketing wrote it, you don't understand your customer.

### 5. FAQ That Avoids Hard Questions
If your FAQ only contains softballs, you haven't done the hard thinking. The FAQ should make you uncomfortable.

### 6. Treating It as Documentation
The PR/FAQ is a decision-making tool, not documentation. It's meant to force thinking *before* building, not capture decisions after.

## Applying Working Backwards: Checklists

### Before Writing the PR/FAQ
- [ ] Do I understand the customer problem from real customer research?
- [ ] Can I describe who the customer is specifically (not "everyone")?
- [ ] Am I genuinely open to killing this idea?
- [ ] Is this big enough to warrant a PR/FAQ?

### Reviewing the Press Release
- [ ] Is the headline clear and specific?
- [ ] Does the problem paragraph feel urgent and real?
- [ ] Is the customer specifically defined?
- [ ] Is the solution paragraph focused on outcomes, not technology?
- [ ] Does the customer quote sound like a real person?
- [ ] Are there concrete, measurable claims?
- [ ] Is it free of jargon and hyperbole?
- [ ] Could someone outside the company understand it?

### Reviewing the FAQ
- [ ] Does the external FAQ answer what customers would actually ask?
- [ ] Does the internal FAQ address uncomfortable questions?
- [ ] Is there a realistic resource and timeline estimate?
- [ ] Are dependencies and risks identified?
- [ ] Are success metrics defined?
- [ ] Is there a legitimate plan to succeed, not just a vision?

### After the Review
- [ ] Did you incorporate feedback and iterate?
- [ ] Did you consider killing the idea if feedback was consistently negative?
- [ ] Is there clear approval to proceed (or a clear decision not to)?

## Quick Reference

**The core idea:** Start with the customer problem and work backward to the solution. Write the press release before you build anything.

**The document:** Internal press release + FAQ. The PR forces clarity on what and why. The FAQ forces clarity on how and whether.

**The test (from Jeff Bezos):**
1. Is it a big idea?
2. Is it something we should be doing?
3. Is there a legitimate plan to succeed?

**When to use it:** New products, major features, strategic initiatives. Not bug fixes or A/B tests.

**The review process:** Start with the author, expand to small team, then wider team, then leadership. Many ideas die before reaching the top — that's the point.

**Success indicator:** If you can't write a compelling press release, you don't have a compelling product.

---

