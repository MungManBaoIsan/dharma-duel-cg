# Reasoning: Card Database Design

## Goal

Design a card database structure that made each of the 40 Buddhist figures a complete, educational artefact — not just a row of stats. The brief called for a name, an archetype subtitle, a 2–3 bullet fact file, a 1–2 line famous story, and 6 comparative stats. The fact file and story were intentional: the game should teach as players play, not just reward mechanical stat optimisation. Players who pause to read should leave with real knowledge about a Buddhist figure.

## Iteration history

The first version had 39 cards and used Mythic Significance as the sixth stat (see `stat-system-redesign` for that iteration). The card count grew to 40 specifically so each player would start with exactly 20 cards — a clean, even split that mattered for Pass & Play fairness.

Strategic additions across v2.8–v2.9:
- **Kisa Gotami** — added as a "trap card" (Power 45) to increase skill ceiling and reward players who remember the deck
- **Emperor Ashoka** — added to represent the post-Buddha spread of the Dharma and give non-monastic power a Gold-tier card
- **Sujata** — added as a second trap card (Power 35) and to represent the role of lay generosity in enabling the Buddha's enlightenment
- **Amrapali** — added to show Transformation 98 (courtesan to arahant) and improve female representation
- **Devaputra Mara** — added to expand the Mara faction and introduce a double-trap card (low Transformation and Merit)

Individual Five Ascetics cards (Kondanna, Bhaddiya, Vappa, Mahanama, Assaji) were removed. Añña Kondañña was re-added as a separate named card with his own story as the first arahant after the Buddha.

## Failure modes the final version handles

- **Generic praise in fact files** — early versions sometimes said things like "was a great teacher." The prompt now specifies "historically specific claims" and the rubric flags generic phrases.
- **Missing fields** — early JSON had inconsistent key names. The prompt now specifies all required keys explicitly.
- **Non-extensible structure** — using JSON (rather than embedded Python dicts) means the card database can be edited without touching code, making it accessible to non-programmers who want to add cards.

## Outcome

40 cards in `data/cards.json`, each with all required fields. The database became the single authoritative source driving all other systems: the UI renderer, the card viewer, the ranking system, and the tier display. Adding a new card requires only a new JSON object — no code changes needed.

## What I'd change next

Some fact files are stronger than others — the more famous figures (Buddha, Angulimala) have richer stories than minor figures (Channa, Nanda). A review pass specifically to enrich the weaker fact files would improve educational depth.

## Tags

`content-generation` `game-design` `data-modeling` `buddhist-history`
