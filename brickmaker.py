import pygame
from pygame.sprite import Sprite
from settings import Settings
from purplebricks import PurpleBricks
from redbricks import RedBricks


class BrickMaker(Sprite):
    """A Class which manages the making of all the bricks in the game"""

    def __init__(self, bb_game):
        super().__init__()
        self.screen = bb_game.screen
        self.settings = Settings()

        self.stats = bb_game.stats

        # Purple Bricks Grouping
        self.purplebricks = pygame.sprite.Group()
        self._create_rows_purples(bb_game)

        # Red Bricks Grouping
        self.redbricks = pygame.sprite.Group()
        self._create_rows_reds(bb_game)


    def _create_rows_purples(self,bb_game):
        """Create a row of purple bricks"""
        purplebrick = PurpleBricks(bb_game)
        purplebrick_width = purplebrick.rect.width

        # Available space equals total space minus two times half the brick width for margins.
        available_space_x = self.settings.screen_width - 2 * (0.5 * purplebrick_width)
        number_bricks_x = available_space_x // purplebrick_width

        for multiplier in self.settings.pbpositions:

            for brick_number in range(int(number_bricks_x)):
                purplebrick = PurpleBricks(self)

                # Starting point of a brick = (Origin distance) + (Separation * bricks distances)
                purplebrick.x = (0.4 * purplebrick_width) + (1.02 * purplebrick_width * brick_number)

                purplebrick.rect.x = purplebrick.x
                purplebrick.rect.y = (self.settings.ybseparation *
                                      multiplier * purplebrick.rect.height)

                self.purplebricks.add(purplebrick)

    def _create_rows_reds(self, bb_game):
        """Create a row of red bricks"""
        redbrick = RedBricks(bb_game)
        redbrick_width = redbrick.rect.width

        # Available space equals total space minus two times half the brick width for margins.
        available_space_x = self.settings.screen_width - 2 * (0.5 * redbrick_width)
        number_bricks_x = available_space_x // redbrick_width

        for multiplier in self.settings.rbpositions:
            for brick_number in range(int(number_bricks_x)):
                redbrick = RedBricks(self)

                # Starting point of a brick = (Origin distance) + (Separation * bricks distances)
                redbrick.x = (0.4 * redbrick_width) + (1.02 * redbrick_width * brick_number)
                redbrick.rect.x = redbrick.x

                # y coordinate of red bricks,from the top of screen is, two times their width. +5 is the separation
                # between top and bottom layers.
                redbrick.rect.y = (self.settings.ybseparation *
                                   multiplier * redbrick.rect.height)

                self.redbricks.add(redbrick)
