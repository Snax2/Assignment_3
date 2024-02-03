import pygame
from gamedata import levels


class Node(pygame.sprite.Sprite):
    def __init__(self,pos,status,token_speed):
        super().__init__()
        self.image = pygame.Surface((100,80))
        if status == 'available':
            self.image.fill('blue')
        else:
            self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

        self.detection_zone = pygame.Rect(self.rect.centerx - (token_speed/2),self.rect.centery - (token_speed),token_speed,token_speed)

class Token(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.center = self.pos

class Overworld:
    def __init__(self,start_level,max_level,surface):

        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        #logic
        self.move_direction = pygame.math.Vector2(0,0)
        self.speed = 7
        self.moving = False
        #sprites
        self.setup_nodes()
        self.setup_token()

    def setup_token(self):
        self.token = pygame.sprite.GroupSingle()
        token_sprite = Token(self.nodes.sprites()[self.current_level].rect.center)
        self.token.add(token_sprite)

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available',self.speed)
            else:
                node_sprite = Node(node_data['node_pos'],'locked',self.speed)
            self.nodes.add(node_sprite)

    def draw_path(self):
        points = [node['node_pos'] for index, node in enumerate(levels.values()) if index <= self.max_level]
        pygame.draw.lines(self.display_surface,'green',False,points,5)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data('next')
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_LEFT] and self.current_level >0:
                self.move_direction = self.get_movement_data('previous')
                self.current_level -= 1
                self.moving = True

    def get_movement_data(self,target):
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
        if target == 'next':
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()



    def update_token(self):
        if self.moving and self.move_direction:
            self.token.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.token.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0,0)


    def run(self):
        self.draw_path()
        self.input()
        self.update_token()
        self.token.update()
        self.nodes.draw(self.display_surface)
        self.token.draw(self.display_surface)

