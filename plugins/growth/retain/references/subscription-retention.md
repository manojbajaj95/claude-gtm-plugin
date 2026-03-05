# Retain Subscription Retention Strategies

Cancellation flow optimization and save offer implementation.

---

## Subscription Retention Flow

```markdown
## Subscription Retention Flow

### Cancellation Funnel
| Step | Option | Expected Conversion |
|------|--------|-------------------|
| 1 | 解約理由の選択 | 100% (required) |
| 2 | 一時停止オプション提示 | 20-25% accept |
| 3 | ダウングレード提案 | 15-20% accept |
| 4 | 割引オファー | 10-15% accept |
| 5 | 解約完了（理由収集） | Remaining |

### Pause Options
| Duration | Eligibility | Data Retention | Re-activation Rate |
|----------|-------------|----------------|-------------------|
| 1ヶ月 | 全ユーザー | 全データ保持 | 70%+ |
| 2ヶ月 | 6ヶ月以上利用 | 全データ保持 | 60%+ |
| 3ヶ月 | 1年以上利用 | 全データ保持 | 50%+ |

### Save Offer Matrix
| Churn Reason | Offer Type | Discount | Duration |
|--------------|-----------|----------|----------|
| 高すぎる | 割引 | 30% | 3ヶ月 |
| 予算削減 | ダウングレード | - | - |
| 使いこなせない | トレーニング | 無料 | - |
| 一時的に不要 | 一時停止 | - | 最大3ヶ月 |
| 競合製品 | 特別オファー | 40% | 6ヶ月 |
```

---

## Retention Flow Implementation

```typescript
// lib/subscription-retention.ts
interface RetentionOffer {
  type: 'pause' | 'downgrade' | 'discount' | 'training' | 'none';
  details: {
    pauseDuration?: number;
    targetPlan?: string;
    discountPercent?: number;
    discountDuration?: number;
    trainingType?: string;
  };
  priority: number;
  expectedSaveRate: number;
}

interface ChurnReason {
  category: 'price' | 'features' | 'usage' | 'temporary' | 'competitor' | 'other';
  subReason: string;
}

function generateRetentionOffers(context: UserContext): RetentionOffer[] {
  const offers: RetentionOffer[] = [];

  // Pause offer (universal, but duration based on tenure)
  if (context.previousSaveAttempts === 0) {
    const pauseDuration = context.tenure > 365 ? 90 :
                          context.tenure > 180 ? 60 : 30;
    offers.push({
      type: 'pause',
      details: { pauseDuration },
      priority: 1,
      expectedSaveRate: 0.22
    });
  }

  // Reason-specific offers
  switch (context.churnReason.category) {
    case 'price':
      offers.push({
        type: 'downgrade',
        details: { targetPlan: getDowngradePlan(context.plan) },
        priority: 2,
        expectedSaveRate: 0.18
      });
      if (context.tenure > 90) {
        offers.push({
          type: 'discount',
          details: {
            discountPercent: context.mrr > 10000 ? 30 : 20,
            discountDuration: 3
          },
          priority: 3,
          expectedSaveRate: 0.12
        });
      }
      break;

    case 'usage':
    case 'features':
      offers.push({
        type: 'training',
        details: { trainingType: 'onboarding_refresh' },
        priority: 2,
        expectedSaveRate: 0.15
      });
      break;

    case 'competitor':
      if (context.tenure > 180) {
        offers.push({
          type: 'discount',
          details: { discountPercent: 40, discountDuration: 6 },
          priority: 2,
          expectedSaveRate: 0.10
        });
      }
      break;
  }

  return offers.sort((a, b) => a.priority - b.priority);
}
```

---

## Retention Metrics Template

```markdown
## Subscription Retention Report: [Period]

### Cancellation Funnel Performance
| Step | Entries | Exits | Conversion |
|------|---------|-------|------------|
| 解約開始 | [N] | - | - |
| 一時停止受諾 | [N] | [N saved] | [X%] |
| ダウングレード受諾 | [N] | [N saved] | [X%] |
| 割引受諾 | [N] | [N saved] | [X%] |
| 解約完了 | [N] | - | - |

### Save Offer Effectiveness
| Offer Type | Offered | Accepted | Rate | Revenue Saved |
|------------|---------|----------|------|---------------|
| 一時停止 | [N] | [N] | [X%] | ¥[X] |
| ダウングレード | [N] | [N] | [X%] | ¥[X] |
| 30%割引 | [N] | [N] | [X%] | ¥[X] |

### Pause Reactivation Tracking
| Pause Duration | Started | Reactivated | Rate |
|----------------|---------|-------------|------|
| 1ヶ月 | [N] | [N] | [X%] |
| 2ヶ月 | [N] | [N] | [X%] |
| 3ヶ月 | [N] | [N] | [X%] |
```
