# Archetype Naming System

> **Category:** content-generation
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game — card identity
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Replaces AI-generated generic archetype labels with user-selected names that are both theologically accurate and clear to non-expert players. Also establishes the Legend card system (4 cards with gold borders and star icons).

## The prompt

```
[After reviewing AI-generated options for all archetype categories]

Buddha: B (The Awakened One) — make it a shiny legend card
Chief Disciples: A (Chief Disciples)
Five Ascetics group: A (First Sangha) — group card
Individual Five: remove individual cards, add Añña Kondañña as separate Foremost Disciple
Great Disciples: A (Foremost Disciples) — Angulimala: Redeemed Disciple (shiny legend card)
Bhikkhunis: Chief Bhikkhunis
Laywomen: Different — Chief Laywomen
Family: The Sakya Clan
Siddhartha: The Bodhisatta — shiny legend card
Yasodhara: The Sakya Clan
Rahula: Same as Foremost Disciples — update stats to arahant Rahula (not the boy)
Devadatta: The Adversary
Kings: A (Royal Patrons)
Anathapindika: A (Foremost Donor)
Vessantara: B (Jātaka Legend) — shiny legend card
Mara group: Forces of Māra (group cards — Mara & His Retinue, Mara's Daughters, Mara's Army)
Nagas: A (Nāga Protectors)
Devas: D (Deva Protectors)
```

## Inputs

- AI-generated candidate archetype names (presented as multiple-choice options)
- User's theological knowledge to judge accuracy
- User's preference for clarity to non-expert players

## Expected output

Updated `cards.json` with new archetype values. Four cards marked `legend: true` with visual gold-border treatment in the UI. Individual Five Ascetics removed; Añña Kondañña added as a named card. Rahula's stats updated to reflect adult arahant attainment.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
- Versions: [`versions/v1-original-archetypes.md`](./versions/v1-original-archetypes.md)
