# Customer Success - Sharp Edges

## Onboarding Abandonment

### **Id**
onboarding-abandonment
### **Summary**
Complex onboarding that users never complete
### **Severity**
critical
### **Situation**
  15-step onboarding flow. Completion rate is 20%. Users who complete
  retain at 80%. Users who do not complete churn at 90%. Most value
  never delivered.
  
### **Why**
  Every step is friction. Users have limited patience. If they do not
  reach value quickly, they leave. Front-load value, minimize steps.
  
### **Solution**
  Minimum viable onboarding:
  
  1. Single key action to value (under 5 minutes)
  2. Progressive disclosure of advanced features
  3. Measure step completion rates
  4. Remove steps with high drop-off
  
  The goal is first value moment, not complete understanding.
  
### **Symptoms**
  - Low onboarding completion rate
  - High early churn
  - Many steps before value
  - Users asking basic questions after onboarding
### **Detection Pattern**


## Lagging Indicator Blindness

### **Id**
lagging-indicator-blindness
### **Summary**
Only measuring revenue, missing leading indicators
### **Severity**
high
### **Situation**
  MRR looks fine. Suddenly drops 30% in a month. Team surprised. Actually
  engagement had been declining for months. Nobody was watching.
  
### **Why**
  Revenue is a lagging indicator. By the time it drops, damage is done.
  Leading indicators give warning. Engagement, feature adoption, support
  sentiment - these predict revenue changes.
  
### **Solution**
  Leading indicator dashboard:
  
  Daily: Active users, key feature usage
  Weekly: Feature adoption, support ticket sentiment
  Monthly: NPS trends, health score distribution
  
  Alert on leading indicator drops before revenue impact.
  
### **Symptoms**
  - Only tracking revenue metrics
  - Surprised by churn
  - No engagement tracking
  - Reactive not proactive
### **Detection Pattern**


## Peanut Butter Spreading

### **Id**
peanut-butter-spreading
### **Summary**
Same success effort for all customers regardless of value
### **Severity**
high
### **Situation**
  Enterprise customer worth $100K/year gets same attention as $50/month
  self-serve customer. Enterprise churns for lack of attention.
  Self-serve customers get more time than they are worth.
  
### **Why**
  Success resources are finite. Spreading evenly ignores economics.
  High-value customers need high-touch. Low-value customers need
  efficient self-serve. Match effort to customer value.
  
### **Solution**
  Tiered success model:
  
  Enterprise ($50K+): Dedicated CSM, quarterly business reviews
  Mid-market ($1K-50K): Shared CSM, monthly check-ins
  SMB ($100-1K): Tech-touch, automated sequences
  Self-serve (under $100): Community and self-help
  
  Calculate cost-to-serve vs customer value for each tier.
  
### **Symptoms**
  - Same approach for all customers
  - Enterprise customers feel neglected
  - Too much time on low-value accounts
  - No tier definitions
### **Detection Pattern**


## Health Score Fiction

### **Id**
health-score-fiction
### **Summary**
Health scores that do not actually predict churn
### **Severity**
high
### **Situation**
  Health score shows green. Customer churns. Score was based on logins,
  not actual value delivery. Looked healthy, was not.
  
### **Why**
  Health scores are only useful if they predict outcomes. Many scores
  measure activity, not value. Validate your score against actual
  churn data. Iterate until predictive.
  
### **Solution**
  Health score validation:
  
  1. Run retrospective analysis on churned customers
  2. What did their health scores look like 30, 60, 90 days before churn?
  3. What signals did we miss?
  4. Add those signals to the score
  5. Test prediction accuracy monthly
  
  A score that does not predict is worse than no score.
  
### **Symptoms**
  - Churns from green accounts
  - No retrospective on churned customers
  - Score never updated
  - Activity-based not value-based
### **Detection Pattern**


## Renewal Surprise

### **Id**
renewal-surprise
### **Summary**
Only engaging at renewal time
### **Severity**
high
### **Situation**
  Ignore customer for 11 months. Suddenly engage at renewal. Customer
  has already decided to leave. Too late. Discount offered in desperation.
  
### **Why**
  Renewal is an outcome, not an activity. The decision happens throughout
  the relationship. Quarterly business reviews, ongoing value delivery,
  proactive engagement - these determine renewal.
  
### **Solution**
  Renewal is earned throughout the year:
  
  Quarterly: Business review, success metrics review
  Monthly: Check-in on goals and blockers
  Ongoing: Product education, feature announcements
  At renewal: Celebration of value delivered, expansion discussion
  
  No surprises at renewal because relationship is continuous.
  
### **Symptoms**
  - Renewal outreach only near end date
  - Low renewal rate
  - Customers surprised by renewal
  - No QBRs or regular touchpoints
