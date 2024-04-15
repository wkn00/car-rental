from PySide6.QtWidgets import QButtonGroup, QHeaderView, QTableWidgetItem
from data_access.customer_database import CustomerDatabase

class CustomerInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.customer_database = CustomerDatabase()  #fix name to car_database

        self.main_window.updateTable = self.update_table
        self.main_window.customersMenu.clicked.connect(self.displayCustomersPage)

        self.main_window.customer_action_stack.setCurrentIndex(0)

        #self.main_window.customerTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Create the button group
        self.main_window.customerRadioGroup = QButtonGroup(self.main_window)
        
        # Add radio buttons to the group
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_addRadio)
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_editRadio)
        self.main_window.customerRadioGroup.addButton(self.main_window.customer_deleteRadio)

        self.main_window.customerAddButton.clicked.connect(self.add_customer)

        self.main_window.customerRadioGroup.buttonToggled.connect(self.handleCarRadioToggle)

        self.update_table()

    def displayCustomersPage(self):
        # Set the current index of pages_stack to 0 (car_page)
        self.main_window.pages_stack.setCurrentIndex(1)
        self.main_window.page_name_label.setText("Car Rental - Customers")

    def handleCarRadioToggle(self, button, checked):
        # This function will be called whenever any radio button's checked state changes
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

    def update_table(self):
        rows = self.customer_database.get_all_customers()

        self.main_window.customerTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.customerTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.customerTable.verticalHeader().setVisible(False)

