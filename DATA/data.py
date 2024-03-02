import os

# Очистка экрана
def clear():
    os.system("cls")

clear()

import time
import random
import DATA.audio.data_audio as da
import json
import pyautogui
import ctypes

# Инициализация переменных
room_types, chances, num_rooms, num_each_type = ["Monster", "Altar", "Shop", "Meadow"] ,[10, 5, 20, 10], 20, [1, 1, 3, 1]

shop_types = ["firearms", "alchemy"]

#                                                                                               run   meny  play   autor  skipE  errorL  CH   batl   GO     SH   data
run, meny, play, autors, skip_enter, errore_load, creating_hero, batle, game_over, shop, data = True, True, False, False, False, False, True, True, False, False, {}

#                                                                                                       DP     MR     PhyR     PR    TR    ManaR  ECAXP
DoublePunch, MagicResist, PhysicalResist, PoisonResist, ToxinResist, ManaRecovery, EarningCoinsAndXP = False, False, False, False, False, False, False

#                                                                    MRI  PRI  poiRI TRI
MagicResistInt, PhysicalResistInt, PoisonResistInt, ToxinResistInt = 1.8, 1.8, 1.8,  1.8 

#                                                                               name    class   Dm  HP  mHP G  XP XTL L  IS P
name, heroClass, Dm, Hp, maxHp, gold, Xp, XpToLv, Lv, improvementStar, points = "NULL", "NULL", 20, 70, 70, 0, 0, 10, 0, 0, 0

#                                          item H  CH  WE1 WE2
item, helmet, chestplate, weapon, weapon2 = [], "", "", "", ""

room_map = []

hdl = ctypes.windll.kernel32.GetStdHandle(-11)

logo = [
    "▄▄▄█████▓ █     █░ ██▓ ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓    ▄████▄   ██░ ██  ██▀███   ▒█████   ███▄    █  ██▓ ▄████▄   ██▓    ▓█████   ██████",
    "▓  ██▒ ▓▒▓█░ █ ░█░▓██▒▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒   ▒██▀ ▀█  ▓██░ ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▀ ▀█  ▓██▒    ▓█   ▀ ▒██    ▒",
    "▒ ▓██░ ▒░▒█░ █ ░█ ▒██▒▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░   ▒▓█    ▄ ▒██▀▀██░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██▒▒▓█    ▄ ▒██░    ▒███   ░ ▓██▄",
    "░ ▓██▓ ░ ░█░ █ ░█ ░██░▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░    ▒▓▓▄ ▄██▒░▓█ ░██ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░██░▒▓▓▄ ▄██▒▒██░    ▒▓█  ▄   ▒   ██▒",
    "  ▒██▒ ░ ░░██▒██▓ ░██░░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░    ▒ ▓███▀ ░░▓█▒░██▓░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░██░▒ ▓███▀ ░░██████▒░▒████▒▒██████▒▒",
    "  ▒ ░░   ░ ▓░▒ ▒  ░▓  ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░      ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░",
    "    ░      ▒ ░ ░   ▒ ░░ ░ ▒  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░         ░  ▒    ▒ ░▒░ ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░  ▒   ░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░",
    "  ░        ░   ░   ▒ ░  ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░         ░         ░  ░░ ░  ░░   ░ ░ ░ ░ ▒     ░   ░ ░  ▒ ░░          ░ ░      ░   ░  ░  ░",
    "             ░     ░      ░  ░ ░        ░  ░  ░  ░            ░ ░       ░  ░  ░   ░         ░ ░           ░  ░  ░ ░          ░  ░   ░  ░      ░",
    "                                                              ░                                                 ░"
]

# Генерация карты
def generate_map():
    map_size = 20
    room_map = []

    max_monster_count_in_row = random.randint(1, 5)
    current_monster_count = 0

    while True:
        first_room_type = random.choice(room_types)
        if first_room_type not in ["Meadow", "Altar"]:
            room_map.append(first_room_type)
            break

    for _ in range(map_size - 2):
        last_room_type = room_map[-1]

        if last_room_type == "Monster" and current_monster_count < max_monster_count_in_row:
            room_type = "Monster"
            current_monster_count += 1
        else:
            available_types = [rtype for rtype in room_types if rtype != last_room_type]
            room_type = random.choice(available_types)

            if room_type == "Monster":
                current_monster_count = 1
            else:
                current_monster_count = 0

        room_map.append(room_type)

    return room_map

