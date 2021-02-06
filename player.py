import pygame
from pygame.locals import *

class Nave(pygame.sprite.Sprite):
    def __init__(self,*grupo):
        super(Nave,self).__init__(*grupo)
        self.image = pygame.image.load('data/player.png')
        self.image = pygame.transform.scale(self.image, (150,150))

        self.rect = self.image.get_rect()
        self.rect[0] = 20
        self.rect[1] = 300

        self.speed = 7
    def update(self,*args):
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            self.rect[1] -= self.speed
        if keys[K_DOWN]:
            self.rect[1] += self.speed
        
        if self.rect[1] < 0:
            self.rect[1] = 0 
        if self.rect[1] > 600 - 150:
            self.rect[1] = 600 - 150
