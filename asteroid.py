import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,*grupo):
        super(Asteroid,self).__init__(*grupo)
        self.image = pygame.image.load('data/asteroid.png')
        self.image = pygame.transform.scale(self.image, (100,100))

        self.rect = self.image.get_rect()
        self.rect[0] = 800 + random.randint(1, 400)
        self.rect[1] = random.randint(1, 500)

        self.speed = random.randint(6, 9)
    def update(self,*args):
        self.rect[0] -= self.speed

        if self.rect.right < 0:
            self.kill()
