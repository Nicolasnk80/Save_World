import pygame

class Shot(pygame.sprite.Sprite):
    def __init__(self,*grupo):
        super(Shot,self).__init__(*grupo)
        self.image = pygame.image.load('data/asteroid.png')
        self.image = pygame.transform.scale(self.image, (10,10))

        self.rect = self.image.get_rect()

        self.speed = 10
    def update(self,*args):
        self.rect[0] += self.speed

        if self.rect.right < 0:
            self.kill()
