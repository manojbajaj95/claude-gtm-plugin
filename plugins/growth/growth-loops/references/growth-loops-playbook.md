# Growth Loops Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Core Insight: Loops vs. Funnels

Most growth thinking is **funnel thinking**: a linear path from acquisition to activation to retention. But funnels have a fundamental problem — they don't generate their own fuel. You have to keep pouring resources in at the top.

**Loops are different.** In a loop, the output of each cycle becomes the input for the next:

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────┐ │
│   │   NEW       │    │   VALUE     │    │ OUTPUT  │ │
└──►│   USER      │───►│  DELIVERY   │───►│ CREATES │─┘
    │   INPUT     │    │  (Product)  │    │ INPUT   │
    └─────────────┘    └─────────────┘    └─────────┘

    Example: Content Loop
    ┌──────────────────────────────────────────────────┐
    │                                                  │
    │   User        Creates       Content ranks       │
    └──►signs up ──► content ────► in Google ──────────┘
                                  (brings new users)
```

### Why This Matters

- **Funnels are linear**: $1 in → some users out → start over
- **Loops compound**: Each user generates a fraction of the next user
- **Funnels exhaust resources**: You can't scale indefinitely
- **Loops create sustainability**: Growth generates its own fuel

## The Three Types of Growth Loops

### 1. Viral Loops

Users invite or share with other users as part of getting value from the product.

**How it works:**
- User gets value from product
- To get more value, they invite/share with others
- Those others become new users
- Cycle repeats

**Examples:**
- Dropbox: Invite friends → get more storage
- Figma: Share designs → collaborators sign up
- Slack: Invite teammates → messaging works better

**Key metric:** Viral coefficient (K-factor) — how many new users does each user bring?

### 2. Content Loops

User activity creates content that attracts new users through search or discovery.

**How it works:**
- User creates content while using product
- Content gets indexed/discovered
- New users find content
- New users sign up and create more content

**Examples:**
- Pinterest: Users save pins → pins rank in Google → new users find pins
- Coda: Users create templates → templates shared publicly → new users copy templates
- Eventbrite: Creators make events → events rank in search → attendees discover events

**Key metric:** Content-to-signup conversion rate

### 3. Sales/Product-Led Sales Loops

Product usage creates qualified opportunities for sales conversations.

**How it works:**
- User signs up and uses product (self-serve)
- Usage signals indicate enterprise readiness (PQA)
- Sales engages based on usage data
- Closed deals → company-wide adoption → more usage signals

**Examples:**
- Amplitude: Individual PM uses analytics → team grows → enterprise conversation
- Miro: Designer creates boards → team collaborates → sales engages at 7+ users
- HubSpot: Marketer uses free tools → usage qualifies account → sales closes enterprise

**Key metric:** PQA (Product Qualified Account) conversion to closed-won

## Product-Led Sales: The Bridge

For B2B companies, there's often a bridge needed between product-led growth (self-serve) and enterprise sales. This is **Product-Led Sales (PLS)**.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  INDIVIDUAL     │     │     TEAM        │     │   ENTERPRISE    │
│  USE CASE       │────►│   ADOPTION      │────►│   VALUE PROP    │
│  (Self-serve)   │     │   (Organic)     │     │   (Sales-led)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘

 "I need data for   →   "My team uses    →   "Data-driven culture
  my decisions"          this now"            for our company"
```

### Key PLS Concepts

**PQA (Product Qualified Account):** An account that has reached usage thresholds indicating readiness for a sales conversation. Defined by:
- **Volume**: Number of users (magic number is often 7+)
- **Velocity**: Rate of change (sudden increase in users or usage)
- **Feature breadth**: Which features are being used
- **Behavioral signals**: Admin changes, pricing page visits, terms-of-use page views

**PQL (Product Qualified Lead):** An individual within a PQA who has decision-making power. Important distinction: most users are NOT buyers. In enterprise deals, you often need to find the buyer outside your user base.

**The $10K ceiling:** Self-serve monetization caps around $10,000 (credit card limits, willingness to pay). Above that, you need sales to tell the enterprise story.

## Platform Cycles: A Special Case

New distribution platforms (like Facebook in 2007, iOS App Store, SEO, and potentially ChatGPT) follow a predictable four-step cycle:

### Step 0: Competitive Market
- Multiple players battling for dominance
- No clear winner yet
- High stakes = fierce competition

### Step 1: Moat + Platform Opening
- Winner identifies their moat (data, network effects, engagement)
- Opens platform to third parties
- Value exchange: "Build on us, we give you distribution"

