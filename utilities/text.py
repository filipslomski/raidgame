import pygame
from utilities.position import Position
from utilities.colors import Colors


class Text:

    init = None

    def __init__(self, init):
        self.init = init

    def text_objects(self, text, font):
        textSurface = font.render(text, True, Colors.BLACK)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, position):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (position.x, position.y)
        self.init.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()