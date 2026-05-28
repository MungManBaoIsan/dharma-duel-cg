# AI Difficulty Levels and UI Features

> **Category:** code-generation
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game — AI and UI
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Implements 4 named AI difficulty levels (Easy/Moderate/Hard/Smart), adds the Card Viewer with 9 sort options and overall rankings, adds the Story Reader with the Dharma Council epic framing, and replaces the "?" card back with a drawn Dharmachakra wheel.

## The prompt (composite)

```
I'm happy pass & play mode works great. For play against AI, should computer always
select highest stat? Or would it be better if computer used skill & made strategic
selections?

Can we add 3 Computer Modes?
1. Easy AI Mode — low odds of AI winning
2. Moderate AI Mode — medium odds of AI winning
3. Hard AI Mode — high odds of AI winning
Add a 4th mode called Smart AI Mode (behaves like a strategic human):
  60% — Picks top 2 stats (smart/aggressive)
  30% — Picks middle stats (unpredictable)
  10% — Picks weak stats (human-like mistakes)
  Unpredictable and varied. More fun and challenging!

In the card viewer, can you add a Card ranking table to show card ranks 1 to 40
(1 being overall strongest card)?

Context Story to add to main menu [epic story text]:
In the sacred groves of ancient India, a mystical tournament unfolds. The Dharma
Council has convened... [full text]

Replace hidden on the back of every card with a Dharmachakra Wheel [actual drawn
graphics, not a text character — 8 spokes, hub, decorative dots, gold on dark brown].
```

## Inputs

- Existing single-AI (always highest stat) game.py
- Card viewer without ranking sort
- Original Sāgara context story (to be replaced)
- "?" text card back (to be replaced with graphics)

## Expected output

- `game.py` with `computer_choose_stat(difficulty)` implementing 4 strategy mixes
- Difficulty selection menu between main menu and game start
- Card viewer with 9th sort option ("Ranking") showing rank column 1–40
- Story reader accessible from main menu with full Dharma Council text
- `ui.py` `draw_card_back()` using `pygame.draw.circle` and `pygame.draw.line` for wheel

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
