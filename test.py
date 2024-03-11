import os
import time

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map = False  # Добавляем переменную map в класс Player и инициализируем её значением False

def display_map(map_array, player):
    os.system('cls' if os.name == 'nt' else 'clear')  # очистить экран
    for y, row in enumerate(map_array):
        for x, char in enumerate(row):
            if player.x == x and player.y == y:
                print('@', end='')
            elif not player.map and (abs(player.x - x) > 3 or abs(player.y - y) > 3):  # Если карта закрыта и клетка находится далеко от игрока
                print(' ', end='')  # Показываем пустую клетку
            else:
                print(char, end='')
        print()
        time.sleep(0.05)  # добавим небольшую задержку для лучшей анимации

def main():
    layerMapGUI_1 = [
        "               *****************               ",
        "          ****        \          ****          ",
        "       ***             \              ***       ",
        "     **                 \___   ʘ         **     ",
        "    *                       \              *    ",
        "   *                         \              *   ",
        "  *                           \              *  ",
        " *     ₲                       \   ___________* ",
        " *                              \ /           * ",
        "*                                Y             *",
        "*                               /              *",
        "*                              /               *",
        "*                             /       ₩        *",
        "*                            /                 *",
        " *                          /                 * ",
        " *———————ɿ              ___ɺ__________________* ",
        "  *       ‾\___________/                     *  ",
        "   *                                        *   ",
        "    *                                      *    ",
        "     **                  ƒ               **     ",
        "       ***                            ***       ",
        "          ****                    ****          ",
        "               ******************               "
    ]

    player = Player(29, 19)

    while True:
        display_map(layerMapGUI_1, player)
        move = input('Куда вы хотите пойти? (W/A/S/D): ')
        if move.lower() == 'w' and layerMapGUI_1[player.y - 1][player.x] != '*':
            player.y -= 1
        elif move.lower() == 's' and layerMapGUI_1[player.y + 1][player.x] != '*':
            player.y += 1
        elif move.lower() == 'a' and layerMapGUI_1[player.y][player.x - 1] != '*':
            player.x -= 1
        elif move.lower() == 'd' and layerMapGUI_1[player.y][player.x + 1] != '*':
            player.x += 1

if __name__ == "__main__":
    main()
