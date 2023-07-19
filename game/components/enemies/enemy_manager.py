import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT

class EnemyManager():
    NUMBER_OF_ENEMIES = 1
    INCREASE_ENEMY = 1

    #--> Naves Enemigas
    #SHIP_ENEMIES = {0:'left', 1:'right'}

    def __init__(self):
        self.enemies = []
        self.index = 0
        #self.move = self.SHIP_ENEMIES[random.randint(0,1)]
    
    def update(self):
        self.add_enemy()        
        for enemy in self.enemies:            
            enemy.update()            
            if enemy.rect.y >= SCREEN_HEIGHT:
                #self.enemies.remove(enemy)
                self.enemies.clear()
                self.INCREASE_ENEMY += self.NUMBER_OF_ENEMIES                 

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.INCREASE_ENEMY:    
            enemy = Enemy()
            self.enemies.append(enemy)          

    #def move_ship_enemy(self):
