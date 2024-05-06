# okokokokok wazzup man

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
    monsterMax = 78


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
    "       ***                  *        ***       ",
    "     **       ₩            *            **     ",
    "    *                     *               *    ",
    "   *     *****************                  *  ",
    "  *     *                            ʘ      *  ",
    " *     ************************              * ",
    " *                             *************** ",
    "*    *******************                      *",
    "*   *                  *         ₲            *",
    "*   ***************    *                      *",
    "*                  **  *                      *",
    "*              ₩     *************            *",
    " *                               *           * ",
    " *                     ******    *           * ",
    "  *   f   *****       *      *    ***********  ",
    "   *******     *     *        *            *   ",
    "    *         *     *          ************    ",
    "     **       ******                    **     ",
    "       ***                           ***       ",
    "          ****                   ****          ",
    "              *******************              ",
]
class layer3():
    Name = ""
    XSpawn, YSpawn = 6, 16  # Координаты точки спауна (ƒ)
    XSettlements_1, YSettlements_1 = 14, 3  # Координаты первого поселения (₩)
    XSettlements_2, YSettlements_2 = 15, 13  # Координаты второго поселения (₩)
    XBoss, YBoss = 32, 9  # Координаты босса (₲)
    XExit, YExit = 37, 5  # Координаты выхода (ʘ)
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