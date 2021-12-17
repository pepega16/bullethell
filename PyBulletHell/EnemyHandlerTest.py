import EnemyHandler

import unittest

class EnemyHandlerTest(unittest.TestCase):
    def test_spawn(self):
        """Проверяем работает ли создание врагов"""
        spawner = EnemyHandler.EnemySpawner(0,0)
        spawner.spawn()
        
        self.assertEqual(1, spawner.enemies.__len__())

        cooldown = spawner.cooldown

        for i in range(cooldown):
            spawner.spawn()
        
        spawner.spawn()

        self.assertEqual(2, spawner.enemies.__len__())



if __name__ == '__main__':
    unittest.main(exit=False)