import pygame
from gamedata import levels


class Node(pygame.sprite.Sprite):
    def __init__(self,pos,status):
        super().__init__()
        self.image = pygame.Surface((100,80))
        if status == 'available':
            self.image.fill('blue')
        else:
            self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

class Token(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)



class Overworld:
    def __init__(self,start_level,max_level,surface):

        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

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
                node_sprite = Node(node_data['node_pos'], 'available')
            else:
                node_sprite = Node(node_data['node_pos'],'locked')
            self.nodes.add(node_sprite)

    def draw_path(self):
        points = [node['node_pos'] for index, node in enumerate(levels.values()) if index <= self.max_level]
        pygame.draw.lines(self.display_surface,'green',False,points,5)




    def run(self):
        self.draw_path()
        self.nodes.draw(self.display_surface)
        self.token.draw(self.display_surface)

