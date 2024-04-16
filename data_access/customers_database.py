import sqlite3
from data_access.database_manager import DATABASE_FILE  # Import the constant for the database file path

class CustomerDatabase:
    def __init__(self):
        # No more creation or setting up of the database in here, just initialization
        pass

    def add_customer(self, customer_name, customer_number, customer_email):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customers (customer_name, customer_number, customer_email) VALUES (?, ?, ?)",
                           (customer_name, customer_number, customer_email))
            conn.commit()

    def customer_exists(self, customer_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM customers WHERE customer_id = ?", (customer_id,))
            return cursor.fetchone()

    def get_customer_by_id(self, customer_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
            return cursor.fetchone()

    def edit_customer(self, customer_id, customer_name, customer_number, customer_email):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE customers SET
                customer_name = ?,
                customer_number = ?,
                customer_email = ?
                WHERE customer_id = ?
                """, (customer_name, customer_number, customer_email, customer_id))
            conn.commit()

    def delete_customer(self, customer_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
            conn.commit()


    def search_customers_by_mobile(self, mobile_number):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT customers.customer_id, customers.customer_name, customers.customer_number, customers.customer_email, cars.car_reg, cars.car_make, cars.car_year
                FROM customers
                LEFT JOIN rentals ON customers.customer_id = rentals.customer_id
                LEFT JOIN cars ON rentals.car_id = cars.car_id
                WHERE customers.customer_number LIKE ?
            """, ('%' + mobile_number + '%',))
            return cursor.fetchall()

    def get_all_customers(self):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers")
            return cursor.fetchall()
