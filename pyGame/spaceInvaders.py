import pygame
import random

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (150,50,255)
YELLOW = (255,255,0)
GREEN = (0, 20, 15)

a = True

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
        self.rect.y = random.randrange(-100,0)
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
        self.rect.y = 975
        # Set speed of the sprite
        self.speed = 0
        self.lives = 5 
    # End Proceure

    # Class update function - runs for each pass through the game loop
    def player_set_speed(self):
        self.rect.x = self.rect.x + self.speed
        # if self.rect.y >= 1000:
            # Spawn a invaderflake randomly on x-axis and on 0 on y-axis
            # self.rect.x = random.randrange(0, 1200)
            # self.rect.y = 0 + self.speed   

# End class


class Bullet(pygame.sprite.Sprite):
    # Define the constructor for Invader
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = player.get_x() + 10
        self.rect.y = 700
    def update(self):
        # Move bullet up 
        self.rect.y = self.rect.y - 3
        pygame.sprite.groupcollide(bullet_list, Invader_group, True, True)
        

## -- Initialise PyGame
pygame.init()

# --- set font for the scoreboard
font = pygame.font.Font('freesansbold.ttf', 32)

# -- Blank Screen
size = (1200, 1000)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Invader")

# -- Exit game flag set to false
done = False


# Create a list of the Invader blocks
Invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

## -- Create the invaders
number_of_flakes = 10 
for x in range(number_of_flakes):
    my_Invader = Invader(WHITE, 20, 5, 5)
    Invader_group.add(my_Invader)
    all_sprites_group.add(my_Invader)

## -- create a player
player = Player(YELLOW, 30, 30)
all_sprites_group.add(player)

# Create a list of all bullets
# bullet_list = pygame.sprite.Group()

# Procedure to fire bullet
def fire():
    mybullet = Bullet(WHITE, 3, 7)
    all_sprites_group.add(mybullet)
    

## -- game loop
while not done:
    # User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                a = True
            elif event.key == pygame.K_RIGHT:
                a = True
            elif event.key == pygame.K_UP:
                fire()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.rect.x < 0:
            player.rect.x = 0
        else:
            player.rect.x = player.rect.x - 20
    if keys[pygame.K_RIGHT]:
        if player.rect.x >= 1200 - 25:
            player.rect.x = 1200 - 25
        else:
            player.rect.x = player.rect.x + 20
    
    # -- Game logic goes after this comment
    all_sprites_group.update()
    player_hit_group = pygame.sprite.spritecollide(player, Invader_group, True)

    for foo in player_hit_group:
        player.lives = player.lives - 1


    # -- Screen background is BLACK
    screen.fill(GREEN)

    # -- Draw here
    all_sprites_group.draw(screen)

    # -- lives 
    lives = font.render("LIVES : " + str(player.lives), True, (255, 255, 255))
    screen.blit(lives, (400, 50))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(40)
    
#End While - End of game loop
pygame.quit()

