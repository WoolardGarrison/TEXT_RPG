import pygame

pygame.mixer.init()

def play_sound_print():
    # Загрузка и воспроизведение звука
    print_sound = pygame.mixer.Sound("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/print.wav")
    print_sound.play()

def play_sound_print2():
    # Загрузка и воспроизведение звука
    print2_sound = pygame.mixer.Sound("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/print2.wav")
    print2_sound.play()

def play_background_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/BGmusic.wav")
    pygame.mixer.music.play(-1)

def play_background_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/BGmusic.wav")
    pygame.mixer.music.play(-1)

def stop_background_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/BGmusic.wav")
    pygame.mixer.music.stop()

def play_battle_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/Battle Music.wav")
    pygame.mixer.music.play(-1)

def stop_battle_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/Battle Music.wav")
    pygame.mixer.music.stop()

def play_shop_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/Shop Music.wav")
    pygame.mixer.music.play(-1)

def stop_shop_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/Shop Music.wav")
    pygame.mixer.music.stop()

def play_forest_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/Forest Music.wav")
    pygame.mixer.music.play(-1)

def stop_forest_music():
    # Загрузка и воспроизведение фоновой музыки
    pygame.mixer.music.load("D:/Python/2Dgame/Windows/TextRPG/DATA/audio/Forest Music.wav")
    pygame.mixer.music.stop()

if __name__ == "__main__":
    play_background_music()
    input()