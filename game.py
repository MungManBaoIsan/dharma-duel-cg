"""
Game logic module for Dharma Duel Card Game.

Handles game state, turn management, and Top Trumps mechanics.
"""

import random
from card import Card, CardDeck


class Game:
    """
    Manages the Top Trumps game logic and state.
    
    Traditional Top Trumps rules:
    - Deck is split between two players
    - Active player chooses a stat to compare
    - Higher stat wins both cards
    - Winner becomes active player
    - Game ends when one player has all cards
    """
    
    def __init__(self):
        """Initialize a new game."""
        self.deck = CardDeck()
        self.player_hand = []
        self.computer_hand = []
        self.current_player_card = None
        self.current_computer_card = None
        self.active_player = None  # 'player' or 'computer'
        self.game_over = False
        self.winner = None
        self.round_winner = None
        self.last_stat_compared = None
        self.player_score = 0  # Rounds won
        self.computer_score = 0
        self.battle_pile = []  # Cards in play during tie battles
        
    def start_new_game(self, karmic_chaos=False):
        """
        Start a new game by shuffling and dealing cards.
        """
        self.karmic_chaos = karmic_chaos
        
        # Reset game state
        self.player_hand = []
        self.computer_hand = []
        self.game_over = False
        self.winner = None
        self.player_score = 0
        self.computer_score = 0
        self.battle_pile = []
        
        # Shuffle all cards
        all_cards = list(self.deck.cards)
        random.shuffle(all_cards)
        
        # Deal cards alternately to each player
        for i, card in enumerate(all_cards):
            if i % 2 == 0:
                self.player_hand.append(card)
            else:
                self.computer_hand.append(card)
        
        # Player always starts first
        self.active_player = 'player'
        
        # Draw first cards
        self._draw_next_cards()
        
        print(f"✓ Game started!")
        print(f"  Player: {len(self.player_hand)} cards")
        print(f"  Computer: {len(self.computer_hand)} cards")
    
    def _draw_next_cards(self):
        """
        Draw the next card for each player from their hands.
        """
        if self.player_hand:
            self.current_player_card = self.player_hand[0]
        else:
            self.current_player_card = None
            
        if self.computer_hand:
            self.current_computer_card = self.computer_hand[0]
        else:
            self.current_computer_card = None
    
    def get_available_stats(self):
        """
        Get list of stats that can be chosen for comparison.
        
        Returns:
            list: List of (stat_key, display_name) tuples
        """
        return [(stat, Card.STAT_NAMES[stat]) for stat in Card.STAT_ORDER]
    
    def compare_cards(self, chosen_stat):
        """
        Compare the current cards on the chosen stat.
        Traditional Top Trumps: Winner takes all cards and goes next.
        
        Args:
            chosen_stat (str): Stat to compare (e.g., 'power', 'wisdom')
            
        Returns:
            dict: Round result with winner, stats, and next active player
        """
        if not self.current_player_card or not self.current_computer_card:
            return None
        
        self.last_stat_compared = chosen_stat
        
        # Get stat values
        player_value = self.current_player_card.get_stat(chosen_stat)
        computer_value = self.current_computer_card.get_stat(chosen_stat)
        
        # Determine winner
        if player_value > computer_value:
            self.round_winner = 'player'
            next_active = 'player'  # Winner goes next
        elif computer_value > player_value:
            self.round_winner = 'computer'
            next_active = 'computer'  # Winner goes next
        else:
            self.round_winner = 'tie'
            next_active = self.active_player  # Same player continues on tie
        
        # Prepare result
        result = {
            'winner': self.round_winner,
            'stat_name': Card.STAT_NAMES[chosen_stat],
            'player_value': player_value,
            'computer_value': computer_value,
            'player_card': self.current_player_card.name,
            'computer_card': self.current_computer_card.name,
            'next_active': next_active
        }
        
        return result
    
    def resolve_round(self):
        """
        Resolve the round by moving cards to winner's hand.
        Traditional Top Trumps rules:
        - Winner takes all cards (including battle pile)
        - Winner becomes active player
        - On tie: Cards stay face-up, battle continues
        """
        if self.round_winner == 'player':
            # Player wins all cards in play
            won_cards = [self.player_hand.pop(0), self.computer_hand.pop(0)]
            
            # Add any battle pile cards
            won_cards.extend(self.battle_pile)
            self.battle_pile = []
            
            # Add to player's hand
            self.player_hand.extend(won_cards)
            self.player_score += 1
            
            # Winner goes next
            self.active_player = 'player'
            
        elif self.round_winner == 'computer':
            # Computer wins all cards in play
            won_cards = [self.player_hand.pop(0), self.computer_hand.pop(0)]
            
            # Add any battle pile cards
            won_cards.extend(self.battle_pile)
            self.battle_pile = []
            
            # Add to computer's hand
            self.computer_hand.extend(won_cards)
            self.computer_score += 1
            
            # Winner goes next
            self.active_player = 'computer'
            
        else:  # Tie - Battle!
            # Add current cards to battle pile (face-up)
            self.battle_pile.append(self.player_hand.pop(0))
            self.battle_pile.append(self.computer_hand.pop(0))
            
            # Check if players have more cards for battle
            if len(self.player_hand) == 0 or len(self.computer_hand) == 0:
                # Can't continue battle - player with cards wins all
                if len(self.player_hand) > 0:
                    self.player_hand.extend(self.battle_pile)
                    self.winner = 'player'
                elif len(self.computer_hand) > 0:
                    self.computer_hand.extend(self.battle_pile)
                    self.winner = 'computer'
                else:
                    # Both out - shouldn't happen but handle it
                    self.winner = 'tie'
                self.battle_pile = []
                self.game_over = True
                return
            
            # Players have cards - continue battle
            # Active player stays the same for tie-break
        
        # Check for game over
        if len(self.player_hand) == 0:
            self.game_over = True
            self.winner = 'computer'
        elif len(self.computer_hand) == 0:
            self.game_over = True
            self.winner = 'player'
        
        # Draw next cards if game continues
        if not self.game_over:
            self._draw_next_cards()
    
    def get_computer_stat_choice(self, difficulty='smart'):
        """
        Computer AI chooses stat from its current card based on difficulty.
        
        Args:
            difficulty (str): 'easy', 'moderate', 'hard', or 'smart'
        
        Returns:
            str: Stat key that computer chooses
        """
        if not self.current_computer_card:
            return None
        
        import random
        
        # Get all stats and values
        stats = []
        for stat in Card.STAT_ORDER:
            value = self.current_computer_card.get_stat(stat)
            stats.append((stat, value))
        
        # Sort by value (highest first)
        stats.sort(key=lambda x: x[1], reverse=True)
        
        # Different AI strategies based on difficulty
        
        if difficulty == 'easy':
            # EASY MODE - AI makes poor choices
            # 20% top stats, 30% middle stats, 50% weak stats
            # Low win rate for AI
            rand = random.random()
            if rand < 0.20:
                # Occasionally picks good stat
                top_stats = stats[:2]
                chosen = random.choice(top_stats)
            elif rand < 0.50:
                # Sometimes picks middle stat
                if len(stats) >= 4:
                    middle_stats = stats[2:4]
                else:
                    middle_stats = stats[2:]
                chosen = random.choice(middle_stats) if middle_stats else stats[-1]
            else:
                # Usually picks weak stat
                weak_stats = stats[-2:]
                chosen = random.choice(weak_stats)
        
        elif difficulty == 'moderate':
            # MODERATE MODE - Balanced play
            # 40% top stats, 40% middle stats, 20% weak stats
            # Medium win rate for AI
            rand = random.random()
            if rand < 0.40:
                # Often picks good stat
                top_stats = stats[:2]
                chosen = random.choice(top_stats)
            elif rand < 0.80:
                # Often picks middle stat
                if len(stats) >= 4:
                    middle_stats = stats[2:4]
                else:
                    middle_stats = stats[2:]
                chosen = random.choice(middle_stats) if middle_stats else stats[0]
            else:
                # Sometimes picks weak stat
                weak_stats = stats[-2:]
                chosen = random.choice(weak_stats)
        
        elif difficulty == 'hard':
            # HARD MODE - Optimal play with rare mistakes
            # 85% top stats, 10% middle stats, 5% weak stats
            # High win rate for AI
            rand = random.random()
            if rand < 0.85:
                # Almost always picks best stat
                top_stats = stats[:2]
                chosen = random.choice(top_stats)
            elif rand < 0.95:
                # Rarely picks middle stat
                if len(stats) >= 4:
                    middle_stats = stats[2:4]
                else:
                    middle_stats = stats[2:]
                chosen = random.choice(middle_stats) if middle_stats else stats[0]
            else:
                # Very rarely makes mistakes
                weak_stats = stats[-2:]
                chosen = random.choice(weak_stats)
        
        else:  # 'smart' (default)
            # SMART MODE - Strategic human-like play
            # 60% top stats, 30% middle stats, 10% weak stats
            # Balanced, unpredictable, fun to play against
            rand = random.random()
            if rand < 0.60:
                # Usually picks good stat (aggressive play)
                top_stats = stats[:2]
                chosen = random.choice(top_stats)
            elif rand < 0.90:
                # Sometimes picks middle stat (unpredictable)
                if len(stats) >= 4:
                    middle_stats = stats[2:4]
                else:
                    middle_stats = stats[2:]
                chosen = random.choice(middle_stats) if middle_stats else stats[0]
            else:
                # Occasionally makes mistakes (human-like)
                weak_stats = stats[-2:]
                chosen = random.choice(weak_stats)
        
        return chosen[0]
    
    def get_game_state(self):
        """
        Get current game state for display.
        
        Returns:
            dict: Current game state information
        """
        return {
            'player_cards_remaining': len(self.player_hand),
            'computer_cards_remaining': len(self.computer_hand),
            'active_player': self.active_player,
            'player_card': self.current_player_card,
            'computer_card': self.current_computer_card,
            'game_over': self.game_over,
            'winner': self.winner,
            'player_score': self.player_score,
            'computer_score': self.computer_score,
            'battle_pile': len(self.battle_pile),
            'is_battle': len(self.battle_pile) > 0
        }
