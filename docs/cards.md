# Card Database Guide

This guide explains how to add, modify, or remove cards from the Dharma Duel Card Game.

## Card Data Location

All cards are stored in: `data/cards.json`

## Card Structure

Each card is a JSON object with the following fields:

```json
{
  "id": 1,
  "name": "Character Name",
  "archetype": "Category Name",
  "fact_file": [
    "First fact about character",
    "Second fact about character",
    "Third fact about character"
  ],
  "famous_story": "A brief 1-2 line story about the character's most famous moment or significance.",
  "stats": {
    "power": 75,
    "wisdom": 80,
    "resolve": 70,
    "influence": 65,
    "transformation": 85,
    "mythic_significance": 70
  }
}
```

## Field Descriptions

### id (required)
- **Type**: Integer
- **Description**: Unique identifier for the card
- **Rules**: Must be unique, typically sequential (1, 2, 3, ...)

### name (required)
- **Type**: String
- **Description**: Character's name as it appears on the card
- **Tips**: 
  - Include clarifying text in parentheses if needed (e.g., "Siddhartha Gautama (The Prince)")
  - Keep under 40 characters for best display
  - Long names will be word-wrapped automatically

### archetype (required)
- **Type**: String
- **Description**: Category/group the character belongs to
- **Current Archetypes**:
  - "Family & Early Life"
  - "The First Students & Early Disciples"
  - "The Two Chief Disciples"
  - "Other Great Disciples"
  - "Famous Female Disciples"
  - "Important Royal Figures"
  - "Donors & Supporters"
  - "Mythic, Cosmic & Supernatural"
  - "Nagas (Serpent Beings)"
  - "Devas (Gods)"
  - "Jataka Story Legend"
  - "The Enlightened Sage"

### fact_file (required)
- **Type**: Array of strings
- **Description**: 2-3 key facts about the character
- **Guidelines**:
  - Keep each fact to one sentence
  - Focus on most interesting/important information
  - Aim for 10-20 words per fact
  - Will be word-wrapped automatically if too long

**Example**:
```json
"fact_file": [
  "Former serial killer who wore a garland of fingers",
  "Converted by Buddha despite killing 999 people",
  "Became arahant and symbol of redemption"
]
```

### famous_story (required)
- **Type**: String
- **Description**: Brief narrative of character's most famous moment
- **Guidelines**:
  - 1-2 sentences (30-50 words ideal)
  - Focus on one memorable event or achievement
  - Will be word-wrapped automatically

**Example**:
```json
"famous_story": "Chased Buddha to kill him for his 1,000th victim but couldn't catch him, leading to his conversion and complete transformation."
```

### stats (required)
- **Type**: Object with six numeric properties
- **Description**: Character's attributes for gameplay comparison
- **Range**: 1-100 for each stat
- **Stats Explained**:

#### power (1-100)
Physical strength, martial ability, psychic powers, supernatural abilities
- 100: Buddha (perfect in all)
- 95: Maha Moggallana (foremost in psychic powers), Mara
- 90: Angulimala (serial killer turned monk)
- 50-70: Normal monks and lay followers
- 35-45: Non-combatants, children

#### wisdom (1-100)
Spiritual insight, teaching ability, understanding of Dhamma
- 100: Buddha
- 98: Sariputta (chief disciple, foremost in wisdom)
- 90+: Great disciples with high realization
- 70-85: Learned disciples
- 45-65: Beginning practitioners

#### resolve (1-100)
Determination, discipline, ability to maintain practice, willpower
- 100: Buddha
- 90-95: Those who maintained extreme practices (Kassapa, Mahapajapati, Angulimala)
- 80-85: Dedicated disciples
- 70-75: Good practitioners
- 60-70: Average commitment

#### influence (1-100)
Impact on others, leadership, historical significance, ability to inspire
- 100: Buddha
- 90: Sariputta, Ananda, chief disciples
- 85-88: Kings, major donors, chief nuns
- 70-80: Important disciples
- 50-60: Lesser-known figures

