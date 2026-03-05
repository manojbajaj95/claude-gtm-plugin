# TEMPLATES (User Onboarding)

Copy/paste the templates below. Keep everything in plain language; avoid jargon in user-facing copy.

## 1) Onboarding Brief (context + goal)

**Product:**  
**Segment(s):**  
**Stage:** pre-PMF / early PMF / growth / mature  
**Platform(s):** web / iOS / Android / desktop  
**FTUE entry point:** (e.g., invite link, app store, marketing site → signup)  

**Goal (baseline → target by date):**  
**Primary metric:**  
**Guardrails:** (support tickets, drop-off, revenue, performance, unsubscribes)  

**Constraints:** (timebox, capacity, policies, privacy/legal/brand)  
**Non-goals / “do not do” list:**  

## 2) FTUE Journey Map (step-by-step)

| Step # | User goal | What the product asks | Value delivered (if any) | Friction / confusion | Current metric (event/proxy) |
|---:|---|---|---|---|---|
| 1 |  |  |  |  |  |

### Friction Log

| Friction | Where it happens | Likely cause | Severity (H/M/L) | Fix idea (short) |
|---|---|---|---|---|
|  |  |  |  |  |

## 3) Activation / “Aha Moment” Spec

**Candidate aha behaviors (3–5):**
- 1)
- 2)
- 3)

**Chosen activation definition (behavioral):**  
**Threshold / time window:** (e.g., “does X twice within 7 days”)  
**Why this is value (user POV):**  
**Why this predicts retention (business POV):**  

**Validation plan:**
- Correlate activation with D7/D30 retention (by segment)
- If possible: experiment/holdout to test causality

**Instrumentation requirements:** (events + properties you must track)

## 4) First 30 Seconds Spec (“make it feel magical”)

**Entry context:** (new user path, permissions, default state)  
**One-sentence promise:** (what the user will get right away)  
**The “win” in 30 seconds:** (what the user accomplishes)  

**Script (what happens):**
1) User sees…
2) User does…
3) Product responds with…
4) Next step CTA is…

**Design principles:**
- Defer non-essential questions (progressive disclosure)
- Prefer interactive doing over passive reading
- Provide instant feedback + visible progress

**Success criteria (measurable):**
- Time-to-first-win: ___ seconds
- % users reaching first-win event: ___
- Guardrail(s): ___

## 5) First Mile Plan (milestones → activation)

**Milestones (3–6):**

| Milestone # | User intent | Product mechanic(s) | What “done” looks like | Leading indicator metric |
|---:|---|---|---|---|
| 1 |  |  |  |  |

**Notes:**
- Each milestone should use real product actions (avoid “tour-only” steps).
- Use defaults/templates/demo data to reduce blank-state pain.

## 6) Experiment Backlog (prioritized)

Scoring: **Impact × Confidence ÷ Effort** (1–5 each).

| Rank | Experiment | Hypothesis | Primary metric | Guardrail | ICE score | Effort notes |
|---:|---|---|---|---|---:|---|
| 1 |  |  |  |  |  |  |

### Experiment Card

**Name:**  
**Problem / insight:**  
**Hypothesis:** If we ___ then ___ because ___.  
**Change:** (what exactly changes in product)  
**Audience:** (segment, new vs returning, platform)  
**Primary metric:**  
**Guardrails:**  
**Instrumentation:** (events/properties needed)  
**Duration / sample:**  
**Rollout:** (feature flag, % ramp, holdout)  
**Rollback plan:**  
**Risks / edge cases:**  

## 7) Measurement + Instrumentation Plan

**Key definitions:**
- Signup completion = …
- First key action = …
- First-win event = …
- Activation event = …

**Event schema (minimum viable):**

| Event | When fired | Key properties | Used in |
|---|---|---|---|
| signup_started |  |  | funnel |
| signup_completed |  |  | funnel |
| first_win_completed |  |  | time-to-value |
| activated |  |  | activation rate |

**Dashboards to create:**
- FTUE funnel (by segment/platform)
- Time-to-first-win distribution (median/p75)
- Activation rate + early retention (D1/D7) by segment
- Guardrails (support tickets, performance, unsubscribes)

## 8) Rollout / Rollback Plan

**Release mechanism:** feature flag / staged rollout / A/B test  
**Ramp plan:** 0% → 10% → 50% → 100% with checkpoints  
**Monitor:** primary metric + guardrails + errors/perf  
**Rollback trigger:** (what number or signal forces rollback)  
**Comms:** (internal + external if needed)  

