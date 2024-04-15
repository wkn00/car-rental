from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from data_access.rental_database import RentalDatabase
from data_access.customer_database import CustomerDatabase
from data_access.car_database import CarDatabase

class RentalInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.rental_database = RentalDatabase()
        self.customer_database = CustomerDatabase()
        self.car_database = CarDatabase()

        self.main_window.updateTable = self.update_table
        self.main_window.rentalMenu.clicked.connect(self.displayRentalPage)
        self.main_window.rentalStartButton.clicked.connect(self.start_rental)
        self.main_window.rentalEndButton.clicked.connect(self.end_rental)
        self.update_table()


    def displayRentalPage(self):
        self.main_window.pages_stack.setCurrentIndex(2)
        self.main_window.page_name_label.setText("Car Rental - Rentals Page")

    def start_rental(self):
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
        rental_id = self.main_window.rentalRentalID.text().strip()  # Ensure this is the correct QLineEdit name
        if rental_id.isdigit():
            rental_details = self.rental_database.get_rental_by_id(rental_id)
            if rental_details:
                confirm_msg = QMessageBox.question(self.main_window, 'Confirm Deletion',
                                                "Are you sure you want to end this rental?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if confirm_msg == QMessageBox.Yes:
                    self.rental_database.delete_rental(rental_id)
                    QMessageBox.information(self.main_window, "Rental Ended", "The rental has been successfully ended.")
                    self.update_table()  # Refresh the table to reflect the rental has ended
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No rental found with the provided ID.')
        else:
            QMessageBox.warning(self.main_window, "Input Error", "Please enter a valid numeric rental ID.")

        self.main_window.rentalRentalID.clear()  # Clear the input field after processing


    def update_table(self):
        rows = self.rental_database.get_all_rentals()
        self.main_window.rentalTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.rentalTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.rentalTable.verticalHeader().setVisible(False)


