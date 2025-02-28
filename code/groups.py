from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen_display = pygame.display.get_surface()
        
        
    def draw(self):
        for sprite in self:
            for i in range(5):
                self.screen_display.blit(sprite.shadow, sprite.rect.topleft + pygame.Vector2(i, i))
            
        for sprite in self:
            self.screen_display.blit(sprite.image, sprite.rect)