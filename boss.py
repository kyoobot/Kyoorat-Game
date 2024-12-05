import pygame
import os
from settings import *
import random



class Boss(pygame.sprite.Sprite):
    def __init__(self, boss_img, wholegame):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_img
        self.rect = self.image.get_rect()
        self.mask = None
        # self.radius = int(self.rect.width * .6 / 2)
        # pygame.draw.circle(self.image,RED, self.rect.center,self.radius)
        #self.speedx = random.randrange(1,8)
        #self.speedy = random.randrange(-2,2)
        self.width = 600
        self.height = 500
        self.rect.x = WIDTH + self.width + 20
        self.rect.y = HEIGHT/2 - self.rect.center[1]
        self.scale = 1

        self.game = wholegame

        # gameplay stats
        self.health = 3000
        self.bosstime = False
        self.invincible = True
        self.has_entered_arena = False
        self.has_transitioned_to_phase_2 = False
        self.phase = 1 

        #animation variables!
        self.animation_list = []
        self.animation_steps = [5,7,5,4]
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0 
        self.action = 0
        self.step_counter = 0 

        # for loop for animation, works with update(self)
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation): 
                temp_img_list.append(self._get_image(self.step_counter))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

        
        self.update()

    def _get_image(self, frame):
        image = pygame.Surface((self.width,self.height)).convert_alpha()
        image.blit(self.image,(0,0),((frame * self.width), 0,self.width,self.height))
        image = pygame.transform.scale(image,(self.width * self.scale, self.height * self.scale))
        image.set_colorkey(GREEN)
        return image


    def update(self):
        # self.rect.x -= self.speedx
        # self.rect.y -= self.speedy
        # if self.rect.left < 0 or self.rect.bottom > HEIGHT or self.rect.top < 0: 
        #     self.rect.x = random.randrange(WIDTH - self.rect.width,WIDTH - 60)
        #     self.rect.y = random.randrange(0,HEIGHT - self.rect.height)
        #     self.speedx = random.randrange(1,8)

        # update animation, from init
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown: 
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
        self.image = self.animation_list[self.action][self.frame]
        self.mask = pygame.mask.from_surface(self.image)

        # bosstime
        if self.bosstime:
            if not self.has_entered_arena:
                self.move_into_arena()
            else: 
                self.invincible = False
            # check health for 2nd phase
            if self.health <= 1500:
                self.phase = 2
            if self.phase == 2:
                if not self.has_transitioned_to_phase_2:
                    self.invincible = True
                    self.move_to_phase_2() 
    
    def move_into_arena(self):
        if self.rect.x > WIDTH - self.width:
            self.rect.x -= 5
        else:
            self.has_entered_arena = True

    def move_to_phase_2(self): 
        if self.action != 2: 
            self.action = 2
        else: 
            if self.frame >= len(self.animation_list[self.action]):
                self.action = 4
                self.has_transitioned_to_phase_2 = True
                self.invincible = False
