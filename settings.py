class Settings:
    """A class to save all the settings of the game"""

    def __init__(self):
        self.screen_height = 500
        self.screen_width = 1200
        self.bgroundclr = (0,0,0)

        self.paddle_speed = 3           # Paddle Speed

        self.ybseparation = 1.2         # Separation between bricks along vertical

        self.pbpositions = [1,3,5,7]    # Purple Brick Positions
        self.rbpositions = [2,4,6]      # Red Brick Positions

        self.ball_speed = 1             # Ball Speed
        self.balltspeed = [self.ball_speed,self.ball_speed]

        self.lives = 3                  # Total Lives of a Player