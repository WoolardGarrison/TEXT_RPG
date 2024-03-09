import time
import os

layerMapGUI_1 = [
    "                   *****************               ",
    "              ****        \          ****          ",
    "           ***             \              ***       ",
    "         **                 \___   ʘ         **     ",
    "        *                       \              *    ",
    "       *                         \              *   ",
    "      *                           \              *  ",
    "     *     ௹                      \   ___________* ",
    "     *                              \ /           * ",
    "    *                                Y             *",
    "    *                               /              *",
    "    *                              |               *",
    "    *                             /       ₩        *",
    "    *                            /                 *",
    "     *                          /                 * ",
    "     *———————ɿ               __⊥__________________* ",
    "      *       ‾৲———————————✓                     *  ",
    "       *                                        *   ",
    "        *                                      *    ",
    "         **                  ※               **     ",
    "           ***                            ***       ",
    "              ****                    ****          ",
    "                   ******************               "
]
layerMapGUI_2 = [
    "               ******************               ",
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
    "*\        /                                   *",
    "* ‾‾‾\   /                                    *",
    " *    ‾‾‾‾‾‾\                                * ",
    " *           ‾‾‾‾\                           * ",
    "  *               \        /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾*  ",
    "   *     ௹         Y‾‾‾‾‾‾                *   ",
    "    *               \                     *    ",
    "     **              |    ₩             **     ",
    "       ***           |               ***       ",
    "          ****       |           ****          ",
    "               *****************         ",
]

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
    "              *******************               ",
]
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
    "              *******************               ",
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
    "              *******************               ",
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
    "              *******************               ",
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
    "              *******************               ",
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
    "              *******************               ",
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
    "              *******************               ",
]

if __name__ == "__main__":
    def clear():
        os.system("cls")
        
    def play_animation(frames, delay=0.3):
        clear()
        for frame in frames:
            print(frame)
            time.sleep(delay)

    play_animation(layer_1, 0.3)
    input()