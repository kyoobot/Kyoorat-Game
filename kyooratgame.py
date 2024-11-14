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

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

# making a class for the Player
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # I will stick with convert_alpha for now, but i will keep the convert/ color key method in mind in case i need it
        self.image = pygame.image.load(os.path.join(img_folder,"testsprite.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width/2
        self.rect.bottom = screen_height - 10
        self.speedx = 0 
    def update(self):
        self.speedx = 0 
        # looking for keypresses to move! speedx = 0 makes sure sprite doesnt move anymore once key isnt pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx

pygame.init()
pygame.display.set_caption('Kyoorat Game')

#new icon
rat_icon = pygame.image.load(os.path.join(img_folder,"kyooraticon.png"))
pygame.display.set_icon(rat_icon)
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 60
all_sprites = pygame.sprite.Group()
# player = class Player
player = Player()
all_sprites.add(player)


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
    screen.fill(BLUE)
    all_sprites.draw(screen)

    #after drawing everything flip the display
    pygame.display.flip()

pygame.quit()


