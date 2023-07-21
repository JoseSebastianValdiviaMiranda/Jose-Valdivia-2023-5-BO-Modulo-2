import pygame

from game.utils.constants import BG, FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu():
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        self.y_pos = 0  #--> posicion y que se asignara a la imagen.
        self.x_pos = 0  #--> posicion x que se asignara a la imagen.
        self.background_image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT)) #--> Imagen de Fondo.
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        #-->Game Over        
        self.game_over = self.font.render(message, True, (255,255,255))        
        #-->Score
        self.score = self.font.render('', True, (255,255,255))             
        #-->Highest_score
        self.highest_score = self.font.render('', True, (255,255,255))       
        #-->Total_Deadths
        self.total_deaths = self.font.render('', True, (255,255,255))       

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):        
        screen.blit(self.game_over, (self.HALF_SCREEN_WIDTH - (self.game_over.get_width() / 2), self.HALF_SCREEN_HEIGHT ))
        screen.blit(self.score, (self.HALF_SCREEN_WIDTH - (self.score.get_width() / 2), self.HALF_SCREEN_HEIGHT + (self.score.get_height() * 1.8)))
        screen.blit(self.highest_score, (self.HALF_SCREEN_WIDTH - (self.highest_score.get_width() / 2), self.HALF_SCREEN_HEIGHT  + (self.score.get_height() * 1.8)  + (self.highest_score.get_height() * 1.8)))
        screen.blit(self.total_deaths, (self.HALF_SCREEN_WIDTH - (self.total_deaths.get_width() / 2), self.HALF_SCREEN_HEIGHT  + (self.score.get_height() * 1.8)  + (self.highest_score.get_height() * 1.8) +  + (self.total_deaths.get_height() * 1.8)))
    
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                game.running = False                
            elif event.type == pygame.KEYDOWN:
                game.run()
    
    def update_message(self, game_over, score, highest_score, total_deaths):
        #-->Game Over
        self.game_over = self.font.render(game_over, True, (255,255,255))        
        #-->Score
        self.score = self.font.render(score, True, (255,255,255))       
        #-->Highest Score
        self.highest_score = self.font.render(highest_score, True, (255,255,255))                       
        #-->Total deaths
        self.total_deaths = self.font.render(total_deaths, True, (255,255,255))

    def reset_screen_color(self, screen):
        screen.blit(self.background_image, (self.x_pos, self.y_pos))
