from db import get_db_connection
from models import ProductManager, Customer

class Controller:
    def __init__(self):
        self.conn = get_db_connection()

    def register_user(self, user_type, user_data):
        if self.conn:
            cursor = self.conn.cursor()
            if user_type == 'ProductManager':
                query = """
                INSERT INTO product_managers (name, contact, email, gender, city, state, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (
                    user_data['name'], user_data['contact'], user_data['email'],
                    user_data['gender'], user_data['city'], user_data['state'], user_data['password']
                ))
            elif user_type == 'Customer':
                query = """
                INSERT INTO customers (name, contact, email, gender, city, state, balance, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (
                    user_data['name'], user_data['contact'], user_data['email'],
                    user_data['gender'], user_data['city'], user_data['state'], user_data['balance'], user_data['password']
                ))
            self.conn.commit()

    def login_user(self, user_type, email, password):
        if self.conn:
            cursor = self.conn.cursor()
            if user_type == 'ProductManager':
                query = "SELECT * FROM product_managers WHERE email = %s AND password = %s"
            else:
                query = "SELECT * FROM customers WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user = cursor.fetchone()
            return user

    def manage_stock(self, product_name, quantity, price):
        if self.conn:
            cursor = self.conn.cursor()
            query = "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)"
            cursor.execute(query, (product_name, quantity, price))
            self.conn.commit()

    def view_stock(self):
        if self.conn:
            cursor = self.conn.cursor()
            query = "SELECT * FROM products"
            cursor.execute(query)
            products = cursor.fetchall()
            return products

    def purchase_stock(self, customer_id, product_id, quantity):
        if self.conn:
            cursor = self.conn.cursor()
            query = "INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
            cursor.execute(query, (customer_id, product_id, quantity))
            self.conn.commit()

    def view_orders(self, customer_id):
        if self.conn:
            cursor = self.conn.cursor()
            query = "SELECT * FROM orders WHERE customer_id = %s"
            cursor.execute(query, (customer_id,))
            orders = cursor.fetchall()
            return orders
