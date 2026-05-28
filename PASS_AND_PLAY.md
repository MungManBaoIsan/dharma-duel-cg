# Pass & Play - 2-Player Mode

## Overview

Dharma Duel now includes **Pass & Play** mode, allowing two players to compete on the same device!

---

## Game Modes

### VS COMPUTER
- **Classic mode**: Play against AI
- **Computer chooses**: Best stat automatically
- **Solo play**: Perfect for practicing

### VS PLAYER (Pass & Play)
- **2-player mode**: Play with a friend
- **Take turns**: Share the same device
- **Both choose**: Each player picks their stat
- **More fun**: Human competition!

---

## How to Play Pass & Play

### 1. Start the Game
```
┌──────────────┐  ┌──────────────┐
│ VS COMPUTER  │  │  VS PLAYER   │
│              │  │ ← Click this │
└──────────────┘  └──────────────┘
```
Click **"VS PLAYER"** on the main menu

### 2. Game Setup
- Deck is shuffled and split evenly
- Player 1 gets ~20 cards
- Player 2 gets ~19 cards
- Player 1 always starts first

### 3. Player 1's Turn
```
📚 20                          19 📚
PLAYER 1 STACK          PLAYER 2 STACK

        PLAYER 1'S TURN - Choose a stat

┌──────────────┐    ┌──────────────┐
│ Player 1's   │    │ Player 2's   │
│ Card         │    │ Card (hidden)│
│              │    │              │
│ Click a stat │    │ Stats: ???   │
└──────────────┘    └──────────────┘
```
- **Player 1** looks at their card
- **Player 1** clicks a stat they think will win
- **Player 2's card reveals**

### 4. Result Display
```
        Player 1 wins! Wisdom: 85 vs 70

┌──────────────┐    ┌──────────────┐
│ Player 1's   │    │ Player 2's   │
│ Card         │    │ Card         │
│ Wisdom: 85   │    │ Wisdom: 70   │
└──────────────┘    └──────────────┘
```
- Both cards visible
- Winner announced
- Cards move to winner's stack

### 5. Pass the Device
- **IMPORTANT**: Pass device to next player!
- Winner of round goes next
- Other player's cards stay hidden

### 6. Player 2's Turn
```
📚 21                          18 📚
PLAYER 1 STACK          PLAYER 2 STACK

        PLAYER 2'S TURN - Choose a stat
```
- **Player 2** now chooses a stat
- Same process repeats
- Keep playing until someone has all 39 cards!

---

## Key Differences from VS Computer

| Feature | VS Computer | VS Player |
|---------|-------------|-----------|
| **Opponent** | AI | Human friend |
| **Stat choice** | Auto (best stat) | Manual (you choose) |
| **Turn speed** | 1.5s delay | Instant |
| **Cards hidden** | Yes (computer's) | Yes (opponent's) |
| **Device passing** | No | Yes! |
| **Labels** | YOU / COMPUTER | PLAYER 1 / PLAYER 2 |

---

## Pass & Play Etiquette

### Do's ✅
- **Pass device after your turn**
- **Don't look at opponent's cards** while passing
- **Wait for your turn** to look at screen
- **Be honest** about stat values
- **Have fun!**

### Don'ts ❌
- **Don't peek** at opponent's cards
- **Don't memorize** their cards
- **Don't rush** the other player
- **Don't argue** about results (computer calculates!)

---

## Strategy Tips for 2-Player

### When It's Your Turn
1. **Study your card** - Read all stats carefully
2. **Think strategically** - What's your strongest stat?
3. **Remember history** - What stats has opponent won with?
4. **Be decisive** - Click your best stat

### When It's Opponent's Turn
1. **Look away** - Give them privacy
2. **Wait patiently** - Don't rush them
3. **Stay engaged** - Watch the result!
4. **Learn** - See what stats they choose

### General Strategy
- **High-value stats** usually win
- **Buddha card** wins almost everything (100s)
- **Mara card** has low Merit but high Power
- **Mix it up** - Don't always choose same stat

---

## Example Game Flow

### Round 1
```
Player 1's turn → Chooses Wisdom
Result: Player 1 wins! Wisdom: 92 vs 75
Player 1 now has 21 cards, Player 2 has 18
```

### Round 2
```
Player 1's turn again (winner continues)
Chooses Power → Result: Player 2 wins! Power: 50 vs 85
Player 2 now has 20 cards, Player 1 has 19
```

### Round 3
```
Player 2's turn (they won last round)
Chooses Merit → Result: Player 2 wins! Merit: 95 vs 70
Player 2 now has 22 cards, Player 1 has 17
```

...continues until one player has all 39 cards!

---

## Perfect For

### Friends & Family
✅ **Game nights** - Fun group activity  
✅ **Teaching** - Learn together  
✅ **Competition** - Friendly rivalry  
✅ **Breaks** - Quick 10-15 min games  

### Monastic Setting
✅ **Monastery recreation** - Wholesome entertainment  
✅ **Dhamma education** - Learn about disciples  
✅ **Community bonding** - Share with sangha  
✅ **Teaching tool** - For new monks/nuns  

### Learning
✅ **Character knowledge** - Learn who's who  
✅ **Stat understanding** - See enlightenment levels  
✅ **Strategy** - Think about best moves  
✅ **Buddhist history** - Famous stories  

---

## Technical Details

### Turn Management
- Game tracks `active_player` ('player' or 'computer')
- In Pass & Play: 'player' = Player 1, 'computer' = Player 2
- Labels automatically update based on mode
- Turn indicator shows correct player name

### Card Visibility
- **Your turn**: See your cards, opponent hidden
- **Opponent turn**: See opponent cards (after choice)
- **Result**: Both cards visible
- **No peeking!** Cards only show during appropriate turns

### Device Passing
- No automatic hiding (trust-based)
- Players responsible for not peeking
- Works best with honor system
- Can sit across from each other

---

## Accessibility

### Works On
✅ **Laptop** - 14" and up  
✅ **Desktop** - Any monitor  
✅ **Tablet** - If can run Python/Pygame  

### Best Setup
- **Face-to-face**: Sit across table
- **Side-by-side**: Sit next to each other
- **Rotate device**: Turn screen between turns
- **Honor system**: Trust each other

---

## Future Enhancements

Potential additions for v3.0:
- **Privacy mode** - Auto-hide cards during pass
- **Timer** - Optional turn time limits
- **Best of 3/5** - Tournament mode
- **Statistics** - Track wins per player
- **More players** - 3-4 player support
- **Network play** - Online multiplayer

---

## Troubleshooting

### "I saw opponent's cards while passing"
- Look away while passing
- Can hold hand over screen
- Trust each other to play fair

### "We're not sure whose turn it is"
- Check the turn indicator at top
- Says "PLAYER 1'S TURN" or "PLAYER 2'S TURN"
- Winner of last round goes next

### "Can we go back to computer mode?"
- Click PLAY AGAIN after game ends
- Returns to main menu
- Choose VS COMPUTER this time

---

**Version**: 2.0  
**Feature**: Pass & Play Mode  
**Players**: 2  
**Device**: Shared  
**Status**: Fully functional!

🙏 **Enjoy playing with friends!** 🙏
