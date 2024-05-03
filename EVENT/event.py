import math
import sys
import os
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))

import DATA.monster_data as md
import DATA.data_persons as dp
import DATA.data as d
import random
import DATA.item_data as itemd

chances = [70, 30]


def monster():
    d.batle = True

    random_monster = random.choice(list(md.forest.keys()))

    monster_name = md.forest[random_monster]["name"]
    monster_Hp = md.forest[random_monster]["Hp"]
    monster_Damage = md.forest[random_monster]["Damage"]
    monster_PResist = md.forest[random_monster]["PhysicalResist"]
    monster_MResist = md.forest[random_monster]["MagicResist"]
    monster_PDamage = md.forest[random_monster]["PhysicalDamage"]
    monster_MDamage = md.forest[random_monster]["MagicDamage"]
    monster_PoiResist = md.forest[random_monster]["PoisonResist"]
    monster_agresia = md.forest[random_monster]["agresia"]
    monster_Xp = md.forest[random_monster]["Xp"]
    monster_Coin = md.forest[random_monster]["Coin"]
    monster_speed = md.forest[random_monster]["speed"]

    d.create_table("info", True, None, {0 : "center"}, 40, f"on your way you met a {monster_name}")

    input("> ")
    d.da.stop_background_music()
    d.da.play_battle_music()

    while d.batle:
        d.create_table("info", True, [0], {0: "center"}, 25, f"{monster_name}", f"HP : {monster_Hp}", f"DAMAGE : {monster_Damage}")
        d.create_table("info", False, [0, 2], {0: "center"}, 25, f"{d.name}", f"HP : {d.Hp}", f"DAMAGE : {d.Dm}", f"1, attack {monster_name}", "2, run")
        
        dest = input("> ")

        if dest == "1":
            damage_multiplier = 2 if d.heroClass == "THIEF" else 1

            if d.heroClass == "SWORDSMAN":
                monster_Hp -= math.ceil((d.Dm * damage_multiplier) * monster_PResist)
            elif d.heroClass == "THIEF":
                monster_Hp -= math.ceil((d.Dm * damage_multiplier) * monster_PResist)
            elif d.heroClass == "MAGICIAN":
                monster_Hp -= math.ceil((d.Dm * damage_multiplier) * monster_MResist)
            elif d.heroClass == "NULL":
                monster_Hp -= 5 + d.Dm * damage_multiplier
            
            monster_Hp = max(0, monster_Hp)
            d.create_table("info", True, None, {0: "center"}, 45, f"you hit the {monster_name}, he has {monster_Hp} HP")
            input("> ")

        elif dest == "2":
            if random.random() > monster_agresia or d.speed > monster_speed:
                d.create_table("info", True, [0], {0: "center"}, 25, "you runs away", "gold : 0", "XP : 0")
                d.batle = False
                input("")
                break
            else:
                d.create_table("info", True, None, {0: "center"}, 25, "you couldn't escape")
                input("> ")
        
        if monster_Hp <= 0:
            if d.EarningCoinsAndXP:
                monster_Xp *= 2
                monster_Coin *= 2
                d.Xp += monster_Xp
                d.gold += monster_Coin
                d.create_table("info", True, [0], {0: "center"}, 25, f"VICTORY", f"gold : {monster_Coin}", f"XP : {d.Xp}/{d.XpToLv}")
                if d.Xp >= d.XpToLv:
                    d.Lv += 1
                    d.Xp -= d.XpToLv
                    d.XpToLv = math.ceil(d.XpToLv * 1.5)
                    d.maxHp = math.ceil(d.maxHp * 1.5)
                    d.Hp = d.maxHp
                    d.improvementStar += 1
                    d.Dm += 5
                    d.create_table("info", False, [0], {0: "center"}, 25, f"NEW LEVEL", f"HP : {d.maxHp}", f"XP : {d.Xp}/{d.XpToLv}", f"Damege : {d.Dm}", f"improvement star : {d.improvementStar}")
                input("> ")
                d.batle = False
                break
            else:
                d.Xp += monster_Xp
                d.gold += monster_Coin
                d.create_table("info", True, [0], {0: "center"}, 25, f"VICTORY", f"gold : {monster_Coin}", f"XP : {monster_Xp}")
                if d.Xp >= d.XpToLv:
                    d.Lv += 1
                    d.Xp -= d.XpToLv
                    d.XpToLv = math.ceil(d.XpToLv * 1.5)
                    d.maxHp = math.ceil(d.maxHp * 1.5)
                    d.improvementStar += 1
                    d.Dm += 5
                    d.create_table("info", False, [0], {0: "center"}, 25, f"NEW LEVEL", f"HP : {d.maxHp}", f"XP : {d.Xp}/{d.XpToLv}", f"Damege : {d.Dm}", f"improvement star : {d.improvementStar}")
                input("> ")
                d.batle = False
                break

        if monster_Hp < 12 and random.random() > monster_agresia:
            d.create_table("info", True, [0], {0: "center"}, 25, "the monster ran away", "gold : 0", "XP : 0")
            input("> ")
            d.batle = False
            break

        if monster_PDamage:
            d.Hp -= math.ceil(((monster_Damage * (1 - d.PhysicalResistInt)) * (1 - d.MagicPhysicalResistInt)) * (1 - (d.helmetResistInt + d.chestplateResistInt + d.shieldResistInt)))
            
        elif monster_MDamage:
            d.Hp -= math.ceil(((monster_Damage * (1 - d.MagicResistInt)) * (1 - d.MagicPhysicalResistInt)) * (1 - (d.helmetResistInt + d.chestplateResistInt + d.shieldResistInt)))
        
        if d.Hp <= 0:
            d.game_over = True
            break

    d.da.stop_battle_music()
    d.da.play_background_music()

