import pygame
from objects.dynamic.bullets.bullet import Bullet
from init import Init
from gamePhase import GamePhase
from utilities.consts.game import Game


class FireboltBullet(Bullet):

    image_path = "images/bullets/firebolt_bullet.jpg"

    def __init__(self, speed, start_position, target_position, damage):
        super(FireboltBullet, self).__init__(speed, start_position, target_position, damage)
        self.image = pygame.image.load_extended(self.image_path)

    def display(self):
        if GamePhase.phase == 2 and (
                self.position.x != self.target_position.x or self.position.y != self.target_position.y):
            Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move(self):
        dx, dy = (self.target_position.x - self.start_position.x, self.target_position.y - self.start_position.y)
        stepx, stepy = (float(dx) / Game.FRAME_RATE, float(dy) / Game.FRAME_RATE)
        self.position.x += stepx
        self.position.y += stepy

    def destroy(self):
        pass