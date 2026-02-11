# Customer Success

## Patterns


---
  #### **Name**
Activation Milestones
  #### **Description**
Define specific value moments users must hit to become activated
  #### **When**
Designing onboarding flows or measuring activation success
  #### **Example**
    Instead of: "User logged in = activated"
    Define specific value milestones:
    
    Slack: Team sent 2,000 messages
    Dropbox: User added 1 file from 1 device
    Superhuman: User processed inbox to zero once
    
    Benefits:
    - Clear target for onboarding design
    - Predictive of retention (activated users stay)
    - Actionable metric to optimize
    
    Track time-to-activation and activation rate. Both should trend down over time
    

---
  #### **Name**
Proactive Health Monitoring
  #### **Description**
Build health scores that predict churn before users decide to leave
  #### **When**
Designing customer success operations and intervention playbooks
  #### **Example**
    Health Score Components:
    1. Product usage (40%): DAU trend, feature adoption depth
    2. Support health (20%): Ticket volume, sentiment, unresolved issues
    3. Relationship (20%): Last CSM touch, executive engagement
    4. Business fit (20%): Growth trajectory, budget cycles
    
    Green (80-100): Expansion focus
    Yellow (60-79): Check-in call within 1 week
    Orange (40-59): Executive outreach, action plan
    Red (0-39): All-hands save attempt
    
    Validate score by checking correlation with actual churn. Iterate formula
    

---
  #### **Name**
Segmented Engagement
  #### **Description**
Design different CS motions for different customer segments
  #### **When**
Scaling customer success beyond one-size-fits-all approach
  #### **Example**
    Enterprise ($50K+ ARR):
    - Dedicated CSM
    - Quarterly business reviews
    - Custom onboarding
    - Executive relationship
    
    Mid-market ($5K-$50K ARR):
    - Pooled CSM (1:50 ratio)
    - Automated onboarding with human touchpoints
    - Health monitoring with proactive outreach
    
    Self-serve (<$5K ARR):
    - Fully automated sequences
    - In-app guidance
    - Help center, no human touch
    - Intervention only on high-fit leads
    

---
  #### **Name**
Time-to-Value Optimization
  #### **Description**
Ruthlessly reduce time from signup to first value moment
  #### **When**
Improving activation rates and reducing early churn
  #### **Example**
    Measure current time-to-value: 4 days from signup to activation
    
    Optimize:
    1. Remove friction: Reduce signup fields from 12 to 3
    2. Provide templates: Pre-populated examples vs blank slate
    3. Async setup: Let users explore while data imports
    4. Progressive disclosure: Don't teach everything upfront
    
    Result: Time-to-value reduced to 8 minutes
    Impact: Activation rate 23% → 47%
    
    Every minute matters. Measure and optimize aggressively
    

---
  #### **Name**
Leading Indicator Dashboards
  #### **Description**
Track metrics that predict future outcomes, not just outcomes
  #### **When**
Building CS dashboards and alert systems
  #### **Example**
    Lagging indicator: Churn rate (too late to act)
    
    Leading indicators:
    - Usage trend: DAU/WAU declining over 2 weeks
    - Feature adoption stagnation: No new features used in 30 days
    - Support sentiment: Negative CSAT in last 3 tickets
    - Login frequency drop: From daily to weekly
    
    Set up automated alerts when leading indicators decline.
    Intervene early, not at cancellation
    

---
  #### **Name**
Expansion Triggers
  #### **Description**
Identify behavioral signals that indicate expansion readiness
  #### **When**
Designing expansion playbooks and upsell motions
  #### **Example**
    Expansion triggers (automated detection):
    - Approaching plan limits (80% of seats, API calls, storage)
    - Power user behavior (daily usage, all features adopted)
    - Team growth (adding users, inviting colleagues)
    - Cross-sell signals (using integrations, exporting data)
    
    Playbook:
    1. Automated in-app nudge showing value of upgrade
    2. If no action in 7 days, CSM outreach with ROI case
    3. Offer trial of premium features
    
    Expansion should feel inevitable, not pushy
    

## Anti-Patterns


---
  #### **Name**
Onboarding as Checklist
  #### **Description**
Long list of tasks with no clear path to value
  #### **Why**
    15-step setup wizards overwhelm users. They give up before reaching value.
    Completion rates plummet. Most users never activate
    
  #### **Instead**
    Minimum viable onboarding to first value moment. Get users to "aha" in minutes,
    not hours. Use progressive disclosure - teach advanced features after activation
    

---
  #### **Name**
Vanity Health Scores
  #### **Description**
Health scores that look good but don't predict churn
  #### **Why**
    Score based on logins only ignores actual value delivery. Gives false confidence.
    Real churn signals missed. "Healthy" customers churn, surprise ensues
    
  #### **Instead**
    Validate health scores against actual churn data. Iterate formula until predictive.
    Include usage depth, not just frequency. Weight by correlation with retention
    

---
  #### **Name**
Spray and Pray Outreach
  #### **Description**
Mass emails that ignore customer context and lifecycle stage
  #### **Why**
    Same monthly newsletter to churning and expanding customers. Irrelevant noise.
    Users trained to ignore your emails. Unsubscribe rates increase
    
  #### **Instead**
    Segment by lifecycle stage and health score. Different messages for different
    states. Onboarding tips for new users, expansion offers for power users, win-back
    for dormant. Make every message relevant
    

---
  #### **Name**
Saving at Cancellation
  #### **Description**
Only trying to retain at the moment of churn decision
  #### **Why**
    Too late. Trust already eroded. Discount offers signal you were overcharging.
    Attracts price-sensitive customers who will churn again
    
  #### **Instead**
    Intervene early when health score declines. Build relationship before crisis.
    Proactive check-ins when usage drops. Solve problems before they become churn
    

---
  #### **Name**
Ignoring Power Users
  #### **Description**
All focus on at-risk customers, none on advocates
  #### **Why**
    Missed expansion revenue from happiest customers. Missed advocacy and referrals.
    Missed word-of-mouth growth. Squeaky wheel gets oil, happy users get ignored
    
  #### **Instead**
    Build advocacy program for happy customers. Make it easy to refer, review, share.
    Expansion conversations with power users. Feature beta access. Community programs
    

---
  #### **Name**
Generic Onboarding
  #### **Description**
Same onboarding flow for all users regardless of use case or experience
  #### **Why**
    Enterprise IT admin and solo freelancer get same experience. Wastes time,
    misses context. Generic advice doesn't help anyone
    
  #### **Instead**
    Segment onboarding by role, company size, use case. Ask 1-2 questions upfront,
    customize flow. Show enterprise features to enterprise users, simplicity to solo.
    Personalization drives activation
    