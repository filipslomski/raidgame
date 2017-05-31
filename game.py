import pygame
from utilities.colors import Colors
from init import Init
from objects.car import Car
from objects.obstacle import Obstacle
from utilities.consts import Consts

init = Init(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_CAPTION)
init.initialise()

# init objects
car = Car(init)
car.spawn()
obstacle = Obstacle(init)
obstacle.spawn()

key_bindings = {
    pygame.K_LEFT: car.move_left,
    pygame.K_RIGHT: car.move_right,
    #pygame.K_UP: car.move_up,
    #pygame.K_DOWN: car.move_down
}


def event_control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in key_bindings:
                key_bindings[event.key]()

while True:
    init.clock.tick(Consts.FRAME_RATE)
    init.gameDisplay.fill(Colors.WHITE)

    event_control()

    car.display()
    obstacle.display()
    obstacle.move()

    pygame.display.update()