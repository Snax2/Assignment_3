import pygame
from support import import_csv_layout
from settings import tile_size
from tiles import Tile

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface


        platform_layout = import_csv_layout(level_data['Platforms'])
        self.platform_sprites = self.create_tile_group(platform_layout,'Platform')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'Platform':
                        sprite = Tile(tile_size,x,y)
                        sprite_group.add(sprite)

        return sprite_group



    def run(self):
        #Run game
        self.platform_sprites.draw(self.display_surface)