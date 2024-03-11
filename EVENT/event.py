import math
import sys
import os
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))

import DATA.monster_data as md
import DATA.data_persons as dp
import DATA.data as d
import random

chances = [60, 40]


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

    d.create_table("info", True, None, {0 : "center"}, 40, f"on your way you met a {monster_name}")

    input("> ")
    d.da.stop_background_music()
    d.da.play_battle_music()

    while d.batle:
        d.create_table("info", True, [0], {0 : "center"}, 25, f"{monster_name}", f"HP : {monster_Hp}", f"DAMAGE : {monster_Damage}")

        d.create_table("info", False, [0, 2], {0 : "center"}, 25, f"{d.name}", f"HP : {d.Hp}", f"DAMAGE : {d.Dm}", f"1, attack {monster_name}", "2, run")

        dest = input("> ")

        if dest == "1":
            if d.heroClass == "SWORDSMAN":
                monster_Hp = monster_Hp - math.ceil(d.Dm * monster_PResist)
            elif d.heroClass == "THIEF":
                monster_Hp = monster_Hp - math.ceil((d.Dm * monster_PResist) *2)
            elif d.heroClass == "MAGICIAN":
                monster_Hp = monster_Hp - math.ceil(d.Dm * monster_MResist)
            elif d.heroClass == "NULL":
                monster_Hp = monster_Hp - 5 - d.Dm
            
            if monster_Hp < 0:
                monster_Hp = 0

            d.create_table("info", True, None, {0 : "center"}, 45, f"you hit the {monster_name}, he has {monster_Hp} HP" )
            input("> ")

        elif dest == "2":
            if random.random() > monster_agresia :
                d.create_table("info", True, [0], {0 : "center"}, 25, "you runs away", "gold : 0", "XP : 0")
                d.batle = False
                input("")
                break
            else:
                d.create_table("info", True, None, {0 : "center"}, 25, "you couldn't escape" )
                input("> ")
        
        if monster_Hp <= 0:

            if d.EarningCoinsAndXP:
                monster_Xp = monster_Xp * 2
                monster_Coin = monster_Coin * 2

                d.Xp = d.Xp + monster_Xp
                d.gold = d.gold + monster_Coin
                d.create_table("info", True, [0], {0 : "center"}, 25, f"VICTORY", f"gold : {monster_Coin}", f"XP : {d.Xp}/{d.XpToLv}")

                if d.Xp >= d.XpToLv:
                    d.Lv = d.Lv + 1
                    d.Xp = d.Xp - d.XpToLv
                    d.XpToLv = d.XpToLv + 100

                    
                    d.maxHp = d.maxHp + 50
                    d.Hp = d.maxHp
                    d.improvementStar = d.improvementStar + 1
                    d.create_table("info", False, [0], {0 : "center"}, 25, f"NEW LEVEL", f"HP : {d.maxHp}", f"XP : {d.Xp}/{d.XpToLv}", f"improvement star : {d.improvementStar}")
                input("> ")
                d.batle = False
                break
            else:

                d.Xp = d.Xp + monster_Xp
                d.gold = d.gold + monster_Coin

                d.create_table("info", True, [0], {0 : "center"}, 25, f"VICTORY", f"gold : {monster_Coin}", f"XP : {monster_Xp}")

                if d.Xp >= d.XpToLv:
                    d.Lv = d.Lv + 1
                    d.Xp = d.Xp - d.XpToLv
                    d.XpToLv = math.ceil(d.XpToLv * 1.5)

                    d.maxHp = math.ceil(d.maxHp * 1.5)
                    d.improvementStar = d.improvementStar + 1
                    d.create_table("info", False, [0], {0 : "center"}, 25, f"NEW LEVEL", f"HP : {d.maxHp}", f"XP : {d.Xp}/{d.XpToLv}", f"improvement star : {d.improvementStar}")
                input("> ")
                d.batle = False
                break
                

        if monster_Hp < 12 and random.random() > monster_agresia :

            d.create_table("info", True, [0], {0 : "center"}, 25, "the monster ran away", "gold : 0", "XP : 0")
            input("> ")
            d.batle = False
            break

        if monster_PDamage == True:
            d.Hp = d.Hp - math.ceil(monster_Damage * d.PhysicalResistInt)
        elif monster_MDamage == True:
            d.Hp = d.Hp - math.ceil(monster_Damage * d.MagicResistInt)
        
        if d.Hp <=0 :
            d.game_over = True
            break
    d.da.stop_battle_music()
    d.da.play_background_music()