def visit_shop(shop_type, phrases, items):
    random_items = random.sample(items, 3)
    gold_prices = [random.randint(item["minGold"], item["maxGold"]) for item in random_items]

    d.create_table("info", True, [0], {0: "center"}, 35, shop_type, f"{phrases}")
    d.shop = True
    input("> ")

    while d.shop:
        d.create_table("info", True, [0, 3], {0: "center"}, 35, shop_type, *[f"{i + 1}, {item['name']} | {gold_prices[i]} gold" for i, item in enumerate(random_items)], f"GOLD : {d.gold}", "0, exit")
        dest = input("> ")

        if dest == "0":
            phrases_exit = random.choice(dp.blacksmith_purchase_exit if shop_type == "blacksmith" else dp.alchemist_purchase_exit)
            d.create_table("info", True, [0], {0: "center"}, 35, shop_type, f"{phrases_exit}")
            input("> ")
            return False

        elif dest.isdigit() and 0 < int(dest) <= len(random_items):
            item_index = int(dest) - 1
            if random_items[item_index]['name'] == "--------":
                phrases_no_product = random.choice(dp.blacksmith_phrases_no_product if shop_type == "blacksmith" else dp.alchemist_phrases_no_product)
                d.create_table("info", True, [0], {0: "center"}, 35, shop_type, f"{phrases_no_product}")
                input("> ")
            else:
                if d.gold >= gold_prices[item_index]:
                    d.gold -= gold_prices[item_index]
                    d.item.append(random_items[item_index]['ID'])
                    thank_phrase = random.choice(dp.blacksmith_purchase_phrases if shop_type == "blacksmith" else dp.alchemist_purchase_phrases)
                    d.create_table("info", True, [0, 3], {0: "center"}, 35, shop_type, f"{thank_phrase}")
                    input("> ")

                    random_items[item_index]['name'] = "--------"
                else:
                    phrases_no_gold = random.choice(dp.blacksmith_purchase_no_gold if shop_type == "blacksmith" else dp.alchemist_purchase_no_gold)
                    d.create_table("info", True, [0], {0: "center"}, 35, shop_type, f"{phrases_no_gold}")
                    input("> ")
        else:
            d.create_table("info", True, [0], {0: "center"}, 35, shop_type, "Invalid option. Please try again.")
            input("> ")

    return True


