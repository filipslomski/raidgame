import pygame
from init import Init
from gamePhase import GamePhase


class Dungeon(object):

    position = None
    image = None
    dungeon_type = None

    def __init__(self, dungeon_type):
        self.image = pygame.image.load_extended(dungeon_type.image_path)
        self.dungeon_type = dungeon_type

    def spawn(self):
        self.position = self.dungeon_type.image_position

    def display(self):
        if GamePhase.get_phase() == 1:
            Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))