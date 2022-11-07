import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
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

sunX = 120
sunY = 180

# game loop
while not done:
    # user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # endif
    # next event

    screen.fill(BLACK)  # screen is black

    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (40,100),40,0)

    if sunX < SIZE[0]:
        sunX += 5
    else:
        sunX = 0
    
    # flip display to reveal new position of objects
    pygame.display.flip()

    # the clock ticks over
    clock.tick(60)
# endwhile and end of game loop

pygame.quit()