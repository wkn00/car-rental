import sqlite3

class CustomerDatabase:
    def __init__(self):
        self.db_file = "customers.db"  # Define the database file path here
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS customers")
            cursor.execute("""
                CREATE TABLE customers (
                    id INTEGER PRIMARY KEY,
                    customer_name TEXT,
                    customer_number TEXT,
                    customer_email TEXT
                )""")
            conn.commit()

    def add_customer(self, customer_name, customer_number, customer_email):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customers (customer_name, customer_number, customer_email) VALUES (?, ?, ?)",
                           (customer_name, customer_number, customer_email))
            conn.commit()

    def customer_exists(self, customer_id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM customers WHERE id = ?", (customer_id,))
            return cursor.fetchone() is not None

    def search_customers_by_mobile(self, mobile_number):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE customer_number LIKE ?", ('%' + mobile_number + '%',))
            return cursor.fetchall()


    def get_all_customers(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers")
            return cursor.fetchall()
