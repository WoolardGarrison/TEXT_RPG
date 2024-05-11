import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))

import DATA.data as d
import DATA.item_data as itemD

if __name__ == "__main__":
    d.inventory = True

item_ids = d.item

while d.inventory:

    matching_classes_names = []
    matching_classes = {}

    item_index = 1

    # Перебираем все ID предметов
    for item_id in item_ids:
        for class_item in itemD.all_item:
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
        
        if chosen_item["type"] == 1:
            itemD.use_potions(chosen_item["ID"])

        input("> ")

