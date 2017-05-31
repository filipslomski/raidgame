import pygame
from colors import Colors


class Text():

    init = None

    def __init__(self, init):
        self.init = init

    @staticmethod
    def text_objects(text, font):
        textSurface = font.render(text, True, Colors.BLACK)
        return textSurface, textSurface.get_rect()

    @classmethod
    def message_display(cls, text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = cls.text_objects(text, largeText)
        TextRect.center = ((cls.init.display_width / 2), (cls.init.display_height / 2))
        cls.init.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()