# Game Concept — Dharma Duel CG

> **Category:** game-design
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game (initial scoping)
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Establishes the complete project scope for a Top Trumps–style card game built around 40 Buddhist figures from ancient India — setting format, deliverables, character roster, stat names, and release strategy before any code is written.

## The prompt

```
A Top Trump inspired card game during the time of Buddha in Ancient India as context.
So like Star Wars Top Trumps, this game should include various characters including
Buddha's disciples, Buddha & Siddhartha Gautama etc.

Code Style:
I would like both: Clean, professional code structured in a way that could realistically scale.
Inline comments where learning value is high, especially around Pygame loops, rendering,
and event handling. Separate documentation (markdown or similar) describing architecture,
file layout, how to add new cards, and how to run the game.

Deliverables:
- Main game file (main.py)
- Card data stored separately (JSON preferred)
- Assets folder containing placeholder card images, fonts, optional sound placeholders
- A Card class/module (card.py)
- A Game logic module (game.py)
- A separate module for UI/menu system
- Documentation: README.md and cards.md

Scope: Iterative releases.
v1.0 Minimal playable prototype (load card database, display two cards, compare selected stats,
basic win/lose flow, very simple UI)

Stat names: Power, Wisdom, Resolve, Influence, Transformation, Mythic Significance

Characters:
Family & Early Life: Siddhartha Gautama (The Prince), King Suddhodana, Queen Maya,
Mahapajapati Gotami, Yasodhara, Rahula, Devadatta, Nanda.
First Students & Early Disciples: The 5 Ascetics (one card), Kondanna, Bhaddiya, Vappa,
Mahanama, Assaji.
Two Chief Disciples: Sariputta, Maha Moggallana.
Other Great Disciples: Maha Kassapa, Ananda, Anuruddha, Channa, Upali, Angulimala.
Famous Female Disciples: Khema, Uppalavanna, Visakha, Queen Mallika.
Important Royal Figures: King Bimbisara of Magadha, King Pasenadi.
Donors & Supporters: Anathapindika.
Mythic, Cosmic & Supernatural: Mara & His Retinue, Mara's Daughters, Mara's Army.
Nagas: Mucalinda Naga, Naga Kings.
Devas: Sakka (Indra) King of Devas, Four Great Kings, Pajapati/Mahabrahma.
Jataka Legend: Vessantara.
The Enlightened Sage: Buddha.

Each card at top has a fact file 2-3 points & at bottom a famous story 1-2 lines.
Call it Dharma Duel Card Game (DharmaDuelCG).
Game mechanics: Traditional Top Trumps.
```

## Inputs

- Character roster (provided by user from Buddhist knowledge and research)
- Stat framework (6 stats, named by user)
- Code style preferences (verbose inline comments, separate documentation)
- Scope boundary (iterative releases, v1.0 prototype first)

## Expected output

A complete v1.0 project scaffold: `main.py`, `game.py`, `card.py`, `ui.py`, `data/cards.json` (39 cards), `requirements.txt`, `README.md`, `docs/cards.md`. Each card in the JSON must have name, archetype, fact_file (list), famous_story, and six stat fields.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
