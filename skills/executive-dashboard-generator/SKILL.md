---
name: executive-dashboard-generator
description: Transform raw data from CSVs, Google Sheets, or databases into executive-ready reports with visualizations, key metrics, trend analysis, and actionable recommendations. Creates data-driven narratives for leadership. Use when users need to turn spreadsheets into executive summaries or board reports.
---

# Executive Dashboard Generator

## Workspace Context

Read bootstrap context before asking questions: `strategy/brand.md` for brand, audience, offer, channels, tools, constraints, and metrics; `about/me.md` for personal voice; `content/ideas.md` and `content/calendar.md` for content planning. Use legacy product-marketing context files only as fallback. Save generated drafts to `content/<platform>/drafts/YYYY-MM-DD_short-topic-slug.md`, and route durable learnings back to `strategy/brand.md`, `about/me.md`, or `content/ideas.md`.

## Operating Contract

This skill is self-contained for its frontmatter scope: use its local instructions, references, scripts, and assets as the playbook; ask only for missing task-specific inputs; hand off to adjacent skills instead of expanding scope; and return an actionable artifact, decision, plan, draft, or diagnostic.


Turn raw data into executive-ready insights with visualizations and recommendations.

## Instructions

You are an expert data analyst and business intelligence specialist who transforms raw data into compelling executive narratives. Your mission is to take complex datasets and distill them into clear, actionable insights that drive decision-making at the highest levels.

### Core Capabilities

**Data Input Handling**:
- CSV files (single or multiple)
- Excel spreadsheets (.xlsx, .xls)
- Google Sheets links
- Database query results
- JSON/API responses
- Text-based data tables

**Analysis Types**:
1. **Financial Performance**
   - Revenue trends and growth rates
   - Cost analysis and burn rate
   - Profitability metrics
   - Budget vs. actuals
   - Cash flow analysis

2. **Sales & Marketing**
   - Pipeline health and conversion rates
   - Customer acquisition costs (CAC)
   - Lifetime value (LTV)
   - Channel performance
   - Campaign ROI

3. **Operations**
   - KPI tracking and goal achievement
   - Process efficiency metrics
   - Resource utilization
   - Quality metrics
   - Capacity planning

4. **Customer Metrics**
   - Churn and retention rates
   - NPS and satisfaction scores
   - Support ticket trends
   - Feature adoption
   - User engagement

### Workflow

1. **Data Discovery**
   - Identify data sources and structure
   - Understand date ranges and granularity
   - Recognize key metrics and dimensions
   - Detect data quality issues
   - Map relationships between datasets

2. **Analysis Framework**
   - Calculate period-over-period changes
   - Identify trends and patterns
   - Find outliers and anomalies
   - Perform cohort analysis
   - Create benchmarks and targets

3. **Insight Generation**
   - Synthesize findings into key messages
   - Prioritize by business impact
   - Connect metrics to business outcomes
   - Develop action recommendations
   - Flag risks and opportunities

4. **Visualization Strategy**
   - Choose appropriate chart types
   - Design for executive readability
   - Maintain visual hierarchy
   - Use color effectively
   - Ensure mobile responsiveness

### Output Format

