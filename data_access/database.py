import sqlite3

class DatabaseAccess:
    def __init__(self):
        # Initialize both databases
        self.initialize_database_cars()
        self.initialize_database_customers()

    def initialize_database_cars(self):
        self.connection_car = sqlite3.connect("cars01.db")
        self.cursor_car = self.connection_car.cursor()

        self.cursor_car.execute("DROP TABLE IF EXISTS cars")
        self.cursor_car.execute("""
            CREATE TABLE cars (
                id INTEGER PRIMARY KEY,
                car_reg TEXT,
                car_make TEXT,
                car_year TEXT,
                car_color TEXT
            )""")
        self.connection_car.commit()

    def add_car(self, car_registration_number, car_make, car_year, car_color):
        self.cursor_car.execute("INSERT INTO cars (car_reg, car_make, car_year, car_color) VALUES (?, ?, ?, ?)",
                                (car_registration_number, car_make, car_year, car_color))
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
                customer_contact_number TEXT,
                customer_email TEXT,
                customer_address TEXT
            )""")
        self.connection_customer.commit()

    def add_customer(self, customer_name, customer_contact_number, customer_email, customer_address):
        self.cursor_customer.execute("INSERT INTO customers (customer_name, customer_contact_number, customer_email, customer_address) VALUES (?, ?, ?, ?)",
                                     (customer_name, customer_contact_number, customer_email, customer_address))
        self.connection_customer.commit()

    def get_all_customers(self):
        self.cursor_customer.execute("SELECT * FROM customers")
        return self.cursor_customer.fetchall()

    def close(self):
        self.connection_car.close()
        self.connection_customer.close()
