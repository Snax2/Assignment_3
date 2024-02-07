import pygame

class UI:
    def __init__(self, surface):
        super().__init__()
        #setup
        self.display_surface = surface

        #Health
        self.health_bar = pygame.image.load('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Power bar.png').convert_alpha()

        #Coins
        self.score = pygame.image.load('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/Coin/Coin_1.png').convert_alpha()
        self.score_rect = self.score.get_rect(topleft = (50,200))#change??
        self.font = pygame.font.Font('/Users/snax/Desktop/SUPER BART/Level/Level/Graphics/ARCADEPI.TTF',20)


    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (20, 10))

    def show_score(self,amount):
        self.display_surface.blit(self.score,self.score_rect)
        score_surface = self.font.render(str(amount),False,'red')
        score_rect = score_surface.get_rect(midleft = (self.score_rect.right +4,self.score_rect.centery))
        self.display_surface.blit(score_surface,score_rect)