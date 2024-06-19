import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='product_management'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
