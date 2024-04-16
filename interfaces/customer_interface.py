from PySide6.QtWidgets import QButtonGroup, QMessageBox, QTableWidgetItem
from data_access.customers_database import CustomerDatabase  # Importing the customer database access class

class CustomerInterface:
    def __init__(self, main_window):
        self.main_window = main_window  # Main window of the application where the UI components are contained
        self.customer_database = CustomerDatabase()  # Instance of the CustomerDatabase to handle database operations

        self.main_window.updateTable = self.update_table  # Linking the update table method to the UI
        self.main_window.customersMenu.clicked.connect(self.displayCustomersPage)

        self.main_window.customer_action_stack.setCurrentIndex(0)  # Setting the initial view to the first page of the customer actions
        self.main_window.customerRadioGroup = QButtonGroup(self.main_window)  # Grouping radio buttons for customer actions

        # Adding radio buttons to the group and setting their actions
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_addRadio)
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_editRadio)
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_deleteRadio)
        self.main_window.customerRadioGroup.buttonToggled.connect(self.handleCustomerRadioToggle)

        # Connecting buttons for adding, editing, and deleting customers
        self.main_window.customerAddButton.clicked.connect(self.add_customer)
        self.main_window.customerEditButton.clicked.connect(self.edit_customer)
        self.main_window.customerRemoveButton.clicked.connect(self.remove_customer)

        self.main_window.customerEditCustomerID.editingFinished.connect(self.populate_customer_details)

        self.update_table()  # Initial call to populate the customer table

    def displayCustomersPage(self):
        # Sets the customer page as the current view
        self.main_window.pages_stack.setCurrentIndex(1)
        self.main_window.page_name_label.setText("Car Rental - Customers Page")

    def handleCustomerRadioToggle(self, button, checked):
        # Handles the toggling between different customer management options (add, edit, delete)
        if checked:
            index = {
                self.main_window.customer_addRadio: 1,
                self.main_window.customer_editRadio: 2,
                self.main_window.customer_deleteRadio: 3
            }.get(button, 0)
            self.main_window.customer_action_stack.setCurrentIndex(index)
            self.main_window.page_name_label.setText(f"Car Rental - Customers - {button.text()}")

    def add_customer(self):
        # Adds a new customer to the database
        customerName = self.main_window.customerName.text()
        customerNumber = self.main_window.customerNumber.text()
        customerEmail = self.main_window.customerEmail.text()
        self.customer_database.add_customer(customerName, customerNumber, customerEmail)
        self.main_window.customerName.clear()
        self.main_window.customerNumber.clear()
        self.main_window.customerEmail.clear()
        self.update_table()

    def edit_customer(self):
        # Edits an existing customer's details
        customer_id = self.main_window.customerEditCustomerID.text().strip()
        if not customer_id.isdigit():
            QMessageBox.warning(self.main_window, 'Input Error', 'Customer ID must be a numeric value.')
            return
        customerName = self.main_window.customerEditName.text().strip()
        customerNumber = self.main_window.customerEditNumber.text().strip()
        customerEmail = self.main_window.customerEditEmail.text().strip()
        self.customer_database.edit_customer(customer_id, customerName, customerNumber, customerEmail)
        QMessageBox.information(self.main_window, 'Success', 'Customer information updated successfully.')
        self.update_table()

    def populate_customer_details(self):
        # Fills in the customer details for editing when a customer ID is entered
        customer_id = self.main_window.customerEditCustomerID.text().strip()
        if customer_id.isdigit():
            customer_details = self.customer_database.get_customer_by_id(customer_id)
            if customer_details:
                self.main_window.customerEditName.setText(customer_details[1])
                self.main_window.customerEditNumber.setText(str(customer_details[2]))
                self.main_window.customerEditEmail.setText(customer_details[3])
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No customer found with the provided ID.')

    def remove_customer(self):
        # Removes a customer from the database
        customer_id = self.main_window.customerRemoveCustomerID.text().strip()
        if customer_id.isdigit() and self.customer_database.get_customer_by_id(customer_id):
            confirm_msg = QMessageBox.question(self.main_window, 'Confirm Deletion', "Are you sure you want to delete this customer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_msg == QMessageBox.Yes:
                self.customer_database.delete_customer(customer_id)
                QMessageBox.information(self.main_window, 'Success', 'Customer has been deleted successfully.')
                self.update_table()
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No customer found with the provided ID.')

    def update_table(self):
        # Updates the customer table with the current data from the database
        rows = self.customer_database.get_all_customers()
        self.main_window.customerTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.customerTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.customerTable.verticalHeader().setVisible(False)
