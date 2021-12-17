import BulletHandler

import unittest
import pygame

class BulletHandlerTest(unittest.TestCase):
    def test_move(self):
        """Проверяем работает ли передвижение пули"""
        bullet_sprite = pygame.image.load('Sprites/orangebullet.png')

        bullet = BulletHandler.Bullet((0,0),bullet_sprite,BulletHandler.Direction.UP)
        
        bullet.move()

        self.assertEqual(-10, bullet.y)


if __name__ == '__main__':
    unittest.main(exit=False)