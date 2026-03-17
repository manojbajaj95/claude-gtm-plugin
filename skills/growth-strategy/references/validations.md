# Growth Strategy - Validations

## Growth Strategy Without Metrics

### **Id**
growth-no-metrics
### **Severity**
error
### **Type**
regex
### **Pattern**
  - growth|scale|expand|increase
### **Message**
Growth mentioned without metrics. What are you growing? How much? By when? Define it.
### **Fix Action**
Set specific metrics: MAU, revenue, signups, retention? What number? What timeframe? Make it measurable.
### **Applies To**
  - *.md
  - *.txt
  - README*

## Unclear Growth Channels

### **Id**
growth-unclear-channels
### **Severity**
error
### **Type**
regex
### **Pattern**
  - marketing|acquisition|attract|reach
### **Message**
Growth without specific channels. 'Marketing' is not a channel. How exactly will you reach people?
### **Fix Action**
Name channels: SEO? Paid ads? Referral? Content? Pick 1-2 to start. More channels = less focus.
### **Applies To**
  - *.md
  - *.txt

## Vanity Metrics Focus

### **Id**
growth-vanity-metrics
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - impressions|views|followers|likes|traffic|visitors
### **Message**
Vanity metrics detected. Views and followers don't pay bills. Focus on revenue, retention, engagement.
### **Fix Action**
Track value metrics: paying customers, revenue, retention rate, LTV, activation rate
### **Applies To**
  - *.md
  - *.txt

## No Growth Experiments Defined

### **Id**
growth-no-experiments
### **Severity**
error
### **Type**
regex
### **Pattern**
  - test|try|experiment|hypothesis
### **Message**
Growth experiments without structure. What's the hypothesis? Success criteria? Timeline to evaluate?
### **Fix Action**
Structure experiments: hypothesis, metric, target, timeline. Run, measure, learn, iterate.
### **Applies To**
  - *.md
  - *.txt

## No Funnel Metrics

### **Id**
growth-no-funnel
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - conversion|signup|trial|purchase|onboard
### **Message**
Conversion mentioned without funnel breakdown. Where are people dropping off? You need to know.
### **Fix Action**
Map funnel: visit → signup → activate → convert → retain. Measure each step. Find bottleneck.
### **Applies To**
  - *.md
  - *.txt

## Paid Acquisition Only Strategy

### **Id**
growth-paid-only
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - ads|advertising|paid|ppc|sponsored
### **Message**
Paid-only growth strategy. When money stops, growth stops. Build owned channels: SEO, content, referral.
### **Fix Action**
Mix channels: 1 paid (fast), 1 organic (sustainable), 1 viral (scalable). Don't depend on one.
### **Applies To**
  - *.md
  - *.txt

## Acquisition Without Retention

### **Id**
growth-no-retention
### **Severity**
error
### **Type**
regex
### **Pattern**
  - acquire|acquisition|get.?users|attract.?customers
### **Message**
Acquisition focus without retention strategy. Leaky bucket problem. Fix retention before scaling acquisition.
### **Fix Action**
Measure retention first: Week 1, Week 4, Month 3 retention. If below 40%, fix product before scaling.
### **Applies To**
  - *.md
  - *.txt

## No Unit Economics Defined

### **Id**
growth-no-unit-economics
### **Severity**
error
### **Type**
regex
### **Pattern**
  - scale|grow|expand|acquire
### **Message**
Scaling without unit economics. CAC vs LTV ratio must work before scaling. Otherwise you lose money faster.
### **Fix Action**
Calculate: CAC (cost to acquire), LTV (lifetime value). LTV should be 3x CAC minimum. If not, fix first.
### **Applies To**
  - *.md
  - *.txt

## Trying Every Channel at Once

### **Id**
growth-everything-at-once
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - and|also|plus|as.?well.?as|in.?addition
### **Message**
Too many channels at once. Spreading thin across 10 channels = mediocre results everywhere. Focus wins.
### **Fix Action**
Pick ONE primary channel to master. Get it working. Then layer on a second. Serial, not parallel.
### **Applies To**
  - *.md
  - *.txt

## No Growth Loops Identified

### **Id**
growth-no-loops
### **Severity**
info
### **Type**
regex
### **Pattern**
  - viral|network.?effect|referral|word.?of.?mouth
### **Message**
Viral growth mentioned without loop structure. What action creates more users? Map the actual loop.
### **Fix Action**
Design loop: user action → new exposure → new users → more actions. Make it measurable and improvable.
### **Applies To**
  - *.md
  - *.txt

## Premature Scaling Signs

### **Id**
growth-premature-scaling
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - scale.?up|ramp.?up|accelerate|aggressive|blitz
### **Message**
Scaling language before product-market fit. Scaling a product people don't want = fast death.
### **Fix Action**
Validate PMF first: 40%+ users very disappointed if product disappeared. Get that, then scale.
### **Applies To**
  - *.md
  - *.txt

## No Activation Metric

### **Id**
growth-no-activation
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - signup|register|new.?user|trial
### **Message**
Signup without activation definition. Signup is not success. What action = real value experienced?
### **Fix Action**
Define activation: first action that correlates with retention. Measure and optimize that, not just signups.
### **Applies To**
  - *.md
  - *.txt