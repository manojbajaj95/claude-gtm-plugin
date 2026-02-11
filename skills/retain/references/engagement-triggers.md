# Retain Re-engagement Triggers

Trigger configuration and message templates.

---

## Trigger Configuration

```typescript
// lib/engagement-triggers.ts
interface EngagementTrigger {
  name: string;
  condition: (user: UserData) => boolean;
  action: 'email' | 'push' | 'in_app' | 'sms';
  template: string;
  delay: number;  // hours after condition is met
  maxFrequency: number;  // max times per month
}

const engagementTriggers: EngagementTrigger[] = [
  {
    name: 'dormant_3_days',
    condition: (user) => daysSinceLastVisit(user) >= 3 && daysSinceLastVisit(user) < 7,
    action: 'push',
    template: 'miss_you_3_days',
    delay: 0,
    maxFrequency: 4
  },
  {
    name: 'dormant_7_days',
    condition: (user) => daysSinceLastVisit(user) >= 7 && daysSinceLastVisit(user) < 14,
    action: 'email',
    template: 'win_back_7_days',
    delay: 12,
    maxFrequency: 2
  },
  {
    name: 'incomplete_onboarding',
    condition: (user) => !user.onboardingComplete && daysSinceSignup(user) >= 1,
    action: 'email',
    template: 'complete_setup',
    delay: 24,
    maxFrequency: 3
  },
  {
    name: 'feature_discovery',
    condition: (user) => user.sessionsCount > 5 && !user.hasUsedFeature('advanced_search'),
    action: 'in_app',
    template: 'discover_feature',
    delay: 0,
    maxFrequency: 1
  },
  {
    name: 'streak_at_risk',
    condition: (user) => user.currentStreak > 0 && hoursUntilStreakExpires(user) < 6,
    action: 'push',
    template: 'protect_streak',
    delay: 0,
    maxFrequency: 30
  }
];
```

---

## Message Templates

```typescript
// lib/engagement-templates.ts
const templates = {
  miss_you_3_days: {
    title: 'お待ちしています！',
    body: '最後のご利用から3日が経ちました。[最近の更新]をチェックしませんか？',
    cta: '今すぐチェック'
  },

  win_back_7_days: {
    subject: '[名前]さん、お元気ですか？',
    body: `
      しばらくお見えになりませんね。

      最近、新機能[機能名]を追加しました！
      [メリット]ができるようになりました。

      ぜひお試しください。
    `,
    cta: '新機能を見る'
  },

  complete_setup: {
    subject: 'あと少しで完了です！',
    body: `
      セットアップが途中です。

      残りのステップを完了すると、
      [ベネフィット]が使えるようになります。

      5分で完了できます。
    `,
    cta: 'セットアップを続ける'
  },

  protect_streak: {
    title: '連続記録を守りましょう！',
    body: '現在[N]日連続！今日も利用して記録を伸ばしましょう。',
    cta: '利用する'
  }
};
```
