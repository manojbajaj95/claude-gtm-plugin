# Product Market Fit - Sharp Edges

## Pmf Survey Misuse

### **Id**
pmf-survey-misuse
### **Summary**
Running PMF survey incorrectly
### **Severity**
high
### **Situation**
PMF survey gives misleading results
### **Why**
  Wrong respondents surveyed.
  Too few responses.
  Biased sample.
  
### **Solution**
  ## Correct PMF Survey Execution
  
  ### Common Mistakes
  
  | Mistake | Result |
  |---------|--------|
  | Survey all signups | Includes people who never tried |
  | Only survey power users | Inflates score |
  | Too few responses | No statistical validity |
  | Leading introduction | Biases responses |
  
  ### Correct Protocol
  
  ```
  1. Define eligible respondents:
     - Used product 2+ times
     - Active in last 14 days
     - Experienced core value proposition
  
  2. Reach sufficient sample:
     - Minimum: 40 responses
     - Better: 100+ responses
  
  3. Avoid bias:
     - Neutral survey introduction
     - Don't mention you hope for specific answer
     - Randomize option order if possible
  ```
  
  ### Sample Size by Stage
  
  | Company Stage | Minimum | Recommended |
  |---------------|---------|-------------|
  | Early (< 100 users) | 20-30 | All eligible |
  | Growing (100-1000) | 50 | 100 |
  | Scaling (1000+) | 100 | 200+ |
  
  ### Interpreting Results
  
  ```
  Score = (Very Disappointed / Total) × 100%
  
  <25%: Clear problem
  25-40%: Getting closer
  40%+: PMF signal
  
  But also segment:
  - Is there 40%+ in any segment?
  - What differentiates high-scorers?
  ```
  
### **Symptoms**
  - Survey score volatile
  - Results don't match reality
  - Can't act on results
### **Detection Pattern**
PMF survey|sean ellis|very disappointed

## Retention Misread

### **Id**
retention-misread
### **Summary**
Misinterpreting retention curves
### **Severity**
high
### **Situation**
Wrong conclusions from retention data
### **Why**
  Looking at wrong timeframe.
  Not cohorted properly.
  Not segmented.
  
### **Solution**
  ## Correct Retention Analysis
  
  ### Cohort Analysis Setup
  
  ```
  Cohort = Users who started in same time period
  
  Week 0: 100 users sign up
  Week 1: 40 return (40%)
  Week 2: 30 return (30%)
  Week 4: 20 return (20%)
  Week 8: 18 return (18%)
  Week 12: 17 return (17%) ← Flattening
  
  Compare cohorts over time.
  ```
  
  ### What to Look For
  
  | Pattern | Meaning |
  |---------|---------|
  | Drops to zero | No PMF |
  | Flattens at low % | Niche PMF |
  | Flattens at high % | Strong PMF |
  | Improves over time | Product getting better |
  | Worsens over time | PMF degrading |
  
  ### Common Misreads
  
  | Misread | Reality |
  |---------|---------|
  | "70% left after month 1" | 30% retained may be great |
  | "Retention is 50%" | Is that Day 1 or Month 6? |
  | "We have good retention" | Compared to what benchmark? |
  
  ### Segment Retention
  
  ```
  Don't just look at blended:
  
  Segment A: 35% Month 3 retention
  Segment B: 8% Month 3 retention
  Blended: 20% (misleading)
  
  Focus on Segment A!
  ```
  
  ### Retention Benchmarks
  
  | Category | Good M1 | Good M3 | Good M6 |
  |----------|---------|---------|---------|
  | Consumer social | 25% | 15% | 10% |
  | Consumer utility | 35% | 25% | 20% |
  | B2B SaaS | 50% | 35% | 30% |
  | Enterprise | 70% | 60% | 55% |
  
### **Symptoms**
  - Conflicting conclusions about retention
  - "Good" retention but poor business outcomes
  - No cohort analysis
### **Detection Pattern**
retention|cohort|churn

## Scaling Prematurely

### **Id**
scaling-prematurely
### **Summary**
Scaling growth before PMF confirmed
### **Severity**
high
### **Situation**
High CAC, poor retention, accelerating burn
### **Why**
  Pressure to show growth.
  Assumption of PMF.
  Investors expect scaling.
  
