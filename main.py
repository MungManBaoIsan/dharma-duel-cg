"""
Dharma Duel Card Game - Main Entry Point

A Top Trumps style card game set in ancient India during Buddha's time.
"""

import pygame
import sys
from game import Game
from ui import UI


class DharmaDuel:
    """
    Main game controller that manages game flow and state.
    """
    
    def __init__(self):
        """Initialize the game."""
        self.ui = UI()
        self.game = Game()
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Game state tracking
        self.state = 'menu'  # 'menu', 'difficulty_select', 'playing', 'round_result', 'game_over', 'card_viewer', 'story_reader'
        self.game_mode = None  # 'computer' or 'player' (2-player pass & play)
        self.ai_difficulty = None  # 'easy', 'moderate', 'hard', 'smart'
        self.selected_stat = None
        self.round_result = None
        
        # Card viewer state
        self.viewer_index = 0
        self.viewer_sort = 'id'
    
    def run(self):
        """Main game loop."""
        running = True
        
        while running:
            # Handle different game states
            if self.state == 'menu':
                action = self.ui.draw_main_menu()
                if action == 'computer':
                    self.game_mode = 'computer'
                    self.state = 'difficulty_select'  # Go to difficulty selection
                elif action == 'player':
                    self.game_mode = 'player'
                    self.ai_difficulty = None
                    self.start_game()
                elif action == 'view_cards':
                    self.state = 'card_viewer'
                    self.viewer_index = 0
                    self.viewer_sort = 'id'
                elif action == 'read_story':
                    self.state = 'story_reader'
                elif action == 'quit':
                    running = False
            
            elif self.state == 'difficulty_select':
                difficulty = self.ui.draw_difficulty_menu()
                if difficulty in ['easy', 'moderate', 'hard', 'smart']:
                    self.ai_difficulty = difficulty
                    self.start_game()
                elif difficulty == 'back':
                    self.state = 'menu'
            
            elif self.state == 'story_reader':
                action = self.ui.draw_story_screen()
                
                if action == 'back':
                    self.state = 'menu'
                elif action == 'quit':
                    running = False
            
            elif self.state == 'card_viewer':
                action, new_index, new_sort = self.ui.draw_card_viewer(
                    self.game.deck, 
                    self.viewer_index,
                    self.viewer_sort
                )
                
                if action == 'back':
                    self.state = 'menu'
                elif action == 'quit':
                    running = False
                elif action == 'navigate':
                    self.viewer_index = new_index
                elif action == 'sort':
                    self.viewer_sort = new_sort
                    self.viewer_index = new_index
            
            elif self.state == 'playing':
                self.handle_playing_state()
            
            elif self.state == 'round_result':
                self.handle_result_state()
            
            elif self.state == 'game_over':
                self.handle_game_over_state()
            
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()
    
    def start_game(self):
        """Start a new game."""
        self.game.start_new_game()
        self.state = 'playing'
        self.selected_stat = None
        self.round_result = None
    
    def handle_playing_state(self):
        """Handle the playing state (choosing stats and comparing)."""
        game_state = self.game.get_game_state()
        
        # Draw current game state
        self.ui.draw_game_state(game_state, self.selected_stat, self.round_result, self.game_mode)
        
        # Update display once per frame
        pygame.display.flip()
        
        # Check whose turn it is
        active_player = self.game.active_player
        
        # ONLY auto-select in VS COMPUTER mode when it's computer's turn
        if self.game_mode == 'computer' and active_player == 'computer':
            # Computer auto-selects (only in VS Computer mode)
            if not hasattr(self, '_computer_delay_started'):
                self._computer_delay_started = pygame.time.get_ticks()
            
            # Wait 500ms before computer acts
            if pygame.time.get_ticks() - self._computer_delay_started > 500:
                self.computer_choose_stat()
                del self._computer_delay_started
            
            # Still handle quit event during delay
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        # ALL OTHER CASES: Manual selection (VS Computer player turn, or Pass & Play both players)
        else:
            # Pass & Play: Both Player 1 and Player 2 select manually
            # VS Computer: Player selects manually on their turn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Active player clicks stat
                    clicked_stat = self.ui.check_stat_click(event.pos)
                    if clicked_stat:
                        self.player_choose_stat(clicked_stat)
    
    def player_choose_stat(self, stat_key):
        """
        Handle player choosing a stat.
        
        Args:
            stat_key (str): The stat chosen by player
        """
        self.selected_stat = stat_key
        
        # Compare cards
        self.round_result = self.game.compare_cards(stat_key)
        
        # Switch to result display state
        self.state = 'round_result'
    
    def computer_choose_stat(self):
        """Handle computer choosing a stat."""
        # Computer AI picks stat based on difficulty
        stat_key = self.game.get_computer_stat_choice(self.ai_difficulty)
        self.selected_stat = stat_key
        
        # Compare cards
        self.round_result = self.game.compare_cards(stat_key)
        
        # Switch to result display state
        self.state = 'round_result'
    
    def handle_result_state(self):
        """Handle displaying the round result - wait for player to click Next Round."""
        game_state = self.game.get_game_state()
        
        # Clear any pending events when first entering result state
        # This prevents accidental clicks from triggering Next Round immediately
        if not hasattr(self, '_result_state_initialized'):
            pygame.event.clear()
            self._result_state_initialized = True
        
        # Always show both cards revealed and result message
        self.ui.draw_game_state(game_state, self.selected_stat, self.round_result, self.game_mode)
        
        # Draw "Next Round" button
        next_button = self.ui.draw_next_round_button()
        
        # Update display once per frame
        pygame.display.flip()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if Next Round button was clicked
                if next_button and next_button.collidepoint(event.pos):
                    # Resolve the round
                    self.game.resolve_round()
                    
                    # Clear initialization flag for next time
                    del self._result_state_initialized
                    
                    # Check if game is over
                    if self.game.game_over:
                        self.state = 'game_over'
                    else:
                        # Continue to next round
                        self.state = 'playing'
                        self.selected_stat = None
                        self.round_result = None
    
    def handle_game_over_state(self):
        """Handle game over screen."""
        game_state = self.game.get_game_state()
        
        # Draw final game state
        self.ui.draw_game_state(game_state, self.selected_stat, self.round_result, self.game_mode)
        
        # Draw game over overlay
        play_again_button = self.ui.draw_game_over(self.game.winner, self.game_mode)
        
        # Update display once per frame
        pygame.display.flip()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    # Restart game
                    self.start_game()


def main():
    """Entry point for the game."""
    print("=" * 60)
    print("DHARMA DUEL CARD GAME")
    print("=" * 60)
    print("\nStarting game...")
    
    try:
        game = DharmaDuel()
        game.run()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
