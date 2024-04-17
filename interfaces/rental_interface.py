from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from data_access.rentals_database import RentalDatabase
from data_access.customers_database import CustomerDatabase
from data_access.cars_database import CarDatabase

class RentalInterface:
    def __init__(self, main_window):
        self.main_window = main_window  # Main window of the application where the UI components are contained
        self.rental_database = RentalDatabase()  # Instance to access rental database operations
        self.customer_database = CustomerDatabase()  # Instance to access customer database operations
        self.car_database = CarDatabase()  # Instance to access car database operations

        self.main_window.updateTable = self.update_table  # Linking the update table method to the UI
        self.main_window.rentalMenu.clicked.connect(self.displayRentalPage)
        self.main_window.rentalStartButton.clicked.connect(self.start_rental)
        self.main_window.rentalEndButton.clicked.connect(self.end_rental)
        self.update_table()  # Initial call to populate the rental table

    def displayRentalPage(self):
        # Sets the rental page as the current view
        self.main_window.pages_stack.setCurrentIndex(2)
        self.main_window.page_name_label.setText("Car Rental - Rentals Page")

    def start_rental(self):
        # Initiates a new rental if valid IDs are provided and the car is not already rented
        car_id = self.main_window.rentalCarID.text().strip()
        customer_id = self.main_window.rentalCustomerID.text().strip()
        if car_id.isdigit() and customer_id.isdigit():
            if self.car_database.car_exists(car_id) and self.customer_database.customer_exists(customer_id):
                if not self.rental_database.start_rental(car_id, customer_id):
                    QMessageBox.warning(self.main_window, "Rental Failed", "This car is already assigned to a customer.")
                else:
                    QMessageBox.information(self.main_window, "Rental Started", "Car has been successfully assigned to a customer.")
                    self.update_table()
            else:
                QMessageBox.warning(self.main_window, "Non-existent Entities", "Either the car or customer does not exist.")
        else:
            QMessageBox.warning(self.main_window, "Input Error", "Please enter valid numeric IDs for both car and customer.")
        self.main_window.rentalCarID.clear()
        self.main_window.rentalCustomerID.clear()

    def end_rental(self):
        # Ends a rental based on the given rental ID after confirmation
        rental_id = self.main_window.rentalRentalID.text().strip()
        if rental_id.isdigit():
            rental_details = self.rental_database.get_rental_by_id(rental_id)
            if rental_details:
                confirm_msg = QMessageBox.question(self.main_window, 'Confirm Deletion', "Are you sure you want to end this rental?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if confirm_msg == QMessageBox.Yes:
                    self.rental_database.delete_rental(rental_id)
                    QMessageBox.information(self.main_window, "Rental Ended", "The rental has been successfully ended.")
                    self.update_table()
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No rental found with the provided ID.')
        else:
            QMessageBox.warning(self.main_window, "Input Error", "Please enter a valid numeric rental ID.")
        self.main_window.rentalRentalID.clear()

    def update_table(self):
        # Updates the rental table with the current data from the database
        rows = self.rental_database.get_all_rentals()
        self.main_window.rentalTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.rentalTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.rentalTable.verticalHeader().setVisible(False)