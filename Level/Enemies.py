import pygame
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Enemy')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(1,2)


    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        if self.speed < 0:
            self.image = pygame.transform.flip (self.image,True,False)

    def turn(self):
        self.speed *= -1

    def update(self,shift):
        self.rect.x += shift
        self.Animate()
        self.move()
        self.reverse()


