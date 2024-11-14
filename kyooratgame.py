import pygame 
import random

pygame.init()
pygame.display.set_caption('Kyoorat Game')
screen_width = 800
screen_height = 600
#new icon
rat_icon = pygame.image.load("kyooraticon.png")
pygame.display.set_icon(rat_icon)
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 30

screen = pygame.display.set_mode((screen_width,screen_height))

running = True

while running == True: 
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.display.flip()
pygame.quit()

