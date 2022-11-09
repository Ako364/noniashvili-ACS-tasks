import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,0)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()

# screen config
SIZE = (500, 600)

screen = pygame.display.set_mode(SIZE) #size
pygame.display.set_caption("My Window") #title

# Exit game flag set to false
done = False
clock = pygame.time.Clock()

circX = 360
circY = 230

y = 255

step = 2
stepY = 2

# game loop
while not done:
    # user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # endif
    # next event

    screen.fill(BLACK)  # screen is black

    pygame.draw.rect(screen, BLUE, (100,100,300,300))
    pygame.draw.circle(screen, YELLOW, (circX,circY),20,0)

    circX += step
    if circX > 400:
        step = -step 
        
    circY += stepY
    if circY > 400: 
        stepY = -stepY
    
    if circY > 250:
        if y > 5:
            y -= 5
    elif circY < 250:
        if y < 250:
            y += 5
    
    # flip display to reveal new position of objects
    pygame.display.flip()

    # the clock ticks over
    clock.tick(60)
# endwhile and end of game loop

pygame.quit()