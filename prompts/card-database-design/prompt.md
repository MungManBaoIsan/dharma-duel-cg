# Card Database Design

> **Category:** content-generation
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game — data layer
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Generates the complete card database as a JSON file — each of the 40 Buddhist figures as a structured record containing name, archetype, tier, legend status, overall rating, six stats, a 3-bullet fact file, and a 1–2 sentence famous story.

## The prompt

```
Create the complete cards.json database with all characters, their stats, fact files,
and famous stories.

Each card must have:
- name
- archetype (subheading)
- fact_file: 2-3 bullet points of historically accurate information
- famous_story: 1-2 lines describing the character's most famous moment
- stats:
    power (physical/psychic strength, 1-100)
    wisdom (understanding, enlightenment, 1-100)
    resolve (determination, discipline, 1-100)
    influence (leadership, political power, 1-100)
    transformation (personal change, spiritual growth, 1-100)
    merit (canonical attainment level based on Four Stages of Enlightenment, 1-100)

Merit scale:
    100 = Sammā-Sambuddha (Buddha)
    95-98 = Arahant (fully enlightened)
    85-92 = Non-returner (Anāgāmī)
    75-82 = Once-returner (Sakadāgāmī)
    65-72 = Stream-enterer (Sotāpanna)
    55-65 = Devoted practitioners
    45-55 = Good lay supporters
    35-45 = Mixed karma practitioners
    20-35 = Beings with much defilement
    10-20 = Antagonists, harmful beings

Assign an overall_rating (average of all 6 stats, rounded to 1 decimal place).
Assign a tier: "platinum" if overall >= 95, "gold" if >= 85, "silver" if >= 70, "bronze" otherwise.
Mark legend: true for Buddha, Siddhartha, Angulimala, Vessantara only.

Card count: 40 total (to allow an even 20 vs 20 split).
```

## Inputs

- Character roster (40 figures, established in game-concept prompt)
- Merit scale based on Etadagga Sutta (AN 1.188–234)
- Tier thresholds (95/85/70/0)
- Legend status criteria (4 cards only)

## Expected output

A valid JSON array of 40 card objects. Each object must have all required keys. Stats must be integers 1–100. Fact files must be historically specific (not generic praise). Famous stories must reference a real canonical event.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
