import io
import sys
import pytest
from data_structures import get_names, get_spiciest_foods, print_spicy_foods, \
                           create_spicy_food, get_spicy_food_by_cuisine, \
                           print_spiciest_foods, get_average_heat_level

class TestDataStructures:
    '''Module data_structures.py'''

    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        }
    ]

    def test_get_names(self):
        '''contains function get_names() that retrieves names from list of foods.'''
        assert get_names(self.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

    def test_get_spiciest_foods(self):
        '''contains function get_spiciest_foods() that returns foods with a heat_level over 5.'''
        heat_level_threshold = 5
        expected = [
            {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
            {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
        ]
        result = get_spiciest_foods(self.SPICY_FOODS, heat_level_threshold)
        assert result == expected

    def test_print_spicy_foods(self):
        '''contains function print_spicy_foods that returns all foods formatted with 🌶 emojis.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spicy_foods(self.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        expected_output = "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" + \
                          "Buffalo Wings (American) | Heat Level: 🌶🌶🌶\n" + \
                          "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"
        assert captured_out.getvalue() == expected_output

    def test_get_spicy_food_by_cuisine(self):
        '''contains function get_spicy_food_by_cuisine that returns the food that matches a cuisine.'''
        assert get_spicy_food_by_cuisine(self.SPICY_FOODS, "American") == {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        }

    def test_print_spiciest_foods(self):
        '''contains function print_spiciest_foods that returns foods with heat_level over 5 formatted with 🌶 emojis.'''
        heat_level_threshold = 5
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spiciest_foods(self.SPICY_FOODS, heat_level_threshold)
        sys.stdout = sys.__stdout__
        expected_output = "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" + \
                          "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"
        assert captured_out.getvalue() == expected_output

    def test_get_average_heat_level(self):
        '''contains function get_average_heat_level that returns average of heat_levels in spicy_foods.'''
        assert get_average_heat_level(self.SPICY_FOODS) == 6

    def test_create_spicy_food(self):
        '''contains function create_spicy_food that returns original list of spicy_foods with new spicy_food added.'''
        new_food = {
            'name': 'Griot',
            'cuisine': 'Haitian',
            'heat_level': 10,
        }
        updated_list = create_spicy_food(self.SPICY_FOODS, new_food)
        expected = [
            {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
            {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
            {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
            {"name": "Griot", "cuisine": "Haitian", "heat_level": 10},
        ]
        assert updated_list == expected
