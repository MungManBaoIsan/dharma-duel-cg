# Prompt Changelog — Dharma Duel Card Game

Chronological record of prompt creation and refinement. Newest entries at top.

---

## ai-and-ui-features

### Dec 2025 — v3 (4 difficulty levels)
**Change:** Expanded from 1 Smart AI mode to 4 named difficulty levels (Easy/Moderate/Hard/Smart).
**Reason:** A single mode can't serve both beginners using the game as a teaching tool and experienced players wanting a real challenge.
**Impact:** Easy mode makes the AI beatable for new players; Smart mode provides human-feeling unpredictability for experienced play.

### Dec 2025 — v2 (Smart AI mode)
**Change:** Added 60/30/10 strategic AI (top-2/middle/weak stat distribution).
**Reason:** Always-highest-stat AI was predictable and boring after a few games.
**Impact:** AI makes occasional deliberate mistakes, making games more exciting and less rote.

### Dec 2025 — v1 (initial)
**Change:** Card viewer with 8 sort options, basic story context (Sāgara's tale), "?" text card back.
**Reason:** Players needed a way to study the deck before playing; a story set context.
**Impact:** Card viewer functional. Story tone later found to be wrong for a game context.

---

## balance-tuning

### Dec 2025 — v4 (Wisdom 100, Influence 90)
**Change:** Raised Buddha's Wisdom to 100 (Perfectly Enlightened One), raised Influence to 90 (founded a world religion).
**Reason:** Wisdom 98 left Buddha tied with Sariputta — theologically incorrect. Influence 85 underrepresented a 2,500-year civilisational impact.
**Impact:** Buddha's overall rating rises to 97.5. Ashoka (Influence 95) remains the one card that can beat him on Influence.

### Dec 2025 — v3 (Power reduced to 95)
**Change:** Reduced Buddha's Power from 97 to 95.
**Reason:** Creates tie battles with Moggallana and Mara rather than guaranteed wins.
**Impact:** Power battles become an exciting strategic option rather than a safe choice.

### Dec 2025 — v2 (contextual weaknesses)
**Change:** Implemented Option 1 balance: Power 97, Influence 85. All other stats remain 100.
**Reason:** Theological justification — Buddha renounced violence (lower Power) and worldly political power (lower Influence).
**Impact:** Buddha went from unbeatable to ~90% win rate. Seven cards can now beat him on Influence.

### Dec 2025 — v1 (all-100s, deprecated)
**Change:** Buddha at Power/Wisdom/Resolve/Influence/Transformation/Merit all = 100.
**Reason:** Initial generation defaulted to maximum values.
**Impact:** Game trivial when Buddha is drawn — no stat choice matters. Discarded.

---

## game-mechanics

### Dec 2025 — v7 (phantom click fix)
**Change:** Added `pygame.event.clear()` on entering result state.
**Reason:** Stale queued mouse events caused automatic Next Round advancement.
**Impact:** Result screen stays until player makes an explicit new click.

### Dec 2025 — v6 (Next Round button)
**Change:** Replaced 5-second auto-advance timer with manual `[NEXT ROUND →]` button.
**Reason:** Players need time to read both their own card AND the opponent's revealed card — educational game should not rush players.
**Impact:** Full player control over pacing; card reading becomes part of the experience.

### Dec 2025 — v5 (Pass & Play card clickability)
**Change:** Made `is_player_card` conditional on `active_player` and `game_mode` rather than hardcoded to left card.
**Reason:** Player 2's card (right side) was never clickable — `is_player_card=False` was hardcoded, so Player 2 was clicking Player 1's stats.
**Impact:** Pass & Play actually works — each player clicks their own card's stats on their turn.

### Dec 2025 — v4 (battle pile)
**Change:** Added war-style tie resolution: tied cards go to battle pile, fresh cards drawn, winner takes all.
**Reason:** Traditional Top Trumps rule for ties.
**Impact:** Ties create high-stakes rounds with 2–8+ cards at stake.

### Dec 2025 — v3 (card hiding)
**Change:** Opponent card shows Dharmachakra wheel (fully hidden) until stat is selected.
**Reason:** Seeing opponent name/archetype before choosing stat removed the strategic blind-choice element.
**Impact:** Strategy restored — you choose based on your own card, not the opponent's.

### Dec 2025 — v2 (winner controls)
**Change:** Winner of each round becomes active player for next round.
**Reason:** Traditional Top Trumps rule — winner controls. Alternating turns is incorrect.
**Impact:** Winning streaks possible; momentum reflects skill.

### Dec 2025 — v1 (alternating turns, deprecated)
**Change:** Turns alternated regardless of who won.
**Reason:** Initial implementation defaulted to alternating for perceived fairness.
**Impact:** Not real Top Trumps behaviour; no momentum. Discarded.

---

## archetype-naming

### Dec 2025 — v2 (user-selected labels)
**Change:** Replaced all 16 AI-generated archetypes with user-selected labels.
**Reason:** Original labels were imprecise (conflated ordained nuns with laywomen) and forgettable ("Other Great Disciples").
**Impact:** Each archetype is now both theologically accurate and clear to non-expert players.

### Dec 2025 — v1 (AI-generated, deprecated)
**Change:** Initial labels generated automatically.
**Reason:** Placeholder labels to scaffold the card data quickly.
**Impact:** Functionally adequate but educationally imprecise. Discarded.

---

## stat-system-redesign

### Dec 2025 — v2 (Merit, current)
**Change:** Replaced Mythic Significance with Merit; recalculated all 40 cards using the Four Stages of Enlightenment scale.
**Reason:** Mythic Significance was too vague and subjective — no canonical source, impossible to verify.
**Impact:** Historical accuracy for the sixth stat rose from ~50–60% to ~85–90%. Now cross-referenced with Etadagga Sutta (AN 1.188–234).

### Dec 2025 — v1 (Mythic Significance, deprecated)
**Change:** Initial sixth stat assigned based on "cosmological prominence."
**Reason:** Seemed thematically appropriate at first design stage.
**Impact:** Unverifiable, inconsistent, not a real Buddhist concept. Replaced.

---

## card-database-design

### Dec 2025 — v2 (40 cards, Merit field, tier + rating)
**Change:** Card count 39→40 (even split), Mythic Significance→Merit, added overall_rating and tier fields, replaced individual Five Ascetics with group card + Añña Kondañña separate.
**Reason:** Even 20v20 split required; accuracy improvements; trap cards added; better roster structure.
**Impact:** Complete 40-card database, all fields present, tier system operational.

### Dec 2025 — v1 (39 cards, initial)
**Change:** Initial card database generation.
**Reason:** Scaffold the data layer before building game logic.
**Impact:** Working 39-card JSON database. Refined through multiple subsequent iterations.

---

## game-concept

### Dec 2025 — v1 (foundational)
**Change:** Initial project scoping and concept establishment.
**Reason:** Set up the game vision, format, characters, and file structure before writing any code.
**Impact:** Complete v1.0 prototype generated from this single scoping session.
