---
title: External and Internal FAQs Serve Different Purposes
impact: MEDIUM
tags: faq, structure, completeness
---

## External and Internal FAQs Serve Different Purposes

The FAQ has two sections that serve completely different audiences. Treating them the same — or skipping one — undermines the document's value.

**Incorrect (merged or incomplete FAQ):**

> **FAQ:**
>
> Q: How does it work?
> A: The feature automatically syncs your inventory across channels.
>
> Q: How much does it cost?
> A: Pricing will be determined closer to launch.
>
> Q: What resources do we need?
> A: 2 engineers and 1 PM.
>
> Q: What are the risks?
> A: We'll work through any issues as they arise.
>
> *What's wrong:* This mixes customer questions and internal questions without clear separation. The internal questions are answered with hand-waves. There's no depth.

**Correct (structured and complete FAQ):**

> **External FAQ (Customer Questions):**
>
> Q: How does it work?
> A: Connect your Amazon, Shopify, and eBay accounts. The system reads your inventory every 60 seconds and pushes updates to all channels within 5 minutes. You'll see a dashboard showing sync status and any conflicts.
>
> Q: How much does it cost?
> A: Free for sellers with under 50 SKUs. $29/month for 50-500 SKUs. Enterprise pricing for 500+ SKUs (contact sales).
>
> Q: What if there's a sync conflict?
> A: The system alerts you via email and dashboard. You can set rules for automatic resolution (e.g., "lowest count wins") or manually resolve each case.
>
> Q: Does it work with other channels?
> A: At launch: Amazon, Shopify, eBay, Walmart. Additional channels in H2: Etsy, WooCommerce, BigCommerce.
>
> ---
>
> **Internal FAQ (Stakeholder Questions):**
>
> Q: What resources are required?
> A: Phase 1 (MVP): 4 engineers, 1 PM, 0.5 designer for 4 months. Phase 2 (additional channels): 2 engineers for 3 months.
>
> Q: What are the key technical risks?
> A: Rate limiting from partner APIs. Mitigation: We've tested sustainable polling rates. Shopify limits us to 2 calls/second; we've designed batching to stay under this.
>
> Q: Why will this succeed when InventoryLab and Sellbrite already exist?
> A: [Detailed competitive analysis with specific differentiators]
>
> Q: What are the dependencies?
> A: Payments team for billing infrastructure (committed for Q2). No other external dependencies.
>
> Q: What's the business case?
> A: [Detailed revenue projection, cost analysis, break-even timeline]

**Why it matters:**

External FAQ answers ensure you've thought through the customer experience. Internal FAQ answers ensure you've thought through the business viability. Skipping either means you're presenting an incomplete picture — and will face those questions unprepared in leadership review.
