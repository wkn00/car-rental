import sqlite3
import json
import csv
import xml.etree.ElementTree as ET
from data_access.database_manager import DATABASE_FILE  # Ensure this path is correctly imported

class ExportDatabase:
    def __init__(self):
        pass  # Initialization is empty as the DATABASE_FILE is handled globally

    def fetch_data_from_database(self):
        """ Fetches data from the database and returns it in a dictionary format. """
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            data = {
                'cars': cursor.execute("SELECT car_id, car_reg, car_make, car_year FROM cars").fetchall(),
                'customers': cursor.execute("SELECT customer_id, customer_name, customer_number, customer_email FROM customers").fetchall(),
                'rentals': cursor.execute("SELECT rental_id, car_id, customer_id, start_date FROM rentals").fetchall()
            }
        return data

    def export_data_to_csv(self, data, filename):
        """ Writes the provided data to a CSV file specified by filename. """
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Writing cars data
            writer.writerow(['car_id', 'car_reg', 'car_make', 'car_year'])
            for car in data['cars']:
                writer.writerow(car)
            # Writing customers data
            writer.writerow([])
            writer.writerow(['customer_id', 'customer_name', 'customer_number', 'customer_email'])
            for customer in data['customers']:
                writer.writerow(customer)
            # Writing rentals data
            writer.writerow([])
            writer.writerow(['rental_id', 'car_id', 'customer_id', 'start_date'])
            for rental in data['rentals']:
                writer.writerow(rental)

    def export_data_to_xml(self, data, filename):
        root = ET.Element("CarRentalData")

        # Create and append customer elements
        cars_element = ET.SubElement(root, "Cars")
        for car in data['cars']:
            cars_element = ET.SubElement(customers_element, "Car")
            cars_element.set('car_id', str(car[0]))
            ET.SubElement(cars_element, "car_reg").text = str(car[1])
            ET.SubElement(cars_element, "car_make").text = str(car[2])
            ET.SubElement(cars_element, "car_year").text = str(car[3])

        # Create and append customer elements
        customers_element = ET.SubElement(root, "Customers")
        for customer in data['customers']:
            customer_element = ET.SubElement(customers_element, "Customer")
            customer_element.set('customer_id', str(customer[0]))
            ET.SubElement(customer_element, "customer_name").text = str(customer[1])
            ET.SubElement(customer_element, "customer_number").text = str(customer[2])
            ET.SubElement(customer_element, "customer_email").text = str(customer[3])

        # Create and append rental elements
        rentals_element = ET.SubElement(root, "Rentals")
        for rental in data['rentals']:
            rental_element = ET.SubElement(rentals_element, "Rental")
            rental_element.set('rental_id', str(rental[0]))
            ET.SubElement(rental_element, "car_id").text = str(rental[1])
            ET.SubElement(rental_element, "customer_id").text = str(rental[2])
            ET.SubElement(rental_element, "start_date").text = str(rental[3])

        # Write to file
        tree = ET.ElementTree(root)
        with open(filename, 'wb') as file:  # Note 'wb' to write bytes, which is needed for xml_declaration
            tree.write(file, encoding='utf-8', xml_declaration=True)

        print(f"Data successfully exported to {filename}")


    def export_data_to_json(self, data, filename):
        """ Writes the provided data to a JSON file specified by filename. """
        json_data = {
            'cars': [dict(zip(['car_id', 'car_reg', 'car_make', 'car_year'], car)) for car in data['cars']],
            'customers': [dict(zip(['customer_id', 'customer_name', 'customer_number', 'customer_email'], customer)) for customer in data['customers']],
            'rentals': [dict(zip(['rental_id', 'car_id', 'customer_id', 'start_date'], rental)) for rental in data['rentals']]
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
