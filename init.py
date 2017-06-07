import pygame

from utilities.consts.game import Game


class Init:

    gameDisplay = None
    clock = None
    display_width = Game.SCREEN_WIDTH
    display_height = Game.SCREEN_HEIGHT
    caption = Game.SCREEN_CAPTION

    @classmethod
    def initialise(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()
