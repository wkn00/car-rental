import sqlite3
import datetime
from data_access.database_manager import DATABASE_FILE  # Importing the path to the unified database file.

class RentalDatabase:
    def __init__(self):
        pass

    def start_rental(self, car_id, customer_id):
        # Starts a rental if the car is not already rented.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            if not self.is_car_rented(car_id, cursor):  # Check if the car is currently rented using a cursor.
                today = datetime.date.today()
                cursor.execute("INSERT INTO rentals (car_id, customer_id, start_date) VALUES (?, ?, ?)",
                                (car_id, customer_id, today))  # Insert a new rental record.
                conn.commit()  # Commit the transaction.
                return True
        return False  # Return False if the car is already rented.

    def is_car_rented(self, car_id, cursor):
        # Checks if a specific car is currently rented.
        cursor.execute("SELECT * FROM rentals WHERE car_id = ?", (car_id,))
        return cursor.fetchone() is not None  # Returns True if there is a rental record for the car, False otherwise.

    def delete_rental(self, rental_id):
        # Deletes a rental by its ID.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rentals WHERE rental_id = ?", (rental_id,))  # Execute the delete statement.
            conn.commit()  # Commit the transaction.

    def get_rental_by_id(self, rental_id):
        # Retrieves a specific rental by its ID.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rentals WHERE rental_id = ?", (rental_id,))  # SQL query to find a rental by ID.
            return cursor.fetchone()  # Returns the rental record.

    def get_all_rentals(self):
        # Retrieves all rental records from the database.
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rentals")
            return cursor.fetchall()  # Returns a list of all rentals in the database.