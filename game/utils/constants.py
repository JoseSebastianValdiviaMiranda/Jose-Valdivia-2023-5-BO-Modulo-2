import pygame
import os
pygame.mixer.init()
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

#-->Constantes, Sonidos del juego.
SPACE_SOUND = pygame.mixer.Sound("game/assets/Sounds/space_sound.mp3")
BULLET_PLAYER_SOUND = pygame.mixer.Sound("game/assets/Sounds/bullet_player_sound.mp3")
BULLET_ENEMY_SOUND = pygame.mixer.Sound("game/assets/Sounds/bullet_enemy_sound.mp3")
POWER_UP_SOUND = pygame.mixer.Sound("game/assets/Sounds/powerup_sound.mp3")
EXPLOCION_SOUND = pygame.mixer.Sound("game/assets/Sounds/sound_explocion.mp3")

#-->Constantes, detalles del mundo.
PLANET_EARTH = pygame.image.load(os.path.join(IMG_DIR, "Planets/Earth.png"))
MOON = pygame.image.load(os.path.join(IMG_DIR, "Planets/Moon.png"))
ASTEROID = pygame.image.load(os.path.join(IMG_DIR, "Planets/Asteroid.png"))

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
HEART_RED = pygame.image.load(os.path.join(IMG_DIR, "Planets/hearth.png"))
HEART_SIZE = pygame.transform.scale(HEART_RED, (40, 40))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
