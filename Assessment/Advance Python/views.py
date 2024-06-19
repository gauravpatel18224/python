import tkinter as tk
from tkinter import messagebox
from controller import Controller

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management Application")
        self.controller = Controller()

        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Welcome to Product Management Application").pack()
        tk.Button(self.root, text="Product Manager", command=self.product_manager_menu).pack()
        tk.Button(self.root, text="Customer", command=self.customer_menu).pack()

    def product_manager_menu(self):
        self.clear_screen()
        tk.Button(self.root, text="Register", command=lambda: self.registration_form('ProductManager')).pack()
        tk.Button(self.root, text="Login", command=lambda: self.login_form('ProductManager')).pack()

    def customer_menu(self):
        self.clear_screen()
        tk.Button(self.root, text="Register", command=lambda: self.registration_form('Customer')).pack()
        tk.Button(self.root, text="Login", command=lambda: self.login_form('Customer')).pack()

    def registration_form(self, user_type):
        self.clear_screen()
        tk.Label(self.root, text=f"{user_type} Registration").pack()
        
        tk.Label(self.root, text="Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Contact").pack()
        contact_entry = tk.Entry(self.root)
        contact_entry.pack()

        tk.Label(self.root, text="Email").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="Gender").pack()
        gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(self.root, text="Male", variable=gender_var, value="Male").pack()
        tk.Radiobutton(self.root, text="Female", variable=gender_var, value="Female").pack()

        tk.Label(self.root, text="City").pack()
        city_entry = tk.Entry(self.root)
        city_entry.pack()

        tk.Label(self.root, text="State").pack()
        state_entry = tk.Entry(self.root)
        state_entry.pack()

        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show='*')
        password_entry.pack()

        if user_type == 'Customer':
            tk.Label(self.root, text="Balance").pack()
            balance_entry = tk.Entry(self.root)
            balance_entry.pack()

        def register_user():
            user_data = {
                'name': name_entry.get(),
                'contact': contact_entry.get(),
                'email': email_entry.get(),
                'gender': gender_var.get(),
                'city': city_entry.get(),
                'state': state_entry.get(),
                'password': password_entry.get()
            }
            if user_type == 'Customer':
                user_data['balance'] = balance_entry.get()

            self.controller.register_user(user_type, user_data)
            self.show_message(f"{user_type} registered successfully")
            self.main_menu()

        tk.Button(self.root, text="Register", command=register_user).pack()

    def login_form(self, user_type):
        self.clear_screen()
        tk.Label(self.root, text=f"{user_type} Login").pack()
        
        tk.Label(self.root, text="Email").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show='*')
        password_entry.pack()

        def login_user():
            email = email_entry.get()
            password = password_entry.get()
            user = self.controller.login_user(user_type, email, password)
            if user:
                self.show_message(f"{user_type} logged in successfully")
                if user_type == 'ProductManager':
                    self.product_manager_dashboard()
                else:
                    self.customer_dashboard(user[0])
            else:
                self.show_message("Invalid credentials")

        tk.Button(self.root, text="Login", command=login_user).pack()

    def product_manager_dashboard(self):
        self.clear_screen()
        tk.Button(self.root, text="Manage Stocks", command=self.manage_stocks).pack()
        tk.Button(self.root, text="View Stocks", command=self.view_stocks).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack()

    def manage_stocks(self):
        self.clear_screen()
        tk.Label(self.root, text="Manage Stocks").pack()
        
        tk.Label(self.root, text="Product Name").pack()
        product_name_entry = tk.Entry(self.root)
        product_name_entry.pack()

        tk.Label(self.root, text="Quantity").pack()
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack()

        tk.Label(self.root, text="Price").pack()
        price_entry = tk.Entry(self.root)
        price_entry.pack()

        def add_stock():
            product_name = product_name_entry.get()
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            self.controller.manage_stock(product_name, quantity, price)
            self.show_message("Stock added successfully")
            self.product_manager_dashboard()

        tk.Button(self.root, text="Add Stock", command=add_stock).pack()
        tk.Button(self.root, text="Back", command=self.product_manager_dashboard).pack()

    def view_stocks(self):
        self.clear_screen()
        tk.Label(self.root, text="Stock List").pack()
        stocks = self.controller.view_stock()
        for stock in stocks:
            tk.Label(self.root, text=f"ID: {stock[0]}, Name: {stock[1]}, Quantity: {stock[2]}, Price: {stock[3]}").pack()
        tk.Button(self.root, text="Back", command=self.product_manager_dashboard).pack()

    def customer_dashboard(self, customer_id):
        self.clear_screen()
        tk.Button(self.root, text="Purchase Stock", command=lambda: self.purchase_stock(customer_id)).pack()
        tk.Button(self.root, text="View Orders", command=lambda: self.view_orders(customer_id)).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu).pack()

    def purchase_stock(self, customer_id):
        self.clear_screen()
        tk.Label(self.root, text="Purchase Stock").pack()
        
        tk.Label(self.root, text="Product ID").pack()
        product_id_entry = tk.Entry(self.root)
        product_id_entry.pack()

        tk.Label(self.root, text="Quantity").pack()
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack()

        def purchase():
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            self.controller.purchase_stock(customer_id, product_id, quantity)
            self.show_message("Stock purchased successfully")
            self.customer_dashboard(customer_id)

        tk.Button(self.root, text="Purchase", command=purchase).pack()
        tk.Button(self.root, text="Back", command=lambda: self.customer_dashboard(customer_id)).pack()

    def view_orders(self, customer_id):
        self.clear_screen()
        tk.Label(self.root, text="Order List").pack()
        orders = self.controller.view_orders(customer_id)
        for order in orders:
            tk.Label(self.root, text=f"Order ID: {order[0]}, Product ID: {order[2]}, Quantity: {order[3]}").pack()
        tk.Button(self.root, text="Back", command=lambda: self.customer_dashboard(customer_id)).pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_message(self, message):
        messagebox.showinfo("Information", message)
