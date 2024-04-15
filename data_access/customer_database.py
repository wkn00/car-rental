import sqlite3

class CustomerDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("customers.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS customers")
        self.cursor.execute("""
            CREATE TABLE customers (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                customer_number TEXT,
                customer_email TEXT
            )""")
        self.connection.commit()

    def add_customer(self, customer_name, customer_number, customer_email):
        self.cursor.execute("INSERT INTO customers (customer_name, customer_number, customer_email) VALUES (?, ?, ?)",
                            (customer_name, customer_number, customer_email))
        self.connection.commit()

    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
