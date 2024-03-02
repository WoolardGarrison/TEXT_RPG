import time
import os

layer_1 = [
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