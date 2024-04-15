from PySide6.QtWidgets import QListWidgetItem
from data_access.car_database import CarDatabase
from data_access.customer_database import CustomerDatabase

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
                item = QListWidgetItem(f"ID: {car[0]}, Reg: {car[1]}, Make: {car[2]}, Year: {car[3]}")
                self.main_window.carsList.addItem(item)
        else:
            self.main_window.carsList.addItem("No cars found with the given registration number.")

    def search_customer(self):
        mobile_number = self.main_window.searchCustomer.text().strip()
        results = self.customer_database.search_customers_by_mobile(mobile_number)
        self.main_window.customerList.clear()
        if results:
            for customer in results:
                item = QListWidgetItem(f"ID: {customer[0]}, Name: {customer[1]}, Mobile: {customer[2]}, Email: {customer[3]}")
                self.main_window.customerList.addItem(item)
        else:
            self.main_window.customerList.addItem("No customers found with the given mobile number.")
