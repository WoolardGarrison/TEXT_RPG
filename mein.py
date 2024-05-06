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
    import DATA.Language as l

    if d.Language == "EN":
        l.i18n.set('locale', 'en')
    elif d.Language == "RU":
        l.i18n.set('locale', 'ru')
    else:
        l.i18n.set('locale', 'en')


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
                    l.i18n.t('exit_menu'),
                    l.i18n.t('graphics'),
                    l.i18n.t('music'),
                    l.i18n.t('code'),
                    l.i18n.t('plot'),
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
                l.i18n.t('new_game'),
                l.i18n.t('load_game'),
                l.i18n.t('authors'),
                l.i18n.t('exit_game'),
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
                            {0: "center"},
                            22,
                            l.i18n.t('enter_name'),
                        )
                        d.name = input("> ")

                        if len(d.name) > 7:
                            d.create_table(
                                "error",
                                True,
                                None,
                                None,
                                22,
                                l.i18n.t('name_too_long'),
                            )
                            input("> ")

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
                                    26,
                                    l.i18n.t('class'),
                                    l.i18n.t('magician_button'),
                                    l.i18n.t('thief_button'),
                                    l.i18n.t('swordsman_button'),
                                )

                                classChoice = input("> ")

                                if classChoice == "q":
                                    d.create_table(
                                        "info",
                                        True,
                                        [0, 2],
                                        {0:"center"},
                                        22,
                                        l.i18n.t('magician'),
                                        l.i18n.t('magician_resistance'),
                                        l.i18n.t('magician_mana'),
                                        l.i18n.t('magician_hp'),
                                        l.i18n.t('magician_damage'),
                                    )
                                    input("> ")

                                elif classChoice == "w":
                                    d.create_table(
                                        "info",
                                        True,
                                        [0, 3],
                                        {0:"center"},
                                        22,
                                        l.i18n.t('thief'),
                                        l.i18n.t('thief_poison_resistance'),
                                        l.i18n.t('thief_toxin_resistance'),
                                        l.i18n.t('thief_rewards'),
                                        l.i18n.t('thief_hp'),
                                        l.i18n.t('thief_damage'),
                                    )
                                    input("> ")

                                elif classChoice == "e":
                                    d.create_table(
                                        "info",
                                        True,
                                        [0, 1],
                                        {0:"center"},
                                        22,
                                        l.i18n.t('swordsman'),
                                        l.i18n.t('swordsman_physical_resistance'),
                                        l.i18n.t('swordsman_hp'),
                                        l.i18n.t('swordsman_damage'),
                                    )
                                    input("> ")

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
                        d.create_table(
                            "info",
                            True,
                            None,
                            {0 : "center"},
                            26,
                            l.i18n.t('welcome') + d.name,
                        )

                        input("> ")

                        d.meny = False
                        d.play = True

                elif else_choice == "3":
                    d.autors = True

                elif else_choice == "0":
                    quit()

        while d.play:
            d.play_animation(d.text_rpg_logo, 0.2)

            d.saveFile()

            d.create_table(
                "info",
                False, 
                [1],
                None,
                22,
                l.i18n.t('exit_menu'),
                l.i18n.t('start_game'),
                f"{l.i18n.t('player_name')} {d.name}",
                f"{l.i18n.t('class')} : {d.heroClass}",
                f"HP : {d.Hp}",
                f"{l.i18n.t('player_gold')} : {d.gold}",
                f"XP : {d.Xp} / {d.XpToLv}",
                f"Lv : {d.Lv}"
            )

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

                    event.start_game(1, player)

                if d.layer == 2:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer2.XSpawn
                        d.Py = d.ld.layer2.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(2, player)

                elif d.layer == 3:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer3.XSpawn
                        d.Py = d.ld.layer3.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(3, player)

                elif d.layer == 4:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer4.XSpawn
                        d.Py = d.ld.layer4.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(4, player)

                elif d.layer == 5:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer5.XSpawn
                        d.Py = d.ld.layer5.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(5, player)

                elif d.layer == 6:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer6.XSpawn
                        d.Py = d.ld.layer6.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(6, player)

                elif d.layer == 7:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer7.XSpawn
                        d.Py = d.ld.layer7.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(7, player)
                    
                elif d.layer == 8:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer8.XSpawn
                        d.Py = d.ld.layer8.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(8, player)

                elif d.layer == 9:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layer9.XSpawn
                        d.Py = d.ld.layer9.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(9, player)
                else:
                    d.loadFile()

                    if d.Px == 0 and d.Py == 0:
                        d.Px = d.ld.layerCheatcr.XSpawn
                        d.Py = d.ld.layerCheatcr.YSpawn

                    player = d.Player(d.Px, d.Py)

                    event.start_game(10, player)

                    
        while d.game_over:
            d.create_table("info", True, [0, 2], {0 : "center", 1 : "center"}, 25, f"{d.name}", f"point : {d.points}", f"HP : {d.maxHp}", f"damage : {d.Dm}", f"gold : {d.gold}", f"Lv : {d.Lv}")
            input("> ")
            d.play = False
            d.meny = True
            d.game_over = False

except Exception as e:
    # Логирование ошибок
    logging.error(f'ERORRE : |{str(e)}| \n\r', exc_info=True)