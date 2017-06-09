import pygame
from objects.dynamic.bullets.bullet import Bullet
from init import Init
from gamePhase import GamePhase


class BoltBullet(Bullet):

    image_path = "images/bullets/bolt_bullet.jpg"

    def __init__(self, speed, start_position, target_position, damage):
        super(BoltBullet, self).__init__(speed, start_position, target_position, damage)
        self.image = pygame.image.load_extended(self.image_path)

    def display(self):
        if GamePhase.phase == 2:
            Init.gameDisplay.blit(self.image, (self.current_position.x, self.current_position.y))

    def move(self):
        pass

    def destroy(self):
        pass