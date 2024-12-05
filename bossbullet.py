import pygame
from settings import *

class BossBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.width = 100
        self.height = 100
        self.rect.x = x
        self.rect.y = y 
        self.speedx = 5
        self.scale = 3
        self.image = pygame.transform.scale(self.image,(self.width * self.scale, self.height * self.scale))
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect.x -= self.speedx
        # kill if it goes off screen
        if self.rect.left < 0 - 500:
            self.kill()
