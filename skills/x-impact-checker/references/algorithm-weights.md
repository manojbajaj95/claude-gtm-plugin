# X Algorithm Weight Reference

Complete reference for X's open-source recommendation algorithm (2026 version).

## Source

- **Repository**: https://github.com/xai-org/x-algorithm
- **Weighted Scorer**: `home-mixer/scorers/weighted_scorer.rs`
- **ML Model**: Phoenix (Grok-based transformer)
- **Last Updated**: January 2026

## Overview

The X recommendation algorithm uses a two-stage prediction system:
1. **Phoenix ML Model** predicts probabilities for 19+ engagement actions
2. **Weighted Scorer** combines these predictions with algorithm-defined weights to compute final ranking scores

This skill implements the scoring logic in text-based heuristic form for pre-publishing optimization.

---

## Phoenix Engagement Predictions (19 Signals)

Phoenix predicts probabilities for these user actions:

### Positive Engagement Signals (15)
```
P(favorite)              // Like button
P(reply)                 // Reply to post
P(retweet)               // Retweet/share
P(quote)                 // Quote tweet
P(click)                 // Click on any link
P(profile_click)         // Click on author profile
P(video_view)            // Video playback (VQV: Video Quality View)
P(photo_expand)          // Expand photo/media
P(share)                 // Generic share action
P(share_via_dm)          // Share via Direct Message
P(share_via_copy_link)   // Copy link to share elsewhere
P(dwell)                 // Initial reading time
P(continuous_dwell)      // Sustained attention time
P(quoted_click)          // Click on quoted tweet
P(follow_author)         // Follow the author
```

### Negative Engagement Signals (4)
```
P(not_interested)        // "Not interested in this tweet"
P(block)                 // Block author
P(mute)                  // Mute author
P(report)                // Report tweet/author
```

---

## Complete Score Calculation (19 Elements)

From `weighted_scorer.rs`:

```rust
combined_score =
    favorite_score * FAVORITE_WEIGHT                    // ~0.5
  + reply_score * REPLY_WEIGHT                          // ~1.0 (highest)
  + retweet_score * RETWEET_WEIGHT                      // ~0.75
  + quote_score * QUOTE_WEIGHT                          // ~0.45
  + click_score * CLICK_WEIGHT                          // ~0.2
  + profile_click_score * PROFILE_CLICK_WEIGHT          // ~0.2
  + video_view_score * vqv_weight(video)                // ~0.15 (conditional)
  + photo_expand_score * PHOTO_EXPAND_WEIGHT            // ~0.18
  + share_score * SHARE_WEIGHT                          // ~0.1
  + share_dm_score * SHARE_VIA_DM_WEIGHT                // ~0.1
  + share_link_score * SHARE_VIA_COPY_LINK_WEIGHT       // ~0.1
  + dwell_score * DWELL_WEIGHT                          // ~0.25
  + continuous_dwell_score * CONTINUOUS_DWELL_WEIGHT    // ~0.18
  + quoted_click_score * QUOTED_CLICK_WEIGHT            // ~0.15
  + follow_author_score * FOLLOW_AUTHOR_WEIGHT          // ~0.18
  + not_interested_score * NOT_INTERESTED_WEIGHT        // ~-0.6 (negative)
  + block_author_score * BLOCK_AUTHOR_WEIGHT            // ~-1.2 (negative)
  + mute_author_score * MUTE_AUTHOR_WEIGHT              // ~-0.6 (negative)
  + report_score * REPORT_WEIGHT                        // ~-1.5 (negative)
```

Then apply normalization:
```rust
final_score = normalize_score(offset_score(combined_score))
```

---

## Skill Weight Mapping (100-Point System)

The skill redistributes algorithm weights proportionally to create a user-friendly 100-point scale:

### Tier 1: Core Engagement (60 points)
Conversation drivers and strong sharing signals.

| Algorithm Signal | Skill Factor | Points | Rationale |
|-----------------|--------------|--------|-----------|
| REPLY_WEIGHT (1.0) | Reply Potential | 22 | Highest algorithm weight - conversations drive visibility |
| RETWEET_WEIGHT (0.75) | Retweet Potential | 16 | Strong amplification signal |
| FAVORITE_WEIGHT (0.5) | Favorite Potential | 12 | Most common action, moderate weight |
| QUOTE_WEIGHT (0.45) | Quote Potential | 10 | Commentary adds value |

### Tier 2: Extended Engagement (25 points)
Media interactions and sustained attention metrics.

| Algorithm Signal | Skill Factor | Points | Rationale |
|-----------------|--------------|--------|-----------|
| DWELL_WEIGHT (0.25) | Dwell Time | 6 | Initial reading/comprehension time |
| CONTINUOUS_DWELL_WEIGHT (0.18) | Continuous Dwell Time | 4 | Sustained attention beyond initial read |
| CLICK_WEIGHT (0.2) | Click Potential | 5 | External link engagement |
| PHOTO_EXPAND_WEIGHT (0.18) | Photo Expand Potential | 4 | Visual content engagement |
| VQV_WEIGHT (0.15) | Video View Potential | 3 | Video engagement (conditional on duration) |
| QUOTED_CLICK_WEIGHT (0.15) | Quoted Click Potential | 3 | Investigation of quoted source |

### Tier 3: Relationship Building (15 points)
Author discovery and long-term value signals.

