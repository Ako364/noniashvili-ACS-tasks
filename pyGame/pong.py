import pygame

# -- Global Constants
ballWidth = 20
a=True
score = 0

# -- ball initial position
x_val = 5
y_val = 5

# -- ball speed
x_direction = 5
y_direction = 5

# -- paddle size
paddL = 15
paddW = 80

# -- paddle position
xPadd = 0 
yPadd = 20

xPadd2 = 985
yPadd2 = 0

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (150,50,255)
YELLOW = (255,255,0)
GREEN = (0, 20, 15)

# -- Initialise PyGame
pygame.init()

# --- set font for the scoreboard
font = pygame.font.Font('freesansbold.ttf', 32)

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
    if x_val <= 0 or x_val >= 1000-ballWidth:
        x_direction *= -1
        score -= 1
    else: 
        x_direction = x_direction

    if y_val <= 0 or y_val >= 700-ballWidth:
        y_direction *= -1
    else: 
        y_direction = y_direction

    if x_val == 15:
        if y_val >= yPadd and y_val <= yPadd + 70:
            x_direction *= -1
            score += 1 

    if x_val == xPadd2 - 20:
        x_direction *= -1
    
    x_val = x_val + x_direction
    y_val = y_val + y_direction   

    yPadd2 = yPadd2 + y_direction


    # -- Screen background is BLACK
    screen.fill (GREEN)
    
    # -- Draw here

    pygame.draw.rect(screen, WHITE, (xPadd2,yPadd2,paddL,paddW))
    pygame.draw.rect(screen, WHITE, (x_val,y_val,ballWidth,ballWidth))
    pygame.draw.rect(screen, WHITE, (xPadd, yPadd, paddL, paddW))

    # -- Scores
    score1 = font.render("SCORE : " + str(score), True, (255, 255, 255))
    screen.blit(score1, (400, 50))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()

