"""
UI module for Dharma Duel Card Game.

Handles all Pygame rendering: cards, stats, menus, and game screens.
"""

import pygame
from card import Card


class Colors:
    """Color palette for the game."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GOLD = (212, 175, 55)
    DARK_GOLD = (184, 134, 11)
    SAFFRON = (255, 153, 51)
    MAROON = (128, 0, 0)
    DARK_RED = (139, 0, 0)
    CREAM = (255, 253, 208)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    GREEN = (0, 150, 0)
    RED = (200, 0, 0)
    BLUE = (0, 100, 200)
    LIGHT_BLUE = (100, 150, 255)
    BROWN = (139, 69, 19)  # Saddle brown
    DARK_BROWN = (101, 67, 33)  # Darker brown for card back
    CARD_BG = (245, 245, 220)  # Beige
    CARD_BORDER = (139, 69, 19)  # Saddle brown


class UI:
    """
    Manages all game rendering and user interface.
    """
    
    def __init__(self, screen_width=1200, screen_height=700):
        """
        Initialize UI system.
        
        Args:
            screen_width (int): Window width (optimized for 14" laptop)
            screen_height (int): Window height (optimized for 14" laptop)
        """
        pygame.init()
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dharma Duel Card Game")
        
        # Load fonts (using system fonts for now)
        self.title_font = pygame.font.Font(None, 42)
        self.header_font = pygame.font.Font(None, 32)
        self.stat_font = pygame.font.Font(None, 24)
        self.text_font = pygame.font.Font(None, 20)
        self.small_font = pygame.font.Font(None, 16)
        
        # Card dimensions and positions (scaled down for laptop)
        self.card_width = 360
        self.card_height = 580
        self.card_padding = 40
        
        # Calculate card positions (side by side with gap)
        gap = 80
        total_card_width = (self.card_width * 2) + gap
        start_x = (screen_width - total_card_width) // 2
        
        self.player_card_x = start_x
        self.computer_card_x = start_x + self.card_width + gap
        self.card_y = 100  # Moved down to make room for progress bar
        
        # Button tracking for stat selection
        self.stat_buttons = []  # Will store (rect, stat_key) tuples
        
    def draw_main_menu(self):
        """
        Draw the main menu screen with game mode selection.
        
        Returns:
            str: Action based on user input ('computer', 'player', 'quit', None)
        """
        self.screen.fill(Colors.MAROON)
        
        # Title
        title = self.title_font.render("DHARMA DUEL", True, Colors.GOLD)
        title_rect = title.get_rect(center=(self.screen_width // 2, 100))
        self.screen.blit(title, title_rect)
        
        subtitle = self.header_font.render("Card Game", True, Colors.CREAM)
        subtitle_rect = subtitle.get_rect(center=(self.screen_width // 2, 145))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Instructions
        instructions = [
            "Ancient India • Buddha's Time",
            "",
            "Top Trumps style card battle",
            "Choose your best stat to win cards",
            "",
            "SELECT MODE:"
        ]
        
        y = 200
        for line in instructions:
            text = self.text_font.render(line, True, Colors.CREAM)
            text_rect = text.get_rect(center=(self.screen_width // 2, y))
            self.screen.blit(text, text_rect)
            y += 30
        
        # Button dimensions
        button_width = 250
        button_height = 60
        button_gap = 20
        
        # Calculate positions for FOUR buttons (2 rows of 2)
        row1_y = y + 20
        row2_y = row1_y + button_height + button_gap
        
        col1_x = (self.screen_width // 2) - button_width - (button_gap // 2)
        col2_x = (self.screen_width // 2) + (button_gap // 2)
        
        # VS COMPUTER button (top left)
        computer_button = pygame.Rect(col1_x, row1_y, button_width, button_height)
        
        # VS PLAYER button (top right)
        player_button = pygame.Rect(col2_x, row1_y, button_width, button_height)
        
        # VIEW CARDS button (bottom left)
        view_button = pygame.Rect(col1_x, row2_y, button_width, button_height)
        
        # READ STORY button (bottom right) - NEW!
        story_button = pygame.Rect(col2_x, row2_y, button_width, button_height)
        
        # Check for hover
        mouse_pos = pygame.mouse.get_pos()
        
        # Draw Computer button (top left)
        if computer_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, computer_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, computer_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, computer_button, 3, border_radius=10)
        
        comp_text = self.stat_font.render("VS COMPUTER", True, text_color)
        comp_text_rect = comp_text.get_rect(center=computer_button.center)
        self.screen.blit(comp_text, comp_text_rect)
        
        comp_desc = self.small_font.render("Play against AI", True, text_color)
        comp_desc_rect = comp_desc.get_rect(center=(computer_button.centerx, 
                                                      computer_button.centery + 20))
        self.screen.blit(comp_desc, comp_desc_rect)
        
        # Draw Player button (top right)
        if player_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, player_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, player_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, player_button, 3, border_radius=10)
        
        player_text = self.stat_font.render("VS PLAYER", True, text_color)
        player_text_rect = player_text.get_rect(center=player_button.center)
        self.screen.blit(player_text, player_text_rect)
        
        player_desc = self.small_font.render("Pass & Play", True, text_color)
        player_desc_rect = player_desc.get_rect(center=(player_button.centerx, 
                                                          player_button.centery + 20))
        self.screen.blit(player_desc, player_desc_rect)
        
        # Draw View Cards button (bottom left)
        if view_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, view_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, view_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, view_button, 3, border_radius=10)
        
        view_text = self.stat_font.render("VIEW CARDS", True, text_color)
        view_text_rect = view_text.get_rect(center=view_button.center)
        self.screen.blit(view_text, view_text_rect)
        
        view_desc = self.small_font.render("Compare all 40", True, text_color)
        view_desc_rect = view_desc.get_rect(center=(view_button.centerx, 
                                                      view_button.centery + 20))
        self.screen.blit(view_desc, view_desc_rect)
        
        # Draw Read Story button (bottom right) - NEW!
        if story_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, story_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, story_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, story_button, 3, border_radius=10)
        
        story_text = self.stat_font.render("READ STORY", True, text_color)
        story_text_rect = story_text.get_rect(center=story_button.center)
        self.screen.blit(story_text, story_text_rect)
        
        story_desc = self.small_font.render("Epic legend", True, text_color)
        story_desc_rect = story_desc.get_rect(center=(story_button.centerx, 
                                                        story_button.centery + 20))
        self.screen.blit(story_desc, story_desc_rect)
        
        # Help text
        help_text = self.small_font.render("Discover the legend of the Dharma Council - an epic gathering of 40 legendary beings", 
                                            True, Colors.LIGHT_GRAY)
        help_rect = help_text.get_rect(center=(self.screen_width // 2, row2_y + button_height + 20))
        self.screen.blit(help_text, help_rect)
        
        # Check for click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if computer_button.collidepoint(event.pos):
                    return 'computer'
                elif player_button.collidepoint(event.pos):
                    return 'player'
                elif view_button.collidepoint(event.pos):
                    return 'view_cards'
                elif story_button.collidepoint(event.pos):
                    return 'read_story'
        
        pygame.display.flip()
        return None
    
    def draw_difficulty_menu(self):
        """
        Draw the AI difficulty selection menu.
        
        Returns:
            str: Difficulty level ('easy', 'moderate', 'hard', 'smart', 'back')
        """
        self.screen.fill(Colors.MAROON)
        
        # Title
        title = self.title_font.render("SELECT DIFFICULTY", True, Colors.GOLD)
        title_rect = title.get_rect(center=(self.screen_width // 2, 80))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.text_font.render("Choose your AI opponent's skill level", True, Colors.CREAM)
        subtitle_rect = subtitle.get_rect(center=(self.screen_width // 2, 130))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Button dimensions
        button_width = 400
        button_height = 80
        button_gap = 15
        start_y = 180
        
        # Create 4 difficulty buttons
        easy_button = pygame.Rect(
            (self.screen_width - button_width) // 2,
            start_y,
            button_width,
            button_height
        )
        
        moderate_button = pygame.Rect(
            (self.screen_width - button_width) // 2,
            start_y + (button_height + button_gap),
            button_width,
            button_height
        )
        
        hard_button = pygame.Rect(
            (self.screen_width - button_width) // 2,
            start_y + 2 * (button_height + button_gap),
            button_width,
            button_height
        )
        
        smart_button = pygame.Rect(
            (self.screen_width - button_width) // 2,
            start_y + 3 * (button_height + button_gap),
            button_width,
            button_height
        )
        
        # Back button
        back_button = pygame.Rect(
            (self.screen_width - 200) // 2,
            self.screen_height - 80,
            200,
            50
        )
        
        mouse_pos = pygame.mouse.get_pos()
        
        # Difficulty buttons data
        difficulties = [
            (easy_button, "1. EASY AI MODE", "Low odds of AI winning", Colors.GREEN),
            (moderate_button, "2. MODERATE AI MODE", "Medium odds of AI winning", Colors.GOLD),
            (hard_button, "3. HARD AI MODE", "High odds of AI winning", Colors.RED),
            (smart_button, "4. SMART AI MODE", "(behaves like a strategic human)", Colors.LIGHT_BLUE)
        ]
        
        # Draw difficulty buttons
        for button, title_text, desc, color in difficulties:
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, color, button, border_radius=10)
                text_color = Colors.BLACK
                desc_color = Colors.BLACK
            else:
                pygame.draw.rect(self.screen, Colors.DARK_GRAY, button, border_radius=10)
                text_color = Colors.CREAM
                desc_color = Colors.LIGHT_GRAY
            pygame.draw.rect(self.screen, color, button, 3, border_radius=10)
            
            # Title
            title_surface = self.stat_font.render(title_text, True, text_color)
            title_rect = title_surface.get_rect(center=(button.centerx, button.centery - 12))
            self.screen.blit(title_surface, title_rect)
            
            # Description
            desc_surface = self.small_font.render(desc, True, desc_color)
            desc_rect = desc_surface.get_rect(center=(button.centerx, button.centery + 15))
            self.screen.blit(desc_surface, desc_rect)
        
        # Draw back button
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, back_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, back_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, back_button, 3, border_radius=10)
        
        back_text = self.stat_font.render("← BACK", True, text_color)
        back_text_rect = back_text.get_rect(center=back_button.center)
        self.screen.blit(back_text, back_text_rect)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'back'
                elif event.key == pygame.K_1:
                    return 'easy'
                elif event.key == pygame.K_2:
                    return 'moderate'
                elif event.key == pygame.K_3:
                    return 'hard'
                elif event.key == pygame.K_4:
                    return 'smart'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return 'easy'
                elif moderate_button.collidepoint(event.pos):
                    return 'moderate'
                elif hard_button.collidepoint(event.pos):
                    return 'hard'
                elif smart_button.collidepoint(event.pos):
                    return 'smart'
                elif back_button.collidepoint(event.pos):
                    return 'back'
        
        pygame.display.flip()
        return None
    
    def draw_card_viewer(self, deck, current_index=0, sort_by='id'):
        """
        Draw card comparison viewer showing all cards.
        
        Args:
            deck (CardDeck): Deck of all cards
            current_index (int): Currently selected card index
            sort_by (str): Sort method - 'id', 'name', 'power', 'wisdom', etc.
            
        Returns:
            tuple: (action, new_index, new_sort) or ('back', None, None)
        """
        self.screen.fill(Colors.MAROON)
        
        # Title
        title_text = self.title_font.render("CARD VIEWER", True, Colors.GOLD)
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 30))
        self.screen.blit(title_text, title_rect)
        
        # Sort all cards
        cards = list(deck.cards)
        if sort_by == 'name':
            cards.sort(key=lambda c: c.name)
        elif sort_by == 'ranking':
            # Sort by overall rating (highest first)
            cards.sort(key=lambda c: c.overall_rating, reverse=True)
        elif sort_by in ['power', 'wisdom', 'resolve', 'influence', 'transformation', 'merit']:
            cards.sort(key=lambda c: c.stats[sort_by], reverse=True)
        # else keep ID order
        
        # Current card display (large, left side)
        current_card = cards[current_index]
        card_x = 50
        card_y = 100
        
        # Draw current card large
        self.draw_card(current_card, card_x, card_y, show_stats=True, is_player_card=True)
        
        # Card info
        info_x = card_x + self.card_width + 40
        info_y = card_y
        
        # Card counter
        counter_text = self.header_font.render(
            f"Card {current_index + 1} of {len(cards)}", 
            True, Colors.CREAM
        )
        counter_rect = counter_text.get_rect(topleft=(info_x, info_y))
        self.screen.blit(counter_text, counter_rect)
        
        # Sort options
        sort_y = info_y + 50
        sort_label = self.text_font.render("Sort by:", True, Colors.CREAM)
        self.screen.blit(sort_label, (info_x, sort_y))
        
        # Sort buttons
        sort_options = [
            ('ID', 'id'),
            ('Name', 'name'),
            ('Ranking', 'ranking'),
            ('Power', 'power'),
            ('Wisdom', 'wisdom'),
            ('Resolve', 'resolve'),
            ('Influence', 'influence'),
            ('Transform', 'transformation'),
            ('Merit', 'merit')
        ]
        
        button_width = 100
        button_height = 35
        button_gap = 10
        sort_button_y = sort_y + 30
        
        sort_buttons = []
        for i, (label, key) in enumerate(sort_options):
            if i < 5:  # First row: ID, Name, Ranking, Power, Wisdom
                btn_x = info_x + (i * (button_width + button_gap))
                btn_y = sort_button_y
            else:  # Second row: Resolve, Influence, Transform, Merit
                btn_x = info_x + ((i - 5) * (button_width + button_gap))
                btn_y = sort_button_y + button_height + button_gap
            
            btn_rect = pygame.Rect(btn_x, btn_y, button_width, button_height)
            sort_buttons.append((btn_rect, key, label))
            
            # Draw button
            mouse_pos = pygame.mouse.get_pos()
            if key == sort_by:
                color = Colors.GOLD
                text_color = Colors.BLACK
            elif btn_rect.collidepoint(mouse_pos):
                color = Colors.SAFFRON
                text_color = Colors.BLACK
            else:
                color = Colors.DARK_GOLD
                text_color = Colors.CREAM
            
            pygame.draw.rect(self.screen, color, btn_rect, border_radius=5)
            pygame.draw.rect(self.screen, Colors.BLACK, btn_rect, 2, border_radius=5)
            
            btn_text = self.small_font.render(label, True, text_color)
            btn_text_rect = btn_text.get_rect(center=btn_rect.center)
            self.screen.blit(btn_text, btn_text_rect)
        
        # Stats comparison table (right side, scrollable list)
        table_x = info_x
        table_y = sort_button_y + (button_height + button_gap) * 2 + 30
        table_width = self.screen_width - info_x - 50
        table_height = self.screen_height - table_y - 100
        
        # Draw comparison table header
        header_text = self.stat_font.render("All Cards Comparison", True, Colors.GOLD)
        self.screen.blit(header_text, (table_x, table_y - 30))
        
        # Table with stats
        row_height = 25
        visible_rows = int(table_height / row_height)
        
        # Column headers for stats (moved higher above table)
        header_y = table_y - 20  # Increased from -5 to -20
        
        # Add rank header if sorted by ranking
        if sort_by == 'ranking':
            rank_header = self.stat_font.render("#", True, Colors.GOLD)
            self.screen.blit(rank_header, (table_x - 30, header_y))
        
        stat_x = table_x + 250
        stat_labels = ['P', 'W', 'R', 'I', 'T', 'M']  # Power, Wisdom, Resolve, Influence, Transform, Merit
        
        # Draw header background for better visibility
        header_bg = pygame.Rect(stat_x - 5, header_y - 3, 70 * 6 + 10, 20)
        pygame.draw.rect(self.screen, Colors.DARK_BROWN, header_bg, border_radius=3)
        
        for i, label in enumerate(stat_labels):
            label_text = self.stat_font.render(label, True, Colors.GOLD)  # Changed from small_font to stat_font for visibility
            self.screen.blit(label_text, (stat_x + (i * 70), header_y))
        
        # Add rating header if sorted by ranking
        if sort_by == 'ranking':
            rating_header = self.stat_font.render("Rating", True, Colors.GOLD)
            self.screen.blit(rating_header, (stat_x + (6 * 70), header_y))
        
        # Scroll offset (show current card in middle if possible)
        scroll_offset = max(0, current_index - visible_rows // 2)
        scroll_offset = min(scroll_offset, len(cards) - visible_rows)
        scroll_offset = max(0, scroll_offset)
        
        for i in range(visible_rows):
            card_idx = scroll_offset + i
            if card_idx >= len(cards):
                break
            
            card = cards[card_idx]
            row_y = table_y + (i * row_height)
            
            # Highlight current card
            if card_idx == current_index:
                highlight_rect = pygame.Rect(table_x - 5, row_y - 2, 
                                             table_width + 10, row_height + 4)
                pygame.draw.rect(self.screen, Colors.GOLD, highlight_rect, 2, border_radius=3)
            
            # Show rank number if sorted by ranking
            if sort_by == 'ranking':
                rank_text = self.small_font.render(f"{card_idx + 1}", True, Colors.GOLD)
                self.screen.blit(rank_text, (table_x - 30, row_y))
            
            # Card name (truncated if needed)
            name = card.name[:20] + "..." if len(card.name) > 20 else card.name
            name_text = self.small_font.render(name, True, Colors.CREAM)
            self.screen.blit(name_text, (table_x, row_y))
            
            # Stats
            stat_x = table_x + 250
            for stat_key in ['power', 'wisdom', 'resolve', 'influence', 'transformation', 'merit']:
                value = card.stats[stat_key]
                
                # Color code by value
                if value == 100:
                    color = Colors.GOLD
                elif value >= 95:
                    color = Colors.GREEN
                elif value >= 90:
                    color = Colors.CREAM
                else:
                    color = Colors.LIGHT_GRAY
                
                stat_text = self.small_font.render(str(value), True, color)
                self.screen.blit(stat_text, (stat_x, row_y))
                stat_x += 70
            
            # Show overall rating if sorted by ranking
            if sort_by == 'ranking':
                rating_color = Colors.GOLD if card.tier == 'platinum' else Colors.GREEN if card.tier == 'gold' else Colors.CREAM
                rating_text = self.small_font.render(f"{card.overall_rating:.1f}", True, rating_color)
                self.screen.blit(rating_text, (stat_x, row_y))
        
        # Navigation buttons
        nav_y = self.screen_height - 70
        
        # Back button
        back_button = pygame.Rect(50, nav_y, 150, 50)
        mouse_pos = pygame.mouse.get_pos()
        
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, back_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, back_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, back_button, 3, border_radius=10)
        
        back_text = self.stat_font.render("← BACK", True, text_color)
        back_text_rect = back_text.get_rect(center=back_button.center)
        self.screen.blit(back_text, back_text_rect)
        
        # Previous/Next buttons
        prev_button = pygame.Rect(250, nav_y, 150, 50)
        next_button = pygame.Rect(420, nav_y, 150, 50)
        
        # Previous button
        if current_index > 0:
            if prev_button.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, Colors.GOLD, prev_button, border_radius=10)
                text_color = Colors.BLACK
            else:
                pygame.draw.rect(self.screen, Colors.DARK_GOLD, prev_button, border_radius=10)
                text_color = Colors.CREAM
            pygame.draw.rect(self.screen, Colors.BLACK, prev_button, 3, border_radius=10)
            
            prev_text = self.stat_font.render("← PREV", True, text_color)
            prev_text_rect = prev_text.get_rect(center=prev_button.center)
            self.screen.blit(prev_text, prev_text_rect)
        
        # Next button
        if current_index < len(cards) - 1:
            if next_button.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, Colors.GOLD, next_button, border_radius=10)
                text_color = Colors.BLACK
            else:
                pygame.draw.rect(self.screen, Colors.DARK_GOLD, next_button, border_radius=10)
                text_color = Colors.CREAM
            pygame.draw.rect(self.screen, Colors.BLACK, next_button, 3, border_radius=10)
            
            next_text = self.stat_font.render("NEXT →", True, text_color)
            next_text_rect = next_text.get_rect(center=next_button.center)
            self.screen.blit(next_text, next_text_rect)
        
        # Instructions
        inst_text = self.small_font.render(
            "Click card in list to view • Arrow keys to navigate • ESC to go back",
            True, Colors.LIGHT_GRAY
        )
        inst_rect = inst_text.get_rect(center=(self.screen_width // 2, nav_y + 25))
        self.screen.blit(inst_text, inst_rect)
        
        # Stat legend (below comparison table, above navigation)
        legend_y = self.screen_height - 90
        legend_text = self.small_font.render(
            "Stats: P=Power  W=Wisdom  R=Resolve  I=Influence  T=Transform  M=Merit",
            True, Colors.CREAM
        )
        legend_rect = legend_text.get_rect(center=(self.screen_width // 2, legend_y))
        self.screen.blit(legend_text, legend_rect)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ('quit', None, None)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ('back', None, None)
                elif event.key == pygame.K_LEFT and current_index > 0:
                    return ('navigate', current_index - 1, sort_by)
                elif event.key == pygame.K_RIGHT and current_index < len(cards) - 1:
                    return ('navigate', current_index + 1, sort_by)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check back button
                if back_button.collidepoint(event.pos):
                    return ('back', None, None)
                
                # Check prev/next buttons
                if current_index > 0 and prev_button.collidepoint(event.pos):
                    return ('navigate', current_index - 1, sort_by)
                if current_index < len(cards) - 1 and next_button.collidepoint(event.pos):
                    return ('navigate', current_index + 1, sort_by)
                
                # Check sort buttons
                for btn_rect, key, label in sort_buttons:
                    if btn_rect.collidepoint(event.pos):
                        return ('sort', 0, key)  # Reset to first card when sorting
                
                # Check if clicked on a card in the list
                for i in range(visible_rows):
                    card_idx = scroll_offset + i
                    if card_idx >= len(cards):
                        break
                    
                    row_y = table_y + (i * row_height)
                    row_rect = pygame.Rect(table_x - 5, row_y - 2, table_width + 10, row_height + 4)
                    
                    if row_rect.collidepoint(event.pos):
                        return ('navigate', card_idx, sort_by)
        
        pygame.display.flip()
        return (None, current_index, sort_by)
    
    def draw_story_screen(self):
        """
        Draw the story screen showing the epic Dharma Council legend.
        
        Returns:
            str: 'back' to return to menu, 'quit' to exit, or None to continue
        """
        self.screen.fill(Colors.MAROON)
        
        # Title
        title_text = self.title_font.render("THE DHARMA COUNCIL", True, Colors.GOLD)
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 30))
        self.screen.blit(title_text, title_rect)
        
        subtitle_text = self.header_font.render("An Epic Gathering of Legends", True, Colors.CREAM)
        subtitle_rect = subtitle_text.get_rect(center=(self.screen_width // 2, 70))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Story box
        story_box = pygame.Rect(80, 110, self.screen_width - 160, self.screen_height - 200)
        pygame.draw.rect(self.screen, Colors.DARK_BROWN, story_box, border_radius=15)
        pygame.draw.rect(self.screen, Colors.GOLD, story_box, 3, border_radius=15)
        
        # Epic story text
        story = (
            "In the sacred groves of ancient India, a mystical tournament unfolds. The Dharma Council has "
            "convened—an assembly of the greatest minds and spirits from Buddha's era.\n\n"
            
            "From the enlightened Buddha himself to fierce Emperor Ashoka, from the wise Sariputta to the "
            "tempting Mara, forty legendary beings have gathered to test their mastery of Power, Wisdom, "
            "Resolve, Influence, Transformation, and Merit.\n\n"
            
            "But this is no ordinary contest. Each battle reveals profound truths about the nature of "
            "enlightenment. The reformed courtesan Amrapali stands equal to mighty emperors. The gentle "
            "benefactor Sujata's merit rivals that of powerful deities. Even Mara, lord of delusion, "
            "commands respect for his influence over mortal minds.\n\n"
            
            "You are summoned to lead these legends in strategic duels. Study their strengths, exploit "
            "their weaknesses, and discover which virtues triumph when enlightenment itself is at stake. "
            "Will Wisdom overcome Power? Can Transformation defeat Influence?\n\n"
            
            "The council awaits. Choose your champion. Let the Dharma Duel begin!"
        )
        
        # Word wrap the story with paragraph breaks
        paragraphs = story.split('\n\n')
        all_lines = []
        max_width = story_box.width - 40
        
        for para in paragraphs:
            words = para.split()
            current_line = []
            
            for word in words:
                test_line = ' '.join(current_line + [word])
                test_surface = self.text_font.render(test_line, True, Colors.CREAM)
                if test_surface.get_width() <= max_width:
                    current_line.append(word)
                else:
                    if current_line:
                        all_lines.append(' '.join(current_line))
                    current_line = [word]
            
            if current_line:
                all_lines.append(' '.join(current_line))
            
            # Add blank line between paragraphs
            all_lines.append('')
        
        # Draw story lines
        text_y = story_box.y + 20
        line_height = 28
        
        for line in all_lines:
            if line:  # Non-empty line
                line_text = self.text_font.render(line, True, Colors.CREAM)
                self.screen.blit(line_text, (story_box.x + 20, text_y))
            text_y += line_height
        
        # Attribution
        attr_y = text_y + 10
        attr_text = self.small_font.render("— The Legend of the Dharma Council", 
                                           True, Colors.LIGHT_GRAY)
        attr_rect = attr_text.get_rect(center=(self.screen_width // 2, attr_y))
        self.screen.blit(attr_text, attr_rect)
        
        # Back button
        back_button = pygame.Rect(self.screen_width // 2 - 100, self.screen_height - 70, 200, 50)
        mouse_pos = pygame.mouse.get_pos()
        
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, back_button, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, back_button, border_radius=10)
            text_color = Colors.CREAM
        pygame.draw.rect(self.screen, Colors.BLACK, back_button, 3, border_radius=10)
        
        back_text = self.stat_font.render("← BACK TO MENU", True, text_color)
        back_text_rect = back_text.get_rect(center=back_button.center)
        self.screen.blit(back_text, back_text_rect)
        
        # Instructions
        inst_text = self.small_font.render("Press ESC or click BACK to return to menu", 
                                          True, Colors.LIGHT_GRAY)
        inst_rect = inst_text.get_rect(center=(self.screen_width // 2, self.screen_height - 15))
        self.screen.blit(inst_text, inst_rect)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'back'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return 'back'
        
        pygame.display.flip()
        return None
    
    def draw_card(self, card, x, y, show_stats=True, is_player_card=True, 
                  highlight_stat=None, winning_stat=None, player_won=False, player_lost=False):
        """
        Draw a single card with fact file, stats, and story.
        
        Args:
            card (Card): Card object to display
            x (int): X position
            y (int): Y position
            show_stats (bool): Whether to show card (False = card back)
            is_player_card (bool): True if player's card (for interaction)
            highlight_stat (str): Stat to highlight (for selection)
            winning_stat (str): Stat that was selected in battle
            player_won (bool): True if this card's owner won the round
            player_lost (bool): True if this card's owner lost the round
        """
        # Card background
        card_rect = pygame.Rect(x, y, self.card_width, self.card_height)
        
        # If stats hidden, show card back instead
        if not show_stats:
            # Card back design - Dharmachakra (Wheel of Dharma)
            pygame.draw.rect(self.screen, Colors.DARK_BROWN, card_rect, border_radius=15)
            pygame.draw.rect(self.screen, Colors.GOLD, card_rect, 4, border_radius=15)
            
            # Draw Dharmachakra wheel (actual graphic)
            center_x = x + self.card_width // 2
            center_y = y + self.card_height // 2 - 20
            
            # Outer circle (rim of wheel)
            outer_radius = 80
            pygame.draw.circle(self.screen, Colors.GOLD, (center_x, center_y), outer_radius, 4)
            
            # Inner circle (hub of wheel)
            hub_radius = 20
            pygame.draw.circle(self.screen, Colors.GOLD, (center_x, center_y), hub_radius)
            pygame.draw.circle(self.screen, Colors.DARK_BROWN, (center_x, center_y), hub_radius - 4)
            
            # Draw 8 spokes (representing the Noble Eightfold Path)
            import math
            for i in range(8):
                angle = math.radians(i * 45)  # 8 spokes, 45 degrees apart
                # Start from hub
                start_x = center_x + hub_radius * math.cos(angle)
                start_y = center_y + hub_radius * math.sin(angle)
                # End at rim
                end_x = center_x + outer_radius * math.cos(angle)
                end_y = center_y + outer_radius * math.sin(angle)
                # Draw spoke
                pygame.draw.line(self.screen, Colors.GOLD, 
                               (start_x, start_y), (end_x, end_y), 3)
            
            # Draw decorative dots between spokes (traditional design)
            dot_radius = outer_radius - 15
            for i in range(8):
                angle = math.radians(i * 45 + 22.5)  # Offset by 22.5 degrees
                dot_x = center_x + dot_radius * math.cos(angle)
                dot_y = center_y + dot_radius * math.sin(angle)
                pygame.draw.circle(self.screen, Colors.GOLD, (int(dot_x), int(dot_y)), 5)
            
            # Draw "Dharma Wheel" text below
            dharma_text = self.header_font.render("Dharma Wheel", True, Colors.CREAM)
            dharma_rect = dharma_text.get_rect(center=(center_x, center_y + 110))
            self.screen.blit(dharma_text, dharma_rect)
            return
        
        # Normal card display (when show_stats=True)
        pygame.draw.rect(self.screen, Colors.CARD_BG, card_rect, border_radius=15)
        
        # Tier-based border colors
        tier_colors = {
            'platinum': (230, 230, 250),  # Light platinum/silver-white
            'gold': Colors.GOLD,           # Gold
            'silver': (192, 192, 192),     # Silver
            'bronze': (205, 127, 50)       # Bronze
        }
        
        border_color = tier_colors.get(card.tier, Colors.CARD_BORDER)
        border_width = 6 if card.tier == 'platinum' else 5 if card.is_legend else 4
        
        # Draw tier-colored border
        pygame.draw.rect(self.screen, border_color, card_rect, border_width, border_radius=15)
        
        # Add rating badge in top-RIGHT corner (larger and clearer)
        rating_text = self.stat_font.render(f"{card.overall_rating:.0f}", True, Colors.BLACK)
        rating_bg = pygame.Rect(x + self.card_width - 50, y + 5, 45, 30)
        
        # Rating background color matches tier
        rating_bg_color = tier_colors.get(card.tier, (205, 127, 50))
        pygame.draw.rect(self.screen, rating_bg_color, rating_bg, border_radius=5)
        pygame.draw.rect(self.screen, Colors.BLACK, rating_bg, 2, border_radius=5)
        
        rating_rect = rating_text.get_rect(center=rating_bg.center)
        self.screen.blit(rating_text, rating_rect)
        
        # Legend cards get star ABOVE rating badge
        if card.is_legend:
            star_text = self.header_font.render("⭐", True, Colors.GOLD)
            star_rect = star_text.get_rect(centerx=rating_bg.centerx, bottom=rating_bg.top - 2)
            self.screen.blit(star_text, star_rect)
        
        current_y = y + 15
        
        # --- FACT FILE SECTION (TOP) ---
        # Card name (smaller font)
        name_text = self.stat_font.render(card.name, True, Colors.MAROON)
        # Word wrap if name is too long
        if name_text.get_width() > self.card_width - 30:
            # Split name for long names
            words = card.name.split()
            line1 = ""
            line2 = ""
            for word in words:
                test_line = line1 + word + " "
                test_surface = self.stat_font.render(test_line, True, Colors.MAROON)
                if test_surface.get_width() <= self.card_width - 30:
                    line1 = test_line
                else:
                    line2 += word + " "
            
            if line1:
                text1 = self.stat_font.render(line1.strip(), True, Colors.MAROON)
                self.screen.blit(text1, (x + 15, current_y))
                current_y += 28
            if line2:
                text2 = self.stat_font.render(line2.strip(), True, Colors.MAROON)
                self.screen.blit(text2, (x + 15, current_y))
                current_y += 28
        else:
            self.screen.blit(name_text, (x + 15, current_y))
            current_y += 30
        
        # Archetype
        archetype_text = self.small_font.render(card.archetype, True, Colors.DARK_GRAY)
        self.screen.blit(archetype_text, (x + 15, current_y))
        current_y += 22
        
        # Divider
        pygame.draw.line(self.screen, Colors.DARK_GOLD, 
                        (x + 15, current_y), (x + self.card_width - 15, current_y), 2)
        current_y += 12
        
        # Fact file points (more compact)
        for fact in card.fact_file:
            # Word wrap facts
            words = fact.split()
            line = ""
            for word in words:
                test_line = line + word + " "
                test_surface = self.small_font.render(test_line, True, Colors.BLACK)
                if test_surface.get_width() <= self.card_width - 35:
                    line = test_line
                else:
                    # Render current line
                    if line:
                        fact_text = self.small_font.render(line.strip(), True, Colors.BLACK)
                        self.screen.blit(fact_text, (x + 18, current_y))
                        current_y += 20
                    line = word + " "
            
            # Render remaining text
            if line:
                fact_text = self.small_font.render(line.strip(), True, Colors.BLACK)
                self.screen.blit(fact_text, (x + 18, current_y))
                current_y += 20
        
        current_y += 8
        
        # --- STATS SECTION (MIDDLE) ---
        pygame.draw.line(self.screen, Colors.DARK_GOLD, 
                        (x + 15, current_y), (x + self.card_width - 15, current_y), 2)
        current_y += 10
        
        # Clear previous stat buttons if this is player's card
        if is_player_card:
            self.stat_buttons = []
        
        # Draw each stat (more compact)
        for stat_key in Card.STAT_ORDER:
            stat_name = Card.STAT_NAMES[stat_key]
            stat_value = card.get_stat(stat_key)
            
            # Create clickable area for player's card
            stat_rect = pygame.Rect(x + 15, current_y, self.card_width - 30, 30)
            
            # Determine background color based on win/loss/highlight
            bg_color = Colors.CREAM
            
            # If this stat was selected and there's a result
            if winning_stat == stat_key:
                if player_won:
                    bg_color = Colors.GREEN  # Win = Green
                elif player_lost:
                    bg_color = Colors.RED    # Loss = Red
                # If tie, stays cream (default)
            # Before result, show hover effect
            elif is_player_card and show_stats and not winning_stat:
                mouse_pos = pygame.mouse.get_pos()
                if stat_rect.collidepoint(mouse_pos):
                    bg_color = Colors.LIGHT_GRAY
            
            # Draw stat background
            pygame.draw.rect(self.screen, bg_color, stat_rect, border_radius=5)
            pygame.draw.rect(self.screen, Colors.DARK_GRAY, stat_rect, 1, border_radius=5)
            
            # Draw stat text (smaller font)
            stat_text = self.text_font.render(stat_name, True, Colors.BLACK)
            self.screen.blit(stat_text, (x + 18, current_y + 6))
            
            # Draw stat value (or ??? if hidden)
            if show_stats:
                value_text = self.text_font.render(str(stat_value), True, Colors.MAROON)
                value_rect = value_text.get_rect(right=x + self.card_width - 22, centery=current_y + 15)
                self.screen.blit(value_text, value_rect)
            else:
                value_text = self.text_font.render("???", True, Colors.DARK_GRAY)
                value_rect = value_text.get_rect(right=x + self.card_width - 22, centery=current_y + 15)
                self.screen.blit(value_text, value_rect)
            
            # Store button for click detection (player's card only)
            if is_player_card and show_stats:
                self.stat_buttons.append((stat_rect, stat_key))
            
            current_y += 34
        
        current_y += 5
        
        # --- FAMOUS STORY SECTION (BOTTOM) ---
        pygame.draw.line(self.screen, Colors.DARK_GOLD, 
                        (x + 15, current_y), (x + self.card_width - 15, current_y), 2)
        current_y += 10
        
        story_label = self.text_font.render("Famous Story:", True, Colors.DARK_GOLD)
        self.screen.blit(story_label, (x + 15, current_y))
        current_y += 22
        
        # Word wrap story (smaller font)
        words = card.famous_story.split()
        line = ""
        for word in words:
            test_line = line + word + " "
            test_surface = self.small_font.render(test_line, True, Colors.BLACK)
            if test_surface.get_width() <= self.card_width - 35:
                line = test_line
            else:
                if line:
                    story_text = self.small_font.render(line.strip(), True, Colors.BLACK)
                    self.screen.blit(story_text, (x + 18, current_y))
                    current_y += 19
                line = word + " "
        
        # Render remaining text
        if line:
            story_text = self.small_font.render(line.strip(), True, Colors.BLACK)
            self.screen.blit(story_text, (x + 18, current_y))
    
    def draw_game_state(self, game_state, selected_stat=None, result=None, game_mode='computer'):
        """
        Draw the main game screen with both cards.
        
        Args:
            game_state (dict): Current game state from Game.get_game_state()
            selected_stat (str): Currently selected stat (for highlighting)
            result (dict): Round result (for showing winner)
        """
        self.screen.fill(Colors.MAROON)
        
        # Draw prominent card counters with visual bars
        player_cards = game_state['player_cards_remaining']
        computer_cards = game_state['computer_cards_remaining']
        total_cards = player_cards + computer_cards
        
        # === CARD STACK VISUALIZATION ===
        # Draw card stack icons to show how many cards each player has
        
        # Calculate bar widths - more compact for laptop
        bar_width = 250
        bar_height = 25
        bar_x = (self.screen_width - bar_width) // 2
        bar_y = 15
        
        # Player bar (left side, green)
        if total_cards > 0:
            player_bar_width = int((player_cards / total_cards) * bar_width)
        else:
            player_bar_width = 0
            
        # Draw progress bar background
        pygame.draw.rect(self.screen, Colors.DARK_GRAY, 
                        (bar_x, bar_y, bar_width, bar_height), border_radius=12)
        
        # Draw player portion (green, from left)
        if player_bar_width > 0:
            pygame.draw.rect(self.screen, Colors.GREEN, 
                            (bar_x, bar_y, player_bar_width, bar_height), border_radius=12)
        
        # Draw computer portion (red, from right)
        computer_bar_width = bar_width - player_bar_width
        if computer_bar_width > 0:
            pygame.draw.rect(self.screen, Colors.RED, 
                            (bar_x + player_bar_width, bar_y, computer_bar_width, bar_height), 
                            border_radius=12)
        
        # Draw border around entire bar
        pygame.draw.rect(self.screen, Colors.GOLD, 
                        (bar_x, bar_y, bar_width, bar_height), 2, border_radius=12)
        
        # === CARD COUNT TEXT - More prominent ===
        # Draw large card counts with "stack" visualization
        count_y = bar_y + bar_height + 8
        
        # Determine labels based on game mode
        if game_mode == 'player':
            player_label_text = "PLAYER 1 STACK"
            opponent_label_text = "PLAYER 2 STACK"
        else:
            player_label_text = "YOUR STACK"
            opponent_label_text = "OPPONENT STACK"
        
        # Player side (left)
        player_stack_text = self.header_font.render(f"📚 {player_cards}", True, Colors.GOLD)
        player_stack_rect = player_stack_text.get_rect(right=bar_x - 20, centery=bar_y + bar_height // 2)
        self.screen.blit(player_stack_text, player_stack_rect)
        
        player_label = self.small_font.render(player_label_text, True, Colors.CREAM)
        player_label_rect = player_label.get_rect(right=bar_x - 20, top=count_y)
        self.screen.blit(player_label, player_label_rect)
        
        # Computer/Player 2 side (right)
        computer_stack_text = self.header_font.render(f"{computer_cards} 📚", True, Colors.GOLD)
        computer_stack_rect = computer_stack_text.get_rect(left=bar_x + bar_width + 20, centery=bar_y + bar_height // 2)
        self.screen.blit(computer_stack_text, computer_stack_rect)
        
        computer_label = self.small_font.render(opponent_label_text, True, Colors.CREAM)
        computer_label_rect = computer_label.get_rect(left=bar_x + bar_width + 20, top=count_y)
        self.screen.blit(computer_label, computer_label_rect)
        
        # Draw rounds won more compactly below
        rounds_y = count_y + 20
        player_rounds = self.small_font.render(
            f"Rounds: {game_state['player_score']}", True, Colors.CREAM
        )
        computer_rounds = self.small_font.render(
            f"Rounds: {game_state['computer_score']}", True, Colors.CREAM
        )
        
        player_rounds_rect = player_rounds.get_rect(right=bar_x - 20, top=rounds_y)
        computer_rounds_rect = computer_rounds.get_rect(left=bar_x + bar_width + 20, top=rounds_y)
        
        self.screen.blit(player_rounds, player_rounds_rect)
        self.screen.blit(computer_rounds, computer_rounds_rect)
        
        # Draw turn indicator (more compact)
        if not game_state['game_over']:
            # Check if in battle mode
            if game_state.get('is_battle', False):
                battle_count = game_state.get('battle_pile', 0)
                if game_state['active_player'] == 'player':
                    if game_mode == 'player':
                        turn_text = f"⚔️ BATTLE! Player 1 choose stat ({battle_count} cards at stake)"
                    else:
                        turn_text = f"⚔️ BATTLE! Choose a stat ({battle_count} cards at stake)"
                else:
                    if game_mode == 'player':
                        turn_text = f"⚔️ BATTLE! Player 2 choosing ({battle_count} cards at stake)"
                    else:
                        turn_text = f"⚔️ BATTLE! Computer choosing ({battle_count} cards at stake)"
                turn_color = Colors.RED
            else:
                # Normal turn
                if game_state['active_player'] == 'player':
                    if game_mode == 'player':
                        turn_text = "PLAYER 1'S TURN - Choose a stat"
                    else:
                        turn_text = "YOUR TURN - Choose a stat"
                    turn_color = Colors.GOLD
                else:
                    if game_mode == 'player':
                        turn_text = "PLAYER 2'S TURN - Choose a stat"
                    else:
                        turn_text = "COMPUTER'S TURN"
                    turn_color = Colors.LIGHT_GRAY
            
            turn_surface = self.stat_font.render(turn_text, True, turn_color)
            turn_rect = turn_surface.get_rect(center=(self.screen_width // 2, 72))
            self.screen.blit(turn_surface, turn_rect)
        
        # Draw result message if present (compact)
        if result:
            if result['winner'] == 'player':
                if game_mode == 'player':
                    msg = f"Player 1 wins! {result['stat_name']}: {result['player_value']} vs {result['computer_value']}"
                    cards_msg = "→ Cards go to Player 1's bottom"
                else:
                    msg = f"You win! {result['stat_name']}: {result['player_value']} vs {result['computer_value']}"
                    cards_msg = "→ Cards go to your bottom deck"
                msg_color = Colors.GREEN
            elif result['winner'] == 'computer':
                if game_mode == 'player':
                    msg = f"Player 2 wins! {result['stat_name']}: {result['computer_value']} vs {result['player_value']}"
                    cards_msg = "→ Cards go to Player 2's bottom"
                else:
                    msg = f"Computer wins! {result['stat_name']}: {result['computer_value']} vs {result['player_value']}"
                    cards_msg = "→ Cards go to opponent's bottom deck"
                msg_color = Colors.RED
            else:
                msg = f"Tie! {result['stat_name']}: {result['player_value']} vs {result['computer_value']}"
                battle_count = game_state.get('battle_pile', 0)
                cards_msg = f"→ Cards to battle pile! ({battle_count} cards at stake)"
                msg_color = Colors.BLUE
            
            # Main result message
            result_surface = self.text_font.render(msg, True, msg_color)
            result_rect = result_surface.get_rect(center=(self.screen_width // 2, 62))
            
            # Background for better visibility
            bg_rect = result_rect.inflate(16, 8)
            pygame.draw.rect(self.screen, Colors.BLACK, bg_rect, border_radius=5)
            self.screen.blit(result_surface, result_rect)
            
            # Card movement indicator (below result)
            cards_surface = self.small_font.render(cards_msg, True, Colors.CREAM)
            cards_rect = cards_surface.get_rect(center=(self.screen_width // 2, 82))
            self.screen.blit(cards_surface, cards_rect)
        
        # Draw cards
        # Determine card visibility based on turn and result
        active_player = game_state['active_player']
        
        # PLAYER 1 CARD (LEFT)
        if game_state['player_card']:
            # Show Player 1's card if:
            # - It's Player 1's turn (before result), OR
            # - Result is shown (after comparison)
            if result is not None:
                # After result - show card with colors
                show_player1_stats = True
                player_won = result.get('winner') == 'player'
                player_lost = result.get('winner') == 'computer'
            elif active_player == 'player':
                # Player 1's turn - show their card
                show_player1_stats = True
                player_won = False
                player_lost = False
            else:
                # Player 2's turn - hide Player 1's card
                show_player1_stats = False
                player_won = False
                player_lost = False
            
            # Player 1's card is clickable when it's their turn (before result)
            is_clickable_card = (active_player == 'player' and result is None)
            
            self.draw_card(
                game_state['player_card'],
                self.player_card_x,
                self.card_y,
                show_stats=show_player1_stats,
                is_player_card=is_clickable_card,  # Only clickable on Player 1's turn
                highlight_stat=None,
                winning_stat=selected_stat if result else None,
                player_won=player_won,
                player_lost=player_lost
            )
        
        # PLAYER 2 CARD (RIGHT)
        if game_state['computer_card']:
            # Show Player 2's card if:
            # - It's Player 2's turn (before result), OR
            # - Result is shown (after comparison)
            if result is not None:
                # After result - show card with colors
                show_player2_stats = True
                computer_won = result.get('winner') == 'computer'
                computer_lost = result.get('winner') == 'player'
            elif active_player == 'computer':
                # Player 2's turn - show their card
                show_player2_stats = True
                computer_won = False
                computer_lost = False
            else:
                # Player 1's turn - hide Player 2's card
                show_player2_stats = False
                computer_won = False
                computer_lost = False
            
            # In Pass & Play mode, Player 2's card should be clickable when it's their turn
            is_clickable_card = (game_mode == 'player' and active_player == 'computer' and result is None)
            
            self.draw_card(
                game_state['computer_card'],
                self.computer_card_x,
                self.card_y,
                show_stats=show_player2_stats,
                is_player_card=is_clickable_card,  # Make clickable for Player 2's turn in Pass & Play
                highlight_stat=None,
                winning_stat=selected_stat if result else None,
                player_won=computer_won,
                player_lost=computer_lost
            )
        
        # Don't call pygame.display.flip() here - let main loop handle it
    
    def check_stat_click(self, pos):
        """
        Check if a stat button was clicked.
        
        Args:
            pos (tuple): Mouse position (x, y)
            
        Returns:
            str: Stat key if clicked, None otherwise
        """
        for rect, stat_key in self.stat_buttons:
            if rect.collidepoint(pos):
                return stat_key
        return None
    
    
    def draw_next_round_button(self):
        """
        Draw a 'Next Round' button for advancing after viewing round result.
        
        Returns:
            pygame.Rect: Button rectangle for click detection
        """
        # Button at bottom center
        button_width = 250
        button_height = 60
        button_x = (self.screen_width - button_width) // 2
        button_y = self.screen_height - 100
        
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        mouse_pos = pygame.mouse.get_pos()
        
        # Hover effect
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Colors.GOLD, button_rect, border_radius=10)
            text_color = Colors.BLACK
        else:
            pygame.draw.rect(self.screen, Colors.DARK_GOLD, button_rect, border_radius=10)
            text_color = Colors.CREAM
        
        pygame.draw.rect(self.screen, Colors.BLACK, button_rect, 3, border_radius=10)
        
        # Button text
        button_text = self.header_font.render("NEXT ROUND →", True, text_color)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.screen.blit(button_text, button_text_rect)
        
        # Instruction text above button
        instruction = self.small_font.render("Click to continue", True, Colors.LIGHT_GRAY)
        instruction_rect = instruction.get_rect(center=(self.screen_width // 2, button_y - 25))
        self.screen.blit(instruction, instruction_rect)
        
        # Don't call pygame.display.flip() here - let main loop handle it
        return button_rect
    
    def draw_game_over(self, winner, game_mode='computer'):
        """
        Draw game over screen.
        
        Args:
            winner (str): 'player' or 'computer'
        """
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(200)
        overlay.fill(Colors.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Result message
        if winner == 'player':
            if game_mode == 'player':
                title_text = "PLAYER 1 WINS!"
                subtitle_text = "Player 1 has collected all the cards!"
            else:
                title_text = "VICTORY!"
                subtitle_text = "You have collected all the cards!"
            color = Colors.GOLD
        else:
            if game_mode == 'player':
                title_text = "PLAYER 2 WINS!"
                subtitle_text = "Player 2 has collected all the cards!"
            else:
                title_text = "DEFEAT"
                subtitle_text = "The computer has collected all the cards"
            color = Colors.RED
        
        title = self.title_font.render(title_text, True, color)
        title_rect = title.get_rect(center=(self.screen_width // 2, 250))
        self.screen.blit(title, title_rect)
        
        subtitle = self.text_font.render(subtitle_text, True, Colors.CREAM)
        subtitle_rect = subtitle.get_rect(center=(self.screen_width // 2, 320))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Play Again button
        button_width = 250
        button_height = 60
        button_x = (self.screen_width - button_width) // 2
        button_y = 450
        
        play_again_button = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(self.screen, Colors.GOLD, play_again_button, border_radius=10)
        pygame.draw.rect(self.screen, Colors.BLACK, play_again_button, 3, border_radius=10)
        
        button_text = self.header_font.render("PLAY AGAIN", True, Colors.BLACK)
        button_text_rect = button_text.get_rect(center=play_again_button.center)
        self.screen.blit(button_text, button_text_rect)
        
        pygame.display.flip()
        
        return play_again_button
    
