import sys
import pygame
from settings import Settings
from paddle import Paddle
from brickmaker import BrickMaker
from ball import Ball
from healthmaker import HealthMaker
from games_stats import GameStats
from button import Button
from time import sleep
from game_end import GameEnd


class BrickBreaker:
    def __init__(self):
        """Game Initializer"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Brick Breaker")

        self.stats = GameStats(self)

        self.paddle = Paddle(self)              # Paddle Instance
        self.paddlesprite = pygame.sprite.Group()
        self.paddlesprite.add(self.paddle)

        self.brick = BrickMaker(self)           # BrickMaker Instance

        self.health = HealthMaker(self)

        self.ball = Ball(self)
        self.ballsprite = pygame.sprite.Group()
        self.ballsprite.add(self.ball)

        self.play_button = Button(self, "Play")
        self.game_end = GameEnd(self)


    def run_game(self):
        while True:
            self._check_events()
            self.paddle.updateposition()        # Method for controlling continuous motion of ship
            self.ball.updateposition()
            self._check_collisions()
            self._healthbar_management()
            self._game_end_conditions()
            self._update_screen()


    def _check_events(self):
        """Response for keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            if self.stats.game_active:
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when player presses PLAY"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
    def _check_keydown_events(self,event):
        """Checks for keydown events"""
        if event.key == pygame.K_RIGHT:
            self.paddle.moving_right = True
            self.ball.paddle_right = True
        elif event.key == pygame.K_LEFT:
            self.paddle.moving_left = True
            self.ball.paddle_left = True
        elif event.key == pygame.K_SPACE:
            self.ball.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Checks for keyup events"""
        if event.key == pygame.K_RIGHT:
            self.paddle.moving_right = False
            self.ball.paddle_right = False
        elif event.key == pygame.K_LEFT:
            self.paddle.moving_left = False
            self.ball.paddle_left = False

    def _check_collisions(self):

        collision_ball_pbrick = pygame.sprite.groupcollide(self.brick.purplebricks, self.ballsprite, True, False)
        if collision_ball_pbrick:
            self.ball.change_course = True
            self.ball.changecoursepurple()

        collision_ball_rbrick = pygame.sprite.groupcollide(self.brick.redbricks, self.ballsprite, True, False)
        if collision_ball_rbrick:
            self.ball.change_course = True
            self.ball.changecoursered()

        collision_ball_paddle = pygame.sprite.groupcollide(self.paddlesprite, self.ballsprite, False, False)
        if collision_ball_paddle:
            self.ball.changecoursepaddle()

    def _healthbar_management(self):

        if self.stats.lives_left < self.stats.t_lives:
            self.health.create_left_healthbar()
            self.stats.t_lives = self.stats.lives_left
            sleep(0.3)
    def _game_end_conditions(self):
        if self.brick.purplebricks and self.brick.redbricks == False:
            self.stats.game_won = True
        elif self.stats.lives_left == 0:
            self.stats.game_lost = True


    def _update_screen(self):
        """Update image on screen, and flip to a new screen"""
        """Redraw the screen each time"""
        self.screen.fill(self.settings.bgroundclr)
        self.paddlesprite.draw(self.screen)
        self.brick.purplebricks.draw(self.screen)
        self.brick.redbricks.draw(self.screen)
        self.health.healthbars.draw(self.screen)
        self.ballsprite.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()
        if self.stats.game_won:
            self.game_end.draw_win()

        elif self.stats.game_lost:
            self.game_end.draw_lost()

        """Make the most recently drawn screen visible"""
        pygame.display.flip()
        """If either game ending conditions are true, wait for 10 seconds 
        and exit the console"""
        if self.stats.game_won or self.stats.game_lost:
            sleep(10)
            sys.exit()


Sc = BrickBreaker()
Sc.run_game()