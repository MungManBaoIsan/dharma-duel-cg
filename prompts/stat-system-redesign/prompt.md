# Stat System Redesign — Merit replaces Mythic Significance

> **Category:** analysis
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game — card data accuracy
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Replaces the sixth stat (Mythic Significance) with Merit — a canonically grounded Buddhist concept — and recalculates all 40 cards' sixth-stat values using the Four Stages of Enlightenment as a scoring scale.

## The prompt

```
Can you change mythic significance to a better universal stat?

For Action Items: Recalculate Merit values for all cards.

Merit should be based on the Four Stages of Enlightenment from the Pali Canon:

Merit scale:
  100 = Sammā-Sambuddha (perfectly self-enlightened)
  95-98 = Arahant (fully enlightened, all 10 fetters destroyed)
  85-92 = Non-returner (Anāgāmī, 5 lower fetters destroyed)
  75-82 = Once-returner (Sakadāgāmī)
  65-72 = Stream-enterer (Sotāpanna, 3 fetters destroyed)
  55-65 = Devoted practitioners (strong practice, not yet stream-entry)
  45-55 = Good lay supporters (dana, sila)
  35-45 = Early practitioners / mixed karma
  20-35 = Beings with much defilement
  10-20 = Antagonists, harmful beings

Cross-reference with the Etadagga Sutta (AN 1.188-234) which lists the
"foremost disciples" — use this as the primary source for assigning
attainment levels to named disciples.
```

## Inputs

- Existing 39-card database with Mythic Significance values
- Four Stages of Enlightenment canonical scale
- Etadagga Sutta (AN 1.188–234) as primary source

## Expected output

Updated `cards.json` where every card has a `merit` field (replacing `mythic_significance`) with values derived from the canonical scale. A `MERIT_SYSTEM.md` documentation file explaining the scale and each assignment.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
- Versions: [`versions/v1-mythic-significance.md`](./versions/v1-mythic-significance.md)
