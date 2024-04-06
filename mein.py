import os
import logging
from datetime import datetime

log_folder = 'LOG'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

log_filename = "LOG__{" + current_time + "}__.log"

log_path = os.path.join(log_folder, log_filename)
logging.basicConfig(filename=log_path, level=logging.DEBUG)

try:
    from DATA.data import clear
    clear()

    from DATA.data import loading_animation, open_console_fullscreen, set_font_size

    imports_list = [
        "DATA.data", "EVENT.event", "sys", "time", "DATA.audio.data_audio",
        "json", "pyautogui", "ctypes", "DATA.level_data", "math", "os",
        "DATA.monster_data", "DATA.data_persons", "DATA.item_data", "load scne",
        "random", "sqlite3", "datetime", "threading", "requests",
        "beautifulsoup4", "selenium", "csv", "uuid", "hashlib",
        "socket", "pygame", "pandas", "openpyxl", "matplotlib",
        "pillow", "asyncio", "asyncpg", "xml", "re",
        "multiprocessing", "logging", "urllib", "datetime",
        "glob", "shutil", "zipfile", "argparse", "configparser"
    ]

    open_console_fullscreen()
    set_font_size(22)
    loading_animation(imports_list)

    import DATA.data as d
    import EVENT.event as event

    if d.Language == "US":
        import DATA.Language.US as l
    elif d.Language == "RU":
        import DATA.Language.RU as l
    else:
        import DATA.Language.US as l


    d.play_animation(d.logo, 0.3)
    d.time.sleep(1)

    set_font_size(23)

    while d.run:

        d.da.play_background_music()

        while d.meny:
            d.clear()

            while d.autors:
                d.create_table(
                    "info", 
                    True, 
                    [0], 
                    None, 
                    22,
                    *l.autors
                )


                skip_enter = True
                autors = False
                choice = ""

                choiceAutors = input ("> ")
                if choiceAutors == "0":
                    break

            d.create_table(
                "info",
                True,
                None,
                None,
                22,
                l.meny
            )

            skip_enter = False

            if not skip_enter:
                else_choice = input("> ")

                if else_choice == "1":
                    while d.creating_hero:

                        d.time.sleep(0.1)

                        d.create_table(
                            "info",
                            True,
                            None,
                            None,
                            22,
                            l.name
                        )
                        d.name = input("> ")

                        if len(d.name) > 7:
                            d.create_table(
                                "error",
                                True,
                                None,
                                None,
                                22,
                                l.namaIsLong
                            )

                        elif d.name == "NULL":
                            d.name = " "

                            d.meny = False
                            d.play = True

                            break
                        else:
                            while d.creating_hero:
                                d.create_table(
                                    "info",
                                    True,
                                    [0],
                                    {0:"center"},
                                    22,
                                    *l.classTable
                                
                                )

                                classChoice = input("> ")

                                if classChoice == "q":
                                    d.create_table(
                                        "info",
                                        True,
                                        [0],
                                        {0:"center"},
                                        22,
                                        *l.magicianInfo
                                    )

                                elif classChoice == "w":
                                    d.create_table(
                                        "info",
                                        True,
                                        [0],
                                        {0:"center"},
                                        22,
                                        *l.thiefInfo
                                    )

                                elif classChoice == "e":
                                    d.create_table("info", True, [0, 1], {0:"center"}, 22, "swordsman", "0, quit to meny", "resistance to ", "  physical attacks", "HP : 190", "damage : 30")

                                elif classChoice == "1":

                                    d.meny = False
                                    d.creating_hero = False
                                    d.play = True

                                    d.heroClass = "MAGICIAN"
                                    d.gold = 20
                                    d.Hp = 160
                                    d.maxHpHp = 160
                                    d.Dm = 15
                                    d.MagicResistInt = 0.89
                                    d.ManaRecovery = True
                                    d.maxMana = 160
                                    d.mana = 160
                                    d.speed = 2

                                    break
                                elif classChoice == "2":

                                    d.meny = False
                                    d.creating_hero = False
                                    d.play = True

                                    d.heroClass = "THIEF"
                                    d.gold = 120
                                    d.Hp = 140
                                    d.maxHpHp = 140
                                    d.Dm = 10
                                    d.PoisonResistInt = 0.89
                                    d.ToxinResistInt = 0.89
                                    d.EarningCoinsAndXP = True
                                    d.DoublePunch = True
                                    d.maxMana = 60
                                    d.mana = 60
                                    d.speed = 3

                                    break
                                elif classChoice == "3":

                                    d.meny = False
                                    d.creating_hero = False
                                    d.play = True

                                    d.heroClass = "SWORDSMAN"
                                    d.gold = 10
                                    d.Hp = 190
                                    d.maxHpHp = 190
                                    d.Dm = 30
                                    d.PhysicalResistInt = 0.89
                                    d.maxMana = 20
                                    d.mana = 20
                                    d.speed = 1

                                    break
                                

                elif else_choice == "2":

                    d.loadFile()
                    if not d.errore_load:
                        d.create_table("info", True, None, None, 22, f"welcome back, {d.name}")

                        input("> ")

                        d.meny = False
                        d.play = True

                elif else_choice == "3":
                    d.autors = True

                elif else_choice == "0":
                    quit()

        while d.play:
            d.clear()
            print("\n████████╗███████╗██╗░░██╗████████╗  ██████╗░██████╗░░██████╗░")
            d.da.play_sound_print2()
            d.time.sleep(0.2)
            print("╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝  ██╔══██╗██╔══██╗██╔════╝░")
            d.da.play_sound_print2()
            d.time.sleep(0.2)
            print("░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░  ██████╔╝██████╔╝██║░░██╗░")
            d.da.play_sound_print2()
            d.time.sleep(0.2)
            print("░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░  ██╔══██╗██╔═══╝░██║░░╚██╗")
            d.da.play_sound_print2()
            d.time.sleep(0.2)
            print("░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░  ██║░░██║██║░░░░░╚██████╔╝")
            d.da.play_sound_print2()
            d.time.sleep(0.2)
            print("░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░")
            d.da.play_sound_print2()

            d.saveFile()

            d.create_table("info", False, [1], None, 22, "0, quit to menu", "1, to start", f"name : {d.name}", f"class : {d.heroClass}", f"HP : {d.Hp}", f"gold : {d.gold}", f"XP : {d.Xp} / {d.XpToLv}", f"Lv : {d.Lv}")

            d.time.sleep(0.1)
            dest = input("> ")

            if dest == "0":
                d.meny = True
                d.play = False
                d.saveFile()
                break
            elif dest == "1":
                d.trips = True
                if d.layer == 1:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer1.XSpawn
                        d.Py = d.ld.layer1.YSpawn

                    player = d.Player(d.Px, d.Py)

                    while d.trips:
                        if d.Hp <= 0:
                            d.trips = False
                            d.game_over = True

                        d.display_map(d.ld.layerMapGUI_1, player)

                        d.create_table("info", False, [0], None, 22, "where do you want to go? (W|A|S|D|)", "Q-qute", "I-inventory", "M-monstronomicon")
                        move = input("> ")

                        if move.lower() == 'w' and d.ld.layerMapGUI_1[player.y - 1][player.x] != '*':
                            if player.y < 0:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer1.YSpawn
                                player.x = d.ld.layer1.XSpawn
                            else:
                                player.y -= 1
                                event.randomEvent()

                        elif move.lower() == 's' and d.ld.layerMapGUI_1[player.y + 1][player.x] != '*':
                            if player.y > 22:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer1.YSpawn
                                player.x = d.ld.layer1.XSpawn
                            else:
                                player.y += 1
                                event.randomEvent()

                        elif move.lower() == 'a' and d.ld.layerMapGUI_1[player.y][player.x - 1] != '*':
                            if player.x < 0:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer1.YSpawn
                                player.x = d.ld.layer1.XSpawn
                            else:
                                player.x -= 1
                                event.randomEvent()

                        elif move.lower() == 'd' and d.ld.layerMapGUI_1[player.y][player.x + 1] != '*':
                            if player.x > 48:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer1.YSpawn
                                player.x = d.ld.layer1.XSpawn
                            else:
                                player.x += 1
                                event.randomEvent()

                        elif move.lower() == 'q':
                            d.Px = player.x
                            d.Py = player.y
                            d.saveFile()
                            d.trips = False

                        elif move.lower() == 'i':
                            event.openInventory()

                        elif move.lower() == 'm':
                            if d.playerMonstronomicon == True:
                                pass
                            else:
                                #доделать
                                d.create_table("info", True, None, None, 22, "")

                if d.layer == 2:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer2.XSpawn
                        d.Py = d.ld.layer2.YSpawn

                    player = d.Player(d.Px, d.Py)

                    while d.trips:
                        if d.Hp <= 0:
                            d.trips = False
                            d.game_over = True

                        d.display_map(d.ld.layerMapGUI_2, player)

                        d.create_table("info", False, [0], None, 22, "where do you want to go? (W|A|S|D|)", "Q-qute", "I-inventory", "M-monstronomicon")
                        move = input("> ")

                        if move.lower() == 'w' and d.ld.layerMapGUI_1[player.y - 1][player.x] != '*':
                            if player.y < 0:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer2.YSpawn
                                player.x = d.ld.layer2.XSpawn
                            else:
                                player.y -= 1
                                event.randomEvent()

                        elif move.lower() == 's' and d.ld.layerMapGUI_1[player.y + 1][player.x] != '*':
                            if player.y > 22:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer2.YSpawn
                                player.x = d.ld.layer2.XSpawn
                            else:
                                player.y += 1
                                event.randomEvent()

                        elif move.lower() == 'a' and d.ld.layerMapGUI_1[player.y][player.x - 1] != '*':
                            if player.x < 0:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer2.YSpawn
                                player.x = d.ld.layer2.XSpawn
                            else:
                                player.x -= 1
                                event.randomEvent()

                        elif move.lower() == 'd' and d.ld.layerMapGUI_1[player.y][player.x + 1] != '*':
                            if player.x > 48:
                                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                                player.y = d.ld.layer2.YSpawn
                                player.x = d.ld.layer2.XSpawn
                            else:
                                player.x += 1
                                event.randomEvent()

                        elif move.lower() == 'q':
                            d.Px = player.x
                            d.Py = player.y
                            d.saveFile()
                            d.trips = False

                        elif move.lower() == 'i':
                            event.openInventory()

                        elif move.lower() == 'm':
                            if d.playerMonstronomicon == True:
                                pass
                            else:
                                d.create_table("info", True, None, None, 22, "you don't have a monstronymicon")

                elif d.layer == 3:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_3, 0.2)
                    else:
                        pass

                elif d.layer == 4:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_4, 0.2)
                    else:
                        pass

                elif d.layer == 5:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_5, 0.2)
                    else:
                        pass

                elif d.layer == 6:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_6, 0.2)
                    else:
                        pass

                elif d.layer == 7:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_7, 0.2)
                    else:
                        pass
                    
                elif d.layer == 8:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_8, 0.2)
                    else:
                        pass

                elif d.layer == 9:
                    if d.playerMap == True:
                        d.play_animation(d.ld.layerMapGUI_9, 0.2)
                    else:
                        pass
                    
        while d.game_over:
            d.create_table("info", False, [0, 2], {0 : "center", 1 : "center"}, 25, f"{d.name}", f"point : {d.points}", f"HP : {d.maxHp}", f"damage : {d.Dm}", f"gold : {d.gold}", f"Lv : {d.Lv}")
            input("> ")
            d.play = False
            d.meny = True
            d.game_over = False

except Exception as e:
    # Логирование ошибок
    logging.error(f'ERORRE : |{str(e)}| \n\r', exc_info=True)