def shop():
    shop_type = random.choice(d.shop_types)
    near_store = True

    while near_store:
        d.create_table("info", True, [0], {0: "center"}, 40, f"this is an {shop_type} shop", "0, move on", "1, go inside")

        dest = input("> ")

        if dest == "0":
            near_store = False
            break
        elif dest == "1":
            d.da.stop_background_music()
            d.da.play_shop_music()

            if d.heroClass == "NULL":
                if shop_type == "firearms":
                    phrases = random.choice(dp.blacksmith_phrases_NULL)
                    d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases}")
                    input("> ")
                    break
                elif shop_type == "alchemy":
                    phrases = random.choice(dp.alchemist_phrases_NULL)
                    visit_shop("alchemy", phrases, itemd.alchemical_items)
                    break
            else:
                if shop_type == "firearms":
                    phrases = random.choice(dp.blacksmith_phrases)
                    visit_shop("blacksmith", phrases, itemd.blacksmith_items)
                    break
                elif shop_type == "alchemy":
                    phrases = random.choice(dp.alchemist_phrases)
                    visit_shop("alchemy", phrases, itemd.alchemical_items)
                    break

    d.da.stop_shop_music()
    d.da.play_background_music()


def randomEvent(monstr_max):
    event = random.choices([1, 2], weights=chances, k=1)[0]

    if event == 1 and monstr_max > 0:
        monster()
        chances[0] = max(0, chances[0] - 5)  # Уменьшаем шансы для события 1 на 10
        chances[1] = min(100, chances[1] + 10)  # Увеличиваем шансы для события 2 на 10
        monstr_max =- 1
    else:
        shop()
        # Изменяем шансы для следующего события
        chances[0] = min(100, chances[0] + 10)  # Увеличиваем шансы для события 1 на 10
        chances[1] = max(0, chances[1] - 10)  # Уменьшаем шансы для события 2 на 10
    return monstr_max

def openInventory():
    d.clear()
    d.inventory = True
    item_ids = d.item

    while d.inventory:

        matching_classes_names = []
        matching_classes = {}

        item_index = 1

        # Перебираем все ID предметов
        for item_id in item_ids:
            for class_item in itemd.all_item:
                if item_id == class_item["ID"]:
                    matching_classes[item_index] = class_item

                    matching_classes_names.append(f"{class_item['name']} | {item_index}")

                    item_index += 1
                    break

        d.create_table("info", True, [0], {0 : "center"}, 45, "inventory", *matching_classes_names )
        d.create_table("info", False, None, None, 15, "0, - exit")

        choice = input("> ")
        
        if choice.isdigit() and int(choice) in matching_classes:
            chosen_item = matching_classes[int(choice)]
            
            while (True):
                d.create_table("info", True, None, {0 : "center"}, 35, "[1] INFO | [2] USE | [3] BACK" )
                choice = input("> ")
                if choice == "1":
                    d.create_table("info", True, None, {0 : "center"}, 22, chosen_item["info"] )

                if choice == "2":

                    if chosen_item["type"] == 1:
                        itemd.use_potions(chosen_item["ID"])
                    
                    elif chosen_item["type"] == 2:
                        d.helmetResistInt = chosen_item["Physical_Resist"]
                        d.helmet = chosen_item["name"]
                        d.helmetID =chosen_item["ID"]
                        d.item.remove(chosen_item["ID"])

                    elif chosen_item["type"] == 3:
                        d.chestplateResistInt = chosen_item["Physical_Resist"]
                        d.chestplate = chosen_item["name"]
                        d.chestplateID =chosen_item["ID"]
                        d.item.remove(chosen_item["ID"])

                    elif chosen_item["type"] == 4:
                        if d.heroClass == "SWORDSMAN":
                            d.Dm += chosen_item["damage"]
                            d.weapon = chosen_item["name"]
                            d.weaponID =chosen_item["ID"]
                            d.item.remove(chosen_item["ID"])
                        else:
                            d.create_table("info", True, None, {0 : "center"}, 35, "this weapon is not suitable for you" )

                    elif chosen_item["type"] == 5:
                        if  d.heroClass == "THIEF":
                            while True:
                                d.create_table("info", True, None, {0 : "center", 1 : "center"}, 35, "Which hand should I take the dagger in?", "[1] left | [2] right")
                                choice = input("> ")
                                if choice == "1":
                                    d.Dm += chosen_item["damage"]
                                    d.weapon = chosen_item["name"]
                                    d.weaponID =chosen_item["ID"]
                                    d.item.remove(chosen_item["ID"])
                                elif choice == "2":
                                    d.Dm += chosen_item["damage"]
                                    d.weapon2 = chosen_item["name"]
                                    d.weapon2ID =chosen_item["ID"]
                                    d.item.remove(chosen_item["ID"])
                        else:
                            d.create_table("info", True, None, {0 : "center"}, 35, "this weapon is not suitable for you" )

                    elif chosen_item["type"] == 6:
                        if d.heroClass == "MAGICIAN":
                            d.Dm += chosen_item["damage"]
                            d.weapon = chosen_item["name"]
                            d.weaponID = chosen_item["ID"]
                            d.maxMana += chosen_item["mana"]
                            d.item.remove(chosen_item["ID"])
                        else:
                            d.create_table("info", True, None, {0 : "center"}, 35, "this weapon is not suitable for you" )
                    
                    elif chosen_item["type"] == 7:
                        if d.heroClass == "SWORDSMAN":
                            d.shieldResistInt = chosen_item["Physical_Resist"]
                            d.weapon2 = chosen_item["name"]
                            d.weapon2ID =chosen_item["ID"]
                            d.item.remove(chosen_item["ID"])
                        else:
                            d.create_table("info", True, None, {0 : "center"}, 35, "this weapon is not suitable for you" )


                    input("> ")
                    break
                
                if choice == "3":
                    break

                input("> ")
        elif choice == "0":
            break

