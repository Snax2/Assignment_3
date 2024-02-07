import pygame
from support import import_csv_layout, import_graphics
from settings import *
from tiles import Tile, StaticTile, Coin
from Enemies import Enemy
from Background import Background
from player import Player
from Level_data import levels


class Level:
    def __init__(self,current_level, surface, load_overworld,change_score):
        #General Setup
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None

        # overworld connection
        self.load_overworld = load_overworld
        self.current_level = current_level
        level_data = levels[self.current_level]
        self.new_max_level = level_data['unlock']

        #UI
        self.change_score = change_score

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

        #Background
        background_image_path = level_data.get('Background', '')
        self.background = Background(background_image_path, surface.get_size())

        #Constraints
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
                        platform_tile_list = import_graphics('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Platforms.png')
                        tile_surface = platform_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)



                    if type == 'Collectables':
                            if val == '0': sprite = Coin(tile_size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Star',10)
                            if val == '4': sprite = Coin(tile_size,x,y,'/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Coin',1)



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
                    new_player = Player((x, y))
                    self.player.add(new_player)
                if val == '2':
                    door_surface = pygame.image.load('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Start_Finish.png').convert_alpha()
                    sprite = StaticTile(tile_size,x,y,door_surface)
                    self.goal.add(sprite)

    def enemy_turn(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.turn()

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.platform_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    #Vertical
    def vertical_collission(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.platform_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    #camera scrolling
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 6
            player.speed = 0
        elif player_x > screen_width * 3/4 and direction_x > 0:
            self.world_shift = -6
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def check_death(self):
        if self.player.sprite.rect.top > screen_height:
            self.load_overworld(self.current_level, 0)

    def check_win(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.goal, False):
            self.load_overworld(self.current_level, self.new_max_level)

    def check_coin_collisions(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite, self.collectables_sprites, True)
        if collided_coins:
            for coin in collided_coins:
                self.change_score(coin.value)

    def run(self):

        #Background
        self.background.draw(self.display_surface)

        #Platforms
        self.platform_sprites.update(self.world_shift)
        self.platform_sprites.draw(self.display_surface)

        #Enemy
        self.enemy_sprites.update(self.world_shift)
        self.enemy_sprites.draw(self.display_surface)

        #Constraints
        self.constraint_sprites.update(self.world_shift)
        self.enemy_turn()

        #Collectables
        self.collectables_sprites.update(self.world_shift)
        self.collectables_sprites.draw(self.display_surface)

        #Player
        self.player.update()
        self.scroll_x()
        self.horizontal_collision()
        self.vertical_collission()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        self.check_death()
        self.check_win()
        self.check_coin_collisions()


