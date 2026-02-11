# Product-Market Fit

## Patterns


---
  #### **Name**
PMF Measurement Framework
  #### **Description**
How to measure product-market fit
  #### **When To Use**
Assessing current PMF status
  #### **Implementation**
    ## PMF Measurement
    
    ### 1. Sean Ellis Survey
    
    **The Question**
    "How would you feel if you could no longer use [product]?"
    
    **Response Options**
    - Very disappointed
    - Somewhat disappointed
    - Not disappointed
    - N/A - I no longer use
    
    **PMF Threshold**
    - 40%+ "Very disappointed" = PMF signal
    - 25-40% = Getting closer
    - <25% = Not there yet
    
    **Who to Survey**
    - Active users only
    - Used product 2+ times
    - Used in last 2 weeks
    - Target: 40-50 responses minimum
    
    ### 2. Retention Metrics
    
    ```
    Cohort Retention Analysis
    
    Week | Users | Retained | Rate
    0    | 1000  | 1000     | 100%
    1    | 1000  | 400      | 40%
    4    | 1000  | 200      | 20%
    8    | 1000  | 150      | 15%
    12   | 1000  | 140      | 14% ← Flattening = good
    
    Look for: Curve flattening, not dropping to zero
    ```
    
    **Retention Benchmarks**
    
    | Category | Good Week 1 | Good Month 3 |
    |----------|-------------|--------------|
    | Consumer | 25%+ | 10%+ |
    | SaaS B2B | 40%+ | 25%+ |
    | Enterprise | 60%+ | 50%+ |
    
    ### 3. NPS as PMF Indicator
    
    ```
    Net Promoter Score
    
    Promoters (9-10): Would recommend
    Passives (7-8): Neutral
    Detractors (0-6): Would not recommend
    
    NPS = % Promoters - % Detractors
    
    PMF signal: NPS > 40
    ```
    
    ### 4. Organic Growth Signals
    
    | Signal | PMF Indicator |
    |--------|---------------|
    | Word-of-mouth referrals | Strong pull |
    | Organic traffic growing | Market seeking you |
    | Low churn despite price increases | Value exceeds price |
    | Users returning without prompts | Habit formation |
    
    ### 5. Revenue PMF Signals
    
    ```
    For paid products:
    
    - Net Revenue Retention > 100% (expansions > churn)
    - Logo Churn < 5% monthly (B2C) or 2% (B2B)
    - Customers paying before fully using
    - Price increases don't cause churn
    ```
    

---
  #### **Name**
Pre-PMF Strategy
  #### **Description**
What to do before PMF
  #### **When To Use**
When PMF not yet achieved
  #### **Implementation**
    ## Pre-PMF Playbook
    
    ### 1. Pre-PMF Priorities
    
    ```
    Focus Order:
    1. Learn (customer conversations, experiments)
    2. Iterate (quick product changes)
    3. Measure (retention, engagement)
    4. Repeat
    
    NOT:
    - Scale
    - Hire aggressively
    - Heavy marketing spend
    ```
    
    ### 2. The PMF Search Process
    
    ```
    Phase 1: Problem Validation
    - Is this a real problem?
    - Do people care enough?
    - Are they actively solving it?
    
    Phase 2: Solution Validation
    - Does our solution work?
    - Is it better than alternatives?
    - Will they pay/switch?
    
    Phase 3: Scale Validation
    - Can we acquire efficiently?
    - Does retention hold at scale?
    - Is the market big enough?
    ```
    
    ### 3. Segment Focus
    
    **Start Narrow**
    ```
    Instead of: "We serve all SMBs"
    Try: "We serve 10-person marketing agencies in Texas"
    
    Find PMF in segment, then expand.
    ```
    
    **Segment Selection Criteria**
    - Acute pain
    - Can reach them
    - They can pay
    - They can decide quickly
    - You understand them
    
    ### 4. Pre-PMF Metrics
    
    | Metric | Why It Matters |
    |--------|----------------|
    | Week 1 retention | Early engagement |
    | Activation rate | Value delivered |
    | Time to value | Onboarding quality |
    | NPS of core users | Satisfaction depth |
    | Repeat usage | Habit formation |
    
    ### 5. Iteration Speed
    
    ```
    Pre-PMF cadence:
    - Ship updates weekly
    - Talk to users daily
    - Measure weekly
    - Pivot when needed
    
    Speed of iteration = Speed of learning
    ```
    
    ### 6. Founder-Market Fit Check
    
    Before blaming product, check:
    - Do we deeply understand the problem?
    - Are we talking to the right customers?
    - Do we have unfair insights?
    - Are we the right team for this problem?
    

