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
car = ObjectFactory(init).create_object(Objects.CAR)
obstacle = ObjectFactory(init).create_object(Objects.OBSTACLE)
collision_detector = CollisionDetector().register_object(car).register_object(obstacle)
score = Score(init).register_object(obstacle)
car.spawn()
obstacle.spawn()

# key bindings
key_bindings = {
    pygame.K_LEFT: car.move_left,
    pygame.K_RIGHT: car.move_right,
    #pygame.K_UP: car.move_up,
    #pygame.K_DOWN: car.move_down
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
    # update score
    score.increase_points()

    # display objects
    car.display()
    obstacle.display()
    score.display()

    obstacle.move()

    collision_detector.check_collisions()

    pygame.display.update()