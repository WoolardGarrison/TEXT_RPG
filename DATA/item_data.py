# названия предмета = {
#   ID : 1
#   названия : "названия",
#   редкость : "Common"\"Uncommon"\"Rare"\"Epic"\"Legendary",
#   тип : 1 - зелье \ 2 - броня \ 3 - оружие,
#   защита\урон : "защита\урон",
#   указание какая защита\урон (физичиская\мфгичиская),
#   другие показатели по надобности
#}

import data as d

# Health Potion 1-5
Health_Potion_1 = {
    "ID" : 0,
    "name" : "Health Potion I",
    "rarity" : "Common",
    "type" : 1,
}

def HealthPotion_1():
    d.Hp += 10

    if d.Hp > d.maxHp:
        d.Hp = d.maxHp
    
    d.item.remove(Health_Potion_1["ID"])


Health_Potion_2 = {
    "ID" : 1,
    "name" : "Health Potion II",
    "rarity" : "Uncommon",
    "type" : 1,
}

def HealthPotion_2():
    d.Hp += 15

    if d.Hp > d.maxHp:
        d.Hp = d.maxHp
    
    d.item.remove(Health_Potion_2["ID"])


Health_Potion_3 = {
    "ID" : 2,
    "name" : "Health Potion III",
    "rarity" : "Rare",
    "type" : 1,
}

def HealthPotion_3():
    d.Hp += 20

    if d.Hp > d.maxHp:
        d.Hp = d.maxHp
    
    d.item.remove(Health_Potion_3["ID"])


Health_Potion_4 = {
    "ID" : 3,
    "name" : "Health Potion IV",
    "rarity" : "Epic",
    "type" : 1,
}

def HealthPotion_4():
    d.Hp += 25

    if d.Hp > d.maxHp:
        d.Hp = d.maxHp
    
    d.item.remove(Health_Potion_4["ID"])


Health_Potion_5 = {
    "ID" : 4,
    "name" : "Health Potion V",
    "rarity" : "Legendary",
    "type" : 1,
}

def HealthPotion_5():
    d.Hp += 35

    if d.Hp > d.maxHp:
        d.Hp = d.maxHp
    
    d.item.remove(Health_Potion_5["ID"])


# Mana Elixir 1-5
Mana_Elixir_1 = {
    "ID" : 5,
    "name" : "Mana Elixir I",
    "rarity" : "Common",
    "type" : 1,
}

def ManaElixir_1():
    d.mana += 10

    if d.mana > d.maxMana:
        d.mana = d.maxMana
    
    d.item.remove(Mana_Elixir_1["ID"])

Mana_Elixir_2 = {
    "ID" : 6,
    "name" : "Mana Elixir II",
    "rarity" : "Uncommon",
    "type" : 1,
}

def ManaElixir_2():
    d.mana += 20

    if d.mana > d.maxMana:
        d.mana = d.maxMana
    
    d.item.remove(Mana_Elixir_2["ID"])

Mana_Elixir_3 = {
    "ID" : 7,
    "name" : "Mana Elixir III",
    "rarity" : "Rare",
    "type" : 1,
}

def ManaElixir_3():
    d.mana += 30

    if d.mana > d.maxMana:
        d.mana = d.maxMana
    
    d.item.remove(Mana_Elixir_3["ID"])

Mana_Elixir_4 = {
    "ID" : 8,
    "name" : "Mana Elixir IV",
    "rarity" : "Epic",
    "type" : 1,
}

def ManaElixir_4():
    d.mana += 40

    if d.mana > d.maxMana:
        d.mana = d.maxMana
    
    d.item.remove(Mana_Elixir_4["ID"])

Mana_Elixir_5 = {
    "ID" : 9,
    "name" : "Mana Elixir V",
    "rarity" : "Legendary",
    "type" : 1,
}

def ManaElixir_5():
    d.mana += 50

    if d.mana > d.maxMana:
        d.mana = d.maxMana
    
    d.item.remove(Mana_Elixir_5["ID"])


# Strength Tonic 1-5
Strength_Tonic_1 = {
    "ID" : 10,
    "name" : "Strength Tonic I",
    "rarity" : "Common",
    "type" : 1,
}

def StrengthTonic_1():
    d.Effects.append(Strength_Tonic_1["ID"])
    
    d.item.remove(Strength_Tonic_1["ID"])

Strength_Tonic_2 = {
    "ID" : 11,
    "name" : "Strength Tonic II",
    "rarity" : "Uncommon",
    "type" : 1,
}

def StrengthTonic_2():
    d.Effects.append(Strength_Tonic_2["ID"])
    
    d.item.remove(Strength_Tonic_2["ID"])

Strength_Tonic_3 = {
    "ID" : 12,
    "name" : "Strength Tonic III",
    "rarity" : "Rare",
    "type" : 1,
}

def StrengthTonic_3():
    d.Effects.append(Strength_Tonic_3["ID"])
    
    d.item.remove(Strength_Tonic_3["ID"])

Strength_Tonic_4 = {
    "ID" : 13,
    "name" : "Strength Tonic IV",
    "rarity" : "Epic",
    "type" : 1,
}

def StrengthTonic_4():
    d.Effects.append(Strength_Tonic_4["ID"])
    
    d.item.remove(Strength_Tonic_4["ID"])

Strength_Tonic_5 = {
    "ID" : 14,
    "name" : "Strength Tonic V",
    "rarity" : "Legendary",
    "type" : 1,
}

def StrengthTonic_5():
    d.Effects.append(Strength_Tonic_5["ID"])
    
    d.item.remove(Strength_Tonic_5["ID"])





item_use_functions = {
    0: HealthPotion_1,
    1: HealthPotion_2,
    2: HealthPotion_3,
    3: HealthPotion_4,
    4: HealthPotion_5,
    5: ManaElixir_1,
    6: ManaElixir_2,
    7: ManaElixir_3,
    8: ManaElixir_4,
    9: ManaElixir_5,
    10: StrengthTonic_1,
    11: StrengthTonic_2,
    12: StrengthTonic_3,
    13: StrengthTonic_4,
    14: StrengthTonic_5,
}

def use_item(item_id):
    if item_id in item_use_functions:
        item_use_functions[item_id]()
    else:
        print("This item cannot be used.")