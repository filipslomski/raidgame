import pygame

from gamePhase import GamePhase
from dungeon_state import DungeonState
from init import Init
from objects.dynamic.object import Object
from objects.static.dungeon import Dungeon
from utilities.consts.other import Other


class Player(Object):
    health = 100
    image_path = "images/units/player.jpg"
    image = None

    def __init__(self):
        self.image = pygame.image.load_extended(self.image_path)
        self.height = 100
        self.width = 71

    def spawn(self, position):
        self.position = position

    def display(self):
        Init.gameDisplay.blit(self.image, (self.position.x, self.position.y))

    def move(self, position):
        if GamePhase.phase < 3:
            self.position.x += position.x
            self.position.y += position.y

    def collision(self, object):
        if type(object) is Dungeon:
            GamePhase.phase = Other.TRANSITION_PHASE_ONE
            DungeonState.current_dungeon = object.dungeon_type

    def shoot(self):
        return False

    def death(self):
        GamePhase.phase = Other.TRANSITION_PHASE_TWO

    def get_health(self):
        return self.health