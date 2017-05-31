import pygame
from init import Init
from colors import Colors
from car import Car
from position import Position
from consts import Consts
from text import Text
from object import Object

init = Init(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_CAPTION)
init.initialise()

# init objects
car = Car(init)
car.spawn()
obstacle = Object(init)
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