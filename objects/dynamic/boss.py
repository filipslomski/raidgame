import pygame
from objects.dynamic.object import Object
from init import Init
from gamePhase import GamePhase


class Boss(Object):
    health = 100
    image_path = "images/units/player.jpg"
    boss_type = None
    image = None

    def __init__(self):
        self.image = pygame.image.load_extended(self.image_path)
        self.width = 50
        self.height = 50

    def set_boss_type(self, boss_type):
        self.boss_type = boss_type

    def spawn(self, position):
        self.position = position

    def display(self):
        if GamePhase.phase == 2:
            Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move(self):
        pass

    def collision(self, object):
        pass

    def death(self):
        pass

    def get_health(self):
        pass