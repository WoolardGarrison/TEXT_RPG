import random

class AlchemicalItem:
    def __init__(self, name, max_gold, min_gold):
        self.name = name
        self.max_gold = max_gold
        self.min_gold = min_gold

alchemical_items = [
    AlchemicalItem("Health Potion", 10, 3),
    AlchemicalItem("Mana Elixir", 15, 5),
    AlchemicalItem("Strength Tonic", 20, 8),
    AlchemicalItem("Speed Draught", 18, 6),
    AlchemicalItem("Defense Elixir", 25, 10),
    AlchemicalItem("Experience Booster", 30, 12),
    AlchemicalItem("Poison Vial", 12, 4),
    AlchemicalItem("Alchemical Reagents", 8, 2),
    AlchemicalItem("Essence of Power", 35, 15),
    AlchemicalItem("Elixir of Tranquility", 22, 7),
    AlchemicalItem("Mystic Catalyst", 28, 10),
    AlchemicalItem("Potion of Elemental Resistance", 32, 12),
    AlchemicalItem("Venomous Brew", 20, 6),
    AlchemicalItem("Philosopher's Stone", 50, 20),
    AlchemicalItem("Bottled Lightning", 40, 15),
    AlchemicalItem("Elixir of Shadows", 38, 14),
    AlchemicalItem("Bane Essence", 45, 18),
    AlchemicalItem("Elixir of Wisdom", 42, 16)
]

random_items = random.sample(alchemical_items, 3)

item1 = random_items[0].name
item2 = random_items[1].name
item3 = random_items[2].name

gold_item1 = random.randint(random_items[0].min_gold, random_items[0].max_gold)
gold_item2 = random.randint(random_items[1].min_gold, random_items[1].max_gold)
gold_item3 = random.randint(random_items[2].min_gold, random_items[2].max_gold)

print("Item 1:", item1)
print("Gold Cost for Item 1:", gold_item1)
print()
print("Item 2:", item2)
print("Gold Cost for Item 2:", gold_item2)
print()
print("Item 3:", item3)
print("Gold Cost for Item 3:", gold_item3)
