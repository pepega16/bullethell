from enum import Enum

class Direction(Enum):
    
     """ Энумиратор прдназначенный для напраления пуль """
     
     UP = 1
     DOWN = -1 

class Bullet:

    """ Класс пули """

    damage = 25
    
    speed = 10

    def __init__(self, spawn_point,sprite, side, if_player = False):
        
        """ Конструктор класса, приниимает параметры точки выстрела, графики пули, направление и выстрел игроком """

        self.x = spawn_point[0]
        self.y = spawn_point[1]
        self.sprite = sprite
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.side = side
        self.if_player = if_player

    def move(self):
        """ Метод двигает пулю в определённом напралвении """
        self.y += -1 * self.side.value * self.speed