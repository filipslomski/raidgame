import pygame
from init import Init
from colors import Colors
from car import Car

init = Init(1600, 900, "Game")
init.initialise()

clock = pygame.time.Clock()
crashed = False

x = (init.display_width * 0.45)
y = (init.display_height * 0.69)

car = Car('car.png', 75, 250, x, y, init)
carImg = pygame.image.load_extended('car.png')

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.pos_x -= 5
            elif event.key == pygame.K_RIGHT:
                car.pos_x += 5
            elif event.key == pygame.K_UP:
                car.pos_y -= 5
            elif event.key == pygame.K_DOWN:
                car.pos_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass

        print(event)


    pygame.display.update()
    init.clock.tick(60)

    init.gameDisplay.fill(Colors.WHITE)
    car.display()

pygame.quit()
quit()