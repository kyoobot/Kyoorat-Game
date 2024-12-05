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
        self.img_folder = os.path.join(game_folder,"sprites")

        pygame.display.set_caption('Kyoorat Game')
        rat_icon = pygame.image.load(os.path.join(self.img_folder,"kyooraticon.png"))
        pygame.display.set_icon(rat_icon)
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        self.playing = True

        self.text_font = pygame.font.SysFont(None, 30)

    
        # gameplay stats
        self.enemy_kills = 0

        #load all game graphics
        # bg sprites and needed variables

        self.bg_images = []
        self.bg_scroll = []
        self.scroll = 0
        self.num_bg_layers = 4
        for i in range(1,self.num_bg_layers+1):
            bg_image = pygame.image.load(os.path.join(self.img_folder,f"bgimage{i}.png")).convert_alpha()
            self.bg_images.append(bg_image)
            self.bg_scroll.append(0)
        self.bg_width = self.bg_images[0].get_width()
        self.tiles = math.ceil(WIDTH / self.bg_width) + self.num_bg_layers
        

        # actor sprites

        self.player_img = pygame.image.load(os.path.join(self.img_folder,"kyoorat.png")).convert_alpha()
        self.bacteria_img = pygame.image.load(os.path.join(self.img_folder,"enemy-Sheet.png")).convert_alpha()
        self.bullet_img = pygame.image.load(os.path.join(self.img_folder,"projectiles1.png")).convert_alpha()



    def new(self):
        #start a new game

        self.enemy_kills = 0

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
        while self.playing == True:
            self.clock.tick(FPS)

            self.events()
            self.update()
            self.draw()

                
    def update(self):
        #game loop update
        
        #check to see if bullet hit an enemy
        hits = []
        for enemy in self.enemies.sprites():
            for bullet in self.bullets.sprites():
                if pygame.sprite.collide_mask(enemy, bullet):
                    enemy.kill()
                    bullet.kill()
                    hits.append(0)
                    break
        #hits = pygame.sprite.groupcollide(self.enemies,self.bullets, True, True)
        for hit in hits:
            self.enemy_kills += 1
            enemy1 = enemybact.EnemyBact(self.bacteria_img)
            self.all_sprites.add(enemy1)
            self.enemies.add(enemy1)

        # check to see if enemy hits player
        #hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        hits = []
        for enemy in self.enemies.sprites():
            if pygame.sprite.collide_mask(self.player, enemy):
                hits.append(0)
        # perform hit logic only if player is not invincible
        if hits and not self.player.invincible:
            # the enemies do 5 dmg to kyoorat per hit
            self.player.health -= 5
            if self.player.health < 0:
                # the game ends, and the player is taken to the game over screen
                self.playing = False
            # give the player invincibility for a short period
            self.player.invincible = True


        
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
        
    def draw_text(self, screen, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))

    def draw(self):
        #game loop - draw
        #self.screen.fill(BLUE)
        # scrolling bg
        for i in range(0, self.tiles):
            speed = 1
            for j in range(0, len(self.bg_images)):
                self.screen.blit(self.bg_images[j], (i * self.bg_width + self.bg_scroll[j] * speed , 0))
                speed += 1
                if i == self.tiles-1:
                    self.bg_scroll[j] -= 1
                
        # reset scroll for each layer if needed
        for i in range (0, self.tiles):
            speed = 1
            for j in range(0, len(self.bg_images)):
                if abs(self.bg_scroll[j]) > self.bg_width:
                    if i == self.tiles - 1:
                        self.bg_scroll[j] = 0
                speed += 1
        
        self.all_sprites.draw(self.screen)

        # draw the gameplay stats on top of everything
        self.draw_text(self.screen, f"Kyroorat | HEALTH: {self.player.health}", self.text_font, (0, 0, 0), 0, 0)
        if self.enemy_kills < 100:
            self.draw_text(self.screen, f"Enemies Destroyed: {self.enemy_kills}/100", self.text_font, (0, 0, 0), WIDTH/2, 0)
        else:
            self.draw_text(self.screen, f"BOSS TIME! - Tardigrade | HEALTH: 3000", self.text_font, (255, 0, 0), WIDTH/2, 0)



        # after drawing everything flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game start screen image
        start_screen = pygame.image.load(os.path.join(self.img_folder,"startscreen.png")).convert_alpha()
        
        # start screen loop - will end when player
        # presses either Enter or Esc
        self.clock.tick(60)

        running = True
        while running:

            # Check for events
            for event in pygame.event.get():
                #check for closing window
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.playing:
                            self.playing = False
                        self.running = False
                        running = False
                    
                    if event.key == pygame.K_RETURN:
                        running = False
            
            self.screen.blit(start_screen, (0, 0))
            pygame.display.flip()


    def show_go_screen(self):
        # game over screen image
        go_screen = pygame.image.load(os.path.join(self.img_folder,"gameover.png")).convert_alpha()
        
        # start screen loop - will end when player
        # presses either Enter or Esc
        self.clock.tick(60)

        running = True
        while running and self.running:

            # Check for events
            for event in pygame.event.get():
                #check for closing window
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.playing:
                            self.playing = False
                        self.running = False
                        running = False
                    
                    if event.key == pygame.K_RETURN:
                        self.playing = True
                        running = False
            
            self.screen.blit(go_screen, (0, 0))
            pygame.display.flip()

g = Game() 

while g.running == True:
    g.show_start_screen()
    g.new()
    g.run()
    g.show_go_screen()

pygame.quit()
