import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y 
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx
        # kill if it goes off screen
        if self.rect.right > WIDTH:
            self.kill()
