import pygame
from support import import_csv_layout, import_graphics
from settings import tile_size
from tiles import Tile, StaticTile, Coin
from Enemies import Enemy

class Level:
    def __init__(self,level_data,surface):
        #General Setup
        self.display_surface = surface
        self.world_shift = -1

        # player
        player_layout = import_csv_layout(level_data['Start/Stop'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        #Platform Setup
        platform_layout = import_csv_layout(level_data['Platforms'])
        self.platform_sprites = self.create_tile_group(platform_layout,'Platform')


        #Collectables
        collectables_layout = import_csv_layout(level_data['Collectables'])
        self.collectables_sprites = self.create_tile_group(collectables_layout,'Collectables')

        #Enemies
        enemy_layout = import_csv_layout(level_data['Enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'Enemies')

        #Start/Stop must change
        #platform_layout = import_csv_layout(level_data['Start/Stop'])
        #self.platform_collectables = self.create_tile_group(platform_layout, 'Start/Stop')

        #Constraints must change
        constraint_layout = import_csv_layout(level_data['Constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, 'Constraints')

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
                            if val == '0': sprite = Coin(tile_size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Star')
                            if val == '4': sprite = Coin(tile_size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Coin')



                    if type == 'Enemies':
                        sprite = Enemy(tile_size,x,y)

                    if type == 'Constraints':
                        sprite = Tile(tile_size,x,y)

                    sprite_group.add(sprite)

        return sprite_group

    def player_setup(self,layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    print('player here')
                if val == '2':
                    door_surface = pygame.image.load('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Start_Finish.png').convert_alpha()
                    sprite = StaticTile(tile_size,x,y,door_surface)
                    self.goal.add(sprite)




    def enemy_turn(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.turn()


    def run(self):
        #Run game

        #Platforms
        self.platform_sprites.update(self.world_shift)
        self.platform_sprites.draw(self.display_surface)

        #enemy
        self.enemy_sprites.update(self.world_shift)

        self.enemy_sprites.draw(self.display_surface)

        self.constraint_sprites.update(self.world_shift)
        self.enemy_turn()

        #Collectables
        self.collectables_sprites.update(self.world_shift)
        self.collectables_sprites.draw(self.display_surface)

        #Player
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)



