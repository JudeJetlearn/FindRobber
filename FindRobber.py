import pygame
import random

from pygame.locals import *
pygame.init()

WIDTH = 900
HEIGHT = 700
TITLE = "Find The Criminal!"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg = pygame.image.load("vault.png")
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
screen.blit(bg,(0,0))

class Police(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("police.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
        
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            #self.rect.move_ip(0, -5)
            self.rect.y = (self.rect.y - 5)
        if pressed_keys[pygame.K_DOWN]:
            #self.rect.move_ip(0, 5)
            self.rect.y = (self.rect.y + 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right < HEIGHT:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom < HEIGHT:
            self.rect.bottom = WIDTH
        
sprites = pygame.sprite.Group()
        
run = True

police = Police() 
sprites.add(police) 
        
while run:
    pygame.display.update()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    sprites.draw(screen)             
    pressed_keys = pygame.key.get_pressed()
    sprites.update(pressed_keys)
            
    pygame.display.update()

pygame.quit()


