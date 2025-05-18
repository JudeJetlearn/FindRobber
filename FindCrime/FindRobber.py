import pygame
import random
import time

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 700
TITLE = "Find The Criminal!"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg = pygame.image.load("vault.png")
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))

score = 50
start_time = time.time()

def draw_score(text,font,text_col,x,y):
    scoretext = font.render(text,True,text_col)
    screen.blit(scoretext,(x,y))
    
def draw_time(text,font,text_col,x,y):
    timetext = font.render(text,True,text_col)
    screen.blit(timetext,(x,y))

class Police(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("police.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
        
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.y = (self.rect.y - 5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.y = (self.rect.y + 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
police_group = pygame.sprite.Group()
        
class Robber(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("robber.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()      
  
        self.rect.y = random.randint(0,700)        
        self.rect.x = random.randint(0,900)   
        
class Baby(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("baby.png")
        self.image = pygame.transform.scale(self.image, (40,70))
        self.rect = self.image.get_rect()

baby_group = pygame.sprite.Group()

for i in range(3):
    
    BABY = Baby()
    
    BABY.rect.x = random.randint(0,WIDTH)  
    BABY.rect.y = random.randint(0,HEIGHT)
    
    
    baby_group.add(BABY)          
        
robber_group = pygame.sprite.Group()    
        
run = True

police = Police() 
police_group.add(police)
Rob = Robber() 
robber_group.add(Rob)
      
font =  pygame.font.SysFont("Arial",50)     
        
while run:
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
          
    screen.blit(bg,(0,0))            
    police_group.draw(screen)  
    robber_group.draw(screen)
    baby_group.draw(screen)           
    pressed_keys = pygame.key.get_pressed()
    police_group.update(pressed_keys)
    
    time_played = time.time() - start_time
    
    draw_score(str(score),font,"white",WIDTH//2,100)
    draw_time(str(time_played // 1),font,"white",435,175)
    
    if pygame.sprite.groupcollide(police_group,robber_group,False,False):
        score = score + 1
        Rob.rect.y = random.randint(0,700)        
        Rob.rect.x = random.randint(0,900)
    
    if time_played >= 5:
        if score >= 50:
            time_played = ""
            message = font.render("You Win!",True,"Gold")
        else:
            time_played = ""
            message = font.render("Better luck Next Time",True,"White")  
        
        screen.blit(message,(400,225))
           
    Hit_Baby = pygame.sprite.spritecollide(police,baby_group,True)
    
    for i in Hit_Baby:
        score = score - 1
        BABY.rect.y = random.randint(0,700)        
        BABY.rect.x = random.randint(0,900)  
           
    pygame.display.update()

pygame.quit()


