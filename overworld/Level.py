import pygame
from settings import screen_width, screen_height
from gamedata import levels


class Level:
    def __init__(self, current_level, surface):
        # level setup
        self.display_surface = surface
        self.current_level = current_level
        level_data = levels[current_level]
        level_content = level_data['content']
        self.new_max_level = level_data['unlock']


        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render(level_content, True, 'White')
        self.text_rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))



    def run(self):
        self.display_surface.blit(self.text_surf, self.text_rect)