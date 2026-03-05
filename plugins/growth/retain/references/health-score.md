# Retain Customer Health Score

Comprehensive health scoring framework and implementation.

---

## Health Score Framework

```markdown
## Customer Health Score Framework

### Health Score Components (100 points total)
| Dimension | Weight | Signals | Calculation |
|-----------|--------|---------|-------------|
| **利用頻度** | 25% | DAU/MAU比率, セッション数, 最終ログイン | (actual/expected) × 25 |
| **機能深度** | 20% | 機能利用率, コア機能使用, 高度機能使用 | (features_used/total_features) × 20 |
| **エンゲージメント** | 20% | 滞在時間, アクション数, コンテンツ作成 | engagement_percentile × 20 |
| **満足度** | 15% | NPS, CSAT, CES, サポート満足度 | (satisfaction_avg/5) × 15 |
| **成長** | 10% | シート追加, プラン変更, 利用量増加 | growth_indicator × 10 |
| **関係性** | 10% | サポート履歴, コミュニティ参加, 紹介実績 | relationship_score × 10 |

### Health Score Thresholds
| Score | Status | Color | Interpretation | Action |
|-------|--------|-------|----------------|--------|
| 80-100 | Healthy | 🟢 | 満足して活用中 | アップセル/紹介依頼 |
| 60-79 | Stable | 🟡 | 安定利用中 | 継続モニタリング |
| 40-59 | At Risk | 🟠 | 離脱リスクあり | 自動介入開始 |
| 0-39 | Critical | 🔴 | 即時対応必要 | 人的介入（1:1対応）|

### Health Trend Analysis
| Trend Pattern | Definition | Response |
|---------------|------------|----------|
| ↑ 改善中 | +10pt/月以上 | 成功事例として記録、紹介依頼 |
| → 安定 | ±5pt/月以内 | 継続的な価値提供 |
| ↓ 悪化中 | -10pt/月以上 | 早期介入、原因調査 |
| ↓↓ 急速悪化 | -20pt/月以上 | 即時エスカレーション |
```

---

## Health Score Implementation

```typescript
// lib/customer-health.ts
interface HealthScoreInput {
  // Usage frequency
  dauMauRatio: number;
  sessionsLast30Days: number;
  daysSinceLastLogin: number;
  // Feature depth
  featuresUsed: number;
  totalFeatures: number;
  coreFeatureUsage: boolean[];
  // Engagement
  avgSessionDuration: number;
  actionsLast30Days: number;
  contentCreated: number;
  // Satisfaction
  npsScore?: number;
  csatScore?: number;
  cesScore?: number;
  // Growth
  seatsAdded: number;
  planUpgraded: boolean;
  usageGrowth: number;
  // Relationship
  supportTicketsResolved: number;
  communityPosts: number;
  referralsMade: number;
}

interface HealthScore {
  overall: number;
  status: 'healthy' | 'stable' | 'at_risk' | 'critical';
  dimensions: {
    usage: number;
    depth: number;
    engagement: number;
    satisfaction: number;
    growth: number;
    relationship: number;
  };
  trend: 'improving' | 'stable' | 'declining' | 'rapid_decline';
  alerts: string[];
  recommendedActions: string[];
}

function calculateHealthScore(input: HealthScoreInput, previousScore?: number): HealthScore {
  const dimensions = {
    usage: calculateUsageScore(input) * 0.25,
    depth: calculateDepthScore(input) * 0.20,
    engagement: calculateEngagementScore(input) * 0.20,
    satisfaction: calculateSatisfactionScore(input) * 0.15,
    growth: calculateGrowthScore(input) * 0.10,
    relationship: calculateRelationshipScore(input) * 0.10
  };

  const overall = Object.values(dimensions).reduce((sum, val) => sum + val, 0);

  let status: HealthScore['status'];
  if (overall >= 80) status = 'healthy';
  else if (overall >= 60) status = 'stable';
  else if (overall >= 40) status = 'at_risk';
  else status = 'critical';

  const scoreDiff = previousScore ? overall - previousScore : 0;
  let trend: HealthScore['trend'];
  if (scoreDiff >= 10) trend = 'improving';
  else if (scoreDiff <= -20) trend = 'rapid_decline';
  else if (scoreDiff <= -10) trend = 'declining';
  else trend = 'stable';

  const alerts = generateAlerts(input, dimensions);
  const recommendedActions = generateRecommendedActions(status, alerts, dimensions);

  return {
    overall: Math.round(overall),
    status,
    dimensions: normalizeToPercent(dimensions),
    trend,
    alerts,
    recommendedActions
  };
}
```

---

## Health Score Report Template

```markdown
## Customer Health Report: [Period]

### Portfolio Overview
| Status | Count | % | MRR | Trend |
|--------|-------|---|-----|-------|
| 🟢 Healthy | [N] | [X%] | ¥[X] | ↑/↓/→ |
| 🟡 Stable | [N] | [X%] | ¥[X] | ↑/↓/→ |
| 🟠 At Risk | [N] | [X%] | ¥[X] | ↑/↓/→ |
| 🔴 Critical | [N] | [X%] | ¥[X] | ↑/↓/→ |

### At-Risk Accounts (Immediate Attention)
| Customer | Score | Trend | Top Alert | Assigned To |
|----------|-------|-------|-----------|-------------|
| [Name] | [X] | ↓ | [Alert] | [CSM] |

### Dimension Analysis
| Dimension | Avg Score | Lowest Segment | Action |
|-----------|-----------|----------------|--------|
| 利用頻度 | [X] | [Segment] | [Action] |
| 機能深度 | [X] | [Segment] | [Action] |
| エンゲージメント | [X] | [Segment] | [Action] |
| 満足度 | [X] | [Segment] | [Action] |
```
