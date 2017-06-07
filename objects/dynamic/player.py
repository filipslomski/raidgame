import pygame
from objects.dynamic.object import Object
from utilities.position import Position
from init import Init


class Player(Object):
    health = 100
    image_path = "images/units/player.png"
    image = None

    def __init__(self):
        self.image = pygame.image.load_extended(self.image_path)

    def spawn(self, position):
        self.position = position

    def display(self):
        Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move(self, position):
        self.position.x += position.x
        self.position.y += position.y

    def collision(self, object):
        pass

    def death(self):
        pass

    def get_health(self):
        pass