# inventory_menu.py
from entity import MenuItem

class RestaurantData:
    def __init__(self):
        # 1. Menu Management
        self.menu = {
            "Pizza": MenuItem("Pizza", 15.00, ["dough", "cheese", "sauce"]),
            "Salad": MenuItem("Salad", 8.00, ["lettuce", "tomato"])
        }
        
        # 4. Inventory Tracking
        self.stock = {"dough": 10, "cheese": 10, "sauce": 10, "lettuce": 10, "tomato": 10}

    def get_menu_item(self, item_name):
        return self.menu.get(item_name)

    def consume_ingredients(self, menu_item):
        # Check and deduct ingredients
        for ingredient in menu_item.ingredients:
            if self.stock.get(ingredient, 0) <= 0:
                print(f"Warning: Out of {ingredient}!")
                return False
            self.stock[ingredient] -= 1
        return True