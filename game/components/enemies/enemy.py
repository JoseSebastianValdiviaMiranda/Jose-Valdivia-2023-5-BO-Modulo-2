import random
import pygame

from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]    
    SPEED_Y = 4
    SPEED_X = 5    
    MOV_X = {0:'left', 1:'right'}
    IMAGE = {1: ENEMY_1, 2: ENEMY_2}

    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30, 100]):
        self.image = pygame.transform.scale(self.IMAGE[image], (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))        
        self.rect = self.image.get_rect()              
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]        
        self.rect.y = self.Y_POS
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.type = "enemy"
        self.shooting_time = random.randint(30, 50)
        
    def update(self, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x            
        else:
            self.rect.x += self.speed_x
        self.change_movement()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement(self):
        self.index += 1     
        if (self.index >= self.move_x_for) or (self.rect.right >= SCREEN_WIDTH) or (self.rect.left <= 0):
            if self.movement_x == 'right':
                self.movement_x = 'left'
            elif self.movement_x == 'left':
                self.movement_x = 'right'
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)