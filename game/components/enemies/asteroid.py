import pygame
import random

from pygame.sprite import Sprite

from game.utils.constants import SCREEN_WIDTH, ASTEROID

class Asteroid(Sprite):
    ASTEROID_WIDTH = 100
    ASTEROID_HEIGHT = 100    
    Y_POS = 20
    SPEED_Y = 2

    def __init__(self):
        self.position_x = random.randrange(50, SCREEN_WIDTH - self.ASTEROID_WIDTH, 50)
        self.image = pygame.transform.scale(ASTEROID, (self.ASTEROID_WIDTH, self.ASTEROID_HEIGHT))
        self.angle = 0
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.image_rotate_rect = self.image_rotate.get_rect()        
        self.image_rotate_rect.x = self.position_x
        self.image_rotate_rect.y = self.Y_POS

    def update(self):
        self.image_rotate_rect.y += self.SPEED_Y
        self.angle += 0.5

    def draw(self, screen):
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        screen.blit(self.image_rotate, (self.image_rotate_rect.x, self.image_rotate_rect.y))
        
