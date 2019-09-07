class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 820
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 6.5

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 8
        self.bullet_height = 8
        self.bullet_color = 255, 10, 10
        self.bullets_allowed = 200

        # Alien settings
        self.alien_speed_factor = 8
        self.fleet_drop_speed = 13
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = -1

        ## game stats
        self.ship_limit = 3
      
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 6.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 8

        # Scoring
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = -1


        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)








