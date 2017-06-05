import pygame

from collisionDetector import CollisionDetector
from consts.objects import Objects
from consts.dungeons import Dungeons
from init import Init
from objects.dynamic.objectFactory import ObjectFactory
from objects.static.dungeonFactory import DungeonFactory
from objects.static.dungeons.lavaDungeon import LavaDungeon
from utilities.colors import Colors
from utilities.consts import Consts

init = Init(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_CAPTION)
init.initialise()

# init objects
player = ObjectFactory(init).create_object(Objects.PLAYER)
lava_dungeon = DungeonFactory(init).create_object(Dungeons.LAVA_DUNGEON)
frost_dungeon = DungeonFactory(init).create_object(Dungeons.FROST_DUNGEON)
collision_detector = CollisionDetector()


# key bindings
key_bindings = {
    #pygame.K_LEFT: ,
    #pygame.K_RIGHT: ,
    #pygame.K_UP: ,
    #pygame.K_DOWN:
}

# event control
def event_control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in key_bindings:
                key_bindings[event.key]()

# main game loop
while True:
    init.clock.tick(Consts.FRAME_RATE)
    init.gameDisplay.fill(Colors.WHITE)

    event_control()

    # display objects

    collision_detector.check_collisions()

    pygame.display.update()