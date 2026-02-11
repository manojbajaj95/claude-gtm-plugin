# Retain Retention Analysis Framework

Cohort retention analysis and churn prediction models.

---

## Cohort Retention Analysis Template

```markdown
## Retention Analysis: [Product/Feature]

### Cohort Retention Table
| Cohort | Week 0 | Week 1 | Week 2 | Week 4 | Week 8 | Week 12 |
|--------|--------|--------|--------|--------|--------|---------|
| Jan W1 | 100% | 42% | 35% | 28% | 22% | 18% |
| Jan W2 | 100% | 45% | 38% | 30% | 24% | 20% |
| Feb W1 | 100% | 48% | 40% | 32% | - | - |

### Key Metrics
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Day 1 Retention | [X%] | [Y%] | [Status] |
| Week 1 Retention | [X%] | [Y%] | [Status] |
| Month 1 Retention | [X%] | [Y%] | [Status] |
| Month 3 Retention | [X%] | [Y%] | [Status] |

### Drop-off Analysis
| Period | Drop-off % | Primary Reason | Intervention |
|--------|-----------|----------------|--------------|
| Day 0-1 | [X%] | [Reason] | [Action] |
| Day 1-7 | [X%] | [Reason] | [Action] |
| Week 1-4 | [X%] | [Reason] | [Action] |

### Retention Curve Shape
- **Flattening Point:** Week [X] (when retention stabilizes)
- **Target:** Increase stable retention to [X%]
```

---

## Churn Prediction Model

```typescript
// lib/churn-prediction.ts
interface ChurnSignals {
  daysSinceLastVisit: number;
  sessionsLast7Days: number;
  sessionsLast30Days: number;
  featureUsageScore: number;    // 0-100
  supportTicketsOpen: number;
  npsScore?: number;
  billingIssues: boolean;
}

interface ChurnRisk {
  score: number;        // 0-100
  level: 'low' | 'medium' | 'high' | 'critical';
  signals: string[];
  recommendedAction: string;
}

function calculateChurnRisk(signals: ChurnSignals): ChurnRisk {
  let riskScore = 0;
  const riskSignals: string[] = [];

  // Inactivity signals
  if (signals.daysSinceLastVisit > 14) {
    riskScore += 30;
    riskSignals.push('14日以上未訪問');
  } else if (signals.daysSinceLastVisit > 7) {
    riskScore += 15;
    riskSignals.push('7日以上未訪問');
  }

  // Engagement decline
  if (signals.sessionsLast7Days < signals.sessionsLast30Days / 4 * 0.5) {
    riskScore += 25;
    riskSignals.push('利用頻度が50%以上減少');
  }

  // Feature adoption
  if (signals.featureUsageScore < 30) {
    riskScore += 20;
    riskSignals.push('主要機能の利用率が低い');
  }

  // Support issues
  if (signals.supportTicketsOpen > 2) {
    riskScore += 15;
    riskSignals.push('複数のサポート問題が未解決');
  }

  // NPS detractor
  if (signals.npsScore !== undefined && signals.npsScore <= 6) {
    riskScore += 20;
    riskSignals.push('NPS批判者');
  }

  // Billing issues
  if (signals.billingIssues) {
    riskScore += 25;
    riskSignals.push('請求に関する問題あり');
  }

  // Determine risk level and action
  let level: ChurnRisk['level'];
  let recommendedAction: string;

  if (riskScore >= 70) {
    level = 'critical';
    recommendedAction = '即座に個別対応（電話/1:1メール）';
  } else if (riskScore >= 50) {
    level = 'high';
    recommendedAction = 'パーソナライズされた再エンゲージメント施策';
  } else if (riskScore >= 30) {
    level = 'medium';
    recommendedAction = '自動リエンゲージメントキャンペーン';
  } else {
    level = 'low';
    recommendedAction = '通常のエンゲージメント施策を継続';
  }

  return {
    score: Math.min(riskScore, 100),
    level,
    signals: riskSignals,
    recommendedAction
  };
}
```
