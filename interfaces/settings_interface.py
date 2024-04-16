from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog

import json
import csv
import xml.etree.ElementTree as ET

class SettingsInterface:
    def __init__(self, main_window):
        self.main_window = main_window


        self.main_window.settingsFrame.hide()
        self.main_window.settingsMenu.clicked.connect(self.displaySettingsPage)

        #self.main_window.importButton.clicked.connect(self.import_from_json)
        self.main_window.exportButton.clicked.connect(self.showExportButtons)

        self.main_window.exportJson.clicked.connect(self.export_data_to_json)  # Connect the export to JSON button
        self.main_window.exportXml.clicked.connect(self.export_data_to_xml)  # Connect the export to XML button
        self.main_window.exportCsv.clicked.connect(self.export_data_to_csv)  # Connect the export to CSV button

    def showExportButtons(self):
        self.main_window.exportButton.hide()
        self.main_window.settingsFrame.show()
        self.main_window.exportJson.show()
        self.main_window.exportXml.show()
        self.main_window.exportCsv.show()


    def displaySettingsPage(self):
        self.main_window.pages_stack.setCurrentIndex(4)
        self.main_window.page_name_label.setText("Car Rental - Settings Page")
        self.main_window.settingsFrame.hide()
        self.main_window.exportButton.show()


    @Slot()
    def export_data_to_csv(self):
        file_name, _ = QFileDialog.getSaveFileName(self.main_window, "Save File", "", "CSV Files (*.csv)")
        if file_name:
            data = self.fetch_data_from_database()
            self.write_data_to_csv(data, file_name)

    def write_data_to_csv(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Writing cars data with headers
            writer.writerow(['Car ID', 'Car Registration', 'Car Make', 'Car Year'])
            for car in data['cars']:
                writer.writerow(car)  # Assuming each tuple in 'cars' corresponds directly to these columns

            # Writing a separator between different sections
            writer.writerow([])
            writer.writerow(['Customer ID', 'Customer Name', 'Customer Number', 'Customer Email'])
            for customer in data['customers']:
                writer.writerow(customer)  # Assuming each tuple in 'customers' corresponds directly to these columns

            # Another separator
            writer.writerow([])
            writer.writerow(['Rental ID', 'Car ID', 'Customer ID', 'Start Date'])
            for rental in data['rentals']:
                writer.writerow(rental)  # Assuming each tuple in 'rentals' corresponds directly to these columns

        QMessageBox.information(self.main_window, "Data successfully exported as CSV to", filename)
        print("Data successfully exported to", filename)
    

    @Slot()
    def export_data_to_xml(self):
        file_name, _ = QFileDialog.getSaveFileName(self.main_window, "Save File", "", "XML Files (*.xml)")
        if file_name:
            data = self.fetch_data_from_database()
            self.write_data_to_xml(data, file_name)

    def write_data_to_xml(self, data, filename):
        root = ET.Element("CarRentalData")

        # Create and append customer elements
        customers_element = ET.SubElement(root, "Customers")
        for customer in data['customers']:
            customer_element = ET.SubElement(customers_element, "Customer")
            customer_element.set('id', str(customer[0]))
            ET.SubElement(customer_element, "Name").text = str(customer[1])
            ET.SubElement(customer_element, "Number").text = str(customer[2])
            ET.SubElement(customer_element, "Email").text = str(customer[3])

        # Create and append rental elements
        rentals_element = ET.SubElement(root, "Rentals")
        for rental in data['rentals']:
            rental_element = ET.SubElement(rentals_element, "Rental")
            rental_element.set('id', str(rental[0]))
            ET.SubElement(rental_element, "CarID").text = str(rental[1])
            ET.SubElement(rental_element, "CustomerID").text = str(rental[2])
            ET.SubElement(rental_element, "StartDate").text = str(rental[3])

        # Using a file object to write XML
        with open(filename, 'wb') as file:  # Note: 'wb' for binary write mode
            tree = ET.ElementTree(root)
            tree.write(file, encoding='utf-8', xml_declaration=True)

        QMessageBox.information(self.main_window, "Export Success", f"Data successfully exported as XML to {filename}")
        print("Data successfully exported to", filename)

    @Slot()
    def export_data_to_json(self):
        file_name, _ = QFileDialog.getSaveFileName(self.main_window, "Save File", "", "JSON Files (*.json)")
        if file_name:
            data = self.fetch_data_from_database()
            self.write_data_to_json(data, file_name)

    def write_data_to_json(self, data, filename):
        # Transforming data into a serializable format
        json_data = {
            'cars': [dict(zip(['id', 'registration', 'make', 'year'], car)) for car in data['cars']],
            'customers': [dict(zip(['id', 'name', 'number', 'email'], customer)) for customer in data['customers']],
            'rentals': [dict(zip(['id', 'car_id', 'customer_id', 'start_date'], rental)) for rental in data['rentals']]
        }

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

        QMessageBox.information(self.main_window, "Data successfully exported as JSON to", filename)
        print("Data successfully exported to", filename)