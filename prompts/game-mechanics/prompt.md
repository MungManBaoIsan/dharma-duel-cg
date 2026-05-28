# Game Mechanics — Traditional Top Trumps Rules

> **Category:** code-generation
> **Model used:** claude-sonnet-4-6
> **Project area:** Dharma Duel Card Game — game logic
> **Status:** production
> **Last updated:** 2025-05-28

## What this prompt does

Establishes the correct Top Trumps game rules and implements them across VS Computer and Pass & Play modes — including winner-controls turns, card hiding, tie battle piles, manual Next Round button, and player-specific card clickability.

## The prompt (composite of key mechanics prompts)

```
Rule adjustments:
1. All players compare top card. Winner takes all top cards and puts them at the
   bottom of his/her stack. Winner starts next turn, choosing a stat.
2. If two or more players tie for best value: all tied players keep their card
   face-up, each plays the next card face-down on top ("battle pile"), the same
   player chooses a new stat from their new top card. Winner of the tie-break
   takes all cards in the middle including the built-up pile.

Not allowed to look at opponent's card before choosing stat. Hide everything.

After each round, regardless whether you win, lose, or tie, can view each other's
card before next round — no timer, just click next round.

For Pass & Play mode: I want Player 1 cards & stack always kept to the left side
of screen. Player 2 cards & stack always on the right. Player 1 is required to
select stat on Player 1 card from Player 1 deck on left side. Player 2 is required
to select stat on Player 2 card from Player 2 deck on right side. The player on
the winning streak selects the stat.
```

## Inputs

- Existing game.py with alternating-turn logic (to be replaced)
- UI with hardcoded left-card clickability (to be fixed for Pass & Play)
- Player mode flag ('computer' or 'player') passed through game state

## Expected output

- `game.py` with `resolve_round()` correctly switching `active_player` to the round winner
- `ui.py` with opponent card showing Dharmachakra wheel (fully hidden) until stat selected
- Manual `[NEXT ROUND →]` button with no auto-advance timer
- Pass & Play: Player 2's card (right side) is clickable when `active_player == 'computer'` and `game_mode == 'player'`
- `pygame.event.clear()` called on entering result state to prevent phantom clicks

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
- Versions: [`versions/v1-alternating-turns.md`](./versions/v1-alternating-turns.md), [`versions/v2-winner-controls.md`](./versions/v2-winner-controls.md)
