from PySide6.QtWidgets import QListWidgetItem
from data_access.cars_database import CarDatabase
from data_access.customers_database import CustomerDatabase
from PySide6.QtCore import Qt

class SearchInterface:
    def __init__(self, main_window):
        self.main_window = main_window  # Reference to the main application window
        self.car_database = CarDatabase()  # Instance for accessing car database operations
        self.customer_database = CustomerDatabase()  # Instance for accessing customer database operations
        
        # Setup connections between UI elements and the corresponding methods
        self.main_window.searchMenu.clicked.connect(self.displaySearchPage)
        self.main_window.searchCarButton.clicked.connect(self.search_car)
        self.main_window.searchCustomerButton.clicked.connect(self.search_customer)
        self.connect_uppercase(self.main_window.searchCar)

    def displaySearchPage(self):
        # Display the search page and update the page label
        self.main_window.pages_stack.setCurrentIndex(3)
        self.main_window.page_name_label.setText("Car Rental - Search Page")

    def connect_uppercase(self, line_edit):
        line_edit.textChanged.connect(lambda text, le=line_edit: le.setText(text.upper()))

    def search_car(self):
        # Retrieves cars from the database based on registration number and updates the list widget
        registration_number = self.main_window.searchCar.text().strip()
        results = self.car_database.search_cars_by_registration(registration_number)
        self.main_window.carsList.clear()
        if results:
            for car in results:
                # Determine if the car is assigned and display appropriate text
                assigned_text = f", Assigned by: {car[4]}" if car[4] else ", Not assigned"
                item_text = f"ID: {car[0]}, Reg: {car[1]}, Make: {car[2]}, Year: {car[3]}{assigned_text}"
                item = QListWidgetItem(item_text)
                item.setTextAlignment(Qt.AlignCenter)  # Center the text horizontally
                self.main_window.carsList.addItem(item)
        else:
            item = QListWidgetItem("No cars found with the given registration number.")
            item.setTextAlignment(Qt.AlignCenter)
            self.main_window.carsList.addItem(item)

    def search_customer(self):
        mobile_number = self.main_window.searchCustomer.text().strip()
        results = self.customer_database.search_customers_by_mobile(mobile_number)
        self.main_window.customerList.clear()
        
        if results:
            grouped_results = {}
            for result in results:
                customer_id = result[0]
                if customer_id not in grouped_results:
                    grouped_results[customer_id] = {
                        "info": f"ID: {result[0]}, Name: {result[1]}, Mobile: {result[2]}, Email: {result[3]}",
                        "cars": []
                    }
                if result[4]:  # Checking if there is a car assigned (i.e., car_reg is not None)
                    grouped_results[customer_id]["cars"].append(
                        f"Assigned Car: Registration Number: {result[4]}, Make: {result[5]}, Year: {result[6]}"
                    )
            
            # Now populate the QListWidget
            for customer_data in grouped_results.values():
                customer_item = QListWidgetItem(customer_data["info"])
                customer_item.setTextAlignment(Qt.AlignCenter)
                self.main_window.customerList.addItem(customer_item)
                if customer_data["cars"]:
                    for car in customer_data["cars"]:
                        car_item = QListWidgetItem(f"    {car}")  # Indent car information for better readability
                        car_item.setTextAlignment(Qt.AlignCenter)
                        self.main_window.customerList.addItem(car_item)
                else:
                    no_car_item = QListWidgetItem("    No assigned cars")
                    no_car_item.setTextAlignment(Qt.AlignCenter)
                    self.main_window.customerList.addItem(no_car_item)
        else:
            item = QListWidgetItem("No customers found with the given mobile number.")
            item.setTextAlignment(Qt.AlignCenter)
            self.main_window.customerList.addItem(item)
