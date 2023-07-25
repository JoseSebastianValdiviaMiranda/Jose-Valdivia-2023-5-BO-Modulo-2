import pygame
from game.components.power_ups.power_up import PowerUps
from game.utils.constants import HEART_RED, DEFAULT_TYPE,HEART_SIZE


class Life(PowerUps):    
    def __init__(self):
        super().__init__(HEART_SIZE, DEFAULT_TYPE)        