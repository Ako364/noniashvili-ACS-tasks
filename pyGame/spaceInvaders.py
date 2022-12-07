import pygame
import random

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (150,50,255)
YELLOW = (255,255,0)
GREEN = (0, 20, 15)

## -- Define the class invader which is a sprite 
class Invader(pygame.sprite.Sprite):
    # Define the cnostructor for invader
    def __init__(self, color, width, height, speed):
        # Call the sprtite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the psoition of the sprite 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1200)
        self.rect.y = random.randrange(-50,0)
        # Set speed of the sprite
        self.speed = speed
    # End Proceure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= 1000:
            # Spawn a invaderflake randomly on x-axis and on 0 on y-axis
            self.rect.x = random.randrange(0, 1200)
            self.rect.y = 0 + self.speed   

# End class

## -- Define the class invader which is a sprite 
class Player(pygame.sprite.Sprite):
    # Define the cnostructor for invader
    def __init__(self, color, width, height):
        # Call the sprtite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the psoition of the sprite 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1200)
        self.rect.y = 300
        # Set speed of the sprite
        self.speed = 0
    # End Proceure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= 1000:
            # Spawn a invaderflake randomly on x-axis and on 0 on y-axis
            self.rect.x = random.randrange(0, 1200)
            self.rect.y = 0 + self.speed   

# End class

## -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1200, 1000)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Invader")

# -- Exit game flag set to false
done = False

# -- Create a list of invader blocks
invader_group = pygame.sprite.Group()

# -- Create the list of all the sprites
all_sprites_group = pygame.sprite.Group()

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

## -- Create the invaderflakes
number_of_flakes = 50 # we are creating invaders
for x in range (number_of_flakes):
    my_invader = Invader(WHITE, 5, 5, random.randrange(2,5)) 
    invader_group.add (my_invader) # adds the new invader to the group of invader
    all_sprites_group.add (my_invader) # adds it to the group of all Sprites 
    #Next x

## -- create a player
player = Player(YELLOW, 10, 10)
all_sprites_group.add(player)

### -- Game Loop
while not done:
    # User input and controls, code to move up and down   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.key == pygame.K_LEFT:
        player.player_set_speed(-3)  # speed set to -3
    elif event.key == pygame.K_RIGHT:
    # - if the right key pressed
        player.player_set_speed(3) # speed set to 3
    elif event.type == pygame.KEYUP:
# - a key released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player.player_set_speed(0)
    #Next event

    # -- Game logic goes after this comment
    all_sprites_group.update()

    # -- Screen background is BLACK
    screen.fill(GREEN)

    # -- Draw here
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(40)
    
#End While - End of game loop
pygame.quit()

