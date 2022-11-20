import pygame

# -- Global Constants
ballWidth = 20

a = True

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
    # User input and controls, code to move up and down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # p1PadY = p1PadY - 20
                a = a
            elif event.key == pygame.K_DOWN:
                a = a
    # Code that somehow makes moving smooth
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if yPadd < 0:
            yPadd = 0
        else:
            yPadd = yPadd - 7
    if keys[pygame.K_DOWN]:
        if yPadd >= 700 - paddW:
            yPadd = 700 - paddW
        else:
            yPadd = yPadd + 7
            #End if        
        #End if 
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

