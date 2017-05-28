import pygame
from init import Init

init = Init(1600, 900, "Game")
init.initialise()

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load_basic('something.png')

def car(x,y):
    init.gameDisplay.blit(carImg, (x,y))

x =  (init.display_width * 0.45)
y = (init.display_height * 0.8)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    init.clock.tick(60)

pygame.quit()
quit()