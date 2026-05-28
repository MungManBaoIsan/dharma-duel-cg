# Reasoning: Game Mechanics — Traditional Top Trumps Rules

## Goal

Implement correct Top Trumps game rules and make both game modes (VS Computer and Pass & Play) feel fair and well-paced. The core rules are: winner controls the next round, same stat compares both cards, ties go to a battle pile, winner takes all accumulated cards.

## Iteration history

**v1 — Alternating turns:** The initial implementation alternated turns regardless of who won. This was wrong for two reasons: it's not how real Top Trumps works, and it removed momentum — a player who made a smart stat choice got no reward for it.

**v2 — Winner controls:** Changed to the correct rule: the winner of each round selects the stat for the next round. This happened to also make the game more exciting, since winning streaks are earned by skill and create genuine momentum.

**v3 — Card hiding:** The opponent's card was initially visible before stat selection (showing name and archetype). Fixed so only the active player's card shows stats; the opponent's card shows a Dharmachakra wheel (fully hidden). This restored the core strategic element — you're choosing based on your card, not theirs.

**v4 — Tie/battle system:** Added war-style battle pile: when both top cards tie on the chosen stat, both cards go face-up to the pile, each player draws a fresh card, and the active player chooses a new stat. The winner takes the entire accumulated pile. Multiple ties chain: the pile grows to 4, 6, 8+ cards, creating high-stakes rounds.

**v5 — Pass & Play card clickability:** The most subtle bug in the project. The UI's `draw_card()` function had `is_player_card` hardcoded to `True` for the left card and `False` for the right. This meant Player 2 (right side) could never click their own stats — they were clicking Player 1's card. Fixed by making `is_player_card` conditional on `active_player` and `game_mode`.

**v6 — Manual Next Round button:** Auto-advance timer (5 seconds) replaced with a manual `[NEXT ROUND →]` button. Reason: players need time to read both the opponent's revealed card AND their own. This is an educational game — rushing players past the card content defeats the purpose. A secondary flickering bug was traced to `pygame.display.flip()` being called inside `draw_game_state()` as well as in the main loop — fixed by removing all flip calls from helper functions and centralising them.

**v7 — Phantom click prevention:** When the game state changed to `round_result`, queued mouse events from the previous state would occasionally trigger an immediate "Next Round" click. Fixed with `pygame.event.clear()` on first entry to the result state.

## Failure modes the final version handles

- Wrong player gaining control (alternating vs winner-controls)
- AI triggering in Pass & Play mode (game_mode check required)
- Player 2 clicking Player 1's stats (hardcoded `is_player_card` bug)
- Button flickering (double display.flip)
- Phantom auto-advance clicks (event queue not cleared on state transition)
- Computer auto-selecting stat in Pass & Play (explicit mode check required)

## Outcome

Two fully working game modes. Both implement traditional Top Trumps: winner controls, same stat compares both cards, tie battle pile, winner takes all accumulated cards. Pass & Play supports two humans sharing one device with no computer AI involvement. The `[NEXT ROUND →]` button gives players full control over pacing.

## What I'd change next

Pass & Play could show a "pass the device to Player 2" interstitial screen to prevent Player 1 from glimpsing Player 2's card during the handoff. This would make the privacy guarantee more airtight in a physical setting.

## Tags

`game-design` `code-generation` `debugging` `agent-workflow`
