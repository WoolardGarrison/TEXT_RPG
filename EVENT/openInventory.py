import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))

import DATA.data as d
import DATA.item_data as itemD

if __name__ == "__main__":
    d.inventory = True

item_ids = d.item

d.open_console_fullscreen()
d.set_font_size(23)

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
        
        while (True):
            d.create_table("info", True, None, {0 : "center"}, 35, "[1] INFO | [2] USE | [3] BACK" )
            choice = input("> ")
            if choice == "1":
                d.create_table("info", True, None, {0 : "center"}, 22, chosen_item["info"] )

            if choice == "2":
                if chosen_item["type"] == 1:
                    itemD.use_potions(chosen_item["ID"])
                input("> ")
                break
            
            if choice == "3":
                break

            input("> ")
    elif choice == "0":
        break