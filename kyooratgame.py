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
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width/2
        self.rect.bottom = screen_height - 10
        self.speedx = 0 
        self.speedy = 0
    def update(self):
        self.speedx = 0 
        self.speedy = 0
        # looking for keypresses to move! speedx = 0 makes sure sprite doesnt move anymore once key isnt pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_s]:
            self.speedy = 8
        if keystate[pygame.K_w]:
            self.speedy = -8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # make sure player sprite doesn't go off screen
        # I added y coordinates as I want to move my character around the screen!
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
    def shoot(self):
        bullet = Bullet(self.rect.left, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

class EnemyBact(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"enemytest.png")).convert_alpha()
        self.image = bacteria_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_height,screen_width)
        self.rect.y = random.randrange(0,screen_height - self.rect.height)
        self.speedx = random.randrange(1,8)
        self.speedy = random.randrange(-2,2)


    def update(self):
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        if self.rect.left < 0 or self.rect.bottom > screen_height or self.rect.top < 0: 
            self.rect.x = random.randrange(screen_width - self.rect.width,screen_width - 60)
            self.rect.y = random.randrange(0,screen_height - self.rect.height)
            self.speedx = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"projectiles1.png")).convert_alpha()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y 
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        # kill if it goes off screen
        if self.rect.right > screen_width:
            self.kill()



pygame.init()
pygame.display.set_caption('Kyoorat Game')

#new icon
rat_icon = pygame.image.load(os.path.join(img_folder,"kyooraticon.png"))
pygame.display.set_icon(rat_icon)
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 60
# load all game graphics 
player_img = pygame.image.load(os.path.join(img_folder,"testsprite.png")).convert_alpha()
bacteria_img = pygame.image.load(os.path.join(img_folder,"enemytest.png")).convert_alpha()
bullet_img = pygame.image.load(os.path.join(img_folder,"projectiles1.png")).convert_alpha()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# player = class Player
player = Player()
all_sprites.add(player)
for index in range(8):
    enemy1 = EnemyBact()
    all_sprites.add(enemy1)
    enemies.add(enemy1)


# Game Loop
running = True

while running == True:
    #keep loop running at right frames per second (speed)
    clock.tick(fps) 
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    #update
    all_sprites.update()
    #draw/render
    screen.fill(BLUE)
    all_sprites.draw(screen)

    #check to see if bullet hit an enemy
    hits = pygame.sprite.groupcollide(enemies,bullets, True, True)
    for hit in hits:
        enemy1 = EnemyBact()
        all_sprites.add(enemy1)
        enemies.add(enemy1)


    # check to see if enemy hits player
    #hits = pygame.sprite.spritecollide(player,enemies,False)
    #if hits:
    #    running = False

    #after drawing everything flip the display
    pygame.display.flip()

pygame.quit()