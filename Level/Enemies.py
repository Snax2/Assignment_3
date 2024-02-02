import pygame
from tiles import AnimatedTile
from random import randint
class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Coin')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3,5)
        #change to correct path after creating png files of enemies


    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        self.speed = -self.speed
        self.image = pygame.transform.flip (self.image,True,False)

    def turn(self):
        self.speed = abs(self.speed)

    def update(self,shift):
        self.rect.x += shift
        self.Animate()
        self.move()


