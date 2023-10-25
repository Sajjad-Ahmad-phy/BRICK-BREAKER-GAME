import pygame
from pygame.sprite import Sprite

class HealthBar(Sprite):
    """A Class to manage the Health Bar"""
    def __init__(self, bb_game):

        super(HealthBar, self).__init__()
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        self.settings = bb_game.settings

        self.image = pygame.image.load('Images/health.bmp')
        self.image = pygame.transform.smoothscale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen_rect.bottomright