import os
import time

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def display_map(map_array, player):
    os.system('cls' if os.name == 'nt' else 'clear')  # очистить экран
    for y, row in enumerate(map_array):
        for x, char in enumerate(row):
            if player.x == x and player.y == y:
                print('@', end='')
            else:
                print(char, end='')
        print()
        time.sleep(0.05)  # добавим небольшую задержку для лучшей анимации

def main():
    map_array = [
        "                   *****************               ",
        "              ****        \\          ****          ",
        "           ***             \\              ***       ",
        "         **                 \\___   ʘ         **     ",
        "        *                       \\              *    ",
        "       *                         \\              *   ",
        "      *                           \\              *  ",
        "     *     ௹                      \\   ___________* ",
        "     *                              \\ /           * ",
        "    *                                Y             *",
        "    *                               /              *",
        "    *                              |               *",
        "    *                             /       ₩        *",
        "    *                            /                 *",
        "     *                          /                 * ",
        "     *———————ɿ               __⊥__________________* ",
        "      *       ‾৲———————————✓                     *  ",
        "       *                                         *   ",
        "        *                                       *    ",
        "         **                  ※               **     ",
        "           ***                            ***       ",
        "              ****                    ****          ",
        "                   ******************               "
    ]

    player = Player(29, 19)

    while True:
        display_map(map_array, player)
        move = input('Куда вы хотите пойти? (W/A/S/D): ')
        if move.lower() == 'w' and map_array[player.y - 1][player.x] != '*':
            player.y -= 1
        elif move.lower() == 's' and map_array[player.y + 1][player.x] != '*':
            player.y += 1
        elif move.lower() == 'a' and map_array[player.y][player.x - 1] != '*':
            player.x -= 1
        elif move.lower() == 'd' and map_array[player.y][player.x + 1] != '*':
            player.x += 1

if __name__ == "__main__":
    main()