room_map = generate_map()

# Функции сохранения и загрузки данных
def saveFile():
    global name, heroClass, Hp, maxHp, gold, Dm, Xp, XpToLv, Lv, DoublePunch, MagicResist, \
           PhysicalResist, PoisonResist, ToxinResist, MagicResistInt, PhysicalResistInt, PoisonResistInt, \
           ToxinResistInt, ManaRecovery, EarningCoinsAndXP, improvementStar, room_map, points, data, item, \
           helmet, chestplate, weapon, weapon2

    data = {
        "name": name,
        "heroClass": heroClass,
        "Hp": Hp,
        "maxHp": maxHp,
        "gold": gold,
        "Dm": Dm,
        "Xp": Xp,
        "XpToLv": XpToLv,
        "Lv": Lv,
        "DoublePunch": DoublePunch,
        "MagicResist": MagicResist,
        "PhysicalResist": PhysicalResist,
        "PoisonResist": PoisonResist,
        "ToxinResist": ToxinResist,
        "MagicResistInt": MagicResistInt,
        "PhysicalResistInt": PhysicalResistInt,
        "PoisonResistInt": PoisonResistInt,
        "ToxinResistInt": ToxinResistInt,
        "ManaRecovery": ManaRecovery,
        "EarningCoinsAndXP": EarningCoinsAndXP,
        "improvementStar": improvementStar,
        "room_map": room_map,
        "points": points,
        "item": item,
        "helmet": helmet, 
        "chestplate": chestplate, 
        "weapon": weapon, 
        "weapon2": weapon2
    }

    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)


def loadFile():
    global errore_load, name, heroClass, Hp, maxHp, gold, Dm, Xp, XpToLv, Lv, DoublePunch, MagicResist, \
           PhysicalResist, PoisonResist, ToxinResist, MagicResistInt, PhysicalResistInt, PoisonResistInt, \
           ToxinResistInt, ManaRecovery, EarningCoinsAndXP, improvementStar, room_map, points, item, \
           helmet, chestplate, weapon, weapon2

    try:
        with open("save.json", "r") as f:
            data = json.load(f)

        # Проверка наличия всех необходимых ключей в загруженных данных
        required_keys = ["name", "heroClass", "Hp", "maxHp", "gold", "Dm", "Xp", "XpToLv", "Lv", "DoublePunch",
                         "MagicResist", "PhysicalResist", "PoisonResist", "ToxinResist", "MagicResistInt",
                         "PhysicalResistInt", "PoisonResistInt", "ToxinResistInt", "ManaRecovery",
                         "EarningCoinsAndXP", "improvementStar", "room_map", "points", "item", "helmet", "chestplate",
                         "weapon", "weapon2"]
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Key '{key}' not found in the loaded data")

        # Присваивание данных из загруженного JSON
        name = data["name"]
        heroClass = data["heroClass"]
        Hp = data["Hp"]
        maxHp = data["maxHp"]
        gold = data["gold"]
        Dm = data["Dm"]
        Xp = data["Xp"]
        XpToLv = data["XpToLv"]
        Lv = data["Lv"]
        DoublePunch = data["DoublePunch"]
        MagicResist = data["MagicResist"]
        PhysicalResist = data["PhysicalResist"]
        PoisonResist = data["PoisonResist"]
        ToxinResist = data["ToxinResist"]
        MagicResistInt = data["MagicResistInt"]
        PhysicalResistInt = data["PhysicalResistInt"]
        PoisonResistInt = data["PoisonResistInt"]
        ToxinResistInt = data["ToxinResistInt"]
        ManaRecovery = data["ManaRecovery"]
        EarningCoinsAndXP = data["EarningCoinsAndXP"]
        improvementStar = data["improvementStar"]
        room_map = data["room_map"]
        points = data["points"]
        item = data["item"]
        helmet = data["helmet"]
        chestplate = data["chestplate"]
        weapon = data["weapon"]
        weapon2 = data["weapon2"]

    except FileNotFoundError:
        create_table("error", True, None, {0: "center"}, 45, "ERROR: File not found. Creating a new one.")
        input("> ")
        errore_load = True
    except json.JSONDecodeError as e:
        create_table("error", True, None, {0: "center"}, 45, "ERROR: Corrupted JSON file.")
        input("> ")
        errore_load = True
    except KeyError as e:
        create_table("error", True, None, {0: "center"}, 45, f"ERROR: Missing key {str(e)}.")
        input("> ")
        errore_load = True

