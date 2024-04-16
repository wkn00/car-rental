import sqlite3
import json
import csv
import xml.etree.ElementTree as ET
from data_access.database_manager import DATABASE_FILE  # Ensure this path is correctly imported

class ImportDatabase:
    def __init__(self):
        pass  # Initialization is empty as the DATABASE_FILE is handled globally

    def import_from_json(self, filename):
        """ Imports data from a JSON file into the database. """
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # Import cars
            if 'cars' in data:
                for car in data['cars']:
                    cursor.execute(
                        "INSERT INTO cars (car_id, car_reg, car_make, car_year) VALUES (?, ?, ?, ?)",
                        (car['id'], car['registration'], car['make'], car['year'])
                    )

            # Import customers
            if 'customers' in data:
                for customer in data['customers']:
                    cursor.execute(
                        "INSERT INTO customers (customer_id, customer_name, customer_number, customer_email) VALUES (?, ?, ?, ?)",
                        (customer['id'], customer['name'], customer['number'], customer['email'])
                    )

            # Import rentals
            if 'rentals' in data:
                for rental in data['rentals']:
                    cursor.execute(
                        "INSERT INTO rentals (rental_id, car_id, customer_id, start_date) VALUES (?, ?, ?, ?)",
                        (rental['id'], rental['car_id'], rental['customer_id'], rental['start_date'])
                    )

            conn.commit()

    def import_from_csv(self, filename):
        """ Imports data from a CSV file into the database. Handles different data sections based on headers. """
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                current_section = None
                for row in reader:
                    if not row or all(x.strip() == '' for x in row):  # Skip empty rows
                        continue
                    if 'Car ID' in row:
                        current_section = 'cars'
                        continue  # Skip header row
                    elif 'Customer ID' in row:
                        current_section = 'customers'
                        continue  # Skip header row
                    elif 'Rental ID' in row:
                        current_section = 'rentals'
                        continue  # Skip header row

                    if current_section == 'cars' and len(row) >= 4:
                        self.add_car(cursor, row[1], row[2], row[3])  # Assuming car_id is autoincrement
                    elif current_section == 'customers' and len(row) >= 4:
                        self.add_customer(cursor, row[1], row[2], row[3])  # Assuming customer_id is autoincrement
                    elif current_section == 'rentals' and len(row) >= 4:
                        self.add_rental(cursor, row[1], row[2], row[3])  # Assuming rental_id is autoincrement

            conn.commit()

    def add_car(self, cursor, car_reg, car_make, car_year):
        """ Adds a car to the database using the provided cursor. """
        cursor.execute(
            "INSERT INTO cars (car_reg, car_make, car_year) VALUES (?, ?, ?)",
            (car_reg, car_make, car_year)
        )

    def add_customer(self, cursor, customer_name, customer_number, customer_email):
        """ Adds a customer to the database using the provided cursor. """
        cursor.execute(
            "INSERT INTO customers (customer_name, customer_number, customer_email) VALUES (?, ?, ?)",
            (customer_name, customer_number, customer_email)
        )

    def add_rental(self, cursor, car_id, customer_id, start_date):
        """ Adds a rental to the database using the provided cursor. """
        cursor.execute(
            "INSERT INTO rentals (car_id, customer_id, start_date) VALUES (?, ?, ?)",
            (car_id, customer_id, start_date)
        )







    def import_from_xml(self, filename):
        """ Imports data from an XML file into the database. """
        tree = ET.parse(filename)
        root = tree.getroot()

        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()

            # Importing cars
            for car_element in root.findall('Cars/Car'):
                cursor.execute(
                    "INSERT INTO cars (car_id, car_reg, car_make, car_year) VALUES (?, ?, ?, ?)",
                    (
                        car_element.get('car_id'),
                        car_element.find('car_reg').text,
                        car_element.find('car_make').text,
                        car_element.find('car_year').text
                    )
                )

            # Importing customers
            for customer_element in root.findall('Customers/Customer'):
                cursor.execute(
                    "INSERT INTO customers (customer_id, customer_name, customer_number, customer_email) VALUES (?, ?, ?, ?)",
                    (
                        customer_element.get('customer_id'),
                        customer_element.find('customer_name').text,
                        customer_element.find('customer_number').text,
                        customer_element.find('customer_email').text
                    )
                )

            # Importing rentals
            for rental_element in root.findall('Rentals/Rental'):
                cursor.execute(
                    "INSERT INTO rentals (rental_id, car_id, customer_id, start_date) VALUES (?, ?, ?, ?)",
                    (
                        rental_element.get('rental_id'),
                        rental_element.find('car_id').text,
                        rental_element.find('customer_id').text,
                        rental_element.find('start_date').text
                    )
                )

            conn.commit()