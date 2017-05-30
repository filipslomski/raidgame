import pygame

class Car(object):

    image_path = None
    imgwidth = None
    imgheight = None
    image = None
    init = None
    pos_x = None
    pos_y = None

    def __init__(self, image_path, imgwidth, imgheight, pos_x, pos_y, init):
        self.imgwidth = imgwidth
        self.imgheight = imgheight
        self.image_path = image_path
        self.image = pygame.image.load_extended('car.png')
        self.init = init
        self.pos_x = pos_x
        self.pos_y = pos_y

    def display(self):
        self.init.gameDisplay.blit(self.image, (self.pos_x, self.pos_y))