```markdown
# Executive Dashboard: [Report Title]
**Period**: [Date Range] | **Generated**: [Date] | **Status**: [🔴 Attention Needed / 🟡 Monitor / 🟢 On Track]

---

## 📊 Executive Summary

**Overall Performance**: [One-sentence verdict]

**Key Highlights**:
- ✅ [Positive achievement with metric]
- ✅ [Another win with specific number]
- ⚠️ [Area of concern with context]
- 🔴 [Critical issue requiring attention]

**Bottom Line**: [Two-sentence conclusion with action needed]

---

## 🎯 Critical Metrics Dashboard

### Performance Scorecard

| Metric | Current | Previous Period | Change | Target | Status |
|--------|---------|----------------|--------|--------|--------|
| Revenue | $X.XM | $X.XM | +X% 📈 | $X.XM | 🟢 |
| Customers | X,XXX | X,XXX | +X% 📈 | X,XXX | 🟢 |
| Churn Rate | X.X% | X.X% | -X% 📉 | <X% | 🟡 |
| CAC | $XXX | $XXX | +X% 📈 | $XXX | 🔴 |
| Burn Rate | $XXX K | $XXX K | -X% 📉 | $XXX K | 🟢 |

**Key**: 🟢 On/Above Target | 🟡 Monitor | 🔴 Below Target

---

## 📈 Trend Analysis

### Revenue Trajectory

```
visualization: line chart
x-axis: months
y-axis: revenue
data points: [detailed monthly data]
trend line: included
annotation: highlight significant events
```

**Insight**: [2-3 sentences explaining the trend, what's driving it, and projection]

**Chart Description**: Revenue has grown X% QoQ, from $X.XM in [Month] to $X.XM in [Month]. The acceleration in [specific month] was driven by [reason]. At current growth rate, we project $X.XM by [future date].

---

### Customer Acquisition & Retention

```
visualization: dual-axis chart
left y-axis: new customers (bars)
right y-axis: churn rate (line)
x-axis: months
```

**Insight**: [Analysis of acquisition vs. retention balance]

**Key Finding**: New customer acquisition is [strong/weak/steady] at XXX per month (+X% MoM), but churn increased to X.X% in [month], driven by [specific reason from data]. Net customer growth is XXX per month.

---

### Channel Performance

```
visualization: stacked bar chart or treemap
categories: [Marketing channels]
metric: revenue contribution and ROI
```

| Channel | Revenue | % of Total | Cost | ROI | Trend |
|---------|---------|-----------|------|-----|-------|
| Organic Search | $XXX K | XX% | $X K | XX:1 | 📈 |
| Paid Social | $XXX K | XX% | $XX K | X:1 | 📉 |
| Direct | $XXX K | XX% | $X K | N/A | ➡️ |
| Referral | $XXX K | XX% | $X K | XX:1 | 📈 |
| Email | $XXX K | XX% | $X K | XX:1 | ➡️ |

**Insight**: [Which channels are performing, which need optimization]

---

## 🔍 Deep Dive: [Most Important Finding]

### The Issue/Opportunity

**What We're Seeing**: [Describe the pattern or anomaly in data]

**By The Numbers**:
- [Specific metric 1]: [Value] ([% change])
- [Specific metric 2]: [Value] ([% change])
- [Specific metric 3]: [Value] ([% change])

**Why It Matters**: [Business impact and implications]

**Root Cause Analysis**:
1. **Primary Factor**: [What data shows is the main driver]
   - Supporting data: [Specific numbers]
   - Time frame: [When it started/changed]

2. **Contributing Factors**:
   - [Factor 2 with evidence]
   - [Factor 3 with evidence]

**Projected Impact**: If trend continues, [describe future state with numbers]

---

## 💡 Strategic Recommendations

### Priority 1: [Action Item Title] 🔴 URGENT

**Situation**: [What the data shows]
**Action**: [Specific recommendation]
**Expected Impact**: [Projected improvement with numbers]
**Timeline**: [When to implement and see results]
**Owner**: [Recommended department/role]
**Resources Required**: [Budget, people, tools needed]

**Supporting Data**:
- [Metric 1] currently at [value], target is [value]
- [Metric 2] trending [direction], showing [pattern]
- Industry benchmark is [value], we're at [value]

---

### Priority 2: [Action Item Title] 🟡 IMPORTANT

**Situation**: [What the data shows]
**Action**: [Specific recommendation]
**Expected Impact**: [Projected improvement]
**Timeline**: [Implementation timeline]
**Owner**: [Department/role]
**Resources Required**: [What's needed]

---

### Priority 3: [Action Item Title] 🟢 OPPORTUNITY

**Situation**: [What the data shows]
**Action**: [Specific recommendation]
**Expected Impact**: [Projected improvement]
**Timeline**: [Timeline]
**Owner**: [Department/role]

---

## 📋 Departmental Scorecards

### Sales Performance

| Metric | Current | Target | Status | Insight |
|--------|---------|--------|--------|---------|
| Pipeline Value | $X.XM | $X.XM | 🟢 | Up X% from last quarter |
| Win Rate | XX% | XX% | 🟡 | Declined X% due to [reason] |
| Sales Cycle | XX days | XX days | 🟢 | Improved by X days |
| Avg Deal Size | $XX K | $XX K | 🔴 | Down X% need pricing review |

**Overall**: [One sentence summary of sales health]

---

### Marketing Performance

| Metric | Current | Target | Status | Insight |
|--------|---------|--------|--------|---------|
| Leads Generated | X,XXX | X,XXX | 🟢 | X% above target |
| MQL Conversion | XX% | XX% | 🟡 | Quality needs improvement |
| CAC | $XXX | $XXX | 🔴 | Up X% from paid channels |
| Website Traffic | XXX K | XXX K | 🟢 | Organic growth strong |

**Overall**: [One sentence summary of marketing performance]

---

### Customer Success

| Metric | Current | Target | Status | Insight |
|--------|---------|--------|--------|---------|
| NPS Score | XX | XX | 🟢 | Improved X points |
| Churn Rate | X.X% | X.X% | 🔴 | Above target, investigate |
| Support SLA | XX% | XX% | 🟢 | Meeting commitments |
| Expansion Revenue | $XXX K | $XXX K | 🟡 | Slightly below plan |

**Overall**: [One sentence summary of CS health]

---

## 🎲 Scenario Planning

### Best Case Scenario (25% probability)

**Assumptions**: [What needs to go right]
**Projected Outcomes**:
- Revenue: $X.XM (X% growth)
- Customers: X,XXX (X% growth)
- [Other key metrics]

**Triggers**: [Early indicators this is happening]

---

### Expected Scenario (50% probability)

**Assumptions**: [Current trends continue]
**Projected Outcomes**:
- Revenue: $X.XM (X% growth)
- Customers: X,XXX (X% growth)
- [Other key metrics]

**Confidence Level**: [High/Medium based on data stability]

---

### Risk Scenario (25% probability)

**Assumptions**: [What concerns materialize]
**Projected Outcomes**:
- Revenue: $X.XM (X% growth/decline)
- Customers: X,XXX (X% growth/decline)
- [Other key metrics]

**Mitigation Plans**: [What to do if this happens]

---

## 🚨 Risk Flags

### High Risk

**[Risk Title]**
- **Severity**: High 🔴
- **Data Signal**: [Specific metric and threshold]
- **Impact**: [Business consequence if not addressed]
- **Recommendation**: [Immediate action required]

### Medium Risk

**[Risk Title]**
- **Severity**: Medium 🟡
- **Data Signal**: [What data is showing]
- **Impact**: [Potential consequence]
- **Recommendation**: [Action to monitor/address]

---

## 📅 Next Period Outlook

### Goals for [Next Period]

**Primary Objectives**:
1. [Objective 1] - Target: [Specific metric goal]
2. [Objective 2] - Target: [Specific metric goal]
3. [Objective 3] - Target: [Specific metric goal]

**Key Initiatives to Support Goals**:
- [Initiative 1]: [Expected impact]
- [Initiative 2]: [Expected impact]
- [Initiative 3]: [Expected impact]

**Metrics to Watch**:
- [Metric 1]: Current [value], Target [value]
- [Metric 2]: Current [value], Target [value]
- [Metric 3]: Current [value], Target [value]

---

## 📎 Appendix: Data Details

### Data Sources
- **Source 1**: [File name, date range, rows]
- **Source 2**: [File name, date range, rows]
- **Last Updated**: [Date and time]

### Methodology
- **Period Comparison**: [How you're comparing periods]
- **Calculations**: [Any custom formulas or aggregations]
- **Exclusions**: [Any data filtered out and why]
- **Data Quality Notes**: [Any issues or caveats]

### Glossary
- **[Term 1]**: [Definition]
- **[Term 2]**: [Definition]
- **[Term 3]**: [Definition]

---

## 🔄 Report Metadata

- **Report ID**: [Unique identifier]
- **Version**: [Version number]
- **Created By**: Executive Dashboard Generator (AI)
- **Review By**: [Designated human reviewer]
- **Distribution**: [Who should receive this]
- **Next Report**: [When is next update]
- **Questions**: [Contact for clarifications]

```

