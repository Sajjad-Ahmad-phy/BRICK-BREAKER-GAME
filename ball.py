import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to manage the ball"""
    
    def __init__(self, bb_game):

        super(Ball, self).__init__()
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        self.settings = bb_game.settings
        self.stats = bb_game.stats

        self.pbrick = bb_game.brick.purplebricks
        self.rbrick = bb_game.brick.redbricks

        self.image = pygame.image.load('Images/ball.bmp')
        self.image = pygame.transform.smoothscale(self.image, (25,25))
        self.rect = self.image.get_rect()

        self.paddle = bb_game.paddle
        # Places the Ball's Rectangle above the Paddle's Rectangle
        self.rect.midbottom = self.paddle.rect.midtop

        self.y = float(self.rect.y)

        # Movement Flags
        self.moving_up = False
        self.change_course = False
        self.moving_right = True   # Controls movement of bound ball
        self.paddle_right = False  # Controls movement of bound ball with paddle moving right
        self.paddle_left = False   # Controls movement of bound ball with paddle moving left


    def updateposition(self):
        """Function to control the motion of ball """

        self.rect = self.rect.move(self.settings.balltspeed)

        if self.change_course:
            self.preventoutofbounds()

            """For launching the ball when pressing Space Key"""
        elif self.moving_up and self.rect.bottom > 0:
            self.settings.balltspeed[1] = -1

            """Controls movement of bound ball"""
        elif self.rect.bottom == self.paddle.rect.top and self.moving_up == False:

            if self.paddle_right:
                self.rect.midbottom = self.paddle.rect.midtop

            if self.paddle_left:
                self.rect.midbottom = self.paddle.rect.midtop

            if self.moving_right:
                self.settings.balltspeed[0] = 1
                self.settings.balltspeed[1] = 0

            if self.rect.right == self.paddle.rect.right:
                self.settings.balltspeed[0] = - self.settings.balltspeed[0]
                self.moving_right = False

            if self.rect.left == self.paddle.rect.left:
                self.settings.balltspeed[0] = - self.settings.balltspeed[0]


    def preventoutofbounds(self):

        # Prevents the ball from going out of bounds
        if self.rect.left < 0 or self.rect.right > self.settings.screen_width:
            self.settings.balltspeed[0] = -self.settings.balltspeed[0]
        if self.rect.top < 0:
            self.settings.balltspeed[1] = -self.settings.balltspeed[1]
        if self.rect.bottom > self.settings.screen_height:
            self.stats.lives_left = self.stats.lives_left - 1
            self.rect.midbottom = self.paddle.rect.midtop
            #print("in ball", self.stats.lives_left)



    def changecoursepurple(self):
        # Reflects the ball after colliding with purple bricks

        for purplebrick in self.pbrick:
            if self.rect.top < purplebrick.rect.bottom or self.rect.bottom > purplebrick.rect.top:
                self.settings.balltspeed[1] = -self.settings.balltspeed[1]
                break
            if self.rect.left < purplebrick.rect.right or self.rect.right > purplebrick.rect.left:
                self.settings.balltspeed[0] = -self.settings.balltspeed[0]
                break

    def changecoursered(self):

        # Reflects the ball after colliding with red bricks

        for redbrick in self.rbrick:
            if self.rect.top < redbrick.rect.bottom or self.rect.bottom > redbrick.rect.top:
                self.settings.balltspeed[1] = -self.settings.balltspeed[1]
                break

            if self.rect.left < redbrick.rect.right or self.rect.right > redbrick.rect.left:
                self.settings.balltspeed[0] = -self.settings.balltspeed[0]
                break

    def changecoursepaddle(self):

        # If the paddle is moving left or right, reflect ball at an angle
        if self.paddle_left:
            self.settings.balltspeed[0] = self.settings.ball_speed
            self.settings.balltspeed[0] = - self.settings.balltspeed[0]
            self.settings.balltspeed[1] = -self.settings.balltspeed[1]
        elif self.paddle_right:
            self.settings.balltspeed[0] = -self.settings.ball_speed
            self.settings.balltspeed[0] = - self.settings.balltspeed[0]
            self.settings.balltspeed[1] = -self.settings.balltspeed[1]
        # If the paddle is stationary, reflect the ball along vertical
        elif self.paddle_right == False or self.paddle_left == False:
            self.settings.balltspeed[0] = 0
            self.settings.balltspeed[1] = - self.settings.balltspeed[1]
        # Prevents Ball from Going inside the Paddle
        elif self.rect.x > self.paddle.rect.x and self.rect.y > self.paddle.rect.y:
            self.rect.midbottom = self.paddle.rect.midtop
            self.settings.balltspeed[0] = - self.settings.balltspeed[0]
            self.settings.balltspeed[1] = -self.settings.balltspeed[1]


    def blitme(self):
        self.screen.blit(self.image,self.rect)




