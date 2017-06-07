import pygame
from gamePhase import GamePhase
from init import Init
from utilities.position import Position


class DungeonInterior():
    background_image = None

    def __init__(self, dungeon_type):
        self.background_image = pygame.image.load_extended(dungeon_type.background_path)

    def display(self):
        pass
        #if GamePhase.get_phase() == 1:
            #Init.gameDisplay.blit(self.background_image, (cos, cos))