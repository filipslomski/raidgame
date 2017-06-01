import random
import pygame
from utilities.position import Position
from objects.object import Object
from utilities.colors import Colors


class Obstacle(Object):

    color = Colors.RED
    speed = 7

    def __init__(self, init):
        super(Obstacle, self).__init__(init)
        self.width = 50
        self.height = 50

    def spawn(self, position = None):
        if position is None:
            self.position = Position(random.randrange(0, self.init.display_width), random.randrange(-500, -100))
        else:
            self.position = position

    def display(self):
        pygame.draw.rect(self.init.gameDisplay, self.color, [self.position.x, self.position.y, self.width, self.height])
        self.spawn_new_if_collapsed()

    def move(self):
        self.position.y += self.speed

    def spawn_new_if_collapsed(self):
        if self.position.y > self.init.display_height:
            self.spawn()

    def collision(self):
        self.speed = 0