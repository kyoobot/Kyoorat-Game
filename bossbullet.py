import pygame
from settings import *

class BossBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = x
        self.rect.centery = y 
        self.speedx = 10

    def update(self):
        self.rect.x -= self.speedx
        # kill if it goes off screen
        if self.rect.left < WIDTH:
            self.kill()