| Algorithm Signal | Skill Factor | Points | Rationale |
|-----------------|--------------|--------|-----------|
| PROFILE_CLICK_WEIGHT (0.2) | Profile Click | 5 | Author discovery interest |
| FOLLOW_AUTHOR_WEIGHT (0.18) | Follow Potential | 4 | Long-term relationship signal |
| SHARE_WEIGHT (0.1) | Share Potential | 2 | Generic sharing |
| SHARE_VIA_DM_WEIGHT (0.1) | Share via DM | 2 | Personal 1-on-1 sharing |
| SHARE_VIA_COPY_LINK_WEIGHT (0.1) | Share via Copy Link | 2 | Reference/bookmark sharing |

### Negative Signals (Penalties)
Subtract from total score based on risk assessment.

| Algorithm Signal | Skill Factor | Range | Rationale |
|-----------------|--------------|-------|-----------|
| NOT_INTERESTED_WEIGHT (-0.6) | Not Interested Risk | -5 to -15 | Mild negative signal |
| MUTE_AUTHOR_WEIGHT (-0.6) | Mute Risk | -5 to -15 | Author-level negative |
| BLOCK_AUTHOR_WEIGHT (-1.2) | Block Risk | -10 to -25 | Strong negative signal |
| REPORT_WEIGHT (-1.5) | Report Risk | -15 to -30 | Severe policy violation |

---

## Conditional Logic

### VQV Weight Eligibility (Video Quality View)

From `weighted_scorer.rs`:

```rust
fn vqv_weight_eligibility(video_duration_ms: Option<u64>) -> f64 {
    video_duration_ms
        .is_some_and(|dur| dur > MIN_VIDEO_DURATION_MS)
        .then_some(VQV_WEIGHT)
        .unwrap_or(0.0)
}
```

**Logic:**
- VQV weight (0.15) only applies if video duration > ~5000ms (5 seconds)
- Short clips don't receive full video engagement credit
- Encourages long-form, high-quality video content

**Skill Implementation:**
Since text analysis cannot detect actual video duration, the skill infers from language:
- "Full tutorial", "in-depth", "complete guide" → assumes >5s (full 3 points)
- "Quick clip", "snippet", "short demo" → assumes <5s (reduced scoring)
- No video markers → 0 points

---

## Score Normalization

### Offset Score Function

Balances positive and negative signals differently:

```rust
fn offset_score(raw_score: f64) -> f64 {
    if raw_score < 0.0 {
        raw_score * NEGATIVE_OFFSET_MULTIPLIER  // ~0.3
    } else {
        raw_score + POSITIVE_OFFSET
    }
}
```

**Purpose:**
- Dampens negative signals to prevent single bad signals from dominating
- Adds baseline boost to positive scores
- Creates more balanced final rankings

### Normalize Score Function

Maps to final range:

```rust
fn normalize_score(score: f64) -> f64 {
    score.max(MIN_SCORE).min(MAX_SCORE)
}
```

**Skill Implementation:**
```
Final Score = Base Score (0-100) + Penalties (-75 to 0)
Normalized = max(0, min(100, Final Score))
```

**Penalty Capping:**
- Total penalties ≤ -20: Applied at full weight
- Total penalties > -20: Gradual dampening
- Total penalties > -75: Hard cap at -75

Prevents over-penalization while maintaining signal importance.

---

## Key Algorithm Insights

1. **Conversations Dominate**
   Reply weight (1.0) is 2× retweet (0.75), 4× video view (0.15). Posts that drive replies rank highest.

2. **Share Actions Split**
   Generic share, DM share, and link copy are tracked separately—each indicates different sharing intent and value.

3. **Time-Based Signals**
   Dwell time (initial) and continuous dwell (sustained) are separate signals. Complexity rewards re-reading.

4. **Media Requires Quality**
   Video view scoring is conditional on duration. Low-effort clips don't get full credit.

5. **Negative Weights Matter**
   Block (-1.2) and report (-1.5) have strong negative impact. Content must avoid triggering these.

6. **Author Value Tracked**
   Profile click and follow indicate author-level interest, not just post-level.

7. **Multi-Action Prediction**
   Algorithm doesn't predict "relevance" but predicts 19 specific action probabilities, each weighted differently.

---

## Text Analysis Limitations

### What This Skill Cannot Detect

Since this is **heuristic text analysis**, not ML prediction:

**Missing Metadata:**
- Actual media presence (photos, videos)
- Real video duration or quality
- Actual click-through rates
- True engagement history
- Author reputation/follower count
- Tweet timestamps or virality metrics

**Cannot Access:**
- Phoenix ML model predictions
- User interaction history
- Network graph relationships
- Real-time engagement signals

### What This Skill Infers From

**Text-Based Heuristics:**
- Language patterns and structure
- Content formatting (threads, lists, etc.)
- Emotional tone and style
- Visual indicators (emojis, markdown)
- Call-to-action strength
- Question vs. statement structure

**Scoring Approach:**
- **Conservative**: Unknown elements get baseline scores
- **Pattern-Based**: Detects language cues (e.g., 📸 for photos, 🧵 for threads)
- **Optimization-Focused**: Best used for pre-publishing content improvement

**Best Use Case:**
Pre-publishing optimization to maximize engagement potential, not post-hoc analytics.

---

## Algorithm Version

- **Based on**: X Algorithm open-source release (xai-org/x-algorithm)
- **Reference Date**: January 2026
- **Implementation**: Heuristic skill (not direct code port)
- **Weights**: Approximated from `weighted_scorer.rs`

**Note**: Actual X algorithm may evolve. This skill reflects the publicly documented version as of 2026.

---

## References

- X Algorithm Repository: https://github.com/xai-org/x-algorithm
- Weighted Scorer Implementation: `home-mixer/scorers/weighted_scorer.rs`
- Phoenix ML Model: Grok-based transformer (not publicly released)
- Skill Implementation: [SKILL.md](../SKILL.md)
