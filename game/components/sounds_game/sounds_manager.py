import pygame

from game.utils.constants import BULLET_ENEMY_SOUND, BULLET_PLAYER_SOUND, POWER_UP_SOUND, SPACE_SOUND, EXPLOCION_SOUND

class SoundsManager():
    def __init__(self):
        self.control_sound = 0.0

    def space_sound_play(self):
        SPACE_SOUND.set_volume(0.2)
        SPACE_SOUND.play(-1)
    
    def space_sound_stop(self):
        SPACE_SOUND.stop()
        
    def enemy_bullet_sound(self):
        BULLET_ENEMY_SOUND.set_volume(0.05)  
        BULLET_ENEMY_SOUND.play()

    def player_bullet_sound(self):
        BULLET_PLAYER_SOUND.set_volume(0.3)
        BULLET_PLAYER_SOUND.play()       

    def power_up_sound(self):
        POWER_UP_SOUND.set_volume(0.12)
        POWER_UP_SOUND.play()

    def explocion_sound(self):
        EXPLOCION_SOUND.set_volume(0.3)
        EXPLOCION_SOUND.play()