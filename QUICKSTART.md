# Dharma Duel Card Game - Quick Start

## Instant Setup (3 Steps)

### 1. Install Python
Make sure you have Python 3.8 or higher:
```bash
python --version
```

### 2. Install Pygame
```bash
pip install pygame
```

### 3. Run the Game
```bash
python main.py
```

That's it! The game should open in a new window.

---

## What You'll See

### Main Menu
- Title: "DHARMA DUEL Card Game"
- Instructions about the game
- START button (click to begin)

### Gameplay Screen
- **Your card** on the left
- **Computer's card** on the right (stats hidden until you choose)
- **Turn indicator** at top ("YOUR TURN - Choose a stat")
- **Card counters** showing remaining cards

### Your Turn
1. Look at your card's stats
2. Click on the stat you think will win
3. Computer's card reveals
4. Winner takes both cards

### Computer's Turn
- Computer chooses automatically
- Both cards reveal
- Result displays for 3 seconds

### Game Over
- Victory or defeat message
- PLAY AGAIN button

---

## Quick Tips

- **Buddha** is the strongest card (100 in everything)
- **Mara** has high Power but low Wisdom
- **Angulimala** has maximum Transformation
- **Sariputta** has 98 Wisdom (highest among disciples)
- Click anywhere during result screen to skip the 3-second wait

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'pygame'"
```bash
pip install pygame
```

### "Command 'python' not found"
Try:
```bash
python3 main.py
```

### Game won't start
Make sure you're in the `dharma_duel_cg` directory:
```bash
cd dharma_duel_cg
python main.py
```

### Still having issues?
Check the full README.md in the `docs/` folder.

---

## File Structure

```
dharma_duel_cg/
├── main.py           ← Start here!
├── game.py
├── card.py
├── ui.py
├── requirements.txt
├── data/
│   └── cards.json    ← All 39 character cards
└── docs/
    ├── README.md     ← Full documentation
    └── cards.md      ← How to add/edit cards
```

---

## Controls

- **Mouse**: Click to select stats
- **Mouse**: Click anywhere to skip result screen
- **Close Window** or **ESC**: Quit game

---

**Enjoy the game!** 🙏
