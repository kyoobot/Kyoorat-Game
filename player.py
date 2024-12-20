import pygame
import os
from settings import *
import bullet

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self, player_img, wholegame):
        pygame.sprite.Sprite.__init__(self)
        # I will stick with convert_alpha for now, but i will keep the convert/ color key method in mind in case i need it
        self.image = player_img
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = WIDTH/6
        self.radius = int(self.rect.height)
        # pygame.draw.circle(self.image,RED, self.rect.center,self.radius)
        self.rect.bottom = HEIGHT/2 + self.image.get_height()
        #self.speedx = 0 
        #self.speedy = 0
        self.game = wholegame
        self.speed = 10
        self.direction = pygame.Vector2()

        # Gameplay stats
        self.health = 100
        self.iframes = 180
        self.invincible = False
        self.blinky = 0


    def update(self):
        #self.speedx = 0 
        #self.speedy = 0
        # looking for keypresses to move! speedx = 0 makes sure sprite doesnt move anymore once key isnt pressed
        keys= pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed 
        
        #if keystate[pygame.K_a]:
        #    self.speedx = -8
        #if keystate[pygame.K_d]:
        #    self.speedx = 8
        #if keystate[pygame.K_s]:
        #    self.speedy = 8
        #if keystate[pygame.K_w]:
        #    self.speedy = -8
        #self.rect.x += self.speedx
        #self.rect.y += self.speedy
        # make sure player sprite doesn't go off screen
        # I added y coordinates as I want to move my character around the screen!
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # update kyroorat's invincibility if needed
        if self.invincible == True:
            self.iframes -= 1

            if self.blinky == 0:
                self.image.set_alpha(125)
                self.blinky = 1
            else:
                self.image.set_alpha(30)
                self.blinky = 0

            
            if self.iframes <= 0:
                self.iframes = 180
                self.invincible = False
                self.image.set_alpha(255)


    def shoot(self):
        shot = bullet.Bullet(self.rect.left, self.rect.centery,self.game.bullet_img)
        self.game.all_sprites.add(shot)
        self.game.bullets.add(shot)
