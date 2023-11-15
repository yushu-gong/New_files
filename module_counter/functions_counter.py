import json
import pandas as pd

combos = pd.read_json('C:\\Users\\Quinn\\Desktop\\py\\New_files\\module_counter\\data\\combos.json')
meals = pd.read_json('C:\\Users\\Quinn\\Desktop\\py\\New_files\\module_counter\\data\\meals.json')

def calories_counter(items, meals, combos):
    total = 0
    not_in_menu = []

    for item in items:
        if item in meals:
            total += meals[item]
        elif item in combos:
            total += combos[item]
        else:
            not_in_menu.append(item)

    if not_in_menu:
        raise ValueError(f"Items not in the menu: {', '.join(not_in_menu)}")
    return total


def prices_counter(items):
    total = 0
    for item in items:
        if item in meals:
            total += meals[item]
        elif item in combos:
            total += combos[item]
        else:
            print(f"{item} is not in the menu")
    return total

