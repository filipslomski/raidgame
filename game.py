import pygame
from init import Init
from colors import Colors
from car import Car
from position import Position
from consts import Consts

init = Init(Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT, Consts.SCREEN_CAPTION)
init.initialise()

car = Car(init)
car.spawn()

key_bindings = {
    pygame.K_LEFT: car.move_left,
    pygame.K_RIGHT: car.move_right,
    pygame.K_UP: car.move_up,
    pygame.K_DOWN: car.move_down
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
    event_control()

    pygame.display.update()
    init.clock.tick(Consts.FRAME_RATE)

    init.gameDisplay.fill(Colors.WHITE)
    car.display()
    if car.out_of_screen:
        pass

