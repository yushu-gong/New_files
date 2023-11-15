#test function.py
import sys
import pandas as pd

sys.path.append("C:\\Users\\Quinn\\Desktop\\py\\New_files")
from unittest import TestCase
from module_counter.exceptions_counter import MealTooBigError, InvalidItemId
from module_counter.functions_counter import calories_counter, prices_counter
combos = pd.read_json('C:\\Users\\Quinn\\Desktop\\py\\New_files\\module_counter\\data\\combos.json')
meals = pd.read_json('C:\\Users\\Quinn\\Desktop\\py\\New_files\\module_counter\\data\\meals.json')

class CaloriesCounterTestCase(TestCase):
    def test_counter_meals_calories(self):
        result = calories_counter(["meal-1", "meal-2", "meal-3"], meals, combos)
        self.assertEqual(result, 1750, f"Expected 1750, got {result}")

    def test_counter_combo_calories(self):
        result = calories_counter(["combo-1", "combo-2"], meals, combos)
        self.assertEqual(result, 1770, f"Expected 1770, got {result}")

    def test_count_meals_and_combos_calories(self):
        result = calories_counter(["meal-1", "combo-1"], meals, combos)
        self.assertEqual(result, 1670, f"Expected 1670, got {result}")

    def test_raise_error_if_calories_are_too_big(self):
        with self.assertRaises(MealTooBigError) as context:
            items = ["combo-1", "combo-2"]
        calories_counter(items, meals, combos)
        self.assertEqual(
        str(context.exception),
        "Meal is too big! 2140 calories is too much!",
        "wrong error message."
    )

        

def test_raise_error_if_item_id_is_valid(self):
    with self.assertRaises(InvalidItemId) as e:
        calories_counter(["meal-0"])
    self.assertEqual(
        str(e.exception),
        "meal-0",
        "wrong error message."
    )

class PriceCounterTestCase(TestCase):
    def test_count_meals_price(self):
        result = prices_counter(["meal-1","meal-2","meal-3"])
        self.assertEqual(result, 18, f"Expected 18, got {result}")

    def test_count_meals_price(self):
        result = prices_counter(["meal-1", "meal-2", "meal-3"], meals, combos)
        self.assertEqual(result, 18, f"Expected 18, got {result}")

def test_count_combo_prices(self):
    result = prices_counter(["combo-1", "combo-2"], meals, combos)
    self.assertEqual(result, 21, f"Expected 21, got {result}")

def test_count_meals_and_combos_prices(self):
    result = prices_counter(["combo-1", "meal-1"], meals, combos)
    self.assertEqual(result, 16, f"Expected 16, got {result}")
