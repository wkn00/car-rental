import sqlite3
from data_access.database_manager import DATABASE_FILE  # Assuming DATABASE_FILE is correctly imported

class CarDatabase:
    def __init__(self):
        # Initialization doesn't require setting up the database anymore.
        pass

    def add_car(self, car_reg, car_make, car_year):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cars (car_reg, car_make, car_year) VALUES (?, ?, ?)",
                           (car_reg, car_make, car_year))
            conn.commit()

    def get_car_by_id(self, car_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,))
            return cursor.fetchone()

    def edit_car(self, car_id, car_reg, car_make, car_year):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE cars SET
                car_reg = ?,
                car_make = ?,
                car_year = ?
                WHERE car_id = ?
                """, (car_reg, car_make, car_year, car_id))
            conn.commit()

    def delete_car(self, car_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))
            conn.commit()

    def search_cars_by_registration(self, registration_number):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT cars.car_id, cars.car_reg, cars.car_make, cars.car_year, customers.customer_name
                FROM cars
                LEFT JOIN rentals ON cars.car_id = rentals.car_id
                LEFT JOIN customers ON rentals.customer_id = customers.customer_id
                WHERE cars.car_reg LIKE ?
            """, ('%' + registration_number + '%',))
            return cursor.fetchall()

    def car_exists(self, car_id):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM cars WHERE car_id = ?", (car_id,))
            return cursor.fetchone() is not None

    def get_all_cars(self):
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars")
            return cursor.fetchall()