### **Solution**
  ## Pre-PMF vs Post-PMF Behavior
  
  ### Pre-PMF Rules
  
  ```
  DO:
  - Keep team small (≤10 people)
  - Conserve cash
  - Focus on retention, not acquisition
  - Talk to users constantly
  - Iterate quickly
  
  DON'T:
  - Hire aggressively
  - Spend on paid acquisition
  - Build for scale
  - Lock in long-term commitments
  ```
  
  ### PMF Confirmation Checklist
  
  Before scaling, confirm:
  - [ ] 40%+ "Very disappointed" (or equivalent)
  - [ ] Retention curve flattens at meaningful level
  - [ ] Can articulate why customers love it
  - [ ] Organic growth present
  - [ ] Repeat purchases / renewals healthy
  
  ### Scaling Readiness
  
  | Area | Pre-PMF | Post-PMF |
  |------|---------|----------|
  | Team | Founders + 5-10 | Start hiring |
  | Spend | Minimal marketing | Invest in acquisition |
  | Product | Rapid iteration | Stabilize and scale |
  | Process | Minimal | Build for scale |
  
  ### When Investors Push Scaling
  
  ```
  Response:
  "We're focused on retention metrics first.
   When we see [specific PMF signals],
   we'll be ready to scale efficiently.
   Scaling now would burn cash on leaky bucket."
  ```
  
### **Symptoms**
  - Burn rate increasing, retention poor
  - Growing team, shrinking efficiency
  - Investor pressure without metrics
### **Detection Pattern**
scaling|growth|team size|burn

## Segment Blindness

### **Id**
segment-blindness
### **Summary**
Missing segment-specific PMF
### **Severity**
medium
### **Situation**
Giving up when overall PMF is weak
### **Why**
  Looking only at aggregate data.
  Not segmenting users.
  Missing hidden success.
  
### **Solution**
  ## Finding Hidden Segment PMF
  
  ### Segmentation Process
  
  ```
  1. Collect user attributes:
     - Company size
     - Industry
     - Role
     - Use case
     - Acquisition source
     - Feature usage
  
  2. Run PMF analysis per segment
  
  3. Find 40%+ pockets
  ```
  
  ### Segment Discovery
  
  | Attribute | How to Get |
  |-----------|------------|
  | Company size | Enrichment (Clearbit) |
  | Industry | Sign-up question or enrichment |
  | Role | Sign-up question |
  | Use case | Onboarding question |
  | Behavior | Product analytics |
  
  ### Acting on Segment PMF
  
  ```
  When you find 40%+ segment:
  
  1. Profile them deeply
  2. Understand why they love it
  3. Find more like them
  4. Build for them specifically
  5. Temporarily ignore low-PMF segments
  ```
  
  ### Common Hidden Segments
  
  | You Thought | Actually |
  |-------------|----------|
  | "All SMBs" | Agencies specifically |
  | "Developers" | Solo developers, not teams |
  | "E-commerce" | Shopify stores <$1M/year |
  
  Focus beats breadth at this stage.
  
### **Symptoms**
  - Overall PMF weak
  - Some users love it, most don't
  - Can't explain who product is for
### **Detection Pattern**
segment|target|ICP

## Pmf Erosion Ignored

### **Id**
pmf-erosion-ignored
### **Summary**
Not noticing PMF degradation
### **Severity**
medium
### **Situation**
Once-strong PMF weakening
### **Why**
  Stopped measuring.
  Market changed.
  Product bloat.
  
### **Solution**
  ## Monitoring PMF Health
  
  ### Early Warning Signals
  
  | Signal | Meaning |
  |--------|---------|
  | Retention declining by cohort | Product or market degrading |
  | PMF score dropping | Value perception declining |
  | NPS declining | Satisfaction erosion |
  | Churn increasing | Competitive pressure |
  | Organic growth slowing | Word-of-mouth weakening |
  
  ### Continuous Monitoring
  
  ```
  Monthly:
  - Retention by cohort
  - Churn analysis
  - NPS score
  
  Quarterly:
  - PMF survey
  - Customer interviews
  - Competitive analysis
  
  Alert Thresholds:
  - PMF score drops 5+ points
  - Retention drops 10%+ vs prior cohort
  - NPS drops 10+ points
  ```
  
  ### Causes of PMF Erosion
  
  | Cause | Detection | Response |
  |-------|-----------|----------|
  | Competition improved | Win rate dropping | Differentiate or improve |
  | Market changed | Customer needs shifting | Rediscover needs |
  | Product bloat | Complexity complaints | Simplify |
  | Core neglected | Basics breaking | Refocus |
  
  ### Recovery Protocol
  
  1. Acknowledge erosion
  2. Interview churned customers
  3. Interview remaining loyal customers
  4. Identify what changed
  5. Return to pre-PMF mindset
  6. Iterate rapidly again
  
### **Symptoms**
  - We used to have such strong retention
  - New competitors winning deals
  - Customers less enthusiastic
### **Detection Pattern**
declining|erosion|lost PMF