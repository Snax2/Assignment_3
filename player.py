import pygame
import support

#Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((24,48))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        #Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.1
        self.jump_height = -2

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

    def import_character_data(self):
        character_path = '../'#must do after creating characters
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)    #jump height
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump (self):
        self.direction.y = self.jump_height

    #
    def update(self):
        self.get_input()

