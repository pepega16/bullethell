import Game

import unittest
from unittest.mock import patch
import pygame
class GameTest(unittest.TestCase):

    def test_alive(self):
        """Проверяем работает ли проверка жив ли игрок"""
        game = Game.Game()
        
        self.assertEqual(True, game.player_alive())

        game.player.health = 0
        self.assertEqual(False, game.player_alive())

    @patch('pygame.key.get_pressed')
    def test_reset(self,patch_keys):
        """Проверяем работает ли нажатие на кнопку рестарта игры"""
        game = Game.Game()
        
        patch_keys.return_value = {pygame.K_r : True}

        game.player.health -= 10
        game.player.x -= 100
        game.player.y -= 100
        game.player.score += 100
        game.player.reset()
        
        game.restart()

        
        self.assertEqual(100, game.player.health)
        self.assertEqual(320, game.player.x)
        self.assertEqual(760, game.player.y)
        self.assertEqual(0, game.player.score)
        


if __name__ == '__main__':
    unittest.main(exit=False)