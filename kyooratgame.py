import pygame 
import random
import os



#dont worry about random being dull rn, it's just not being used, its dull like how a variable is dull when its not used

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"sprites")

# making a class for the Player
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"testsprite.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
    def update(self):
        self.rect.x += 5
        if self.rect.left > screen_width:
            self.rect.right = 0

pygame.init()
pygame.display.set_caption('Kyoorat Game')
screen_width = 800
screen_height = 600
#new icon
rat_icon = pygame.image.load(os.path.join(img_folder,"kyooraticon.png"))
pygame.display.set_icon(rat_icon)
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 30
all_sprites = pygame.sprite.Group()
# player = class Player
player = Player()
all_sprites.add(player)

screen = pygame.display.set_mode((screen_width,screen_height))

# Game Loop
running = True

while running == True:
    #keep loop running at right frames per second (speed)
    clock.tick(fps) 
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update
    all_sprites.update()
    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    #after drawing everything flip the display
    pygame.display.flip()

pygame.quit()


