# Reasoning: Balance Tuning — Buddha Stats and Tier System

## Goal

Make the game strategically balanced: no card should auto-win on any chosen stat, Buddha should feel supreme without being unbeatable, and the overall win rate between players should be as close to 50/50 as possible.

## Iteration history

**v1 — Buddha at all 100s:** Every stat at 100. Primary problem: a card that wins on any chosen stat removes all strategic decision-making. Secondary problem: Power 100 doesn't fit a figure who explicitly renounced violence, and Influence 100 doesn't fit a figure who renounced political power.

**v2 — Option 1 contextual weaknesses (Power 97, Influence 85):** Lowered the two stats with the clearest theological justification. Power 97 still left Buddha as effectively unbeatable on Power (Moggallana is 95). Influence 85 created a genuine weak point — 7 cards could beat him there.

**v3 — Power reduced to 95:** Now ties with Moggallana and Mara on Power, creating tie-battle opportunities. Thematically: Buddha commands the highest spiritual/psychic power but not martial/physical dominance.

**v4 — Wisdom raised to 100, Influence raised to 90:** Buddha is the "Perfectly Self-Enlightened One" — Wisdom 100 is correct. Influence 90 better reflects founding a world religion that shaped Asian civilisation for 2,500 years, while remaining beatable by Emperor Ashoka (95).

Final stats: Power 95 / Wisdom 100 / Resolve 100 / Influence 90 / Transformation 100 / Merit 100 = rating 97.5.

**Tier system added:** Bronze/Silver/Gold/Platinum tiers with colour-coded borders gave players immediate visual feedback on card strength without needing to calculate from six stats. Rating badge (top-right corner, coloured by tier) served both functions: quick assessment and rarity excitement when drawing a Gold or Platinum card.

**10,000-game simulation:** Run to verify overall balance. Result: 49.4% player wins vs 50.6% computer wins — a 1.2% difference. This was a surprise (balance was not consciously targeted through all the individual stat changes), which then became a deliberate design goal to maintain through subsequent card additions.

## Failure modes the final version handles

- **All-100s Buddha:** Any stat chosen = win, no strategy required.
- **Over-nerfed Buddha:** A Buddha below ~85 average would feel wrong and undermine the game's narrative.
- **Unknown card strength:** Without the overall rating and tier badge, players had to mentally average 6 stats to assess a card. The visual system makes this instant.

## Outcome

49.4% vs 50.6% win rate across 10,000 simulated games. Buddha wins ~75–80% of rounds when drawn but is present in only ~2.5% of starting hands, so his impact on global balance is limited. The tier hierarchy (1 Platinum, 7 Gold, 20 Silver, 12 Bronze) creates a collectible-like feeling — Gold cards feel rewarding, Bronze cards feel like underdogs.

## What I'd change next

Trap cards (Sujata Power 35, Devaputra Mara Transformation 25) reward card-memory but punish new players who don't know about them. An optional hint system or first-play tutorial flagging the trap stats would help beginners without removing the strategic depth.

## Tags

`game-design` `analysis` `code-generation`
