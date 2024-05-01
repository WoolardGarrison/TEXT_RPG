import time
import os

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

class layer1():
    Name = ""
    XSpawn, YSpawn = 25, 19  # Координаты точки спауна (ƒ)
    XSettlements, YSettlements = 38, 12  # Координаты первого поселения (₩)
    XBoss, YBoss = 7, 7  # Координаты босса (₲)
    XExit, YExit = 31, 3  # Координаты выхода (ʘ)
    monsterMax = 1


layerMapGUI_2 = [
    "               ******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                        _________**     ",
    "    *                         /           *    ",
    "   *                         /     ʘ       *   ",
    "  *                         /               *  ",
    " *                  _______/                 * ",
    " *          ₩      /                         * ",
    "*                 /                           *",
    "*                /                            *",
    "*          _____/                             *",
    "*\        /              ƒ                    *",
    "* ‾‾‾\   /                                    *",
    " *    ‾‾‾‾‾‾\                                * ",
    " *           ‾‾‾‾\                           * ",
    "  *               \        /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾*  ",
    "   *     ₲          Y‾‾‾‾‾‾                *   ",
    "    *               \                     *    ",
    "     **              |    ₩             **     ",
    "       ***           |               ***       ",
    "          ****       |           ****          ",
    "               *****************               ",
]

class layer2():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87


layerMapGUI_3 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer3():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_4 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer4():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_5 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer5():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_6 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer6():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_7 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer7():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_8 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer8():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_9 = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer9():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 12, 8  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 26, 19  # Координаты второго поселения (₩)
    XBoss, YBoss = 9, 17  # Координаты босса (₲)
    XExit, YExit = 35, 5  # Координаты выхода (ʘ)
    monsterMax = 87

layerMapGUI_cheatcr = [
    "              *******************              ",
    "          ****                   ****          ",
    "       ***                           ***       ",
    "     **                                 **     ",
    "    *                                     *    ",
    "   *                                       *   ",
    "  *                                         *  ",
    " *                                           * ",
    " *                                           * ",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    "*                                             *",
    " *                                           * ",
    " *                                           * ",
    "  *                                         *  ",
    "   *                                       *   ",
    "    *                                     *    ",
    "     **                                 **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layerCheatcr():
    Name = ""
    XSpawn, YSpawn = 25, 12  # Координаты точки спауна (ƒ)

if __name__ == "__main__":
    def clear():
        os.system("cls")
        
    def play_animation(frames, delay=0.3):
        clear()
        for frame in frames:
            print(frame)
            time.sleep(delay)

    play_animation(layerMapGUI_1, 0.3)
    input()