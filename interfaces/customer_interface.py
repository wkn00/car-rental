from PySide6.QtWidgets import QButtonGroup, QMessageBox, QTableWidgetItem
from data_access.customers_database import CustomerDatabase

class CustomerInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.customer_database = CustomerDatabase()

        self.main_window.updateTable = self.update_table
        self.main_window.customersMenu.clicked.connect(self.displayCustomersPage)

        self.main_window.customer_action_stack.setCurrentIndex(0)

        self.main_window.customerRadioGroup = QButtonGroup(self.main_window)

        self.main_window.customerRadioGroup.addButton(self.main_window.customer_addRadio)
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_editRadio)
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_deleteRadio)
        self.main_window.customerRadioGroup.buttonToggled.connect(self.handleCustomerRadioToggle)

        self.main_window.customerAddButton.clicked.connect(self.add_customer)
        self.main_window.customerEditButton.clicked.connect(self.edit_customer)
        self.main_window.customerRemoveButton.clicked.connect(self.remove_customer)

        self.main_window.customerEditCustomerID.editingFinished.connect(self.populate_customer_details)

        self.update_table()

    def displayCustomersPage(self):
        self.main_window.pages_stack.setCurrentIndex(1)
        self.main_window.page_name_label.setText("Car Rental - Customers Page")

    def handleCustomerRadioToggle(self, button, checked):
        if checked:
            if button == self.main_window.customer_addRadio:
                self.main_window.customer_action_stack.setCurrentIndex(1)
                self.main_window.page_name_label.setText("Car Rental - Customers - Add Customers")
            elif button == self.main_window.customer_editRadio:
                self.main_window.customer_action_stack.setCurrentIndex(2)
                self.main_window.page_name_label.setText("Car Rental - Customers - Edit Customers")
            elif button == self.main_window.customer_deleteRadio:
                self.main_window.customer_action_stack.setCurrentIndex(3)
                self.main_window.page_name_label.setText("Car Rental - Customers - Delete Customers")
            else:
                self.main_window.customer_action_stack.setCurrentIndex(0)

    def add_customer(self):
        customerName = self.main_window.customerName.text()
        customerNumber = self.main_window.customerNumber.text()
        customerEmail = self.main_window.customerEmail.text()

        self.customer_database.add_customer(customerName, customerNumber, customerEmail)

        self.main_window.customerName.clear()
        self.main_window.customerNumber.clear()
        self.main_window.customerEmail.clear()

        self.update_table()

    def edit_customer(self):
        customer_id = self.main_window.customerEditCustomerID.text().strip()
        customerName = self.main_window.customerEditName.text().strip()
        customerNumber = self.main_window.customerEditNumber.text().strip()
        customerEmail = self.main_window.customerEditEmail.text().strip()

        if not customer_id.isdigit():
            QMessageBox.warning(self.main_window, 'Input Error', 'Customer ID must be a numeric value.')
            return

        self.customer_database.edit_customer(customer_id, customerName, customerNumber, customerEmail)
        QMessageBox.information(self.main_window, 'Success', 'Customer information updated successfully.')
        self.update_table()

    def populate_customer_details(self):
        customer_id = self.main_window.customerEditCustomerID.text().strip()
        if customer_id.isdigit():
            customer_details = self.customer_database.get_customer_by_id(customer_id)
            if customer_details:
                self.main_window.customerEditName.setText(customer_details[1])
                self.main_window.customerEditNumber.setText(str(customer_details[2]))
                self.main_window.customerEditEmail.setText(customer_details[3])
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No customer found with the provided ID.')
        else:
            QMessageBox.warning(self.main_window, 'Input Error', 'Please enter a valid numeric ID.')

    def remove_customer(self):
        customer_id = self.main_window.customerRemoveCustomerID.text().strip()
        if customer_id.isdigit():
            customer_details = self.customer_database.get_customer_by_id(customer_id)
            if customer_details:
                confirm_msg = QMessageBox.question(self.main_window, 'Confirm Deletion',
                                                   "Are you sure you want to delete this customer?",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if confirm_msg == QMessageBox.Yes:
                    self.customer_database.delete_customer(customer_id)
                    QMessageBox.information(self.main_window, 'Success', 'Customer has been deleted successfully.')
                    self.update_table()
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No customer found with the provided ID.')
        else:
            QMessageBox.warning(self.main_window, 'Input Error', 'Please enter a valid numeric ID.')

        self.main_window.customerRemoveCustomerID.clear()

    def update_table(self):
        rows = self.customer_database.get_all_customers()

        self.main_window.customerTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.customerTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.customerTable.verticalHeader().setVisible(False)
