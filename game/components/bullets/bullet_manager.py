import pygame

from game.utils.constants import SCREEN_HEIGHT

class BulletManager():
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update()
            if bullet.rect.y >= SCREEN_HEIGHT:
                self.enemy_bullets.remove(bullet)

            if bullet.rect.colliderect(game.player.rect) and (bullet.owner == 'enemy'):
                self.enemy_bullets.remove(bullet)
                game.playing = False

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)            

    def add_bullet(self, bullet):        
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)