# Функция создания таблицы
def create_table(style="info", use_clear=True, separator_positions=None, alignment=None, table_width=22, *args):

    def separator_up_info():
        print("Xx" + "_" * (table_width + 2) + "xX")

    def separator_centr_info():
        print("||" + "-" * (table_width + 2) + "||")

    def separator_down_info():
        print("Xx" + "¯" * (table_width + 2) + "xX")

    def separator_up_error():
        print(">>>" + "═" * (table_width + 2) + "<<<")

    def separator_centr_error():
        print("!!!" + "-" * (table_width + 2) + "!!!")

    def separator_down_error():
        print(">>>" + "═" * (table_width + 2) + "<<<")

    if use_clear:
        clear()

    if style == "info":
        separator_up_info()
    elif style == "error":
        separator_up_error()
    da.play_sound_print()
    time.sleep(0.1)

    if style == "info":
        for index, row in enumerate(args):
            time.sleep(0.1)

            if len(row) > table_width:
                words = row.split()  # Разбиваем строку на слова
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) + 1 <= table_width:
                        current_line += word + " "
                    else:
                        lines.append(current_line)
                        current_line = word + " "
                lines.append(current_line)
                for line in lines:
                    print("|| {:<{width}} ||".format(line.strip(), width=table_width))
                    da.play_sound_print()  # проигрываем звук после вывода каждой строки
            else:
                if alignment is not None and index in alignment:
                    if alignment[index] == "center":
                        print("|| {:^{width}} ||".format(row, width=table_width))
                    elif alignment[index] == "right":
                        print("|| {:>{width}} ||".format(row, width=table_width))
                else:
                    print("|| {:<{width}} ||".format(row, width=table_width))
                    da.play_sound_print()  # проигрываем звук после вывода каждой строки

            if separator_positions is not None and index in separator_positions:
                separator_centr_info()

    elif style == "error":
        for index, row in enumerate(args):
            time.sleep(0.1)

            if len(row) > table_width:
                words = row.split()
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) + 1 <= table_width:
                        current_line += word + " "
                    else:
                        lines.append(current_line)
                        current_line = word + " "
                lines.append(current_line)
                for line in lines:
                    print("!!! {:<{width}} !!!".format(line.strip(), width=table_width))
                    da.play_sound_print()
            else:
                if alignment is not None and index in alignment:
                    if alignment[index] == "center":
                        print("!!! {:^{width}} !!!".format(row, width=table_width))
                    elif alignment[index] == "right":
                        print("!!! {:>{width}} !!!".format(row, width=table_width))
                else:
                    print("!!! {:<{width}} !!!".format(row, width=table_width))
                    da.play_sound_print()

            if separator_positions is not None and index in separator_positions:
                separator_centr_error()


    time.sleep(0.1)
    if style == "info":
        separator_down_info()
    elif style == "error":
        separator_down_error()
    da.play_sound_print()

def play_animation(frames, delay=0.3):
    clear()
    for frame in frames:
        print(frame)
        da.play_sound_print2()
        time.sleep(delay)

def open_console_fullscreen():
    pyautogui.press('f11')

def set_font_size(size):
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 0
    font.dwFontSize.X = 0
    font.dwFontSize.Y = size
    font.FontFamily = 0
    font.FontWeight = 400
    font.FaceName = "Consolas"

    ctypes.windll.kernel32.SetCurrentConsoleFontEx(hdl, ctypes.c_ulong(False), ctypes.pointer(font))