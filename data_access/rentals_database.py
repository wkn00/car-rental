import sqlite3
import datetime
from data_access.database_manager import DATABASE_FILE  # Assuming DATABASE_FILE is the path to your unified database

class RentalDatabase:
    def __init__(self):
        # Removed the separate connection initialization
        pass

    def start_rental(self, car_id, customer_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            if not self.is_car_rented(car_id, cursor):  # Pass cursor to use within the method
                today = datetime.date.today()
                cursor.execute("INSERT INTO rentals (car_id, customer_id, start_date) VALUES (?, ?, ?)",
                                (car_id, customer_id, today))
                conn.commit()
                return True
        return False

    def is_car_rented(self, car_id, cursor):
        # Removed the separate connection and use the cursor passed from the calling method
        cursor.execute("SELECT * FROM rentals WHERE car_id = ?", (car_id,))
        return cursor.fetchone() is not None
    
    def delete_rental(self, rental_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rentals WHERE rental_id = ?", (rental_id,))
            conn.commit()

    def get_rental_by_id(self, rental_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rentals WHERE rental_id = ?", (rental_id,))
            return cursor.fetchone()

    def get_all_rentals(self):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rentals")
            return cursor.fetchall()
