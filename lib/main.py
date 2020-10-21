import pygame
from lib.gameClass import game_of_life

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211,211,211)
#Dimensions
PIXEL_SIZE = 10 
MARGIN = 1 


def mainloop(game):
    WINDOW_SIZE = [game.width*(PIXEL_SIZE+MARGIN), game.height*(PIXEL_SIZE+MARGIN)]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Conway's Game of Life")

    pause = True
    speed = 15
    current = (0,0)

    while True:
        #Handle user input
        for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    pygame.quit()
                if pause and pygame.mouse.get_pressed()[0]:
                    try:
                        pos = event.pos 
                    except AttributeError:
                        continue 
                    p = (pos[0]//(PIXEL_SIZE+1),pos[1]//(PIXEL_SIZE+1))
                    if event.type == pygame.MOUSEMOTION:
                        if p != current:
                            game.flip(p)
                        current = p
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        game.flip(p)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = not pause
                    elif event.key== pygame.K_UP:
                        if speed < 60:
                            speed +=1
                    elif event.key == pygame.K_DOWN:
                        if speed > 1:
                            speed -=1

        #Update the game state
        if not pause:
            game.update()
            
        #Display the game
        screen.fill(GREY)
        for row in range(game.width):
            for column in range(game.height):
                color = WHITE
                if game.is_alive((row, column)):
                    color = BLACK  
                pygame.draw.rect(screen,color, 
                                [(MARGIN + PIXEL_SIZE) * row + MARGIN, (MARGIN + PIXEL_SIZE) * column + MARGIN,
                                PIXEL_SIZE, PIXEL_SIZE])
        
        #print(game.alive)
        clock = pygame.time.Clock()
        clock.tick(speed)
        pygame.display.flip()

