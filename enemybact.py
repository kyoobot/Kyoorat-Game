import pygame
import os
from settings import *
import random

class EnemyBact(pygame.sprite.Sprite):
    def __init__(self, bacteria_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = bacteria_img
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .6 / 2)
        # pygame.draw.circle(self.image,RED, self.rect.center,self.radius)
        self.rect.x = random.randrange(WIDTH,HEIGHT)
        self.rect.y = random.randrange(0,HEIGHT - self.rect.height)
        self.speedx = random.randrange(1,8)
        self.speedy = random.randrange(-2,2)


    def update(self):
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        if self.rect.left < 0 or self.rect.bottom > HEIGHT or self.rect.top < 0: 
            self.rect.x = random.randrange(WIDTH - self.rect.width,WIDTH - 60)
            self.rect.y = random.randrange(0,HEIGHT - self.rect.height)
            self.speedx = random.randrange(1,8)