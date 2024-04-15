import sqlite3

class CarDatabase:
    def __init__(self):
        self.db_file = "cars.db"  # Define the database file name here
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS cars")
            cursor.execute("""
                CREATE TABLE cars (
                    id INTEGER PRIMARY KEY,
                    car_reg TEXT,
                    car_make TEXT,
                    car_year TEXT
                )""")
            conn.commit()

    def add_car(self, car_reg, car_make, car_year):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cars (car_reg, car_make, car_year) VALUES (?, ?, ?)",
                           (car_reg, car_make, car_year))
            conn.commit()

    def get_car_by_id(self, car_id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
            return cursor.fetchone()

    def edit_car(self, car_id, car_reg, car_make, car_year):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE cars SET
                car_reg = ?,
                car_make = ?,
                car_year = ?
                WHERE id = ?
                """, (car_reg, car_make, car_year, car_id))
            conn.commit()

    def delete_car(self, car_id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            conn.commit()

    def search_cars_by_registration(self, registration_number):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars WHERE car_reg LIKE ?", ('%' + registration_number + '%',))
            return cursor.fetchall()


    def car_exists(self, car_id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM cars WHERE id = ?", (car_id,))
            return cursor.fetchone() is not None

    def get_all_cars(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars")
            return cursor.fetchall()
