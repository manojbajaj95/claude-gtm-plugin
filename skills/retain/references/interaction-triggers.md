# Retain Interaction Triggers

Question templates for user decision points.

---

## Trigger Summary

| Trigger | Timing | When to Ask |
|---------|--------|-------------|
| ON_STRATEGY_SELECTION | BEFORE_START | Choosing retention strategy |
| ON_NOTIFICATION_CAMPAIGN | ON_RISK | Designing notification campaigns |
| ON_GAMIFICATION | ON_DECISION | Adding gamification elements |
| ON_LOYALTY_PROGRAM | ON_DECISION | Designing loyalty/reward programs |
| ON_CHURN_INTERVENTION | ON_RISK | Intervening with at-risk users |

---

## Question Templates

### ON_STRATEGY_SELECTION

```yaml
questions:
  - question: "Please select a retention improvement approach."
    header: "Improvement Strategy"
    options:
      - label: "Habit formation (Recommended)"
        description: "Create mechanisms to encourage regular usage"
      - label: "Re-engagement"
        description: "Bring back churned users"
      - label: "Loyalty program"
        description: "Reward continued usage"
      - label: "Onboarding improvement"
        description: "Prevent early churn"
    multiSelect: false
```

### ON_NOTIFICATION_CAMPAIGN

```yaml
questions:
  - question: "Please select re-engagement notification frequency."
    header: "Notification Frequency"
    options:
      - label: "Conservative (Recommended)"
        description: "Up to once a week, only valuable notifications"
      - label: "Standard"
        description: "2-3 times per week, personalized notifications"
      - label: "Aggressive"
        description: "Daily, multi-channel notifications"
    multiSelect: false
```

### ON_GAMIFICATION

```yaml
questions:
  - question: "Please select gamification elements."
    header: "Gamification"
    options:
      - label: "Progress display"
        description: "Progress bars, achievement indicators"
      - label: "Streaks"
        description: "Consecutive usage day count"
      - label: "Badges/Achievements"
        description: "Titles awarded for accomplishments"
      - label: "Leaderboard"
        description: "Ranking between users"
    multiSelect: true
```
