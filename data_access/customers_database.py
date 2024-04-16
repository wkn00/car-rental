import sqlite3
from data_access.database_manager import DATABASE_FILE  # Importing the path to the SQLite database file.

class CustomerDatabase:
    def __init__(self):
        pass

    def add_customer(self, customer_name, customer_number, customer_email):
        # Adds a new customer to the database.
        with sqlite3.connect(DATABASE_FILE) as conn:  # Opens a connection to the database.
            cursor = conn.cursor()  # Creates a cursor object using the connection.
            cursor.execute("INSERT INTO customers (customer_name, customer_number, customer_email) VALUES (?, ?, ?)",
                           (customer_name, customer_number, customer_email))  # Executes an SQL statement to insert a new customer.
            conn.commit()  # Commits the transaction.

    def edit_customer(self, customer_id, customer_name, customer_number, customer_email):
        # Updates a customer's details in the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE customers SET
                customer_name = ?,
                customer_number = ?,
                customer_email = ?
                WHERE customer_id = ?
                """, (customer_name, customer_number, customer_email, customer_id))  # SQL update statement.
            conn.commit()  # Commits the changes.

    def delete_customer(self, customer_id):
        # Deletes a customer from the database based on their ID.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))  # SQL delete statement.
            conn.commit()  # Commits the deletion.

    def search_customers_by_mobile(self, mobile_number):
        # Searches for customers by their mobile number, possibly including joined data from rentals and cars.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT customers.customer_id, customers.customer_name, customers.customer_number, customers.customer_email, cars.car_reg, cars.car_make, cars.car_year
                FROM customers
                LEFT JOIN rentals ON customers.customer_id = rentals.customer_id
                LEFT JOIN cars ON rentals.car_id = cars.car_id
                WHERE customers.customer_number LIKE ?
            """, ('%' + mobile_number + '%',))  # SQL search with a wildcard match.
            return cursor.fetchall()  # Returns all matching records.

    def get_customer_by_id(self, customer_id):
        # Retrieves a customer by their ID from the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))  # SQL query to find a customer by ID.
            return cursor.fetchone()  # Returns a single record from the query.

    def get_all_customers(self):
        # Retrieves all customers from the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers")
            return cursor.fetchall()  # Returns a list of all customers in the database.

    def customer_exists(self, customer_id):
        # Checks if a specific customer exists in the database by customer_id.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM customers WHERE customer_id = ?", (customer_id,))
            return cursor.fetchone() is not None  # Returns True if the customer exists, otherwise False.
