import DATA.data as d
import EVENT.event as event

d.clear()
d.open_console_fullscreen()
d.set_font_size(23)
d.play_animation(d.logo, 0.3)
d.time.sleep(3)

while d.run:
    
    d.da.play_background_music()

    while d.meny:
        d.clear()

        while d.autors:

            d.create_table("info", True, [0], None, 22, "0, quit to meny", "graphic : Fantomm", "music : Fantomm", "code : Fantomm ; ...", "plot : Факсянь")

            skip_enter = True
            autors = False
            choice = ""

            choiceAutors = input ("# ")
            if choiceAutors == "0":
                break

        d.create_table("info", True, None, None, 22, "1, new game", "2, load game", "3, autors", "0, quit game")

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

                    d.create_table("info", False, None, None, 22, "where do you want to go? (W|A|S|D| Q-qute)")
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

                    d.create_table("info", False, None, None, 29, "where do you want to go? (W|A|S|D|Q-qute|I-inventory|M-monstronomicon)")
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


