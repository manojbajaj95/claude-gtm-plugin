---
title: The FAQ Must Address What Makes You Uncomfortable
impact: HIGH
tags: faq, risk-analysis, honesty
---

## The FAQ Must Address What Makes You Uncomfortable

The FAQ exists to surface and address hard questions early. If your FAQ only contains softballs, you haven't done the hard thinking.

**Incorrect (softball FAQ):**

> **Internal FAQ:**
>
> Q: What resources do we need?
> A: One PM, two engineers, one designer.
>
> Q: What's the timeline?
> A: 6 months to launch.
>
> Q: How will we measure success?
> A: Customer satisfaction and usage metrics.
>
> Q: What are the dependencies?
> A: We'll work with the relevant teams.

*What's missing:* Every answer is vague and optimistic. There are no hard questions about why this might fail, what happens if dependencies slip, or why customers might not adopt this.

**Correct (hard-hitting FAQ):**

> **Internal FAQ:**
>
> Q: Why did our last two attempts at this problem fail?
> A: Attempt 1 (2019) failed because we underestimated integration complexity — it took 9 months instead of 3. Attempt 2 (2021) launched but saw only 2% adoption because we required customers to change their workflow. This attempt addresses both: we're using a different architecture that avoids the integration, and we're designing around existing workflows rather than requiring change.
>
> Q: What happens if the Platform team can't prioritize our API needs?
> A: This is our biggest risk. We have three mitigation paths: (1) we've already secured tentative Q2 commitment, (2) we have a fallback architecture that's less elegant but doesn't require them, (3) if neither works, we recommend killing the project rather than shipping a compromised version.
>
> Q: Why would customers use this instead of [competitor]?
> A: We don't win on features — [competitor] has more. We win on integration. 70% of our target customers already use Amazon for X, and our solution removes 3 hours/week of manual data sync. Competitor customers face a 6-week migration. Our bet: convenience beats features for this segment.
>
> Q: What if adoption is low in the first 90 days?
> A: Our kill criteria: if <5% of eligible customers activate in 90 days, we'll sunset the feature and reallocate the team. We won't invest in "fixes" without strong signal.

**Why it matters:**

Bill Carr describes the FAQ as the "legitimate plan to succeed" test. Jeff Bezos's three criteria include: "Is there a legitimate plan to succeed? You need to have all three of those things." A brilliant press release with a weak FAQ means you have an idea, not a product.
