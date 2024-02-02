import pygame
from support import import_csv_layout, import_graphics
from settings import tile_size
from tiles import Tile, StaticTile, Coin

class Level:
    def __init__(self,level_data,surface):
        #General Setup
        self.display_surface = surface
        self.world_shift = 0

        #Platform Setup
        platform_layout = import_csv_layout(level_data['Platforms'])
        self.platform_sprites = self.create_tile_group(platform_layout,'Platform')


        #Collectables
        collectables_layout = import_csv_layout(level_data['Collectables'])
        self.collectables_sprites = self.create_tile_group(collectables_layout,'Collectables')

        #Enemies must change
        #platform_layout = import_csv_layout(level_data['Enemies'])
        #self.platform_collectables = self.create_tile_group(platform_layout, 'Enemies')

        #Start/Stop must change
        #platform_layout = import_csv_layout(level_data['Start/Stop'])
        #self.platform_collectables = self.create_tile_group(platform_layout, 'Start/Stop')

        #Constraints must change
        #platform_layout = import_csv_layout(level_data['Constraints'])
        #self.platform_collectables = self.create_tile_group(platform_layout, 'Constraints')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'Platform':
                        platform_tile_list = import_graphics('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/tiles-6 2.png')
                        tile_surface = platform_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)



                    if type == 'Collectables':
                            if val == '0': sprite = Coin(tile_size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Coin')
                            if val == '4': sprite = Coin(tile_size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Coin')
                            #change above to star after creating png files

                    sprite_group.add(sprite)

        return sprite_group



    def run(self):
        #Run game

        #Platforms
        self.platform_sprites.update(self.world_shift)
        self.platform_sprites.draw(self.display_surface)


        #Collectables
        self.collectables_sprites.update(self.world_shift)
        self.collectables_sprites.draw(self.display_surface)


