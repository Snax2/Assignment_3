import pygame

class Background:
    def __init__(self, image_path, screen_size):
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)