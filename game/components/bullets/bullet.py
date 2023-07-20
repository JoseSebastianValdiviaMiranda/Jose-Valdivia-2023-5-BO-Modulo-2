import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY

class Bullet(Sprite):
    BULLET_WIDTH = 10
    BULLET_HEIGHT = 20
    BULLET_PLAYER = pygame.transform.scale(BULLET, (BULLET_WIDTH, BULLET_HEIGHT))
    BULLET_ENEMY = pygame.transform.scale(BULLET_ENEMY, (BULLET_WIDTH, BULLET_HEIGHT))
    BULLETS = {'player': BULLET_PLAYER, 'enemy': BULLET_ENEMY}
    SPEED = 20

    def __init__(self, spaceship):        
        self.image = self.BULLETS[spaceship.type]        
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self):
        if self.owner == 'player':
            self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y)) 