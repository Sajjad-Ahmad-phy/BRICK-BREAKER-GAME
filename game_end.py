import pygame


class GameEnd:
    """A Class responsible for showing Game Won or Ending Messages"""
    def __init__(self, bb_game):

        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        self.settings = bb_game.settings

        self.image_won = pygame.image.load('Images/won.bmp')
        self.image_won = pygame.transform.smoothscale(self.image_won, (1120, 630))
        self.image_won_rect = self.image_won.get_rect()

        self.image_lost = pygame.image.load('Images/lost.bmp')
        self.image_lost = pygame.transform.smoothscale(self.image_lost, (1120, 630))
        self.image_lost_rect = self.image_lost.get_rect()

        # Position the messages
        self.image_won_rect.center = self.screen_rect.center
        self.image_lost_rect.center = self.screen_rect.center

    def draw_win(self):
        self.screen.blit(self.image_won, self.image_won_rect)

    def draw_lost(self):
        self.screen.blit(self.image_lost, self.image_lost_rect)

