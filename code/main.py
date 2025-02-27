from settings import *
from sprites import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pong")
        
        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprite = pygame.sprite.Group()
        self.player = Player((self.all_sprites,self.paddle_sprite))
        self.ball = Ball(self.all_sprites, self.paddle_sprite)
        Opponent((self.all_sprites, self.paddle_sprite), self.ball)
        
        
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            
            #Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Update
            self.all_sprites.update(dt)
            
            # Draw screen
            self.screen_display.fill(COLORS["bg"])
            self.all_sprites.draw(self.screen_display)
            pygame.display.update()
            
        pygame.quit()
      
if __name__ == "__main__":
    game = Game()
    game.run()