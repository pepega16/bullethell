import pygame

def PlaySound(sound_file_name, channel, flag = 0):
    '''Функция предназначенна для проигрывания аудиозаписиб принимает назание файла, канал и флаг'''
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound('Sound/' + sound_file_name),flag)
    pygame.mixer.Channel(channel).set_volume(.25)
    