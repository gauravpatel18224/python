#include <iostream>
#include <string>
#include <vector>

using namespace std;


class FoodItem {
public:
    int id;
    string name;
    double price;

    FoodItem(int i, string n, double p) : id(i), name(n), price(p) {}
};

class OrderItem {
public:
    FoodItem item;
    int quantity;

    OrderItem(FoodItem i, int q) : item(i), quantity(q) {}
};

class Order {
public:
    string customerName;
    vector<OrderItem> items;

    void addItem(OrderItem orderItem) {
        items.push_back(orderItem);
    }

    void displayOrder() {
        cout << "Order for " << customerName << ":\n";
        for (const auto& orderItem : items) {
            cout << orderItem.item.name << " x " << orderItem.quantity << " - $" << orderItem.item.price * orderItem.quantity << "\n";
        }
    }

    double calculateTotal() {
        double total = 0.0;
        for (const auto& orderItem : items) {
            total += orderItem.item.price * orderItem.quantity;
        }
        return total;
    }
};

// Function to display the main menu
void displayMainMenu() {
    cout << "-Menu-\n";
    cout << "1) Pizzas\n";
    cout << "2) Burgers\n";
    cout << "3) Sandwich\n";
    cout << "4) Rolls\n";
    cout << "5) Biryani\n";
}

// Function to display sub-menu based on the main menu choice
void displaySubMenu(int choice) {
    switch (choice) {
        case 1:
            cout << "1) Margherita Pizza - $8.99\n";
            cout << "2) Pepperoni Pizza - $9.99\n";
            cout << "3) Veggie Pizza - $7.99\n";
            break;
        case 2:
            cout << "1) Cheeseburger - $5.49\n";
            cout << "2) Chicken Burger - $6.49\n";
            cout << "3) Veggie Burger - $4.99\n";
            break;
        case 3:
            cout << "1) Club Sandwich - $2.40\n";
            cout << "2) Veg. Crispy Sandwich - $1.60\n";
            cout << "3) Extream Veg Sandwich - $1.00\n";
            break;
        case 4:
            cout << "1) Chicken Roll - $3.49\n";
            cout << "2) Veggie Roll - $2.99\n";
            cout << "3) Paneer Roll - $3.99\n";
            break;
        case 5:
            cout << "1) Chicken Biryani - $6.99\n";
            cout << "2) Veg Biryani - $5.99\n";
            cout << "3) Mutton Biryani - $8.99\n";
            break;
        default:
            cout << "Invalid choice!\n";
    }
}

// Function to get the customer's sub-menu order
void takeSubMenuOrder(int mainChoice, Order& order) {
    int subChoice, quantity;
    cout << "Please enter your choice: ";
    cin >> subChoice;

    // Assuming menu items are initialized like this based on the sub-menu choices
    vector<FoodItem> subMenu;
    switch (mainChoice) {
        case 1:
            subMenu = {
                FoodItem(1, "Margherita Pizza", 8.99),
                FoodItem(2, "Pepperoni Pizza", 9.99),
                FoodItem(3, "Veggie Pizza", 7.99)
            };
            break;
        case 2:
            subMenu = {
                FoodItem(1, "Cheeseburger", 5.49),
                FoodItem(2, "Chicken Burger", 6.49),
                FoodItem(3, "Veggie Burger", 4.99)
            };
            break;
        case 3:
            subMenu = {
                FoodItem(1, "Club Sandwich", 2.40),
                FoodItem(2, "Veg. Crispy Sandwich", 1.60),
                FoodItem(3, "Extream Veg Sandwich", 1.00)
            };
            break;
        case 4:
            subMenu = {
                FoodItem(1, "Chicken Roll", 3.49),
                FoodItem(2, "Veggie Roll", 2.99),
                FoodItem(3, "Paneer Roll", 3.99)
            };
            break;
        case 5:
            subMenu = {
                FoodItem(1, "Chicken Biryani", 6.99),
                FoodItem(2, "Veg Biryani", 5.99),
                FoodItem(3, "Mutton Biryani", 8.99)
            };
            break;
        default:
            cout << "Invalid main menu choice!\n";
            return;
    }

    bool found = false;
    for (const auto& item : subMenu) {
        if (item.id == subChoice) {
            cout << "Please enter the quantity: ";
            cin >> quantity;
            order.addItem(OrderItem(item, quantity));
            cout << item.name << " x " << quantity << " added to your order.\n";
            found = true;
            break;
        }
    }

    if (!found) {
        cout << "Invalid sub-menu choice, please try again.\n";
    }
}

// Function to get the customer's main menu order
void takeOrder(Order& order) {
    int mainChoice;
    while (true) {
        displayMainMenu();
        cout << "Please enter your main menu choice (0 to finish): ";
        cin >> mainChoice;
        if (mainChoice == 0) break;

        displaySubMenu(mainChoice);
        takeSubMenuOrder(mainChoice, order);

        // Display current order and total
        order.displayOrder();
        cout << "Your total bill is $" << order.calculateTotal() << "\n";
        cout << "Your order will be delivered in 40 minutes.\n";
        
        // Ask if the customer wants to continue ordering
        char continueOrdering;
        cout << "Would you like to order anything else? (Y/N): ";
        cin >> continueOrdering;
        if (continueOrdering == 'N' || continueOrdering == 'n') break;
    }
}

int main() {
    string customerName;
    cout << "Please enter your name: ";
    getline(cin, customerName);

    // Create an order for the customer
    Order order;
    order.customerName = customerName;

    cout << "Hello " << customerName << "\n";
    takeOrder(order);

    cout << "\nFinal Order Summary:\n";
    order.displayOrder();
    cout << "Total: $" << order.calculateTotal() << "\n";
    cout << "Thank you for ordering from Tops Tech Fast Food!\n";

    return 0;
}
