import pygame

#from game.components.hearth.heart import Hearts
from game.components.sounds_game.sounds_manager import SoundsManager

from game.utils.constants import SCREEN_HEIGHT, SHIELD_TYPE

class BulletManager():
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.bullet_sound = SoundsManager()        
        #self.heart = Hearts()

    def update(self, game):
        #--> Control bala enemiga.        
        for bullet in self.enemy_bullets:
            bullet.update()
            if bullet.rect.y >= SCREEN_HEIGHT:
                self.enemy_bullets.remove(bullet)

            if bullet.rect.colliderect(game.player.rect) and (bullet.owner == 'enemy'):
                self.enemy_bullets.remove(bullet)
                if self.hearts_total == 0:
                    game.playing = False
                    game.death_count += 1
                elif (game.player.power_up_type != SHIELD_TYPE):                    
                    game.hearts_total -= 1                                     

        #-->Control bala del jugador.
        for bullet in self.player_bullets:
            bullet.update()
            if bullet.rect.y < 0:
                self.player_bullets.remove(bullet)

            #-->Control impacto de la bala del jugador contra el enemigo.
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.bullet_sound.explocion_sound()                    
                    game.enemy_manager.enemies.remove(enemy)
                    game.update_score()
                    self.player_bullets.remove(bullet)        

            #-->Control impacto de la bala del jugador contra el asteroide.
            for asteroid in game.enemy_manager.asteroids:
                if bullet.rect.colliderect(asteroid.image_rotate_rect) and bullet.owner == 'player':
                    self.bullet_sound.explocion_sound()
                    game.enemy_manager.asteroids.remove(asteroid)
                    game.update_score()
                    self.player_bullets.remove(bullet)

    def draw(self, screen):              
        for bullet in self.enemy_bullets:            
            bullet.draw(screen)

        for bullet in self.player_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):        
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
            self.bullet_sound.enemy_bullet_sound()
        elif bullet.owner == 'player' and len(self.player_bullets) < 1:
            self.bullet_sound.player_bullet_sound()
            self.player_bullets.append(bullet)                

    def reset_bullet(self):        
        self.enemy_bullets = []
        self.player_bullets = []       