# Balance Tuning — Buddha Stats and Tier System

> **Category:** game-design
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game — game balance
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Tunes Buddha's stats from all-100s to a balanced but still-supreme profile, adds the tier system (Platinum/Gold/Silver/Bronze) with overall rating badges, and verifies game balance via a 10,000-game simulation.

## The prompt (composite of balance prompts)

```
How to make Buddha beatable? [reviews 5 options]

Implement Option 1 but change Power to 97.
[later]
Decrease Buddha power to 95.
[later]
Should Buddha's influence be higher? What should his stats really be?
Change Wisdom to 100 and Influence to 90.

Should all cards have an overall rating number?
Can you make lowest tier cards bronze, mid tier cards silver & high tier cards gold?
Buddha card is platinum.

Tier thresholds:
- Platinum: overall_rating >= 95
- Gold: overall_rating >= 85
- Silver: overall_rating >= 70
- Bronze: overall_rating < 70

What are the odds of winning for each player?
[runs 10,000-game simulation]
```

## Inputs

- Existing 40-card database with all-100s Buddha
- Request for beatable-but-supreme Buddha profile
- Tier boundaries defined by user
- 10,000 simulation to verify balance

## Expected output

Updated `cards.json` with Buddha at Power 95 / Wisdom 100 / Resolve 100 / Influence 90 / Transformation 100 / Merit 100 (rating 97.5). All 40 cards with `overall_rating` and `tier` fields. Simulation confirming ~49–51% win rate for each side.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
- Versions: [`versions/v1-all-100s.md`](./versions/v1-all-100s.md), [`versions/v2-final-balance.md`](./versions/v2-final-balance.md)
