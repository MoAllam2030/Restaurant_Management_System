# entities.py
from datetime import datetime

class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients  # List of strings

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False

class Order:
    def __init__(self, table):
        self.table = table
        self.items = []
        self.status = "Pending" # Statuses: Pending, Preparing, Served, Paid.
        self.timestamp = datetime.now()

    def add_item(self, menu_item):
        self.items.append(menu_item)
