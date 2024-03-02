import DATA.data as d
import EVENT.event as event

def process_element(element):
    if element == "Monster":
        event.monster()
        d.create_table("info", True, None, {0 : "center"}, 22, "you win and move on")
        input("> ")
    elif element == "Altar":
        # Ваш код для обработки случая с Altar
        print("Обработка случая с Altar")
        input("> ")
    elif element == "Shop":
        event.shop()
        d.create_table("info", True, None, {0 : "center"}, 22, "you leave the store and move on")
        input("> ")
    elif element == "Meadow":
        # Ваш код для обработки случая с Rest
        print("Обработка случая с Rest")
        input("> ")
    else:
        print("Неизвестный элемент")

d.open_console_fullscreen()
d.set_font_size(23)
d.play_animation_logo(d.logo, 0.3)
d.time.sleep(3)

while d.run:
    
    d.da.play_background_music()

    while d.meny:
        d.clear()

        while d.autors:

            d.create_table("info", True, [0], None, 22, "0, quit to meny", "graphic : Fantomm", "music : Fantomm", "code : Fantomm")

            skip_enter = True
            autors = False
            choice = ""

            choiceAutors = input ("# ")
            if choiceAutors == "0":
                break

        d.create_table("info", True, None, None, 22, "1, new game", "2, load game", "3, autors", "4, quit game")

        skip_enter = False
                
        if not skip_enter:
            else_choice = input("> ")

            if else_choice == "1":
                while d.creating_hero:
                    d.time.sleep(0.1)
                    d.name = input("enter your name\n> ")
                    if len(d.name) > 7:
                        print("!!name is too long, maximum length 7 characters!!")
                    elif d.name == "NULL":
                        d.name = " "

                        d.meny = False
                        d.play = True

                        break
                    else:
                        while d.creating_hero:
                            d.create_table("info", True, [0], {0:"center"}, 22, "class", "1, magician \info 'q'", "2, thief \info 'w'", "3, swordsman \info 'e'")
                            classChoice = input("> ")

                            if classChoice == "q":
                                d.create_table("info", True, [0, 1], {0:"center"}, 22, "magician", "0, quit to meny", "resistance to magic", "mana recovery rate++", "HP : 160", "damage : 15")
                                if input("> ") == "0":
                                    pass

                            elif classChoice == "w":
                                d.create_table("info", True, [0, 1], {0:"center"}, 22, "thief", "0, quit to meny", "poison resistance", "toxin resistance", "higher likelihood of", "  earning coins and XP", "HP : 140", "damage : 10 + DP")
                                if input("> ") == "0":
                                    pass

                            elif classChoice == "e":
                                d.create_table("info", True, [0, 1], {0:"center"}, 22, "swordsman", "0, quit to meny", "resistance to ", "  physical attacks", "HP : 190", "damage : 30")
                                if input("> ") == "0":
                                    pass

                            elif classChoice == "1":

                                d.meny = False
                                d.creating_hero = False
                                d.play = True

                                d.heroClass = "MAGICIAN"
                                d.gold = 20
                                d.Hp = 160
                                d.maxHpHp = 160
                                d.Dm = 15
                                d.MagicResist = True
                                d.ManaRecovery = True

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
                                d.PoisonResist = True
                                d.ToxinResist = True
                                d.EarningCoinsAndXP = True
                                d.DoublePunch = True

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
                                d.PhysicalResist = True

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

            elif else_choice == "4":
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
            for index, element in enumerate(d.room_map):
                print(f"Обработка элемента {index}: {element}")
                process_element(element)

                if d.game_over:
                    d.play = False
                    break
            dest = input("> ")
    
    while d.game_over:
        d.create_table("info", False, [0, 2], {0 : "center", 1 : "center"}, 25, f"{d.name}", f"point : {d.points}", f"HP : {d.maxHp}", f"damage : {d.Dm}", f"gold : {d.gold}", f"Lv : {d.Lv}")
        input("> ")
        d.play = False
        d.meny = True
        d.game_over = False


