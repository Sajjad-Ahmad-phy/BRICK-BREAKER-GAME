import pygame.font

class Button:
    """A Class to describe the Play Button"""
    def __init__(self, bb_game, msg):
        self.screen = bb_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0,0,255)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # Building the Button's Rectangle
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Turn the message into a renedered image"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then the message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)