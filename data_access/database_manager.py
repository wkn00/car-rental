import sqlite3

DATABASE_FILE = "car_rental.db"

def initialize_database():
    """ Creates the necessary database tables. """
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cars (
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_reg TEXT,
                    car_make TEXT,
                    car_year INTEGER
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    customer_number INTEGER,
                    customer_email TEXT
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rentals (
                    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_id INTEGER,
                    customer_id INTEGER,
                    start_date DATE,
                    FOREIGN KEY (car_id) REFERENCES cars(car_id),
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                );
            """)
            conn.commit()
            print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred during database initialization: {e}")


def check_and_initialize():
    """ Checks if the database needs to be initialized and does so if necessary for all required tables. """
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # Check for each required table
            tables_required = ['cars', 'customers', 'rentals']
            tables_found = []

            for table in tables_required:
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table,))
                if cursor.fetchone():
                    tables_found.append(table)

            # If not all tables are found, initialize the database
            if len(tables_found) != len(tables_required):
                print(f"Missing tables: {set(tables_required) - set(tables_found)}. Initializing database.")
                initialize_database()
            else:
                print("All necessary tables are present.")

    except sqlite3.Error as e:
        print(f"An error occurred during database check and initialization: {e}")
