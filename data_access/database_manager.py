import sqlite3

DATABASE_FILE = "car_rental.db"  # Path to the SQLite database file.

def initialize_database():
    """ Creates the necessary database tables if they do not already exist. """
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:  # Establish a connection to the SQLite database.
            cursor = conn.cursor()
            # SQL to create a 'cars' table if it doesn't exist.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cars (
                    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_reg TEXT,
                    car_make TEXT,
                    car_year INTEGER
                );
            """)
            # SQL to create a 'customers' table if it doesn't exist.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    customer_number INTEGER,
                    customer_email TEXT
                );
            """)
            # SQL to create a 'rentals' table if it doesn't exist, with foreign keys linked to 'cars' and 'customers'.
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
            conn.commit()  # Commit the transaction to make sure all tables are created.
            print("Database initialized successfully.")
    except sqlite3.Error as e:  # Catch any SQL errors.
        print(f"An error occurred during database initialization: {e}")

def check_and_initialize():
    """ Checks if all required database tables are present and initializes them if necessary. """
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # List of required tables.
            tables_required = ['cars', 'customers', 'rentals']
            tables_found = []

            # Check each table exists and record it if found.
            for table in tables_required:
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table,))
                if cursor.fetchone():
                    tables_found.append(table)

            # Initialize database if any required tables are missing.
            if len(tables_found) != len(tables_required):
                print(f"Missing tables: {set(tables_required) - set(tables_found)}. Initializing database.")
                initialize_database()
            else:
                print("All necessary tables are present.")

    except sqlite3.Error as e:  # Handle any SQL errors that occur.
        print(f"An error occurred during database check and initialization: {e}")
