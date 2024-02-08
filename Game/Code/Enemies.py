import pygame
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Enemy')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(1,2)
        self.squished = False  # Flag to track if the enemy is squished
        self.squish_duration = 0.5  # Duration for which the enemy remains squished (in milliseconds)
        self.squish_timer = 0  # Timer to keep track of squish duration
        self.initial_x = x  # Record initial x position
        self.initial_y = y  # Record initial y position

    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        if self.speed < 0:
            self.image = pygame.transform.flip (self.image,True,False)

    def turn(self):
        self.speed *= -1

    def squish(self):
        self.squished = True
        # Set the image to the squished version
        self.image = pygame.image.load("/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Enemy_Squish.png").convert_alpha()
        self.squish_start_time = pygame.time.get_ticks()


    def update(self, shift):
        if not self.squished:  # Only move if not squished
            self.rect.x += shift
            self.Animate()
            self.move()
            self.reverse()
        else:
            # Check if the squish duration has elapsed
            if pygame.time.get_ticks() - self.squish_start_time >= self.squish_duration * 1000:  # Convert seconds to milliseconds
                # If squish duration is over, remove the enemy from the game
                self.kill()