#### transformation (1-100)
Degree of personal change from previous state, redemption arc
- 100: Angulimala (serial killer → arahant), Buddha
- 90-95: Major life changes (Yasodhara, Khema, Sariputta)
- 80-85: Significant but less dramatic changes
- 60-75: Moderate transformation
- 20-50: Little personal change or villains

#### mythic_significance (1-100)
Importance in Buddhist cosmology, legendary status, symbolic meaning
- 100: Buddha, Mara (primary antagonist)
- 95: Kondanna (first arahant), chief disciples, Brahma
- 85-90: Famous supernatural beings, key disciples
- 70-80: Well-known figures in tradition
- 60-70: Secondary characters

## Adding a New Card

1. Open `data/cards.json` in a text editor

2. Add a comma after the last card's closing brace `}`

3. Add your new card following the structure above

4. Assign a unique ID (next sequential number)

5. Fill in all required fields

6. Assign stats based on the guidelines above

7. Save the file

8. Test by running: `python card.py`

**Example - Adding a new character**:

```json
{
  "id": 40,
  "name": "Sona Kolivisa",
  "archetype": "Other Great Disciples",
  "fact_file": [
    "Former wealthy merchant who became a monk",
    "Foremost in arousing energy and effort",
    "Practiced walking meditation until his feet bled"
  ],
  "famous_story": "Buddha taught him the Middle Way using the simile of tuning a lute - not too tight, not too loose.",
  "stats": {
    "power": 60,
    "wisdom": 75,
    "resolve": 95,
    "influence": 65,
    "transformation": 80,
    "mythic_significance": 70
  }
}
```

## Modifying an Existing Card

1. Open `data/cards.json`

2. Find the card by searching for its name or ID

3. Edit any fields you want to change

4. Save the file

5. Test: `python card.py`

## Removing a Card

1. Open `data/cards.json`

2. Find the card to remove

3. Delete the entire card object (from `{` to `}`)

4. Remove the comma before it (if it was the last card) or after it

5. Save and test

**Warning**: Don't remove too many cards or the game may become unbalanced!

## Balancing Guidelines

### For Balanced Gameplay

- **Average stats**: Most characters should have stats in the 50-80 range
- **Specialists**: Give characters one or two stats above 85
- **Buddha**: Keep at 100 in all stats (he's meant to be the ultimate card)
- **Mara**: High Power/Mythic, low Wisdom/Transformation (thematic opposition)
- **Variety**: Ensure a mix of high/low stats across the deck

### Stat Distribution Recommendations

- **1-30**: Reserved for negative traits or villains
- **30-50**: Below average
- **50-70**: Average/competent
- **70-85**: Skilled/notable
- **85-95**: Exceptional/foremost
- **95-100**: Perfect/supreme (Buddha, or one exceptional quality)

## Testing Your Changes

After modifying cards:

```bash
# Test card loading
python card.py

# Test game with new cards
python main.py
```

## Common Mistakes to Avoid

1. **Missing commas**: Each card needs a comma after it except the last one
2. **Duplicate IDs**: Every card must have a unique ID
3. **Stats out of range**: Keep all stats between 1-100
4. **Invalid JSON**: Use a JSON validator if you get errors
5. **Too long text**: Very long names or stories may not display well

## JSON Validation

Use an online JSON validator (like jsonlint.com) if you encounter errors.

Common JSON rules:
- Strings must be in double quotes `"like this"`
- Numbers don't need quotes
- Arrays use square brackets `[1, 2, 3]`
- Objects use curly braces `{}`
- Last item in array/object has no comma

## Questions?

If you're unsure about appropriate stats for a character:
1. Look at similar existing characters
2. Research the character's role in Buddhist history
3. Consider their unique qualities and achievements
4. Balance gameplay over strict historical accuracy

---

**Happy card creating!**
