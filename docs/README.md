# Dharma Duel Card Game

A Top Trumps style card game set in ancient India during the time of Buddha, featuring historical and mythological characters from Buddhist tradition.

## Overview

Dharma Duel is a two-player card game (you vs. computer) where you compete to collect all cards by comparing character attributes. Each card features:

- **Fact File**: 2-3 key facts about the character
- **Six Stats**: Power, Wisdom, Resolve, Influence, Transformation, Mythic Significance
- **Famous Story**: A 1-2 line story about the character's significance

## Features

- 39 unique character cards spanning multiple archetypes:
  - Buddha's family and early life
  - First disciples and chief disciples
  - Famous monks and nuns
  - Royal patrons
  - Mythological beings (Mara, Nagas, Devas)
  - Jataka legends
- Traditional Top Trumps gameplay
- Clean, thematic UI with Buddhist color scheme
- Simple AI opponent

## Requirements

- Python 3.8 or higher
- Pygame 2.5.2

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install Pygame directly:
   ```bash
   pip install pygame
   ```

## How to Run

From the project directory, run:

```bash
python main.py
```

## How to Play

### Game Rules (Traditional Top Trumps)

1. The deck is shuffled and split evenly between you and the computer
2. Each round, both players reveal their top card
3. The active player chooses which stat to compare
4. The player with the higher value for that stat wins both cards
5. The winner becomes the active player for the next round
6. The game continues until one player has all the cards

### Controls

- **Mouse**: Click on stats when it's your turn
- **Click anywhere**: Skip result screen (or wait 3 seconds)
- Click **PLAY AGAIN** to restart after game over

### Strategy Tips

- Buddha has perfect stats (100 in all categories)
- Mara has high Power and Mythic Significance but low Wisdom and Transformation
- Angulimala has maximum Transformation (100) due to his redemption arc
- Sariputta has 98 Wisdom, highest among disciples
- Maha Moggallana has 95 Power, highest among human disciples

## Project Structure

```
dharma_duel_cg/
├── main.py              # Game entry point and main loop
├── game.py              # Game logic (Top Trumps mechanics)
├── card.py              # Card and CardDeck classes
├── ui.py                # Pygame UI rendering
├── data/
│   └── cards.json       # All card data
├── assets/              # (Future: images, fonts, sounds)
├── docs/
│   ├── README.md        # This file
│   └── cards.md         # Guide for adding/modifying cards
└── requirements.txt     # Python dependencies
```

## File Descriptions

### Core Game Files

- **main.py**: Entry point. Manages game states (menu, playing, result, game over) and the main game loop
- **game.py**: Contains `Game` class with Top Trumps logic, deck shuffling, comparison, and win conditions
- **card.py**: Contains `Card` class (individual cards) and `CardDeck` class (loading and managing all cards)
- **ui.py**: Pygame rendering for menus, cards, stats, and game screens

### Data Files

- **data/cards.json**: JSON database with all 39 character cards including stats, facts, and stories

## Game States

1. **Menu**: Title screen with START button
2. **Playing**: Active gameplay - choose stats or wait for computer
3. **Round Result**: Shows comparison result for 3 seconds
4. **Game Over**: Victory/defeat screen with PLAY AGAIN option

## Color Scheme

The game uses traditional Buddhist colors:
- Maroon and Gold (primary)
- Saffron orange
- Cream/beige for text
- Dark brown for borders

## Future Enhancements (v1.1+)

Potential features for future versions:
- Card images for each character
- Sound effects and background music
- Animations for card flips and stat comparisons
- Difficulty levels for AI
- Statistics tracking
- Custom card art
- Multiplayer mode

## Credits

**Game Design & Development**: Created for Buddhist education and entertainment

**Historical Research**: Stats and stories based on Pali Canon and traditional Buddhist texts

## License

This project is for educational and personal use.

---

## Troubleshooting

### Pygame won't install
- Make sure you have Python 3.8+
- Try: `pip install --upgrade pip`
- Then: `pip install pygame`

### Game won't start
- Check that you're in the correct directory
- Ensure `data/cards.json` exists
- Run: `python card.py` to test card loading

### Cards not displaying correctly
- Check terminal for error messages
- Ensure Pygame window is large enough (1200x800)

---

**Version**: 1.0  
**Last Updated**: December 2024
