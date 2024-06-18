import os
import json

FRUIT_STOCK_FILE = 'fruit_stock.json'

class FruitManager:
    """Class to manage fruit stock operations like add, view, and update."""

    def __init__(self):
        self.fruit_stock = self.load_fruit_stock()

    def load_fruit_stock(self):
        """Load fruit stock from a JSON file."""
        if not os.path.exists(FRUIT_STOCK_FILE):
            return {}
        with open(FRUIT_STOCK_FILE, 'r') as file:
            return json.load(file)

    def save_fruit_stock(self):
        """Save the current fruit stock to a JSON file."""
        with open(FRUIT_STOCK_FILE, 'w') as file:
            json.dump(self.fruit_stock, file, indent=4)

    def add_fruit(self, name, quantity, price):
        """Add fruit to the stock."""
        if name in self.fruit_stock:
            # Validate existing data structure
            if isinstance(self.fruit_stock[name], dict):
                self.fruit_stock[name]['quantity'] += quantity
                self.fruit_stock[name]['price'] = price
            else:
                print(f"Error: Existing data for {name} is corrupted.")
        else:
            self.fruit_stock[name] = {'quantity': quantity, 'price': price}
        self.save_fruit_stock()
        self.log_transaction(f'Added {quantity} kg of {name} at {price} per kg')

    def view_fruit_stock(self):
        """View the current fruit stock."""
        return self.fruit_stock

    def update_fruit_stock(self, name, quantity, price):
        """Update the quantity and price of a fruit in the stock."""
        if name in self.fruit_stock:
            self.fruit_stock[name] = {'quantity': quantity, 'price': price}
            self.save_fruit_stock()
            self.log_transaction(f'Updated {name} to {quantity} kg at {price} per kg')
        else:
            print("Fruit not found in stock.")

    def log_transaction(self, message):
        """Log transactions to a log file."""
        with open('transactions.log', 'a') as log_file:
            log_file.write(message + '\n')
