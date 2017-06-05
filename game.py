import pygame
from utilities.colors import Colors
from init import Init
from consts.objects import Objects
from utilities.consts import Consts
from collisionDetector import CollisionDetector
from score import Score
from objects.objectFactory import ObjectFactory

init = Init(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_CAPTION)
init.initialise()

# init objects
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