# Customer Success - Validations

## Missing Onboarding Flow Definition

### **Id**
cs-no-onboarding-flow
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - signup|registration|create.?account
### **Message**
Signup/registration detected but no onboarding flow found. Users will churn without guidance.
### **Fix Action**
Define onboarding steps: welcome email → first value moment → second session trigger
### **Applies To**
  - *.md
  - *.txt
  - README*

## No Customer Health Score Definition

### **Id**
cs-no-health-score
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - churn|retention|customer.?success
### **Message**
Customer success mentioned but no health score definition found. You cannot improve what you do not measure.
### **Fix Action**
Define health score: usage frequency + feature adoption + support tickets + NPS
### **Applies To**
  - *.md
  - *.txt

## Reactive Support Without Proactive Outreach

### **Id**
cs-reactive-support-only
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - support.?ticket|help.?desk|customer.?support
### **Message**
Support mentioned but no proactive outreach triggers. Waiting for tickets means waiting for problems.
### **Fix Action**
Add proactive triggers: usage drop alerts, milestone celebrations, check-in cadence
### **Applies To**
  - *.md
  - *.txt

## Missing Success Metrics Definition

### **Id**
cs-no-success-metrics
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - customer.?success|cs.?team|success.?manager
### **Message**
Customer success referenced without defined success metrics. What does success look like for customers?
### **Fix Action**
Define customer outcomes: time to value, adoption milestones, business impact metrics
### **Applies To**
  - *.md
  - *.txt

## Feature Announcement Without Adoption Strategy

### **Id**
cs-feature-announcement-no-adoption
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - new.?feature|launch|release.?notes|changelog
### **Message**
Feature release without adoption strategy. Features do not matter if no one uses them.
### **Fix Action**
Add adoption plan: targeted announcement → in-app guidance → adoption tracking → follow-up
### **Applies To**
  - *.md
  - CHANGELOG*
  - RELEASE*

## NPS Survey Without Action Plan

### **Id**
cs-nps-without-action
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - NPS|net.?promoter|survey|feedback.?score
### **Message**
NPS/survey mentioned but no action workflow. Collecting feedback without acting destroys trust.
### **Fix Action**
Define action workflow: detractor rescue process, passive conversion, promoter amplification
### **Applies To**
  - *.md
  - *.txt

## Hardcoded Email Timing

### **Id**
cs-hardcoded-email-timing
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - day.?\d+|after.?\d+.?days|wait.?\d+.?hours
### **Message**
Hardcoded timing in customer communications. Different customers need different cadences.
### **Fix Action**
Use behavior-triggered communications instead of time-based. Trigger on actions, not calendars.
### **Applies To**
  - *.md
  - *.yaml
  - *.json

## Missing Churn Early Warning Indicators

### **Id**
cs-no-churn-indicators
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - churn|cancel|retention
### **Message**
Churn discussed but no early warning indicators defined. Churn is a lagging indicator of problems.
### **Fix Action**
Define leading indicators: login frequency drop, feature usage decline, support sentiment change
### **Applies To**
  - *.md
  - *.txt

## Missing Expansion Opportunity Triggers

### **Id**
cs-no-expansion-triggers
### **Severity**
info
### **Type**
regex
### **Pattern**
  - upsell|expansion|upgrade|tier|plan
### **Message**
Expansion mentioned but no trigger conditions. Expansion should be tied to customer success, not quotas.
### **Fix Action**
Define expansion triggers: hitting usage limits, achieving outcomes, requesting advanced features
### **Applies To**
  - *.md
  - *.txt

## Generic Onboarding Email Copy

### **Id**
cs-generic-onboarding-email
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - welcome.?to|thanks.?for.?signing|get.?started
### **Message**
Generic welcome language detected. Personalized onboarding converts 2-3x better.
### **Fix Action**
Personalize by: use case selected, company size, referral source, first action taken
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Missing Time to Value Definition

### **Id**
cs-no-time-to-value
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - onboard|activation|first.?run|getting.?started
### **Message**
Onboarding discussed but time to value not defined. What is the aha moment and how fast should users get there?
### **Fix Action**
Define TTV target: identify aha moment, measure current TTV, set improvement targets
### **Applies To**
  - *.md
  - *.txt

## Treating All Users The Same

### **Id**
cs-segment-all-users-same
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - all.?users|every.?customer|all.?customers
### **Message**
Treating all users the same detected. Different segments need different success approaches.
### **Fix Action**
Segment by: company size, use case, engagement level, contract value. Differentiate touch model.
### **Applies To**
  - *.md
  - *.txt