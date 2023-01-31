import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    time_surface = test_font.render(f'{current_time}', False, 'Black')
    time_rect = time_surface.get_rect(center= (400,50))
    screen.blit(time_surface, time_rect )
    # print(current_time)

# start the game
pygame.init()

# screen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game 1")
clock = pygame.time.Clock()     #frame rate

game_active = True
start_time = 0
 

# font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  #(font type, font size)


# surface
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# text_surface = test_font.render("Game 1", False, "Black")       #(text information, alias, color)
# text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0


while True:
    # loop for closing screen 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #         player_gravity = -20

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks()/1000)

    if game_active:

        screen.blit(sky_surface,(0,0))     #(surface, position)
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'Pink',text_rect)
        # screen.blit(text_surface,text_rect)
        display_score()

        snail_rect.x-=4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)
        # player_rect.left += 1


        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        
        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill("Red")

    pygame.display.update()
    clock.tick(60)      #frame rate