---
  #### **Name**
PMF Survey Methodology
  #### **Description**
Running the PMF survey properly
  #### **When To Use**
Measuring PMF quantitatively
  #### **Implementation**
    ## PMF Survey Guide
    
    ### 1. Survey Design
    
    **Core Question (Required)**
    "How would you feel if you could no longer use [Product]?"
    
    **Follow-Up Questions (Optional but valuable)**
    - "What is the main benefit you receive?"
    - "What type of person would benefit most?"
    - "How can we improve?"
    
    ### 2. Respondent Criteria
    
    ```
    Include:
    - Used product 2+ times
    - Active in last 14 days
    - Experienced core value
    
    Exclude:
    - Signed up but never used
    - Used once and left
    - Inactive for 30+ days
    ```
    
    ### 3. Sample Size
    
    | Confidence | Sample Needed |
    |------------|---------------|
    | Directional | 30-40 |
    | Solid | 100-150 |
    | Statistical | 200+ |
    
    ### 4. Segment Analysis
    
    ```
    Run survey, then segment by:
    - Use case
    - User type
    - Acquisition source
    - Company size
    - Feature usage
    
    Often: 40%+ PMF in segment, <40% overall
    → Focus on that segment
    ```
    
    ### 5. Survey Cadence
    
    | Stage | Frequency |
    |-------|-----------|
    | Pre-PMF | Monthly |
    | Approaching PMF | Bi-weekly |
    | Post-PMF | Quarterly |
    
    ### 6. Acting on Results
    
    **"Very disappointed" users:**
    - Interview to understand why
    - Find common patterns
    - Build for them
    
    **"Somewhat disappointed" users:**
    - What's missing?
    - What would make them "very"?
    - Quick wins available?
    
    **"Not disappointed" users:**
    - Why are they using?
    - Wrong segment?
    - Education gap?
    

---
  #### **Name**
Post-PMF Strategy
  #### **Description**
What changes after achieving PMF
  #### **When To Use**
After PMF confirmed
  #### **Implementation**
    ## Post-PMF Playbook
    
    ### 1. Recognizing PMF
    
    ```
    You likely have PMF when:
    - 40%+ "Very disappointed" survey score
    - Retention curve flattens
    - Organic growth accelerating
    - Customers pulling for features
    - Hard to keep up with demand
    ```
    
    ### 2. Post-PMF Priorities Shift
    
    | Pre-PMF | Post-PMF |
    |---------|----------|
    | Learn | Scale |
    | Iterate | Systemize |
    | Measure retention | Measure growth |
    | Conserve cash | Invest in growth |
    | Do things that don't scale | Build for scale |
    
    ### 3. Scaling Carefully
    
    ```
    Post-PMF risks:
    - Scaling too fast → Culture breaks
    - Hiring too fast → Quality drops
    - New segments → Lose focus
    - Feature bloat → Dilute PMF
    
    Scale the things that created PMF.
    ```
    
    ### 4. Maintaining PMF
    
    ```
    PMF can erode through:
    - Market changes
    - Competitor improvement
    - Product bloat
    - Customer base shift
    - Neglecting core users
    
    Keep measuring, even post-PMF.
    ```
    
    ### 5. Expanding PMF
    
    ```
    Expand to adjacent segments:
    
    1. Identify adjacent segment
    2. Test PMF in that segment
    3. If PMF: expand
    4. If not: stay focused
    
    Don't assume PMF transfers.
    ```
    
    ### 6. Post-PMF Metrics
    
    | Metric | Why |
    |--------|-----|
    | Net Revenue Retention | Growth efficiency |
    | CAC payback | Acquisition efficiency |
    | Logo retention | Core health |
    | PMF survey score | Ongoing monitoring |
    

