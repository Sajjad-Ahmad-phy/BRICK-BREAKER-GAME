import pygame
from pygame.sprite import Sprite
from settings import Settings
from healthbar import HealthBar

class HealthMaker(Sprite):
    """A Class to aim in creating Health Bars of the Player"""
    def __init__(self, bb_game):
        super().__init__()
        self.screen = bb_game.screen
        self.settings = Settings()

        self.stats = bb_game.stats

        # Health Bar Grouping
        self.healthbars = pygame.sprite.Group()
        self._create_rows_healthbars(bb_game)


    def _create_rows_healthbars(self, bb_game):
        """Creates a row of healthbars"""

        for i in range(3):
            health = HealthBar(bb_game)
            health.rect.x = health.rect.x - (health.rect.width * (i + 1))
            self.healthbars.add(health)


    def create_left_healthbar(self):
        for sprites in self.healthbars:
            sprites.kill()
            break
