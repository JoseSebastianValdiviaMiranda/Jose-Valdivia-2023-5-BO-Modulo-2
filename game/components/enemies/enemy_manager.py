import random

from game.components.enemies.asteroid import Asteroid
from game.components.enemies.enemy import Enemy
from game.components.sounds_game.sounds_manager import SoundsManager
from game.utils.constants import SCREEN_HEIGHT, SHIELD_TYPE

class EnemyManagers():

    def __init__(self):
        self.enemies_1 = []
        self.asteroids_2 = []
        self.highest_asteroid = random.randint(1, 3)
        self.sounds = SoundsManager()        
        self.control = 0        

    def update(self, game):        
        for enemy in self.enemies:            
            enemy.update(game)            
            if enemy.rect.y >= SCREEN_HEIGHT:                
                self.enemies.remove(enemy)                
            
            if enemy.rect.colliderect(game.player.rect):
                if game.hearts_total == 0:
                    game.death_count += 1
                    game.playing = False
                elif game.player.power_up_type == SHIELD_TYPE:
                    self.sounds.explocion_sound()
                    game.update_score()
                    self.enemies.remove(enemy)
                else:
                    game.hearts_total -= 1
                    self.sounds.explocion_sound()
                    game.update_score()
                    self.enemies.remove(enemy)                    

        for asteroid in self.asteroids:            
            asteroid.update(game)            
            if asteroid.image_rotate_rect.y >= SCREEN_HEIGHT:
                self.highest_asteroid = random.randint(1, 3)
                self.asteroids.remove(asteroid)

            if asteroid.image_rotate_rect.colliderect(game.player.rect):                
                if game.hearts_total == 0:
                    game.death_count += 1
                    game.playing = False
                elif game.player.power_up_type == SHIELD_TYPE:
                    self.highest_asteroid = random.randint(1, 3)
                    self.sounds.explocion_sound()
                    game.update_score()
                    self.asteroids.remove(asteroid)
                else:
                    game.hearts_total -= 1
                    self.highest_asteroid = random.randint(1, 3)
                    self.sounds.explocion_sound()
                    game.update_score()
                    self.asteroids.remove(asteroid)

    def draw(self, screen):       
        for enemy in self.enemies:
            enemy.draw(screen)                        
        for asteroid in self.asteroids:
            asteroid.draw(screen)            

    def add_enemy(self):        
        enemy_type = random.randint(1, 2)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            x_speed = 5
            y_speed = 2
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        
        if len(self.enemies) < 1:            
            self.enemies.append(enemy)        
        elif len(self.asteroids) < self.highest_asteroid:
            asteroid = Asteroid()
            self.asteroids.append(asteroid)       

    def reset(self):
        self.enemies = []
        self.asteroids = []       