import sqlite3
import datetime

class RentalDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("rentals.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rentals (
                rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_id INTEGER,
                customer_id INTEGER,
                start_date DATE,
                FOREIGN KEY (car_id) REFERENCES cars(id),
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )""")
        self.connection.commit()

    def start_rental(self, car_id, customer_id):
        today = datetime.date.today()
        self.cursor.execute("INSERT INTO rentals (car_id, customer_id, start_date) VALUES (?, ?, ?)",
                            (car_id, customer_id, today))
        self.connection.commit()

    def get_all_rentals(self):
        self.cursor.execute("SELECT * FROM rentals")
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()
