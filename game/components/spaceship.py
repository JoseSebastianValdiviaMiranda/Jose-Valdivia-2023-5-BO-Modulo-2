import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import DEFAULT_TYPE, SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class SpaceShip(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SHIP_SPEED = 10
    X_POS = (SCREEN_WIDTH//2) -SPACESHIP_WIDTH//2
    Y_POS = 500

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = "player"
        self.shooting_time = random.randint(30, 50)
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
    
    def update(self, user_input, game):        
        if(user_input[pygame.K_LEFT]):
            self.rect.x -= self.SHIP_SPEED
            if(self.rect.left < 0):                            
                self.rect.right = SCREEN_WIDTH
        elif(user_input[pygame.K_RIGHT]):
            self.rect.x += self.SHIP_SPEED
            if(self.rect.right >= SCREEN_WIDTH):
                self.rect.left = 0
        elif(user_input[pygame.K_UP]):
            if(self.rect.top > (SCREEN_HEIGHT//2)):
                self.rect.y -= self.SHIP_SPEED
        elif(user_input[pygame.K_DOWN]):
            if(self.rect.bottom < SCREEN_HEIGHT):
                self.rect.y += self.SHIP_SPEED        
        elif(user_input[pygame.K_SPACE]):
            self.shoot_player(game)
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def shoot_player(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)

    def set_image(self, size = (SPACESHIP_WIDTH, SPACESHIP_HEIGHT), image = SPACESHIP):
        self.image = image        
        self.image = pygame.transform.scale(self.image, size)