def start_game(leyer, player):
    if leyer == 1:
        map = d.ld.layerMapGUI_1
        Leyer = d.ld.layer1

    elif leyer == 2:
        map = d.ld.layerMapGUI_2
        Leyer = d.ld.layer2

    elif leyer == 3:
        map = d.ld.layerMapGUI_3
        Leyer = d.ld.layer3

    elif leyer == 4:
        map = d.ld.layerMapGUI_4
        Leyer = d.ld.layer4

    elif leyer == 5:
        map = d.ld.layerMapGUI_5
        Leyer = d.ld.layer5

    elif leyer == 6:
        map = d.ld.layerMapGUI_6
        Leyer = d.ld.layer6

    elif leyer == 7:
        map = d.ld.layerMapGUI_7
        Leyer = d.ld.layer7

    elif leyer == 8:
        map = d.ld.layerMapGUI_8
        Leyer = d.ld.layer8

    elif leyer == 9:
        map = d.ld.layerMapGUI_9
        Leyer = d.ld.layer9

    else:
        map = d.ld.layerMapGUI_cheatcr
        Leyer = d.ld.layer1

    while d.trips:
        if d.game_over:
            d.trips = False
            break

        d.display_map(map, player)

        d.create_table("info", False, [0], None, 22, "where do you want to go? (W|A|S|D|)", "Q-qute", "I-inventory", "M-monstronomicon")
        move = input("> ")

        if move.lower() == 'w' and map[player.y - 1][player.x] != '*':
            if player.y < 0:
                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                player.y = Leyer.YSpawn
                player.x = Leyer.XSpawn
            else:
                player.y -= 1
                Leyer.monsterMax = randomEvent(Leyer.monsterMax)

        elif move.lower() == 's' and map[player.y + 1][player.x] != '*':
            if player.y > 22:
                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                player.y = Leyer.YSpawn
                player.x = Leyer.XSpawn
            else:
                player.y += 1
                Leyer.monsterMax = randomEvent(Leyer.monsterMax)

        elif move.lower() == 'a' and map[player.y][player.x - 1] != '*':
            if player.x < 0:
                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                player.y = Leyer.YSpawn
                player.x = Leyer.XSpawn
            else:
                player.x -= 1
                Leyer.monsterMax = randomEvent(Leyer.monsterMax)

        elif move.lower() == 'd' and map[player.y][player.x + 1] != '*':
            if player.x > 48:
                d.create_table("erorre", True, None, None, 22, "beyond the bounds of the gaming world")
                player.y = Leyer.YSpawn
                player.x = Leyer.XSpawn
            else:
                player.x += 1
                Leyer.monsterMax = randomEvent(Leyer.monsterMax)

        elif move.lower() == 'q':
            d.Px = player.x
            d.Py = player.y
            d.saveFile()
            d.trips = False

        elif move.lower() == 'i':
            openInventory()

        elif move.lower() == 'm':
            if d.playerMonstronomicon == True:
                pass
            else:
                #доделать
                d.create_table("info", True, None, None, 22, "")

if __name__ == "__main__":
    
    shop()