import pygame


class Init:

    gameDisplay = None
    clock = None
    display_width = 0
    display_height = 0
    caption = ""

    def __init__(self, width, height, caption):
        self.display_width = width
        self.display_height = height
        self.caption = caption

    def initialise(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()