def shop():
    shop_type = random.choice(d.shop_types)
    nearStore = True

    while nearStore:
        d.create_table("info", True, [0], {0 : "center"}, 40, f"this is an {shop_type} shop", "0, move on", "1, go inside")

        dest = input("> ")

        if dest == "0":
            nearStore = False
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
                    random_items = random.sample(dp.alchemical_items, 3)

                    item1 = random_items[0]
                    item2 = random_items[1]
                    item3 = random_items[2]

                    gold_item1 = random.randint(item1["mingold"], item1["maxgold"])
                    gold_item2 = random.randint(item2["mingold"], item2["maxgold"])
                    gold_item3 = random.randint(item3["mingold"], item3["maxgold"])

                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases}")
                    d.shop = True
                    input("> ")

                    while d.shop:
                        d.create_table("info", True, [0, 1, 4], {0 : "center"}, 35, "alchemy",
                                                                                f"gold : {d.gold}",
                                                                                f"1, {item1['name']}  | {gold_item1} gold",
                                                                                f"2, {item2['name']}  | {gold_item2} gold",
                                                                                f"3, {item3['name']}  | {gold_item3} gold",
                                                                                "0, exit")
                        dest = input("> ")

                        if dest == "0":
                            phrases_exit = random.choice(dp.alchemist_purchase_exit)
                            d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_exit}")
                            input("> ")
                            nearStore = False
                            break

                        elif dest == "1":
                            if item1['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.alchemist_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item1:
                                    d.gold =- gold_item1
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.alchemist_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"{thank_phrase}")

                                    item1['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.alchemist_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_gold}")
                                    input("")

                        elif dest == "2":
                            if item2['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.alchemist_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item2:
                                    d.gold =- gold_item2
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.alchemist_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"{thank_phrase}")

                                    item2['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.alchemist_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_gold}")
                                    input("")
                        elif dest == "3":
                            if item3['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.alchemist_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item3:
                                    d.gold =- gold_item3
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.alchemist_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"{thank_phrase}")

                                    item3['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.alchemist_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_gold}")
                                    input("")
                        
            else:
                if shop_type == "firearms":
                    phrases = random.choice(dp.blacksmith_phrases)
                    random_items = random.sample(dp.blacksmith_items, 3)

                    item1 = random_items[0]
                    item2 = random_items[1]
                    item3 = random_items[2]

                    gold_item1 = random.randint(item1["mingold"], item1["maxgold"])
                    gold_item2 = random.randint(item2["mingold"], item2["maxgold"])
                    gold_item3 = random.randint(item3["mingold"], item3["maxgold"])

                    d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases}")
                    d.shop = True
                    input("> ")
                    
                    while d.shop:
                        d.create_table("info", True, [0, 3], {0 : "center"}, 35, "blacksmith", f"1, {item1['name']}  | {gold_item1} gold",
                                                                                            f"2, {item2['name']}  | {gold_item2} gold",
                                                                                            f"3, {item3['name']}  | {gold_item3} gold",
                                                                                            "0, exit")
                        dest = input("> ")

                        if dest == "0":
                            phrases_exit = random.choice(dp.blacksmith_purchase_exit)
                            d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_exit}")
                            input("> ")
                            nearStore = False
                            break

                        elif dest == "1":
                            if item1['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.blacksmith_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item1:
                                    #доделать как зделаю инвентарь
                                    thank_phrase = random.choice(dp.blacksmith_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "blacksmith", f"{thank_phrase}")

                                    item1['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.blacksmith_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_no_gold}")
                                    input("")

                        elif dest == "2":
                            if item2['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.blacksmith_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item2:
                                    d.gold =- gold_item2
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.blacksmith_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "blacksmith", f"{thank_phrase}")

                                    item2['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.blacksmith_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_no_gold}")
                                    input("")
                        elif dest == "3":
                            if item3['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.blacksmith_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item3:
                                    d.gold =- gold_item3
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.blacksmith_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "blacksmith", f"{thank_phrase}")

                                    item3['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.blacksmith_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "blacksmith", f"{phrases_no_gold}")
                                    input("")

                elif shop_type == "alchemy":
                    phrases = random.choice(dp.alchemist_phrases)
                    random_items = random.sample(dp.alchemical_items, 3)

                    item1 = random_items[0]
                    item2 = random_items[1]
                    item3 = random_items[2]

                    gold_item1 = random.randint(item1["mingold"], item1["maxgold"])
                    gold_item2 = random.randint(item2["mingold"], item2["maxgold"])
                    gold_item3 = random.randint(item3["mingold"], item3["maxgold"])

                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases}")
                    d.shop = True
                    input("> ")
                    
                    while d.shop:
                        d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"1, {item1['name']}  | {gold_item1} gold",
                                                                                            f"2, {item2['name']}  | {gold_item2} gold",
                                                                                            f"3, {item3['name']}  | {gold_item3} gold",
                                                                                            "0, exit")
                        dest = input("> ")

                        if dest == "0":
                            phrases_exit = random.choice(dp.alchemist_purchase_exit)
                            d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_exit}")
                            input("> ")
                            nearStore = False
                            break

                        elif dest == "1":
                            if item1['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.alchemist_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item1:
                                    #доделать как зделаю инвентарь
                                    thank_phrase = random.choice(dp.alchemist_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"{thank_phrase}")

                                    item1['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.alchemist_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_gold}")
                                    input("")

                        elif dest == "2":
                            if item2['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.alchemist_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item2:
                                    d.gold =- gold_item2
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.alchemist_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"{thank_phrase}")

                                    item2['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.alchemist_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_gold}")
                                    input("")
                        elif dest == "3":
                            if item3['name'] == "1, --------":
                                phrases_no_produkt = random.choice(dp.alchemist_phrases_no_product)
                                d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_produkt}")
                                input("")
                            else:
                                if d.gold >= gold_item3:
                                    d.gold =- gold_item3
                                    d.item.append(item1['name'])
                                    thank_phrase = random.choice(dp.alchemist_purchase_phrases)
                                    d.create_table("info", True, [0, 3], {0 : "center"}, 35, "alchemy", f"{thank_phrase}")

                                    item3['name'] = "1, --------"
                                else:
                                    phrases_no_gold = random.choice(dp.alchemist_purchase_no_gold)
                                    d.create_table("info", True, [0], {0 : "center"}, 35, "alchemy", f"{phrases_no_gold}")
                                    input("")

    d.da.stop_shop_music()
    d.da.play_background_music()

def randomEvent():
    # Выбираем случайное событие на основе текущих шансов
    event = random.choices([1, 2], weights=chances, k=1)[0]

    # Печатаем выбранное событие
    if event == 1:
        monster()
        # Изменяем шансы для следующего события
        chances[0] = max(0, chances[0] - 10)  # Уменьшаем шансы для события 1 на 10
        chances[1] = min(100, chances[1] + 10)  # Увеличиваем шансы для события 2 на 10
    else:
        shop()
        # Изменяем шансы для следующего события
        chances[0] = min(100, chances[0] + 10)  # Увеличиваем шансы для события 1 на 10
        chances[1] = max(0, chances[1] - 10)  # Уменьшаем шансы для события 2 на 10

def openInventory():
    d.clear()

    print("жду @nikmen2045 ")

    input("> ")

if __name__ == "__main__":
    
    shop()