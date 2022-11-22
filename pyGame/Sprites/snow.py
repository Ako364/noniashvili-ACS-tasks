import pygame
import random
import math

# -- Global Constants

# -- Colours
BLACK = (0,50,50)
WHITE = (255,255,255)
BLUE = (150,50,255)
YELLOW = (255,255,0)

## Define the class snow which is a sprite 
class Snow(pygame.sprite.Sprite):
    # Define the cnostructor for snow
    def __init__(self, color, width, height, speed):
        # Call the sprtite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the psoition of the sprite 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0,400)
        # Set speed of the sprite
        self.speed = speed
    # End Proceure
# End class

# Class update function - runs for each pass through the game loop
def update(self):
    self.rect.y = self.rect.y + self.speed


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (600,400)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Snow")

# -- Exit game flag set to false
done = False


# Create a list of snow blocks
snow_group = pygame.sprite.Group()

# Create the list of all the sprites
all_sprites_group = pygame.sprite.Group()


# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


# Create the snowflakes
number_of_flakes = 50 # we are creating 50 snowflakes
for x in range (number_of_flakes):
    my_snow = Snow(WHITE, 5, 5, 5) # snowflakes are white with size 5 by 5 px
    snow_group.add (my_snow) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add (my_snow) # adds it to the group of all Sprites 
    #Next x


### -- Game Loop
while not done:
    # User input and controls, code to move up and down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Code that somehow makes moving smooth
    
    #Next event


    # -- Game logic goes after this comment
    all_sprites_group.update()

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(20)
    
#End While - End of game loop
pygame.quit()

