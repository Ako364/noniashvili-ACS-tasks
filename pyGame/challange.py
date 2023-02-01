import pygame
import random

a = True

# Global Constants

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (0, 20, 15)



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
        self.rect.x = random.randrange(30, 570)
        self.rect.y = 370
        # Set speed of the sprite
        self.speed = 5
    # End Proceure
    def get_x(self):
        return self.rect.x
    # Class update function - runs for each pass through the game loop
    def player_jump(self):
        for n in range(0,20):
            self.rect.y = self.rect.y - self.speed
            if self.rect.y <= 0 or self.rect.y >= 375:
                self.speed = -1 * self.speed
            n += 1 
            if n == 20:
                self.rect.y = self.rect.y + 5*20
                n = -1
# End class



# Initialise PyGame
pygame.init()

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

## -- create a player
player = Player(YELLOW, 30, 30)
all_sprites_group.add(player)

# Blank Screen
size = (600,400)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("Challange")

# Exit game flag set to false
done = False

# Manages how fast screen refreshes
clock = pygame.time.Clock()


### Game Loop


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
                    print("jump!")
                    player.player_jump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.rect.x < 0:
            player.rect.x = 0
        else:
            player.rect.x = player.rect.x - 10
    if keys[pygame.K_RIGHT]:
        if player.rect.x >= 1200 - 15:
            player.rect.x = 1200 - 15
        else:
            player.rect.x = player.rect.x + 10
    # End event
    
    # Game logic goes after this comment
    
    # -- Screen background is Dark Green 
    screen.fill(GREEN)

    # -- Draw here
    all_sprites_group.draw(screen)
    
    # Flip display to reveal new position of objects
    pygame.display.flip()
    
    # The clock ticks over
    clock.tick(60)
    
    # End While End of game loop
pygame.quit()