import pygame
import os

pygame.mixer.init()

# Установка пути к папке со звуковыми файлами
sound_folder = os.path.join(os.path.dirname(__file__), 'sounds')
pygame.mixer.init()

def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(sound_folder, filename))

def play_sound(sound):
    sound.play()

def play_sound_print():
    # Загрузка и воспроизведение звука
    print_sound = load_sound("print.wav")
    play_sound(print_sound)

def play_sound_print2():
    # Загрузка и воспроизведение звука
    print2_sound = load_sound("print2.wav")
    play_sound(print2_sound)

def play_background_music():
    # Загрузка и воспроизведение фоновой музыки
    bg_music = os.path.join(sound_folder, "BGmusic.wav")
    pygame.mixer.music.load(bg_music)
    pygame.mixer.music.play(-1)

def stop_background_music():
    # Остановка фоновой музыки
    pygame.mixer.music.stop()

def play_battle_music():
    # Загрузка и воспроизведение музыки для битвы
    battle_music = os.path.join(sound_folder, "Battle Music.wav")
    pygame.mixer.music.load(battle_music)
    pygame.mixer.music.play(-1)

def stop_battle_music():
    # Остановка музыки для битвы
    pygame.mixer.music.stop()

def play_shop_music():
    # Загрузка и воспроизведение музыки для магазина
    shop_music = os.path.join(sound_folder, "Shop Music.wav")
    pygame.mixer.music.load(shop_music)
    pygame.mixer.music.play(-1)

def stop_shop_music():
    # Остановка музыки для магазина
    pygame.mixer.music.stop()

def play_forest_music():
    # Загрузка и воспроизведение музыки для леса
    forest_music = os.path.join(sound_folder, "Forest Music.wav")
    pygame.mixer.music.load(forest_music)
    pygame.mixer.music.play(-1)

def stop_forest_music():
    # Остановка музыки для леса
    pygame.mixer.music.stop()

if __name__ == "__main__":
    play_background_music()
    input()