# Retain Onboarding Optimization

Activation framework and milestone tracking.

---

## Activation Framework

```markdown
## Onboarding Optimization Framework

### Activation Milestones
| Milestone | Target Time | Success Criteria | Impact on D30 |
|-----------|-------------|------------------|---------------|
| **M0: アカウント作成** | T+0 | メール認証完了 | Baseline |
| **M1: プロフィール完成** | T+5min | 必須項目入力 | +8% |
| **M2: 最初のアクション** | T+24h | コア機能1回使用 | +15% |
| **M3: 価値体験** | T+3days | 成果物作成/目標達成 | +25% |
| **M4: 習慣形成** | T+7days | 3日以上アクティブ | +35% |
| **M5: 定着** | T+14days | 週2回以上利用 | +45% |

### Time-to-Value (TTV) Optimization
| User Segment | Current TTV | Target TTV | Strategy |
|--------------|-------------|------------|----------|
| 新規ユーザー | [X]分 | [Y]分 | テンプレート提供 |
| 招待ユーザー | [X]分 | [Y]分 | プリセット設定 |
| トライアル | [X]分 | [Y]分 | ガイド付きツアー |
| 有料転換 | [X]分 | [Y]分 | 1:1オンボーディング |

### Progressive Disclosure Schedule
| Week | Available Features | Introduction Method |
|------|-------------------|---------------------|
| Week 1 | 基本機能のみ | チュートリアル |
| Week 2 | +中級機能 | ツールチップ |
| Week 3 | +高度な機能 | フィーチャー紹介 |
| Week 4+ | 全機能 | ヘルプセンター |
```

---

## Onboarding Implementation

```typescript
// lib/onboarding.ts
interface OnboardingMilestone {
  id: string;
  name: string;
  targetTime: number;      // hours from signup
  criteria: (user: UserData) => boolean;
  impact: number;          // % impact on D30 retention
  completed: boolean;
}

const milestoneDefinitions = [
  { id: 'm0_account', name: 'アカウント作成', targetTime: 0, impact: 0 },
  { id: 'm1_profile', name: 'プロフィール完成', targetTime: 0.08, impact: 8 },
  { id: 'm2_first_action', name: '最初のアクション', targetTime: 24, impact: 15 },
  { id: 'm3_value', name: '価値体験', targetTime: 72, impact: 25 },
  { id: 'm4_habit', name: '習慣形成', targetTime: 168, impact: 35 },
  { id: 'm5_established', name: '定着', targetTime: 336, impact: 45 }
];

function checkOnboardingProgress(user: UserData): OnboardingProgress {
  const hoursSinceSignup = getHoursSinceSignup(user);

  const milestones = milestoneDefinitions.map(def => ({
    ...def,
    completed: def.criteria(user)
  }));

  const completedCount = milestones.filter(m => m.completed).length;
  const currentMilestone = milestones.findIndex(m => !m.completed);

  // Check if at risk (behind schedule)
  const expectedMilestone = milestones.findIndex(m => m.targetTime > hoursSinceSignup);
  const isAtRisk = currentMilestone < expectedMilestone - 1;

  return {
    userId: user.id,
    milestones,
    percentComplete: (completedCount / milestones.length) * 100,
    currentMilestone,
    isAtRisk
  };
}

// Onboarding nudge triggers
const onboardingNudges = [
  { trigger: 'profile_incomplete_1h', channel: 'in_app', delay: 1 },
  { trigger: 'no_action_24h', channel: 'email', delay: 24 },
  { trigger: 'no_value_72h', channel: 'email', delay: 72 },
  { trigger: 'habit_risk_5d', channel: 'push', delay: 120 }
];
```

---

## Onboarding Analytics Template

```markdown
## Onboarding Performance Report: [Period]

### Funnel Overview
| Milestone | Reached | Conversion | Avg Time | Target Time |
|-----------|---------|------------|----------|-------------|
| アカウント作成 | [N] | 100% | - | - |
| プロフィール完成 | [N] | [X%] | [X]min | 5min |
| 最初のアクション | [N] | [X%] | [X]h | 24h |
| 価値体験 | [N] | [X%] | [X]d | 3d |
| 習慣形成 | [N] | [X%] | [X]d | 7d |
| 定着 | [N] | [X%] | [X]d | 14d |

### Onboarding → Retention Correlation
| Completed Milestones | D7 Retention | D30 Retention |
|---------------------|--------------|---------------|
| 0-1 | [X%] | [X%] |
| 2-3 | [X%] | [X%] |
| 4-5 | [X%] | [X%] |
| 6 (All) | [X%] | [X%] |

### Improvement Opportunities
1. **Biggest Drop-off:** M[X] → M[Y] ([Z%])
2. **Slowest Transition:** M[X] → M[Y] ([Z] hours avg)
```
