from PySide6.QtWidgets import QListWidgetItem
from data_access.cars_database import CarDatabase
from data_access.customers_database import CustomerDatabase
from PySide6.QtCore import Qt

class SearchInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.car_database = CarDatabase()
        self.customer_database = CustomerDatabase()
        
        self.main_window.searchMenu.clicked.connect(self.displaySearchPage)

        self.main_window.searchCarButton.clicked.connect(self.search_car)
        self.main_window.searchCustomerButton.clicked.connect(self.search_customer)

    def displaySearchPage(self):
        self.main_window.pages_stack.setCurrentIndex(3)
        self.main_window.page_name_label.setText("Car Rental - Search Page")

    def search_car(self):
        registration_number = self.main_window.searchCar.text().strip()
        results = self.car_database.search_cars_by_registration(registration_number)
        self.main_window.carsList.clear()
        if results:
            for car in results:
                # Check if the car is assigned and provide a clear message if not.
                assigned_text = f", Assigned by: {car[4]}" if car[4] else ", Not assigned"
                item_text = f"ID: {car[0]}, Reg: {car[1]}, Make: {car[2]}, Year: {car[3]}{assigned_text}"
                item = QListWidgetItem(item_text)
                item.setTextAlignment(Qt.AlignCenter)  # Set the text alignment to center
                self.main_window.carsList.addItem(item)
        else:
            item = QListWidgetItem("No cars found with the given registration number.")
            item.setTextAlignment(Qt.AlignCenter)  # Set the text alignment to center
            self.main_window.carsList.addItem(item)

    def search_customer(self):
        mobile_number = self.main_window.searchCustomer.text().strip()
        results = self.customer_database.search_customers_by_mobile(mobile_number)
        self.main_window.customerList.clear()
        if results:
            for customer in results:
                # Formulate the customer information and conditionally add car assignment info.
                customer_info = f"ID: {customer[0]}, Name: {customer[1]}, Mobile: {customer[2]}, Email: {customer[3]}"
                car_info = f"Assigned Car: Registration Number: {customer[4]}, Make: {customer[5]}, Year: {customer[6]}" if customer[4] else "No assigned cars"
                item_text = f"{customer_info}\n{car_info}"
                item = QListWidgetItem(item_text)
                item.setTextAlignment(Qt.AlignCenter)  # Set the text alignment to center
                self.main_window.customerList.addItem(item)
        else:
            item = QListWidgetItem("No customers found with the given mobile number.")
            item.setTextAlignment(Qt.AlignCenter)  # Set the text alignment to center
            self.main_window.customerList.addItem(item)
