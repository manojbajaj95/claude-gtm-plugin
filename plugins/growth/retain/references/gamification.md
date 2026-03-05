# Retain Gamification Elements

Badge system and progress tracking.

---

## Badge System

```typescript
// lib/badges.ts
interface Badge {
  id: string;
  name: string;
  description: string;
  icon: string;
  criteria: (user: UserData) => boolean;
  rarity: 'common' | 'rare' | 'epic' | 'legendary';
}

const badges: Badge[] = [
  {
    id: 'first_project',
    name: 'スタートアップ',
    description: '最初のプロジェクトを作成',
    icon: '🚀',
    criteria: (user) => user.projectsCreated >= 1,
    rarity: 'common'
  },
  {
    id: 'streak_7',
    name: 'ウィークリーウォリアー',
    description: '7日連続で利用',
    icon: '🗓️',
    criteria: (user) => user.currentStreak >= 7,
    rarity: 'common'
  },
  {
    id: 'streak_30',
    name: 'マンスリーマスター',
    description: '30日連続で利用',
    icon: '📆',
    criteria: (user) => user.currentStreak >= 30,
    rarity: 'rare'
  },
  {
    id: 'power_user',
    name: 'パワーユーザー',
    description: '全ての主要機能を使用',
    icon: '⚡',
    criteria: (user) => user.featureUsageScore >= 90,
    rarity: 'rare'
  },
  {
    id: 'community_helper',
    name: 'コミュニティヘルパー',
    description: '他のユーザーを10人以上助けた',
    icon: '🤝',
    criteria: (user) => user.helpfulAnswers >= 10,
    rarity: 'epic'
  },
  {
    id: 'og_member',
    name: 'OGメンバー',
    description: 'ベータ版から利用',
    icon: '👑',
    criteria: (user) => user.joinedBefore('2024-01-01'),
    rarity: 'legendary'
  }
];

async function checkAndAwardBadges(userId: string): Promise<Badge[]> {
  const user = await getUserData(userId);
  const earnedBadges = await getEarnedBadges(userId);
  const newBadges: Badge[] = [];

  for (const badge of badges) {
    if (!earnedBadges.includes(badge.id) && badge.criteria(user)) {
      await awardBadge(userId, badge.id);
      newBadges.push(badge);

      trackEvent('badge_earned', {
        badge_id: badge.id,
        badge_name: badge.name,
        rarity: badge.rarity
      });
    }
  }

  return newBadges;
}
```

---

## Progress System

```typescript
// components/ProgressTracker.tsx
interface ProgressLevel {
  level: number;
  name: string;
  minXP: number;
  maxXP: number;
  benefits: string[];
}

const levels: ProgressLevel[] = [
  { level: 1, name: 'ビギナー', minXP: 0, maxXP: 100, benefits: ['基本機能'] },
  { level: 2, name: 'ルーキー', minXP: 100, maxXP: 300, benefits: ['カスタムテーマ'] },
  { level: 3, name: 'レギュラー', minXP: 300, maxXP: 600, benefits: ['優先サポート'] },
  { level: 4, name: 'エキスパート', minXP: 600, maxXP: 1000, benefits: ['ベータ機能アクセス'] },
  { level: 5, name: 'マスター', minXP: 1000, maxXP: Infinity, benefits: ['コミュニティバッジ'] }
];

function getCurrentLevel(xp: number): ProgressLevel {
  return levels.find(l => xp >= l.minXP && xp < l.maxXP) || levels[levels.length - 1];
}

function ProgressTracker({ xp }: { xp: number }) {
  const level = getCurrentLevel(xp);
  const nextLevel = levels[level.level] || level;
  const progress = ((xp - level.minXP) / (level.maxXP - level.minXP)) * 100;

  return (
    <div className="progress-tracker">
      <div className="level-info">
        <span className="level-badge">Lv.{level.level}</span>
        <span className="level-name">{level.name}</span>
      </div>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${Math.min(progress, 100)}%` }}
        />
      </div>

      <div className="xp-info">
        {xp} / {level.maxXP} XP
      </div>

      {level.level < levels.length && (
        <div className="next-benefit">
          次のレベルで解放: {nextLevel.benefits[0]}
        </div>
      )}
    </div>
  );
}
```

---

## Loyalty Program Template

```markdown
## Loyalty Program: [Program Name]

### Point Earning
| Action | Points | Frequency Limit |
|--------|--------|-----------------|
| 日次ログイン | 10 | 1回/日 |
| プロジェクト作成 | 50 | 無制限 |
| タスク完了 | 5 | 無制限 |
| 友達紹介 | 500 | 10回/月 |
| レビュー投稿 | 100 | 1回 |
| ストリーク7日 | 70 | 1回/週 |

### Point Redemption
| Reward | Points | Description |
|--------|--------|-------------|
| 1ヶ月無料 | 1000 | プレミアム1ヶ月分 |
| 限定テーマ | 500 | 特別デザインテーマ |
| ストリーク保護 | 200 | 1回分の保護 |
| プレミアム機能お試し | 300 | 7日間のプレミアム体験 |

### Tier System
| Tier | Points/Year | Benefits |
|------|-------------|----------|
| Bronze | 0-999 | 基本特典 |
| Silver | 1000-4999 | +10%ボーナスポイント |
| Gold | 5000-9999 | +20%ボーナス、優先サポート |
| Platinum | 10000+ | +30%ボーナス、限定機能 |
```
