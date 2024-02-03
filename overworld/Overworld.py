import pygame
from gamedata import levels

class Overworld:
    def __init__(self,start_level,max_level,surface):

        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        #sprites
        self.setup_nodes

    def run(self):
        pass