---
  #### **Name**
Segment-Specific PMF
  #### **Description**
Finding PMF in narrow segments
  #### **When To Use**
When overall PMF is weak but segments may be strong
  #### **Implementation**
    ## Segment PMF Analysis
    
    ### 1. Why Segment
    
    ```
    Overall: 25% "Very disappointed" (No PMF)
    
    But when segmented:
    - Enterprise: 15% (No PMF)
    - SMB: 22% (No PMF)
    - Agencies: 48% (PMF!)
    
    You have PMF - just not where you thought.
    ```
    
    ### 2. Segmentation Dimensions
    
    | Dimension | Examples |
    |-----------|----------|
    | Company size | SMB, Mid-market, Enterprise |
    | Industry | SaaS, E-commerce, Healthcare |
    | Role | Developer, Marketer, Executive |
    | Use case | Collaboration, Analytics, Automation |
    | Acquisition | Organic, Paid, Referral |
    | Geography | Region, Country |
    
    ### 3. Finding Your Strongest Segment
    
    ```
    Process:
    1. Run PMF survey
    2. Segment responses
    3. Find 40%+ segment
    4. Profile that segment deeply
    5. Double down on that segment
    ```
    
    ### 4. ICP Refinement
    
    ```
    From segment analysis:
    
    Ideal Customer Profile:
    - Industry: [Specific]
    - Size: [Specific range]
    - Role: [Specific title]
    - Pain: [Specific problem]
    - Behavior: [How they act]
    ```
    
    ### 5. Segment Expansion Strategy
    
    ```
    1. Dominate core segment (PMF)
    2. Identify adjacent segment
    3. Test PMF in adjacent
    4. If PMF: expand
    5. If not: return to core
    6. Repeat
    
    Concentric circles from strong PMF outward.
    ```
    

## Anti-Patterns


---
  #### **Name**
Vanity Metrics as PMF
  #### **Description**
Mistaking growth for product-market fit
  #### **Why Bad**
    Growth can be bought.
    Retention reveals truth.
    False confidence leads to scaling failure.
    
  #### **What To Do Instead**
    Focus on retention metrics.
    Run PMF survey.
    Track repeat usage, not just signups.
    

---
  #### **Name**
Scaling Before PMF
  #### **Description**
Investing in growth before product-market fit
  #### **Why Bad**
    Accelerating failure.
    Burning cash inefficiently.
    Technical debt from scaling.
    
  #### **What To Do Instead**
    Validate PMF first.
    Stay lean until retention holds.
    Scale what works.
    

---
  #### **Name**
Premature Market Expansion
  #### **Description**
Expanding to new segments before dominating core
  #### **Why Bad**
    Lose focus on what works.
    Dilute PMF.
    Confuse product direction.
    
  #### **What To Do Instead**
    Dominate one segment.
    Expand from strength.
    Test PMF in new segments.
    

---
  #### **Name**
Feature-Market Fit Confusion
  #### **Description**
Believing features create PMF
  #### **Why Bad**
    Features ≠ fit.
    More features can dilute fit.
    Core value matters most.
    
  #### **What To Do Instead**
    PMF comes from solving core problem well.
    Features support, not create, PMF.
    Simplicity often wins.
    

---
  #### **Name**
Ignoring PMF Loss
  #### **Description**
Not noticing PMF degradation
  #### **Why Bad**
    Markets change.
    Competitors improve.
    PMF can erode.
    
  #### **What To Do Instead**
    Continuous PMF measurement.
    Watch retention trends.
    Stay connected to customers.
    