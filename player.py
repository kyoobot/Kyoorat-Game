import pygame
import os
from settings import *
import bullet

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self,player_img, wholegame):
        pygame.sprite.Sprite.__init__(self)
        # I will stick with convert_alpha for now, but i will keep the convert/ color key method in mind in case i need it
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.radius = int(self.rect.height)
        # pygame.draw.circle(self.image,RED, self.rect.center,self.radius)
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0 
        self.speedy = 0
        self.game = wholegame



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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    def shoot(self):
        shot = bullet.Bullet(self.rect.left, self.rect.centery)
        self.game.all_sprites.add(shot)
        self.game.bullets.add(shot)
