import pygame
# -- Global Constants

circX = 10
circY = 125

y = 255

step = 2
stepY = 0.5

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,0)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (0, 20, 15)

# -- Initialise PyGame
pygame.init()

# screen config
SIZE = (1000, 700)

screen = pygame.display.set_mode(SIZE) #size
pygame.display.set_caption("My Window") #title

# Exit game flag set to false
done = False
clock = pygame.time.Clock()

# game loop
while not done:
    # user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # endif
    # next event
    
    # Game logic
    if circX >= 0 and circX <= 1000:
        circX = circX + step
    else:
        circX = 0 + step

    if circY > 0 and circY <= 125:
        stepY = stepY
    else:
        stepY *= -1

    circY = circY - stepY
    
    
    screen.fill(BLACK)  # screen is black

    pygame.draw.rect(screen, GREEN, (400,250,200,200))
    pygame.draw.circle(screen, YELLOW, (circX,circY),20,0)

    
    # flip display to reveal new position of objects
    pygame.display.flip()

    # the clock ticks over
    clock.tick(60)
# endwhile and end of game loop

pygame.quit()