from fruit_manager import FruitManager
from customer import Customer

def main_menu():
    """Display the main menu and return the user's choice."""
    print("\nWELCOME TO FRUIT MARKET")
    print("1) Manager")
    print("2) Customer")
    return input("Select your Role (1-2): ")

def manager_menu():
    """Display the manager menu and return the user's choice."""
    print("\nFruit Market Manager")
    print("1) Add Fruit Stock")
    print("2) View Fruit Stock")
    print("3) Update Fruit Stock")
    return input("Enter your choice (1-3): ")

def add_fruit(manager):
    """Prompt user for fruit details and add to stock."""
    name = input("Enter fruit name: ").strip()
    try:
        quantity = int(input("Enter quantity (in kg): "))
        price = float(input("Enter price (per kg): "))
        manager.add_fruit(name, quantity, price)
        print(f"Added {quantity} kg of {name} at {price} per kg")
    except ValueError:
        print("Invalid quantity or price. Please enter valid numbers.")

def view_fruit(manager):
    """Display the current fruit stock."""
    stock = manager.view_fruit_stock()
    if stock:
        for fruit, details in stock.items():
            if isinstance(details, dict):
                print(f"{fruit}: {details['quantity']} kg at {details['price']} per kg")
            else:
                print(f"Error: Data for {fruit} is corrupted.")
    else:
        print("No fruit in stock.")

def update_fruit(manager):
    """Prompt user for fruit details and update the stock."""
    name = input("Enter fruit name: ").strip()
    if name in manager.view_fruit_stock():
        try:
            quantity = int(input(f"Enter new quantity for {name} (in kg): "))
            price = float(input(f"Enter new price for {name} (per kg): "))
            manager.update_fruit_stock(name, quantity, price)
            print(f"Updated {name} to {quantity} kg at {price} per kg")
        except ValueError:
            print("Invalid quantity or price. Please enter valid numbers.")
    else:
        print("Fruit not found in stock.")

def run():
    """Run the main loop for the fruit store application."""
    manager = FruitManager()
    while True:
        role = main_menu()
        if role == '1':
            while True:
                choice = manager_menu()
                if choice == '1':
                    add_fruit(manager)
                elif choice == '2':
                    view_fruit(manager)
                elif choice == '3':
                    update_fruit(manager)
                else:
                    print("Invalid option. Please select a valid option (1-3).")
                cont = input("Do you want to perform more operations? (y/n): ").lower()
                if cont != 'y':
                    break
        elif role == '2':
            # Placeholder for customer functionality
            print("Customer functionality not yet implemented.")
        else:
            print("Invalid role. Please select a valid role (1-2).")

if __name__ == "__main__":
    run()