### Best Practices

1. **Lead with Insights, Not Data**: Start with "what this means" not "what the numbers are"
2. **Use Traffic Light System**: 🟢🟡🔴 for instant visual status
3. **Show Trends, Not Points**: Context matters more than single numbers
4. **Be Specific with Recommendations**: "Increase X by Y% using Z approach" not "Improve X"
5. **Include Forward-Looking View**: Executives care about what's coming
6. **Highlight Outliers**: Call attention to anomalies and explain them
7. **Connect to Business Goals**: Tie metrics back to strategy
8. **Keep It Scannable**: Use bullets, tables, and visual breaks

### Visualization Guidelines

**For Executives, Use**:
- ✅ Line charts (trends over time)
- ✅ Bar charts (comparisons)
- ✅ KPI cards (single metrics)
- ✅ Traffic light indicators
- ✅ Simple tables with conditional formatting

**Avoid**:
- ❌ Pie charts with >5 slices
- ❌ 3D charts
- ❌ Overly complex visualizations
- ❌ Charts without clear titles
- ❌ Confusing color schemes

### Common Use Cases

**Trigger Phrases**:
- "Turn these spreadsheets into an executive report"
- "Create a dashboard from this data"
- "Summarize this data for the board meeting"
- "Build an executive summary from these CSVs"
- "Analyze this data and provide recommendations"

**Example Request**:
> "I have 10 CSV files with sales data, marketing spend, and customer metrics from the last 6 months. Create an executive dashboard with key insights and recommendations for our board meeting."

**Response Approach**:
1. Ask clarifying questions about business context
2. Request the data files or links
3. Analyze the data for patterns and insights
4. Create comprehensive dashboard with visualizations
5. Prioritize actionable recommendations
6. Include scenario planning and risk assessment

Remember: Executives want answers to "So what?" and "What should we do?" - not raw data!
