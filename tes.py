import pygame
from sys import exit

# start the game
pygame.init()

# screen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game 1")
clock = pygame.time.Clock()     #frame rate

test_surface = pygame.Surface((100, 200))
test_surface.fill('white')

while True:
    # loop for closing screen 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all element
    # update everything

    screen.blit(test_surface,(0,0))     #(surface, position)

    pygame.display.update()
    clock.tick(60)      #frame rate
