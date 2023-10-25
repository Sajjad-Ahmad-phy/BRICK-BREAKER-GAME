import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):

    def __init__(self, bb_game):

        super(Paddle, self).__init__()
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        self.settings = bb_game.settings

        self.image = pygame.image.load('Images/paddle.bmp')
        self.image = pygame.transform.smoothscale(self.image, (150,30))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value of paddle's horizontal position
        self.x = float(self.rect.x)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def updateposition(self):
        """Method which controls continuous motion of the paddle"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.paddle_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.paddle_speed

        # self.image_rect.x = self.x
        # Update rect object from self.x
        if self.x < (self.screen_rect.right - self.rect.width) and self.x > self.screen_rect.left:
            self.rect.x = self.x



    def blitme(self):
        self.screen.blit(self.image, self.rect)
