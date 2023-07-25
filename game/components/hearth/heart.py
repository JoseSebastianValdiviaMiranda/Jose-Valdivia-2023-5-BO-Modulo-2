import pygame
from pygame.sprite import Sprite

from game.utils.constants import HEART, HEART_RED

class Hearts(Sprite):
    HEART_WIDTH = 30
    HEART_HEIGHT = 30
    TOTAL_HEARTS = 4
    def __init__(self):
        self.heart_image = pygame.transform.scale(HEART_RED, (self.HEART_WIDTH, self.HEART_HEIGHT))
        self.heart_low = pygame.transform.scale(HEART, (self.HEART_WIDTH, self.HEART_HEIGHT))
        self.heart_image_rect = self.heart_image.get_rect()
        self.heart_image_rect.x = 30
        self.heart_image_rect.y = 10
        self.deaths = self.TOTAL_HEARTS

    def update(self, game):        
        self.deaths = game.hearts_total        
             
    def draw_heart(self, screen):
        if self.deaths == 4:
            screen.blit(self.heart_low, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 60, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 90, self.heart_image_rect.y))

            screen.blit(self.heart_image, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_image, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
            screen.blit(self.heart_image, (self.heart_image_rect.x + 60, self.heart_image_rect.y))
            screen.blit(self.heart_image, (self.heart_image_rect.x + 90, self.heart_image_rect.y))
        elif self.deaths == 3:
            screen.blit(self.heart_low, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 60, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 90, self.heart_image_rect.y))

            screen.blit(self.heart_image, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_image, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
            screen.blit(self.heart_image, (self.heart_image_rect.x + 60, self.heart_image_rect.y))
        elif self.deaths == 2:
            screen.blit(self.heart_low, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 60, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 90, self.heart_image_rect.y))

            screen.blit(self.heart_image, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_image, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
        elif self.deaths == 1:
            screen.blit(self.heart_low, (self.heart_image_rect.x, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 30, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 60, self.heart_image_rect.y))
            screen.blit(self.heart_low, (self.heart_image_rect.x + 90, self.heart_image_rect.y))

            screen.blit(self.heart_image, (self.heart_image_rect.x, self.heart_image_rect.y))                       