import pygame

from gamePhase import GamePhase
from init import Init
from objects.dynamic.object import Object
from objects.static.dungeon import Dungeon
from utilities.consts.other import Other


class Player(Object):
    health = 100
    image_path = "images/units/player.jpg"
    image = None

    def __init__(self):
        self.image = pygame.image.load_extended(self.image_path)
        self.height = 50
        self.width = 50

    def spawn(self, position):
        self.position = position

    def display(self):
        Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move(self, position):
        self.position.x += position.x
        self.position.y += position.y

    def collision(self, object):
        if type(object) is Dungeon:
            GamePhase.phase = Other.TRANSITION_PHASE

    def death(self):
        pass

    def get_health(self):
        pass