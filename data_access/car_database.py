import sqlite3

class CarDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("cars.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS cars")
        self.cursor.execute("""
            CREATE TABLE cars (
                id INTEGER PRIMARY KEY,
                car_reg TEXT,
                car_make TEXT,
                car_year TEXT
            )""")
        self.connection.commit()

    def add_car(self, car_reg, car_make, car_year):
        self.cursor.execute("INSERT INTO cars (car_reg, car_make, car_year) VALUES (?, ?, ?)",
                            (car_reg, car_make, car_year))
        self.connection.commit()


    def get_car_by_id(self, car_id):
        self.cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        return self.cursor.fetchone()
    

    def edit_car(self, car_id, car_reg, car_make, car_year):
        self.cursor.execute("""
            UPDATE cars SET
            car_reg = ?,
            car_make = ?,
            car_year = ?
            WHERE id = ?
            """, (car_reg, car_make, car_year, car_id))
        self.connection.commit()

    def delete_car(self, car_id):
        self.cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        self.connection.commit()


    def get_all_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
