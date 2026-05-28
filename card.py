"""
Card module for Dharma Duel Card Game.

Handles individual card data and display information.
"""

import json
import sys
from pathlib import Path


def _resource_path(relative_path):
    """Get absolute path — works both in dev and as a PyInstaller bundle."""
    base = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
    return base / relative_path


class Card:
    """
    Represents a single character card in the game.
    
    Attributes:
        id (int): Unique card identifier
        name (str): Character name
        archetype (str): Category/group the character belongs to
        fact_file (list): 2-3 facts about the character
        famous_story (str): 1-2 line story about the character
        stats (dict): Six attributes (power, wisdom, resolve, influence, 
                      transformation, mythic_significance)
    """
    
    # Define stat display names and order
    STAT_NAMES = {
        'power': 'Power',
        'wisdom': 'Wisdom',
        'resolve': 'Resolve',
        'influence': 'Influence',
        'transformation': 'Transformation',
        'merit': 'Merit'
    }
    
    STAT_ORDER = ['power', 'wisdom', 'resolve', 'influence', 
                  'transformation', 'merit']
    
    def __init__(self, card_data):
        """
        Initialize a card from dictionary data.
        
        Args:
            card_data (dict): Card information from JSON
        """
        self.id = card_data['id']
        self.name = card_data['name']
        self.archetype = card_data['archetype']
        self.fact_file = card_data['fact_file']
        self.famous_story = card_data['famous_story']
        self.stats = card_data['stats']
        self.overall_rating = card_data.get('overall_rating', 0)
        self.tier = card_data.get('tier', 'bronze')
        self.is_legend = card_data.get('is_legend', False)  # Legend cards!
    
    def get_stat(self, stat_name):
        """
        Get a specific stat value.
        
        Args:
            stat_name (str): Name of the stat (e.g., 'power', 'wisdom')
            
        Returns:
            int: Stat value (1-100)
        """
        return self.stats.get(stat_name, 0)
    
    def get_stat_display_name(self, stat_name):
        """
        Get the display name for a stat.
        
        Args:
            stat_name (str): Internal stat name
            
        Returns:
            str: Display-friendly stat name
        """
        return self.STAT_NAMES.get(stat_name, stat_name.title())
    
    def compare_stat(self, other_card, stat_name):
        """
        Compare this card's stat with another card's stat.
        
        Args:
            other_card (Card): Card to compare against
            stat_name (str): Stat to compare
            
        Returns:
            int: 1 if this card wins, -1 if loses, 0 if tie
        """
        my_stat = self.get_stat(stat_name)
        their_stat = other_card.get_stat(stat_name)
        
        if my_stat > their_stat:
            return 1
        elif my_stat < their_stat:
            return -1
        else:
            return 0
    
    def __str__(self):
        """String representation of card for debugging."""
        return f"{self.name} ({self.archetype})"
    
    def __repr__(self):
        """Detailed representation for debugging."""
        return f"Card(id={self.id}, name='{self.name}')"


class CardDeck:
    """
    Manages the collection of all cards in the game.
    Handles loading from JSON and deck operations.
    """

    def __init__(self, json_path=None):
        """
        Initialize deck by loading cards from JSON.

        Args:
            json_path (str): Path to cards.json file. If None, defaults to
                             the data/ folder next to this script.
        """
        if json_path is None:
            json_path = _resource_path(Path("data") / "cards.json")

        self.cards = []
        self.load_cards(json_path)
    
    def load_cards(self, json_path):
        """
        Load all cards from JSON file.
        
        Args:
            json_path (str): Path to cards.json
        """
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Create Card objects from JSON data
            for card_data in data['cards']:
                card = Card(card_data)
                self.cards.append(card)
                
            print(f"✓ Loaded {len(self.cards)} cards successfully")
            
        except FileNotFoundError:
            print(f"✗ Error: Could not find {json_path}")
            raise
        except json.JSONDecodeError as e:
            print(f"✗ Error: Invalid JSON in {json_path}: {e}")
            raise
    
    def get_card_by_id(self, card_id):
        """
        Get a specific card by its ID.
        
        Args:
            card_id (int): Card ID to find
            
        Returns:
            Card: Card object or None if not found
        """
        for card in self.cards:
            if card.id == card_id:
                return card
        return None
    
    def get_card_by_name(self, name):
        """
        Get a specific card by its name.
        
        Args:
            name (str): Card name to find
            
        Returns:
            Card: Card object or None if not found
        """
        for card in self.cards:
            if card.name.lower() == name.lower():
                return card
        return None
    
    def get_cards_by_archetype(self, archetype):
        """
        Get all cards of a specific archetype.
        
        Args:
            archetype (str): Archetype to filter by
            
        Returns:
            list: List of Card objects
        """
        return [card for card in self.cards if card.archetype == archetype]
    
    def get_all_archetypes(self):
        """
        Get list of all unique archetypes in the deck.
        
        Returns:
            list: Sorted list of archetype names
        """
        archetypes = set(card.archetype for card in self.cards)
        return sorted(archetypes)
    
    def __len__(self):
        """Return number of cards in deck."""
        return len(self.cards)
    
    def __iter__(self):
        """Allow iteration over cards."""
        return iter(self.cards)


# Test the module if run directly
if __name__ == '__main__':
    print("Testing Card and CardDeck classes...\n")
    
    # Load the deck
    deck = CardDeck()
    
    print(f"\nTotal cards: {len(deck)}")
    print(f"Archetypes: {len(deck.get_all_archetypes())}")
    
    # Test getting a specific card
    buddha = deck.get_card_by_name("Buddha (The Enlightened Sage)")
    if buddha:
        print(f"\n{buddha.name}")
        print(f"Archetype: {buddha.archetype}")
        print(f"Stats: {buddha.stats}")
        print(f"Story: {buddha.famous_story[:50]}...")
    
    # Test comparison
    sariputta = deck.get_card_by_name("Sariputta")
    if buddha and sariputta:
        result = buddha.compare_stat(sariputta, 'wisdom')
        print(f"\nBuddha vs Sariputta (Wisdom): {result}")
