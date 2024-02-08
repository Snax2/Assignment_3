import pygame, sys
from settings import *
from level import Level
from Overworld import Overworld
from UI import UI



class Game:
    def __init__(self):

        #Game attributes
        self.max_level = 0
        self.max_health = 100
        self.current_health = 100
        self.score = 0

        #Audio
        self.level_background_music = pygame.mixer.Sound('/Users/snax/Desktop/SUPER BART/Data/Sounds/Sound Effects/Level_1.mp3')
        self.overworld_background_music = pygame.mixer.Sound('/Users/snax/Desktop/SUPER BART/Data/Sounds/Sound Effects/Overworld.mp3')



        #Overworld
        self.overworld = Overworld(0,self.max_level,screen,self.create_level)
        self.status = 'overworld'
        self.overworld_background_music.play(loops = -1)

        # UI
        self.ui = UI(screen)

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.load_overworld, self.change_score, self.change_health)
        self.status = 'level'
        self.overworld_background_music.stop()
        self.level_background_music.play(loops = -1)





    def load_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level,self.max_level,screen, self.create_level)
        self.status = 'overworld'
        self.overworld_background_music.play(loops = -1)
        self.level_background_music.stop()



    def change_score(self,amount):
        self.score += amount

    def change_health(self,amount):
        self.current_health += amount

    def game_over(self):
        if self.current_health <= 0:
            self.current_health = 100
            self.score = 0
            self.max_level = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_background_music.stop()
            self.overworld_background_music.play(loops=-1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()

            self.ui.show_health(self.current_health, self.max_health)
            self.ui.show_score(self.score)
            self.game_over()

#pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()
    pygame.display.update()
    clock.tick(60)