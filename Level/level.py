import pygame
from support import import_csv_layout

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface


        terrain_layout = import_csv_layout(level_data['Platforms'])
    def run(self):
        #Run game
        pass