### **Detection Pattern**


## Success Vs Support Confusion

### **Id**
success-vs-support-confusion
### **Summary**
Customer success doing support, not success
### **Severity**
medium
### **Situation**
  CSM spends all day answering how-to questions. No time for strategic
  conversations. Customers trained to use CSM as support. No proactive
  success happening.
  
### **Why**
  Success and support are different functions. Success is proactive and
  strategic. Support is reactive and tactical. When success does support,
  nobody does success.
  
### **Solution**
  Clear role separation:
  
  Support: Reactive, tactical, how-to questions
  Success: Proactive, strategic, business outcomes
  
  Escalation paths:
  - Technical issues go to support
  - Strategy questions go to success
  
  Train customers on correct routing from onboarding.
  
### **Symptoms**
  - CSMs answering how-to questions
  - No time for strategic conversations
  - CSM as glorified support
  - No proactive outreach happening
### **Detection Pattern**


## Expansion As Sales

### **Id**
expansion-as-sales
### **Summary**
Expansion conversations that feel like sales pitches
### **Severity**
medium
### **Situation**
  Customer happy with product. CSM pushes upgrade aggressively. Customer
  feels sold to. Trust damaged. Actually churns instead of expanding.
  
### **Why**
  Expansion should feel like helping, not selling. When customers outgrow
  their tier, expansion is natural. Pushing before they are ready damages
  the relationship.
  
### **Solution**
  Expansion through value:
  
  1. Track usage vs plan limits
  2. When approaching limits, explain options
  3. Frame as solution to their growth, not your revenue
  4. If not ready, back off gracefully
  
  Natural expansion signals:
  - Hitting usage limits
  - Asking about features in higher tiers
  - Adding users or use cases
  
### **Symptoms**
  - Aggressive upsell attempts
  - Customers complain about sales pressure
  - Expansion damages relationships
  - Pushing before usage supports it
### **Detection Pattern**


## Ignoring Power Users

### **Id**
ignoring-power-users
### **Summary**
All focus on at-risk, none on advocates
### **Severity**
medium
### **Situation**
  All CSM time on saving at-risk accounts. Happy customers ignored.
  Power users never asked to refer, review, or expand. Advocacy
  opportunity missed.
  
### **Why**
  Happy customers are an asset. They can refer, review, case study,
  expand. Ignoring them leaves revenue and advocacy on the table.
  Balanced attention to risk and opportunity.
  
### **Solution**
  Advocate program:
  
  Identify happy customers (NPS 9-10, high health, frequent users)
  Ask for: Referrals, reviews, case studies, references
  Reward: Early access, exclusive events, recognition
  
  Time allocation: 70% at-risk, 30% advocates (or adjust based on data)
  
### **Symptoms**
  - All focus on red accounts
  - No referral asks
  - No case studies being created
  - Happy customers feel ignored
### **Detection Pattern**


## Manual Scale Failure

### **Id**
manual-scale-failure
### **Summary**
Trying to scale customer success manually
### **Severity**
medium
### **Situation**
  100 customers per CSM. Impossible to give everyone attention.
  Important tasks slip. Quality drops. Team burns out.
  
### **Why**
  Human touch cannot scale linearly. Automation, playbooks, and tech-touch
  must handle low-touch segments. CSM time reserved for high-touch and
  exceptions.
  
### **Solution**
  Scalable success:
  
  Automate: Onboarding sequences, usage-based nudges, renewal reminders
  Playbooks: Standardized responses to common situations
  Self-serve: Knowledge base, community, in-app guidance
  
  CSM time only for:
  - High-value strategic conversations
  - Complex escalations
  - Expansion opportunities
  
### **Symptoms**
  - CSM overwhelmed
  - Inconsistent experience
  - Manual processes for everything
  - No automation in place
### **Detection Pattern**


## Churn Learning Gap

### **Id**
churn-learning-gap
### **Summary**
Not learning from churned customers
### **Severity**
medium
### **Situation**
  Customer churns. Marked as closed-lost. No investigation. Same
  problems keep causing churn. Pattern never identified.
  
### **Why**
  Every churn is a learning opportunity. Why did they leave? What
  could we have done differently? Without learning, the same problems
  cause the same churn forever.
  
### **Solution**
  Churn investigation process:
  
  1. Exit interview (even if brief)
  2. Review health score history
  3. Review support and CSM interactions
  4. Identify: Was this preventable? How?
  5. Monthly churn patterns review
  6. Product and process changes based on learnings
  
### **Symptoms**
  - No exit interviews
  - No churn pattern analysis
  - Same reasons keep causing churn
  - Churn seen as inevitable
### **Detection Pattern**
