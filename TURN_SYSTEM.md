# Turn System & Gameplay Fixes - v2.2

## Three Critical Fixes Implemented

### 1. ✅ Opponent Card Hidden Until Stat Chosen

**Problem**: Could see opponent's stats before making choice

**Fix**: Already implemented correctly!
- Location: `ui.py` line 524
- Code: `show_computer_stats = result is not None`
- Behavior: Opponent's card shows back side (no stats) until you click

**How It Works**:
```python
# In draw_game_state()
if game_state['computer_card']:
    # Hide stats until player chooses
    show_computer_stats = result is not None
    
    self.draw_card(
        game_state['computer_card'],
        show_stats=show_computer_stats,  # False until result
        ...
    )
```

**Player Experience**:
1. Your turn → See YOUR card with stats
2. See OPPONENT card with ??? (back showing)
3. Click a stat → BOTH cards reveal
4. See result → Winner announced
5. Next round → Cards hidden again

---

### 2. ✅ Deck Shuffled Each Game

**Problem**: Same cards in same order each game

**Fix**: Already implemented correctly!
- Location: `game.py` line 51-52
- Code: `random.shuffle(all_cards)`
- Behavior: Completely random card order every game

**How It Works**:
```python
def start_new_game(self):
    # Get all 35 cards
    all_cards = list(self.deck.cards)
    
    # Shuffle them randomly
    random.shuffle(all_cards)  # ← THE MAGIC
    
    # Deal alternately to each player
    for i, card in enumerate(all_cards):
        if i % 2 == 0:
            self.player_hand.append(card)
        else:
            self.computer_hand.append(card)
```

**Result**: 
- Game 1: Mara's Daughters first
- Game 2: Ananda first
- Game 3: King Bimbisara first
- Every game is unique!

---

### 3. ✅ Turn Alternation Fixed (NEW!)

**Problem**: Winner got to go again (traditional Top Trumps rules)

**Old Behavior**:
- Player chooses → Wins → Player goes again
- Player chooses → Wins → Player goes again
- Computer might never get a turn!

**New Behavior**:
- Player chooses → Wins/Loses → Computer's turn
- Computer chooses → Wins/Loses → Player's turn
- Fair alternation every round!

**Code Changes**:

#### `game.py` - resolve_round() method:
```python
# OLD CODE (winner goes next):
if self.round_winner == 'player':
    won_cards = [...]
    self.active_player = 'player'  # ← Player goes again!
elif self.round_winner == 'computer':
    won_cards = [...]
    self.active_player = 'computer'  # ← Computer goes again!

# NEW CODE (alternates):
if self.round_winner == 'player':
    won_cards = [...]
    # No active_player change here
elif self.round_winner == 'computer':
    won_cards = [...]
    # No active_player change here

# Alternate turns REGARDLESS of winner
if self.active_player == 'player':
    self.active_player = 'computer'
else:
    self.active_player = 'player'
```

#### `game.py` - compare_cards() method:
```python
# OLD CODE (winner goes next):
if player_value > computer_value:
    self.round_winner = 'player'
    next_active = 'player'  # ← Winner goes next
elif computer_value > player_value:
    self.round_winner = 'computer'
    next_active = 'computer'  # ← Winner goes next

# NEW CODE (alternates):
if player_value > computer_value:
    self.round_winner = 'player'
elif computer_value > player_value:
    self.round_winner = 'computer'
else:
    self.round_winner = 'tie'

# Next active always alternates
next_active = 'computer' if self.active_player == 'player' else 'player'
```

---

## Gameplay Flow (Complete)

### Starting the Game:
1. **Shuffle deck** → Random card order
2. **Deal cards** → ~18 each (alternating)
3. **Player starts** → First turn always goes to you

### Each Round:

#### Player's Turn:
```
┌─────────────────────────────────────────┐
│ YOUR TURN - Choose a stat              │
├─────────────────────────────────────────┤
│                                         │
│  YOUR CARD          OPPONENT CARD       │
│  ┌──────────┐      ┌──────────┐        │
│  │ Ananda   │      │   ???    │        │
│  │ Power: 75│      │          │        │
│  │ Wisdom:92│      │ Hidden!  │        │
│  │ ...      │      │          │        │
│  └──────────┘      └──────────┘        │
│  [Click a stat!]                        │
└─────────────────────────────────────────┘
```

**You click** → Cards reveal → Result shows → 5 seconds → **Computer's turn**

#### Computer's Turn:
```
┌─────────────────────────────────────────┐
│ COMPUTER'S TURN                         │
├─────────────────────────────────────────┤
│                                         │
│  YOUR CARD          OPPONENT CARD       │
│  ┌──────────┐      ┌──────────┐        │
│  │   ???    │      │ Sariputta│        │
│  │          │      │ Power: 85│        │
│  │ Hidden!  │      │ Wisdom:98│        │
│  │          │      │ ...      │        │
│  └──────────┘      └──────────┘        │
│  [Computer thinking...]                 │
└─────────────────────────────────────────┘
```

