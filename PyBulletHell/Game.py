import pygame
from EnemyHandler import EnemySpawner
from Player import Player
import AudioHandler

class Game:
    
    """ Класс предназначен для главного игрового процесса	"""
    
    caption = 'Bullet Hell'

    display_width = 640
    display_height = 960

    bullets = []

    background_position = 0
    backgorund_speed = 1

    def __init__(self):
    
        """ Этот метод является конструктором класса """
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.caption)
        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        backgorund_sprite = pygame.image.load('Sprites/background.jpg')

        backgorund_sprite1 = pygame.transform.scale(backgorund_sprite, (self.display_width,self.display_height))
        backgorund_sprite2 = pygame.transform.flip(backgorund_sprite1,0,1)

        self.background1 = backgorund_sprite1
        self.background2 = backgorund_sprite2

        self.player = Player((self.display_width/2, self.display_height - 200))
        
        self.enemy_spawner = EnemySpawner(self.display_width - 100, self.display_height - 100)
    
    def GameLoop(self):
        """ Гланый метод игрового цикла """
        game = True

        AudioHandler.PlaySound('Ready.wav',0, -1)

        AudioHandler.PlaySound('Ready.wav', 1)       

        while game:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return

            if self.player_alive() is True:
                self.key_action()
                self.bullets_movement()    
                self.enemy_spawner.spawn()
                self.enemy_spawner.move()
                self.bullets.extend(self.enemy_spawner.Shoot())
                self.check_bullets()
                self.draw_display()
            else:
                self.game_over()
            
            self.restart()

            pygame.display.update()
            self.clock.tick(60)
    
    def player_alive(self):
        """ Этот метод проверяет жив ли игрок """
        return self.player.health > 0

    def check_bullets(self):
        """ Этот метод проверяет коллизию пули с другими объектами
            Коллизия с игроком либо врагом отнимает ему здоровье и пуля удаляется
         """
        for i in self.bullets:
            if i.y <= -200 or i.y >= self.display_height:
                self.bullets.remove(i)
            else:
                if i.if_player is True:
                    collided_enemy = self.check_enemies(i)

                    if collided_enemy is not None:
                        collided_enemy.health -= i.damage

                        if(collided_enemy.health <= 0):
                            self.enemy_spawner.enemies.remove(collided_enemy)
                            self.player.score += 100

                            if collided_enemy.heal is True:
                                self.player.health += i.damage
                                
                            AudioHandler.PlaySound('BigExplode.wav', 2)

                        self.bullets.remove(i)
                else :
                    if i.x >= self.player.x and i.x <= self.player.x + self.player.width \
                        and i.y>= self.player.y and i.y <= self.player.y + self.player.height:
                        self.player.health -= i.damage
                        
                        self.bullets.remove(i)
    
    def check_enemies(self, bullet) :
        """ Этот метод проверяет коллизию пули с врагами """
        for i in self.enemy_spawner.enemies:
            if bullet.x >= i.x and bullet.x <= i.x + i.width \
                    and bullet.y >= i.y and bullet.y <= i.y + i.height:
                return i
        return None

    def restart(self):
        """ Метод нужен для перезапуска игры при нажатии игроком определенной клавиши """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.enemy_spawner.enemies = []
            self.bullets = []
            self.player.reset()            

    def key_action(self):
        """ Метод нужен для взаимодествия игроком с дввижением персонажа """
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and self.player.x > 5:
            self.player.x -= self.player.speed
        if keys[pygame.K_d] and self.player.x < (self.display_width - self.player.width - 5):
            self.player.x += self.player.speed
        if keys[pygame.K_w] and self.player.y > 5:
            self.player.y -= self.player.speed
        if keys[pygame.K_s] and self.player.y < self.display_height - self.player.height - 5:
            self.player.y += self.player.speed

        if self.player.cooldown < 0:
            self.bullets.append(self.player.shoot())
            AudioHandler.PlaySound('Shoot.wav', 1)
        else:
            self.player.cooldown -= 1

    def bullets_movement(self):
        """ Этот метод двигает все пули """
        for i in self.bullets:
            i.move()

    def draw_display(self):
        """ Метод рисует графику """
        height = self.display_height

        if self.background_position <= height:
            self.display.blit(self.background1, (0, self.background_position))
            self.display.blit(self.background2, (0, self.background_position - height))
        elif self.background_position <= height * 2:
            self.display.blit(self.background1, (0, self.background_position - height * 2))
            self.display.blit(self.background2, (0, self.background_position - height))
        else:
            self.background_position = 0

        self.background_position += self.backgorund_speed
        
        self.display.blit(self.player.sprite, (self.player.x, self.player.y))

        for i in self.bullets:
            self.display.blit(i.sprite,(i.x,i.y))

        for i in self.enemy_spawner.enemies:
            self.display.blit(i.sprite,(i.x,i.y))

        self.print_text('Score: ' + str(self.player.score), 20, 20)
        self.print_text('HP: ' + str(self.player.health), self.display_width - 150, 20)
    
    def game_over(self):
        """ Метод рисует графику для конца игры """
        self.display.blit(self.background1, (0, 0))
        self.print_text('SCORE: ' + str(self.player.score), self.display_width/2 - 100, self.display_height/2 - 100)
        self.print_text('Press \"R\" to Restart', self.display_width/2 - 130, self.display_height/2)

    def print_text(self,message, x, y, font_color=(255, 255, 255), font_type='fonts/font.ttf', font_size=40):
        """ Этот метод используется для того, чтобы написать текст на экране, принимает значения текста и координаты """
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.display.blit(text, (x, y))
   