### Step 2: Growth Phase
- Third parties flood in
- Platform grows rapidly
- Early movers get disproportionate distribution

### Step 3: Platform Closing
- Platform monetizes or protects itself
- Organic distribution suppressed
- Push toward paid mechanisms or first-party alternatives

**The key insight:** You cannot opt out of this game. If you don't play, competitors will. It's a prisoner's dilemma.

**Current prediction (2024-2025):** ChatGPT is likely the next major distribution platform. Signals: agent platform hiring, preferred partnerships, context/memory as moat.

## How to Build Your Growth Loop

### Step 1: Identify Your Loop Type

Ask yourself:
- Does your product naturally involve sharing or inviting others? → Viral loop
- Does usage create discoverable content? → Content loop
- Does individual usage signal enterprise value? → Sales loop
- Can you build on an emerging platform? → Platform loop

### Step 2: Map the Complete Cycle

For each loop, identify:
1. **Input**: What starts the cycle? (new user, new content, usage signal)
2. **Action**: What do users do that creates output?
3. **Output**: What does that action produce?
4. **Connection**: How does output become input for the next cycle?

### Step 3: Measure the Efficiency

Key metrics by loop type:
- **Viral**: K-factor (users generated per user)
- **Content**: Content → visit → signup conversion
- **Sales**: PQA → opportunity → closed-won rate
- **Platform**: Distribution per integration

### Step 4: Optimize Each Step

Don't optimize randomly. Identify the weakest link:
- Not enough content being created? → Improve creation UX
- Content not ranking? → Improve SEO fundamentals
- Users not inviting? → Make sharing more valuable
- PQAs not converting? → Better sales enablement

## Common Mistakes

### 1. Treating paid acquisition as a loop
Paid growth doesn't compound. Every dollar you spend buys users, but those users don't generate the next dollar. It's a treadmill, not an engine.

### 2. Hiring a growth team before product-market fit
You cannot outsource finding your growth model. Founders must lead the first wave. Growth teams optimize and scale existing loops — they don't create them from nothing.

### 3. Expecting loops to work without product-market fit
Loops amplify what's already working. If your product doesn't retain, loops just accelerate churn. Fix retention first.

### 4. Over-investing in paid vs. earned channels
The ratio should be ~80% earned/owned (virality, content, product loops) and ~20% paid. Most companies invert this.

### 5. Thinking one channel will last forever
Every channel saturates. Every platform closes. Plan for 18-month cycles and always be testing the next loop.

### 6. Focusing on volume instead of velocity
Sudden changes in growth rate are more predictive than absolute numbers. Track velocity, not just volume.

## Applying Growth Loops: A Checklist

### For Startups (Pre-PMF)
- [ ] What loop is inherent to the product concept?
- [ ] How will usage naturally generate more users?
- [ ] What non-scalable "kindle" tactics unlock the scalable "fire"?
- [ ] Is the founder leading growth, not delegating it?

### For Growth Teams
- [ ] Which loop is our primary engine? (One will dominate)
- [ ] What percentage of effort goes to earned vs. paid?
- [ ] Do we have PQA definitions that sales agrees with?
- [ ] What's the weakest step in our primary loop?

### For Product Teams
- [ ] Does product own pipeline metrics (PQA), not just engagement?
- [ ] How does our product create discoverable content or sharing?
- [ ] What behavioral signals indicate enterprise readiness?
- [ ] Are we designing features for loop contribution, not just usage?

### For B2B Companies
- [ ] What's our individual use case vs. enterprise value prop?
- [ ] At what usage threshold should sales engage? (Often 7+ users)
- [ ] Do we have buyers in our user base, or do we need to find them?
- [ ] How long does it take from signup to enterprise conversation? (Often 12+ months)

### For Platform Bets
- [ ] Which platforms are in "opening" phase?
- [ ] What's the retention/engagement data? (Better predictor than MAU)
- [ ] Can we place focused bets, not spread thin?
- [ ] What's our exit strategy when the platform closes?

## Quick Reference

**The core idea:** Build systems where output becomes input. Each cycle should fuel the next.

**Loop types:** Viral (users invite users), Content (usage creates discoverable content), Sales (usage creates qualified pipeline)

**Product-led sales:** The bridge between self-serve usage and enterprise deals. Product qualifies accounts; sales closes them.

**Platform cycles:** Open → build → close → monetize. Get in early, plan your exit.

**Key metrics:**
- Viral: K-factor
- Content: Content-to-signup rate
- Sales: PQA-to-closed-won rate
- Overall: Time to first loop completion

**The ratio:** 80% earned/owned channels, 20% paid. Most companies get this backwards.

---

