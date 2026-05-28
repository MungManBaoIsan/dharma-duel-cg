# v1 — Alternating Turns (replaced)

The initial turn system alternated turns regardless of who won the previous round.

## The logic

```python
# OLD: Next player always alternates
next_active = 'computer' if self.active_player == 'player' else 'player'
self.active_player = next_active
```

## Why it was wrong

1. **Not how Top Trumps works.** The traditional rule is: winner controls the next round. Alternating is incorrect.
2. **Removed momentum.** Winning a round should reward you with another turn to build on. Alternating gave no strategic reward for smart stat choices.
3. **Created confusion.** Players expected "if I win, it's my turn again" — the alternating behaviour felt broken.

## Replaced by

Winner-controls logic in `game.py:resolve_round()`:

```python
# NEW: Winner becomes active player
if self.round_winner == 'player':
    self.active_player = 'player'
elif self.round_winner == 'computer':
    self.active_player = 'computer'
```
