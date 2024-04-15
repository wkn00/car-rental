from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from data_access.rental_database import RentalDatabase

class RentalInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.rental_database = RentalDatabase()

        self.main_window.updateTable = self.update_table
        self.main_window.rentalMenu.clicked.connect(self.displayRentalPage) 

        self.main_window.rentalStartButton.clicked.connect(self.start_rental)
        
        self.update_table()

    def displayRentalPage(self):
        # Set the current index of pages_stack to 2 (Rental page)
        self.main_window.pages_stack.setCurrentIndex(2)
        self.main_window.page_name_label.setText("Car Rental - Rentals")

    def start_rental(self):
        car_id = self.main_window.rentalCarID.text().strip()
        customer_id = self.main_window.rentalCustomerID.text().strip()

        if car_id.isdigit() and customer_id.isdigit():
            self.rental_database.start_rental(car_id, customer_id)
            QMessageBox.information(self.main_window, 'Rental Started', 'The rental has been successfully started.')
            self.main_window.rentalCarID.clear()
            self.main_window.rentalCustomerID.clear()
            self.update_table()
        else:
            QMessageBox.warning(self.main_window, 'Input Error', 'Please enter valid numeric IDs for both car and customer.')


    def update_table(self):
        rows = self.rental_database.get_all_rentals()

        self.main_window.rentalTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.rentalTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.rentalTable.verticalHeader().setVisible(False)
