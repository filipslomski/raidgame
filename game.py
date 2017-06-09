import pygame
from utilities.consts.dungeons import Dungeons
from collisionDetector import CollisionDetector
from bulletTracker import BulletTracker
from gamePhase import GamePhase
from init import Init
from objects.dynamic.objectFactory import ObjectFactory
from objects.static.dungeonFactory import DungeonFactory
from utilities.colors import Colors
from utilities.consts.objects import Objects
from utilities.consts.game import Game
from utilities.consts.other import Other
from utilities.position import Position

Init.initialise()

# init objects
player = ObjectFactory.create_object(Objects.PLAYER)
boss = ObjectFactory.create_object(Objects.BOSS)
lava_dungeon = DungeonFactory.create_object(Dungeons.DUNGEON_EXTERIOR, Dungeons.LAVA_DUNGEON)
frost_dungeon = DungeonFactory().create_object(Dungeons.DUNGEON_EXTERIOR, Dungeons.FROST_DUNGEON)
collision_detector = CollisionDetector()\
    .register_object(player)\
    .register_object(lava_dungeon)\
    .register_object(frost_dungeon)
bullet_tracker = BulletTracker()
player.spawn(Position(Init.display_width / 2, Init.display_height - player.height))
lava_dungeon.spawn()
frost_dungeon.spawn()

# key bindings
key_bindings = {
    pygame.K_a: 'player.move(Position(-12, 0))',
    pygame.K_d: 'player.move(Position(12, 0))',
    pygame.K_s: 'player.move(Position(0, 12))',
    pygame.K_w: 'player.move(Position(0, -12))'
}


# event control
def event_control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in key_bindings:
                eval(key_bindings[event.key])

# main game loop
while True:
    Init.clock.tick(Game.FRAME_RATE)
    Init.gameDisplay.fill(Colors.WHITE)

    event_control()

    # display objects
    player.display()
    lava_dungeon.display()
    frost_dungeon.display()
    boss.display()

    collision_detector.check_collisions()

    if GamePhase.phase == Other.TRANSITION_PHASE_ONE:
        GamePhase.initiate_second_phase(player, boss, [lava_dungeon, frost_dungeon], collision_detector, bullet_tracker)
    if GamePhase.phase == Other.TRANSITION_PHASE_TWO:
        GamePhase.initiate_third_phase(player, boss, [lava_dungeon, frost_dungeon], collision_detector)
    if GamePhase.phase == 2:
        boss.move()
        bullet_tracker.manage_bullets()

    pygame.display.update()