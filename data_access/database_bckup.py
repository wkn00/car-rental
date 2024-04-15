import sqlite3

class DatabaseAccess:
    def __init__(self):
        # Initialize both databases
        self.initialize_database_cars()
        self.initialize_database_customers()

    def initialize_database_cars(self):
        self.connection_car = sqlite3.connect("cars.db")
        self.cursor_car = self.connection_car.cursor()

        self.cursor_car.execute("DROP TABLE IF EXISTS cars")
        self.cursor_car.execute("""
            CREATE TABLE cars (
                id INTEGER PRIMARY KEY,
                car_reg TEXT,
                car_make TEXT,
                car_year TEXT
            )""")
        self.connection_car.commit()

    def add_car(self, car_reg, car_make, car_year):
        self.cursor_car.execute("INSERT INTO cars (car_reg, car_make, car_year) VALUES (?, ?, ?)",
                                (car_reg, car_make, car_year))
        self.connection_car.commit()

    def get_all_cars(self):
        self.cursor_car.execute("SELECT * FROM cars")
        return self.cursor_car.fetchall()

    def initialize_database_customers(self):
        self.connection_customer = sqlite3.connect("customers.db")
        self.cursor_customer = self.connection_customer.cursor()

        self.cursor_customer.execute("DROP TABLE IF EXISTS customers")
        self.cursor_customer.execute("""
            CREATE TABLE customers (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                customer_number TEXT,
                customer_email TEXT
            )""")
        self.connection_customer.commit()

    def add_customer(self, customer_name, customer_number, customer_email):
        self.cursor_customer.execute("INSERT INTO customers (customer_name, customer_number, customer_email) VALUES (?, ?, ?)",
                                     (customer_name, customer_number, customer_email))
        self.connection_customer.commit()

    def get_all_customers(self):
        self.cursor_customer.execute("SELECT * FROM customers")
        return self.cursor_customer.fetchall()

    def close(self):
        self.connection_car.close()
        self.connection_customer.close()