**Computer auto-picks** (1.5 sec delay) → Cards reveal → Result shows → 5 seconds → **Your turn**

---

## Turn Pattern

### Traditional Top Trumps (OLD):
```
Round 1: Player chooses → Player wins → Player goes again
Round 2: Player chooses → Player wins → Player goes again
Round 3: Player chooses → Player wins → Player goes again
Round 4: Player chooses → Computer wins → Computer goes
Round 5: Computer chooses → Computer wins → Computer goes again
```
**Problem**: Can get long streaks of same player

### Dharma Duel v2.2 (NEW):
```
Round 1: Player chooses → Player wins → Computer's turn
Round 2: Computer chooses → Computer wins → Player's turn
Round 3: Player chooses → Player wins → Computer's turn
Round 4: Computer chooses → Player wins → Player's turn
Round 5: Player chooses → Computer wins → Computer's turn
```
**Benefit**: Fair alternation, both players always engaged!

---

## Tie Behavior

### What Happens on a Tie:
```
Both cards have same stat value (e.g. Power: 85 vs 85)
```

**Card Movement**:
- Both cards go to **back of own hand** (not won)
- Nobody gets extra cards
- Deck doesn't shrink

**Turn Order**:
- **Still alternates!** 
- If it was your turn → Computer's turn next
- Fair even on ties

---

## Benefits of These Fixes

### 1. Fair Play
✅ Both players get equal turns  
✅ Can't dominate by winning streaks  
✅ Strategic on every round

### 2. Better Strategy
✅ Can't see opponent's stats (no cheating)  
✅ Must choose blindly based on your card  
✅ Risk/reward every turn

### 3. More Engaging
✅ Never waiting too long  
✅ Always your turn soon  
✅ Keeps pace moving

### 4. Replayability
✅ Different cards every game  
✅ Can't memorize patterns  
✅ Fresh experience each time

---

## Technical Details

### Files Modified:
- `game.py` (2 methods)
  - `compare_cards()` - next_active logic
  - `resolve_round()` - turn alternation

### Files Already Correct:
- `ui.py` - opponent card hiding ✅
- `game.py` - deck shuffling ✅

### No Changes Needed:
- `main.py` - game flow works correctly
- `card.py` - card data unchanged
- `ui.py` - visual display works perfectly

---

## Testing Results

### Test 1: Opponent Card Hiding
```
✅ Opponent card hidden when your turn
✅ Reveals after you click stat
✅ Hidden again next round
```

### Test 2: Deck Shuffling
```
Game 1 first card: Mara's Daughters
Game 2 first card: Ananda
Game 3 first card: King Bimbisara
✅ Different every time!
```

### Test 3: Turn Alternation
```
Round 1: Player (start) → Computer (next)
Round 2: Computer → Player
Round 3: Player → Computer
✅ Perfect alternation regardless of winner!
```

---

## Comparison to Traditional Top Trumps

| Feature | Traditional Top Trumps | Dharma Duel v2.2 |
|---------|----------------------|------------------|
| **Turn Order** | Winner goes next | Always alternates |
| **Winning Streak** | Yes (can go 10+ times) | No (max 1 turn) |
| **Ties** | Winner stays active | Still alternates |
| **Card Reveal** | Both visible | Opponent hidden |
| **Shuffle** | Manual | Automatic |

**Why Different?**

Traditional Top Trumps was designed for physical cards where:
- Both players could see both cards anyway
- Winner-goes-next adds excitement for kids
- Streaks make victories feel more dramatic

Digital version benefits from:
- Hidden information adds strategy
- Alternating turns feels fairer
- Computer AI gets fair participation
- Better pacing for screen-based play

---

## Player Experience Summary

### Before Fixes (v2.1):
😕 Could see opponent's stats before choosing  
😕 Might play same card order twice  
😕 Winner dominated with long streaks  
😕 Felt unfair when losing  

### After Fixes (v2.2):
😊 Must choose blindly (strategic!)  
😊 Every game has different cards  
😊 Fair turn alternation  
😊 Both players engaged every round  

---

## For Monastery Use

These fixes make Dharma Duel better for:

**Teaching**:
- Fair gameplay models Right Action
- Hidden cards = not clinging to outcomes
- Alternation = mutual respect
- Random shuffle = impermanence

**Recreation**:
- Quick rounds keep attention
- Fair turns prevent frustration  
- Strategic thinking without pressure
- Suitable for all skill levels

**Community**:
- Can play with anyone fairly
- No domination by skilled players
- New each time (replayability)
- Wholesome entertainment

---

**Version**: 2.2 - Turn System Fixed  
**Total Cards**: 35  
**Turn Pattern**: Player ↔ Computer (Alternating)  
**Shuffle**: Every Game  
**Status**: Balanced & Fair! ⚖️🙏
