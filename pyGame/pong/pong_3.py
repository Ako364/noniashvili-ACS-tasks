import pygame

# -- Global Constants
ballWidth = 20

x_val = 0
y_val = 0

x_direction = 5
y_direction = 5

paddL = 15
paddW = 60

xPadd = 0 
yPadd = 20

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)



# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1000,700)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


### -- Game Loop


while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    
    # -- Game logic goes after this comment
    

    if x_val >= 0 and x_val < 1000-ballWidth:
        x_direction = x_direction
    else: 
        x_direction *= -1

    if y_val >= 0 and y_val < 700-ballWidth:
        y_direction = y_direction
    else: 
        y_direction *= -1


    x_val = x_val + x_direction
    y_val = y_val + y_direction    
        
        
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here

    pygame.draw.rect(screen, BLUE, (x_val,y_val,ballWidth,ballWidth))
    pygame.draw.rect(screen, WHITE, (xPadd, yPadd, paddL, paddW))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()