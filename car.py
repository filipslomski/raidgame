import pygame
from position import Position


class Car(object):

    imgwidth = 75
    imgheight = 250
    image_path = "car.png"
    image = None
    init = None
    speed = 7
    position = None # type: Position
    out_of_screen = False

    def __init__(self, init):
        self.image = pygame.image.load_extended(self.image_path)
        self.init = init

    def spawn(self, position = None):
        if position is None:
            self.position = Position(self.init.display_width * 0.45, self.init.display_height * 0.69)
        else:
            self.position = position

    def display(self):
        if self.init.display_width - self.position.x < self.imgwidth or self.init.display_height - self.position.y < self.imgheight:
            self.out_of_screen = True
        else:
            self.init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move_left(self):
        self.position.x -= self.speed

    def move_right(self):
        self.position.x += self.speed

    def move_down(self):
        self.position.y += self.speed

    def move_up(self):
        self.position.y -= self.speed


