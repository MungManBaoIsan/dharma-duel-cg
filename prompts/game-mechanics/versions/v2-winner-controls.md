# v2 — Winner Controls (current)

The winner of each round becomes the active player for the next round and selects the stat.

## The logic

```python
# In game.py:resolve_round()
if self.round_winner == 'player':
    self.active_player = 'player'
elif self.round_winner == 'computer':
    self.active_player = 'computer'
# On tie: active_player unchanged (same player retains control for battle)
```

## Pass & Play mapping

In Pass & Play, "player" = Player 1 (left), "computer" = Player 2 (right). The internal labels are an implementation detail — the game always labels them correctly in the UI as "PLAYER 1" and "PLAYER 2".

## Clickability in Pass & Play

```python
# Player 1's card (left): clickable only on Player 1's turn
is_clickable = (active_player == 'player' and result is None)

# Player 2's card (right): clickable only on Player 2's turn in Pass & Play
is_clickable = (game_mode == 'player' and active_player == 'computer' and result is None)
```

## Status: production — used in v2.9 final
