import pygame
import BulletHandler
from BulletHandler import Direction 

class Player:
    
    """ Класс персонажа	"""
    width = 90
    height = 90
    health = 100
    speed = 10
    default_cooldown = 20
    cooldown = 0
    
    def __init__(self, spawn_point):
        """ Конструтор для класса, принимает точку возраждения персонажа	"""

        self.spawn_point = spawn_point
        self.x = spawn_point[0]
        self.y = spawn_point[1]

        playe_sprite = pygame.image.load('Sprites/player.png')
        playe_sprite = pygame.transform.scale(playe_sprite, (90,90))
        self.sprite = playe_sprite

        bullet_sprite = pygame.image.load('Sprites/orangebullet.png')
        bullet_sprite = pygame.transform.scale(bullet_sprite, (50,50))
        self.bullet_sprite = bullet_sprite

        self.score = 0

    def reset(self):
        """ Метод для сброса атрибуто персонажа	"""
        self.x = self.spawn_point[0]
        self.y = self.spawn_point[1]
        self.health = 100
        self.score = 0

    def shoot(self):
        """ Метод создаёт пулю для выстрела и возращяет её как объект"""
        self.cooldown = self.default_cooldown
        return BulletHandler.Bullet((self.x + self.width/2 - self.bullet_sprite.get_width()/2 , self.y - 50), self.bullet_sprite, Direction.UP, True)
