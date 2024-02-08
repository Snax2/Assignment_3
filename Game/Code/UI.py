import pygame

class UI:
    def __init__(self, surface):
        super().__init__()
        #setup
        self.display_surface = surface

        # Health bar images
        self.health_bar_images = []
        for i in range(9):
            image_path = f'../Graphics/Health/Health_{i}.png'
            self.health_bar_images.append(pygame.image.load(image_path).convert_alpha())

        # Current health index
        self.current_health_index = 100  # Start with full health

        # Health bar position and dimensions
        self.health_bar_rect = self.health_bar_images[0].get_rect(topleft=(20, 10))

        #Coins
        self.score = pygame.image.load('../Graphics/Coin/Coin_1.png').convert_alpha()
        self.score_rect = self.score.get_rect(topleft = (50,120))
        self.font = pygame.font.Font('../Graphics/ARCADEPI.TTF',20)

    def show_health(self, current_health, max_health):

        # Update health bar index based on current health
        health_percent = current_health / max_health
        new_health_index = int((1 - health_percent) * (len(self.health_bar_images) - 1))
        if new_health_index != self.current_health_index:
            self.current_health_index = new_health_index

        # Display current health image
        self.display_surface.blit(self.health_bar_images[self.current_health_index], self.health_bar_rect)

    def show_score(self,amount):
        self.display_surface.blit(self.score,self.score_rect)
        score_surface = self.font.render(str(amount),False,'red')
        score_rect = score_surface.get_rect(midleft = (self.score_rect.right +4,self.score_rect.centery))
        self.display_surface.blit(score_surface,score_rect)