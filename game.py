import pygame

from collisionDetector import CollisionDetector
from consts.objects import Objects
from consts.dungeons import Dungeons
from init import Init
from objects.dynamic.objectFactory import ObjectFactory
from objects.static.dungeonFactory import DungeonFactory
from utilities.position import Position
from utilities.colors import Colors
from utilities.consts import Consts

Init.initialise()

# init objects
player = ObjectFactory.create_object(Objects.PLAYER)
lava_dungeon = DungeonFactory.create_object(Dungeons.DUNGEON_EXTERIOR, Dungeons.LAVA_DUNGEON)
frost_dungeon = DungeonFactory().create_object(Dungeons.DUNGEON_EXTERIOR, Dungeons.FROST_DUNGEON)
collision_detector = CollisionDetector()\
    .register_object(player)\
    .register_object(lava_dungeon)\
    .register_object(frost_dungeon)
player.spawn(Position(Init.display_width / 2, Init.display_height - 50))

# key bindings
key_bindings = {
    pygame.K_A: player.move(Position(-7, 0)),
    pygame.K_D: player.move(Position(7, 0)),
    pygame.K_S: player.move(Position(0, -7)),
    pygame.K_W: player.move(Position(0, 7))
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
    Init.clock.tick(Consts.FRAME_RATE)
    Init.gameDisplay.fill(Colors.WHITE)

    event_control()

    # display objects

    collision_detector.check_collisions()

    pygame.display.update()