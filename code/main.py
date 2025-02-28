from settings import *
from sprites import *
from groups import *
import json

class Game():
    def __init__(self):
        pygame.init()
        self.screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pong")
        
        # Sprites
        self.all_sprites = AllSprites()
        self.paddle_sprite = pygame.sprite.Group()
        self.player = Player((self.all_sprites,self.paddle_sprite))
        self.ball = Ball(self.all_sprites, self.paddle_sprite, self.update_score)
        Opponent((self.all_sprites, self.paddle_sprite), self.ball)
        
        # Score
        try:
            with open(join("data", "score.txt")) as score_file:
                self.score = json.load(score_file)
                
        except:
            self.score = {"player": 0, "opponent": 0}
            
        self.font = pygame.font.Font(None, 160)
        
    
    def display_score(self):
        # player
        player_surf = self.font.render(str(self.score["player"]), True, COLORS["bg detail"])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.screen_display.blit(player_surf, player_rect)
        
        # opponent
        opponent_surf = self.font.render(str(self.score["opponent"]), True, COLORS["bg detail"])
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.screen_display.blit(opponent_surf, opponent_rect)
        
        pygame.draw.line(self.screen_display, COLORS["bg detail"], (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 10)
        
        
    def update_score(self, side):
        self.score["player" if side == "player" else "opponent"] += 1
        
        
          
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            
            #Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join("data", "score.txt"), "w") as score_file:
                        json.dump(self.score, score_file)
                    
            # Update
            self.all_sprites.update(dt)
            
            # Draw screen
            self.screen_display.fill(COLORS["bg"])
            self.display_score()
            self.all_sprites.draw()
            pygame.display.update()
            
        pygame.quit()
      
if __name__ == "__main__":
    game = Game()
    game.run()