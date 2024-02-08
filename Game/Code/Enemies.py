import pygame
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'../Graphics/Enemy')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(1,2)
        self.squished = False
        self.squish_duration = 0.5
        self.squish_timer = 0
        self.initial_x = x
        self.initial_y = y

    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        if self.speed < 0:
            self.image = pygame.transform.flip (self.image,True,False)

    def turn(self):
        self.speed *= -1

    def squish(self):
        self.squished = True
        self.image = pygame.image.load("../Graphics/Enemy_Squish.png").convert_alpha()
        self.squish_start_time = pygame.time.get_ticks()

    def update(self, shift):
        if not self.squished:
            self.rect.x += shift
            self.Animate()
            self.move()
            self.reverse()
        else:
            if pygame.time.get_ticks() - self.squish_start_time >= self.squish_duration * 1000:

                self.kill()

