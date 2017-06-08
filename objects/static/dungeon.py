import pygame
from init import Init
from gamePhase import GamePhase


class Dungeon(object):

    position = None
    image = None
    dungeon_type = None
    width = None
    height = None

    def __init__(self, dungeon_type):
        self.image = pygame.image.load_extended(dungeon_type.image_path)
        self.dungeon_type = dungeon_type
        self.width = dungeon_type.width
        self.height = dungeon_type.height

    def spawn(self):
        self.position = self.dungeon_type.image_position

    def display(self):
        if GamePhase.phase == 1:
            Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def collision(self, object):
        pass

    def remove(self):
        self.width = 0
        self.height = 0
        self.dungeon_type = None
        self.position = None
        self.image = None