import pygame
from Support import import_folder
import os

#Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_data()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['Running'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        #Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.1
        self.jump_height = -2


    def import_character_data(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        character_path = os.path.join(script_dir, '/Users/snax/Desktop/SUPER BART/Data/Images/Bart')
        self.animations = {'Standing': [], 'Running': [], 'Jumping': [], 'Shooting': [], 'Jump_Shoot': [], 'Falling': []}

        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations['Jumping']

        #looping frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
    #User input
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()
    #jump height
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump (self):
        self.direction.y = self.jump_height

    #
    def update(self):
        self.get_input()
        self.animate()

