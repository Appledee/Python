import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
   	 (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in. 
    bullets = Group()
    aliens = Group()

    # Create an instance to store game statistics. 
    stats = GameStats(ai_settings)

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, sb)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
        #else: sys.exit()
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb)
        
run_game()