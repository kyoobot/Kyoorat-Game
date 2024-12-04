import pygame 
import random
import os
from settings import *
import player
import enemybact
import math


class Game:
    def __init__(self):
        #initialize game window, etc
        pygame.init()

        #set up assets folder: 
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder,"sprites")

        pygame.display.set_caption('Kyoorat Game')
        rat_icon = pygame.image.load(os.path.join(img_folder,"kyooraticon.png"))
        pygame.display.set_icon(rat_icon)
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True



        #load all game graphics
        # bg sprites and needed variables

        self.bg_images = []
        self.num_bg_layers = 4
        for i in range(1,self.num_bg_layers+1):
            bg_image = pygame.image.load(os.path.join(img_folder,f"bgimage{i}.png")).convert_alpha()
            self.bg_images.append(bg_image)
        self.bg_width = self.bg_images[0].get_width()
        self.tiles = math.ceil(WIDTH / self.bg_width) + 1
        self.scroll = 0 

        # actor sprites

        self.player_img = pygame.image.load(os.path.join(img_folder,"kyoorat.png")).convert_alpha()
        self.bacteria_img = pygame.image.load(os.path.join(img_folder,"enemy-Sheet.png")).convert_alpha()
        self.bullet_img = pygame.image.load(os.path.join(img_folder,"projectiles1.png")).convert_alpha()



    def new(self):
        #start a new game

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = player.Player(self.player_img, self)
        self.all_sprites.add(self.player)
        
        #meteor behavior for enemy, will be changed        
        for index in range(8):
            enemy1 = enemybact.EnemyBact(self.bacteria_img)
            self.all_sprites.add(enemy1)
            self.enemies.add(enemy1)



        self.run()

    def run(self):
        #game loop

        self.playing = True
        while self.playing == True:
            self.clock.tick(FPS)

            self.events()
            self.update()
            self.draw()

                
    def update(self):
        #game loop update
            #check to see if bullet hit an enemy
        hits = pygame.sprite.groupcollide(self.enemies,self.bullets, True, True)
        for hit in hits:
            enemy1 = enemybact.EnemyBact(self.bacteria_img)
            self.all_sprites.add(enemy1)
            self.enemies.add(enemy1)


        # check to see if enemy hits player
        #hits = pygame.sprite.spritecollide(player,enemies,False)
        if hits:
            self.running = False

        

        
        self.all_sprites.update()
        

    def events(self):
        #game loop - events
        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False

                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.player.shoot()
        
    def draw(self):
        #game loop - draw
        #self.screen.fill(BLUE)
        # scrolling bg
        for i in range(0, self.tiles):
            speed = 1
            for j in self.bg_images:
                self.screen.blit(j, (i * self.bg_width + self.scroll * speed, 0))
                speed += 0.2
                
        self.scroll -= 2 


        # reset scroll 
        if abs(self.scroll) > self.bg_width: 
            self.scroll = 0 
        
        self.all_sprites.draw(self.screen)



        #after drawing everything flip the display
        pygame.display.flip()

    def show_start_screen(self):
        #game splash/start screen
        pass
    def show_go_screen(self):
        #game over/continue
        pass

g = Game()
g.show_start_screen()

while g.running == True:
    g.new()
    g.run()
    g.show_go_screen()

pygame.quit()
