# Prompt Library — Dharma Duel Card Game

[![Prompt Eval](https://github.com/joshuablakemorekay/dharma-duel-cg/actions/workflows/prompt-eval.yml/badge.svg)](https://github.com/joshuablakemorekay/dharma-duel-cg/actions/workflows/prompt-eval.yml)

This folder documents the prompts used to build **Dharma Duel Card Game** — a Pygame Top Trumps game featuring 40 Buddhist figures from ancient India, developed from v1.0 to v2.9 using Claude as a coding and design collaborator.

Each prompt directory contains the final version, the reasoning behind it, an executable evaluation rubric, and version history where the prompt was refined over time. Every rubric runs on every push via GitHub Actions.

---

## Index

| Prompt | Category | What it does | Iterated? |
|--------|----------|--------------|-----------|
| [`game-concept`](./game-concept/) | game-design | Establishes full project scope: format, character roster, stat names, file structure, iterative release plan | No |
| [`card-database-design`](./card-database-design/) | content-generation | Generates all 40 card records as JSON — name, archetype, fact file, famous story, 6 stats, tier, rating | Yes |
| [`stat-system-redesign`](./stat-system-redesign/) | analysis | Replaces Mythic Significance with Merit, grounded in the Four Stages of Enlightenment and Etadagga Sutta | Yes (v1→v2) |
| [`archetype-naming`](./archetype-naming/) | content-generation | Replaces generic AI labels with user-selected archetypes accurate to Buddhist theology and clear to non-experts | Yes (v1→v2) |
| [`game-mechanics`](./game-mechanics/) | code-generation | Implements traditional Top Trumps rules: winner controls, card hiding, battle pile, Pass & Play | Yes (v1→v7) |
| [`balance-tuning`](./balance-tuning/) | game-design | Tunes Buddha from all-100s to a balanced profile; adds tier system and overall ratings | Yes (v1→v4) |
| [`ai-and-ui-features`](./ai-and-ui-features/) | code-generation | Implements 4 AI difficulty levels, card viewer with rankings, Dharma Council story, Dharmachakra wheel | Yes (v1→v3) |

---

## Featured iterations

Prompts where the v1 → final journey shows the most learning:

### [`stat-system-redesign`](./stat-system-redesign/)

The sixth stat started as "Mythic Significance" — a label that sounded good but had no canonical source. When asked "how accurate are these stats?", the answer was ~50–60% for that stat alone. The prompt was rewritten to replace it with **Merit**, grounded in the Four Stages of Enlightenment (Sotāpanna → Sakadāgāmī → Anāgāmī → Arahant → Buddha). Every Merit score is now cross-referenced against the Etadagga Sutta (AN 1.188–234). Accuracy rose to ~85–90%. The change also made the game more educational: a player looking at Angulimala's Merit 98 can now understand he reached full arahantship.

### [`game-mechanics`](./game-mechanics/)

The mechanics went through 7 iterations. v1 alternated turns (wrong — real Top Trumps gives control to the winner). v2–v3 implemented the correct rule but didn't hide opponent cards. v4 added the battle pile for ties. v5 fixed the most subtle bug in the project: Player 2's card was hardcoded to non-clickable (the stat buttons were always on the left card), so Player 2 in Pass & Play could never actually select their own stats. v6 replaced the auto-advance timer with a manual Next Round button (educational game → players need time to read cards). v7 fixed phantom auto-advance clicks caused by stale events in the Pygame queue. The arc from v1 to v7 is a clear demonstration of iterative debugging with increasing understanding of how Pygame's event system works.

### [`balance-tuning`](./balance-tuning/)

Buddha started at all-100s — literally unbeatable on any stat. Through 4 iterations combining theological reasoning (Power 95: non-violent; Influence 90: renounced politics) with gameplay testing (10,000-game simulation), the final stats achieved a 49.4% vs 50.6% win rate. The balance was initially a surprise — the theological adjustments happened to produce near-perfect odds — which then became a deliberate target. This iteration story shows how domain knowledge (Buddhist theology) and quantitative testing (simulation) can be used together to produce good game design.

---

## Skills demonstrated

- [x] **Prompt design** — every prompt has a documented goal and structure
- [x] **Iteration** — see `versions/` subdirectories for prompts that were refined
- [x] **Domain grounding** — prompts use canonical Buddhist sources (Etadagga Sutta, Four Stages) rather than AI invention
- [x] **Evaluation** — every prompt has a rubric with executable pass conditions
- [x] **Automated testing** — rubrics run on every push via [`prompt-eval.yml`](../.github/workflows/prompt-eval.yml)
- [x] **Debugging discipline** — game-mechanics documents 7 iterations of progressive bug discovery and fixes
- [x] **Documentation** — every prompt has a REASONING.md explaining the *why*, not just the *what*

---

## How to read this folder

- **90 seconds:** read this index, then skim the Featured Iterations section above.
- **5 minutes:** read this index plus the REASONING.md for `stat-system-redesign` and `game-mechanics`.
- **Longer:** read [CHANGELOG.md](./CHANGELOG.md) for the full iteration story, then run the eval runner.

## Running the evaluations locally

```bash
pip install pyyaml
python3 scripts/eval_runner.py --provider mock
```

This validates every prompt against its rubric using deterministic fixtures — no API costs. See [`results-summary.md`](./results-summary.md) for the latest run.

To run against the real API: set `ANTHROPIC_API_KEY` and pass `--provider anthropic`.

## Changelog

See [`CHANGELOG.md`](./CHANGELOG.md) for a chronological view of prompt evolution.
