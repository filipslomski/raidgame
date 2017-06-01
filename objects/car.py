import pygame
from utilities.position import Position
from objects.object import Object
from utilities.text import Text


class Car(Object):

    image_path = "images/car.png"
    image = None
    speed = 7

    def __init__(self, init):
        super(Car, self).__init__(init)
        self.image = pygame.image.load_extended(self.image_path)
        self.width = 75
        self.height = 250

    def spawn(self, position = None):
        if position is None:
            self.position = Position(self.init.display_width * 0.45, self.init.display_height * 0.6)
        else:
            self.position = position

    def display(self):
        self.init.gameDisplay.blit(self.image, (self.position.x, self.position.y))
        self.check_if_out_of_screen()

    def move_left(self):
        self.position.x -= self.speed

    def move_right(self):
        self.position.x += self.speed

    def move_down(self):
        self.position.y += self.speed

    def move_up(self):
        self.position.y -= self.speed

    def check_if_out_of_screen(self):
        if self.init.display_width - self.position.x < self.width or self.init.display_height - self.position.y < self.height:
            Text.message_display('You crashed!')

    def collision(self):
        Text.message_display('You crashed!')




