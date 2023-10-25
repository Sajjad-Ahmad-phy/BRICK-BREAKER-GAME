import pygame
from pygame.sprite import Sprite


class RedBricks(Sprite):
    """A class which represents tiles in the game"""

    def __init__(self, bb_game):
        super().__init__()
        self.screen = bb_game.screen

        # Load the image and get its rect attribute
        self.image = pygame.image.load('Images/redbrick.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (75,25))
        self.rect = self.image.get_rect()

        # Put the tile at these coordinates
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the tile's exact position
        self.x = float(self.rect.x)



