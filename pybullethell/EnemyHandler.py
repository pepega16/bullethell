import pygame
import random
import BulletHandler
from BulletHandler import Direction 

class EnemyType:
    
    """ Класс для определения типа врагов	"""
    
    def __init__(self, health, cooldown, speed, sprite, bullet_spite, heal = False):
    
        """ Конструктор для класса, принимает здороввье, время перезарядки, скорость передвижения,
         графику, графику пули и является ли враг лечительным"""

        self.health = health
        self.default_cooldown = cooldown
        self.speed = speed
        self.heal = heal

        playe_sprite = pygame.image.load(sprite)
        playe_sprite = pygame.transform.scale(playe_sprite, (90,90))
        self.sprite = playe_sprite

        bullet = pygame.image.load(bullet_spite)
        bullet = pygame.transform.scale(bullet, (50,50))
        self.bullet_sprite = bullet

class Enemy:
    """ Класс врага """
    width = 90
    height = 90
    x = 0
    y = 0  
    cooldown = 0

    def __init__(self, x, y, other):
        """ Конструктор класса, принимает значения начальной позиции, а так же тип врага """
        self.health = other.health
        self.sprite = other.sprite
        self.default_cooldown = other.default_cooldown
        self.speed = other.speed
        self.heal = other.heal
        self.x = x
        self.y = y
        
        self.bullet_sprite = other.bullet_sprite
    
    def shoot(self):   
        """ Метод создаёт пулю для выстрела и возращяет её как объект"""     
        self.cooldown = self.default_cooldown
        return BulletHandler.Bullet((self.x + self.width/2 - self.bullet_sprite.get_width()/2 , self.y + self.height + 50), self.bullet_sprite, Direction.DOWN)

class EnemySpawner:
    """ Класс для создания врагов"""
    
    enemies = []

    enemy_types = []

    min_cooldown_time = 50 
    max_cooldown_time = 150

    cooldown = 0

    def __init__(self, max_x, max_y):
        """ Конструктор класса, принимает значения минимального и максимального времени между созданием врагов """
        self.max_x = max_x
        self.max_y = max_y
        
        enemy1 = EnemyType(50, 200, 4, 'Sprites/Enemy1.png', 'Sprites/violetbullet.png')
        self.enemy_types.append(enemy1)
        
        enemy2 = EnemyType(75, 100, 2, 'Sprites/Enemy2.png', 'Sprites/redbullet.png')
        self.enemy_types.append(enemy2)

        enemy3 = EnemyType(1, 500, 5, 'Sprites/Heal.png', 'Sprites/geenbullet.png', True)
        self.enemy_types.append(enemy3)

    def spawn(self):
        """ Метод создаёт врага в определённом временном интервале """
        self.cooldown -= 1
        if(self.cooldown <= 0):
            pos_x = random.uniform(0, self.max_x)
            pos_y = -100
            
            type = random.randint(0, self.enemy_types.__len__() - 1)

            enemy = Enemy(pos_x,pos_y,self.enemy_types[type])

            self.enemies.append(enemy)
            
            self.cooldown = random.randint(self.min_cooldown_time,self.max_cooldown_time)

    def move(self):
        """ Метод двигает врага в определённом напралвении """
        for i in self.enemies:
            i.y += i.speed

    def Shoot(self):
        """ Метод нужен для выстрела пули """
        bullets = []
        for i in self.enemies:
            if i.cooldown <= 0:
                bullets.append(i.shoot())
                i.cooldown = i.default_cooldown
            else:
                i.cooldown -= 1
        return bullets
