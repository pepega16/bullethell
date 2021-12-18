import Player

import unittest

class PlayerTest(unittest.TestCase):
    def test_reset(self):
        """Проверяем работает ли сброс аттрибутов класса игрока"""
        player = Player.Player((0,0))
        player.health -= 10
        player.x -= 100
        player.y -= 100
        player.score += 100
        player.reset()
        
        self.assertEqual(100, player.health)
        self.assertEqual(0, player.x)
        self.assertEqual(0, player.y)
        self.assertEqual(0, player.score)


if __name__ == '__main__':
    unittest.main(exit=False)