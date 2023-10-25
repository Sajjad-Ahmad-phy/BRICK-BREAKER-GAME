class GameStats:
    """A Class which contains game ending settings"""
    def __init__(self, bb_game):
        self.settings = bb_game.settings

        self.lives_left = self.settings.lives
        self.t_lives = 3

        self.game_active = False

        self.game_won = False
        self.game_lost = False