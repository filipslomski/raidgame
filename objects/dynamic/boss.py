import pygame
from objects.dynamic.object import Object
from init import Init
from gamePhase import GamePhase
from utilities.consts.other import Other


class Boss(Object):
    image_path = None
    boss_type = None
    image = None
    health = None

    def set_boss_type(self, boss_type):
        self.boss_type = boss_type
        self.health = boss_type.health
        self.image = pygame.image.load_extended(boss_type.image_path)
        self.width = boss_type.width
        self.height = boss_type.height
        self.speed = boss_type.speed

    def spawn(self, position):
        self.position = position

    def display(self):
        if GamePhase.phase == 2:
            Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move(self):
        if GamePhase.phase == 2:
            self.boss_type.move(self.position)

    def shoot(self):
        return self.boss_type.shoot()

    def collision(self, object):
        pass

    def death(self):
        GamePhase.phase = Other.TRANSITION_PHASE_TWO

    def get_health(self):
        return self.health