import sqlite3
from data_access.database_manager import DATABASE_FILE  # Importing the path to the SQLite database file.

class CarDatabase:
    def __init__(self):
        pass

    def add_car(self, car_reg, car_make, car_year):
        # Adds a new car to the database.
        with sqlite3.connect(DATABASE_FILE) as conn:  # Opens a connection to the database.
            cursor = conn.cursor()  # Creates a cursor object using the connection.
            cursor.execute("INSERT INTO cars (car_reg, car_make, car_year) VALUES (?, ?, ?)",
                           (car_reg, car_make, car_year))  # Executes an SQL statement to insert a new car.
            conn.commit()  # Commits the transaction.

    def edit_car(self, car_id, car_reg, car_make, car_year):
        # Updates a car's details in the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE cars SET
                car_reg = ?,
                car_make = ?,
                car_year = ?
                WHERE car_id = ?
                """, (car_reg, car_make, car_year, car_id))  # SQL update statement.
            conn.commit()  # Commits the changes.

    def delete_car(self, car_id):
        # Deletes a car from the database based on its ID.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))  # SQL delete statement.
            conn.commit()  # Commits the deletion.

    def get_car_by_id(self, car_id):
        # Retrieves a car by its ID from the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,))  # SQL query to find a car by ID.
            return cursor.fetchone()  # Returns a single record from the query.

    def search_cars_by_registration(self, registration_number):
        # Searches for cars by their registration number, possibly including joined data from rentals and customers.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT cars.car_id, cars.car_reg, cars.car_make, cars.car_year, customers.customer_name
                FROM cars
                LEFT JOIN rentals ON cars.car_id = rentals.car_id
                LEFT JOIN customers ON rentals.customer_id = customers.customer_id
                WHERE cars.car_reg LIKE ?
            """, ('%' + registration_number + '%',))  # SQL search with a wildcard match.
            return cursor.fetchall()  # Returns all matching records.

    def car_exists(self, car_id):
        # Checks if a specific car exists in the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM cars WHERE car_id = ?", (car_id,))
            return cursor.fetchone() is not None  # Returns True if the car exists, False otherwise.

    def get_all_cars(self):
        # Retrieves all cars from the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars")
            return cursor.fetchall()  # Returns a list of all cars in the database.