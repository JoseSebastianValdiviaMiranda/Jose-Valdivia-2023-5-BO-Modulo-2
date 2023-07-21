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
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
    
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                game.running = False                
            elif event.type == pygame.KEYDOWN:
                game.run()
    
    def update_message(self, message):
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def reset_screen_color(self, screen):
        screen.blit(self.background_image, (self.x_pos, self.y_pos))
