# Retain Habit Formation Design

Hook Model and streak system implementation.

---

## Hook Model Implementation

```markdown
## Hook Model: [Feature/Behavior]

### 1. Trigger (きっかけ)
**External Triggers:**
- Push notification at [time]
- Email digest on [day]
- Calendar reminder

**Internal Triggers:**
- Emotion: [感情/状況] → Product
- Routine: [日課] → Product

### 2. Action (行動)
**Target Behavior:** [最小限の行動]
**Motivation:** [なぜやりたいか]
**Ability:** [どれだけ簡単か]

### 3. Variable Reward (変動報酬)
| Type | Example |
|------|---------|
| Tribe (社会的) | 他ユーザーからのリアクション |
| Hunt (獲得) | 新しいコンテンツの発見 |
| Self (達成) | 進捗の可視化、スキル向上 |

### 4. Investment (投資)
**User invests:**
- 時間（コンテンツ作成）
- データ（プロフィール情報）
- ソーシャル（フォロー/フォロワー）
- 学習（使い方の習得）
```

---

## Streak System Implementation

```typescript
// lib/streaks.ts
interface StreakData {
  userId: string;
  currentStreak: number;
  longestStreak: number;
  lastActivityDate: string;
  streakProtectsRemaining: number;
}

async function updateStreak(userId: string): Promise<StreakData> {
  const streak = await getStreak(userId);
  const today = new Date().toISOString().split('T')[0];
  const lastDate = streak.lastActivityDate;

  const daysDiff = dateDiff(lastDate, today);

  if (daysDiff === 0) {
    // Already active today
    return streak;
  }

  if (daysDiff === 1) {
    // Consecutive day
    streak.currentStreak += 1;
    streak.longestStreak = Math.max(streak.longestStreak, streak.currentStreak);
  } else if (daysDiff === 2 && streak.streakProtectsRemaining > 0) {
    // Missed one day but has protection
    streak.streakProtectsRemaining -= 1;
    streak.currentStreak += 1;
    trackEvent('streak_protected', { streak: streak.currentStreak });
  } else {
    // Streak broken
    trackEvent('streak_broken', {
      streak: streak.currentStreak,
      longestStreak: streak.longestStreak
    });
    streak.currentStreak = 1;
  }

  streak.lastActivityDate = today;
  await saveStreak(streak);

  // Check for milestone
  if ([7, 30, 100, 365].includes(streak.currentStreak)) {
    await awardStreakMilestone(userId, streak.currentStreak);
  }

  return streak;
}

// React component
function StreakDisplay({ streak }: { streak: StreakData }) {
  return (
    <div className="streak-display">
      <div className="current-streak">
        🔥 {streak.currentStreak}日連続
      </div>
      {streak.streakProtectsRemaining > 0 && (
        <div className="streak-protects">
          🛡️ {streak.streakProtectsRemaining}回の保護あり
        </div>
      )}
      <div className="longest-streak">
        最長記録: {streak.longestStreak}日
      </div>
    </div>
  );
}
```
