import pygame
from support import import_folder
import os
from math import sin

#Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface,change_health):
        super().__init__()
        self.import_character_data()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['Running'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        #Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.42
        self.jump_height = -9.6
        self.shoot = False

        #Audio
        self.jump_sound = pygame.mixer.Sound('../Sounds/Sound Effects/Jump.mp3')
        self.jump_sound.set_volume(0.1)
        self.hurt_sound = pygame.mixer.Sound('../Sounds/Bart Voice/Medic.wav')
        self.hurt_sound.set_volume(0.3)

        # User status
        self.status = 'Standing'
        self.right_facing = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_right = False
        self.on_left = False

        #Health
        self.change_health = change_health
        self.invincible = False
        self.invincibility_duration = 400
        self.hurt_time = 0

    def import_character_data(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        character_path = os.path.join(script_dir, '../Graphics/Graphics_Bart/')
        self.animations = {'Standing': [], 'Running': [], 'Jumping': [], 'Shooting': [], 'Jump_Shoot': [], 'Falling': []}

        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.right_facing:
            self.image = image
        else:
            flip_image = pygame.transform.flip(image,True,False)
            self.image = flip_image
        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(225)
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right_facing = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.right_facing = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
            self.jump_sound.play()
        if keys[pygame.K_s]:
            self.start_shooting()
        else:
            self.stop_shooting()

    def start_shooting(self):
        self.is_shooting = True

    def stop_shooting(self):
        self.is_shooting = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump (self):
        self.direction.y = self.jump_height

    def get_status(self):
        if self.direction.y < 0 or self.direction.y > 1:
            if self.is_shooting:
                self.status = 'Jump_Shoot'
            else:
                self.status = 'Jumping' if self.direction.y < 0 else 'Falling'
        else:
            if self.direction.x != 0 or self.is_shooting:
                if self.is_shooting:
                    if self.direction.y == 0:
                        self.status = 'Shooting'
                else:
                    self.status = 'Running'
            else:
                self.status = 'Standing'

    def get_damage(self):
        if not self.invincible:
            self.change_health(-12.5)
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()
            self.hurt_sound.play()

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >=self.invincibility_duration:
                self.invincible = False

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 225
        else: return 0

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.invincibility_timer()
        self.wave_value()

