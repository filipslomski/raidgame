import pygame
import random
from position import Position
from colors import Colors


class Object():

    init = None
    position = None
    width = 50
    height = 50
    color = Colors.RED
    speed = 7

    def __init__(self, init):
        self.init = init

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
