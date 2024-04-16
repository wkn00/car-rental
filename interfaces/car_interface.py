from PySide6.QtWidgets import QButtonGroup, QTableWidgetItem, QMessageBox
from data_access.cars_database import CarDatabase  # Importing the car database access class

class CarInterface:
    def __init__(self, main_window):
        self.main_window = main_window  # Main window of the application where the UI components are contained
        self.car_database = CarDatabase()  # Instance of the CarDatabase to handle database operations

        self.main_window.carsMenu.toggle()  # Automatically toggles the visibility of the cars menu
        self.main_window.updateTable = self.update_table  # Linking the update table method to the UI
        self.main_window.car_action_stack.setCurrentIndex(0)  # Setting the initial view to the first page of the car actions

        # Connecting UI elements to their respective methods
        self.main_window.carsMenu.clicked.connect(self.displayCarsPage)
        self.main_window.carRadioGroup = QButtonGroup(self.main_window)  # Grouping radio buttons for car actions
        self.main_window.carRadioGroup.addButton(self.main_window.car_addRadio)
        self.main_window.carRadioGroup.addButton(self.main_window.car_editRadio)
        self.main_window.carRadioGroup.addButton(self.main_window.car_deleteRadio)
        self.main_window.carRadioGroup.buttonToggled.connect(self.handleCarRadioToggle)

        # Connecting buttons for adding, editing, and deleting cars
        self.main_window.carAddButton.clicked.connect(self.add_car)
        self.main_window.carEditButton.clicked.connect(self.edit_car)
        self.main_window.carEditCarID.editingFinished.connect(self.populate_car_details)
        self.main_window.carRemoveButton.clicked.connect(self.remove_car)

        self.update_table()  # Initial call to populate the car table

    def displayCarsPage(self):
        # Sets the car page as the current view
        self.main_window.pages_stack.setCurrentIndex(0)
        self.main_window.page_name_label.setText("Car Rental - Cars Page")

    def handleCarRadioToggle(self, button, checked):
        # Handles the toggling between different car management options (add, edit, delete)
        if checked:
            index = {
                self.main_window.car_addRadio: 1,
                self.main_window.car_editRadio: 2,
                self.main_window.car_deleteRadio: 3
            }.get(button, 0)
            self.main_window.car_action_stack.setCurrentIndex(index)
            self.main_window.page_name_label.setText(f"Car Rental - Cars - {button.text()}")

    def add_car(self):
        # Adds a new car to the database
        carRegNumber = self.main_window.carRegNumber.text()
        carMake = self.main_window.carMake.text()
        carYear = self.main_window.carYear.text()
        self.car_database.add_car(carRegNumber, carMake, carYear)
        self.main_window.carRegNumber.clear()
        self.main_window.carMake.clear()
        self.main_window.carYear.clear()
        self.update_table()

    def edit_car(self):
        # Edits an existing car's details
        car_id = self.main_window.carEditCarID.text().strip()
        if not car_id.isdigit():
            QMessageBox.warning(self.main_window, 'Input Error', 'Car ID must be a numeric value.')
            return
        car_reg = self.main_window.carEditRegNumber.text().strip()
        car_make = self.main_window.carEditMake.text().strip()
        car_year = self.main_window.carEditYear.text().strip()
        self.car_database.edit_car(car_id, car_reg, car_make, car_year)
        QMessageBox.information(self.main_window, 'Success', 'Car information updated successfully.')
        self.update_table()

    def remove_car(self):
        # Removes a car from the database
        car_id = self.main_window.carRemoveCarID.text().strip()
        if car_id.isdigit() and self.car_database.get_car_by_id(car_id):
            confirm_msg = QMessageBox.question(self.main_window, 'Confirm Deletion', "Are you sure you want to delete this car?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm_msg == QMessageBox.Yes:
                self.car_database.delete_car(car_id)
                QMessageBox.information(self.main_window, 'Success', 'Car has been deleted successfully.')
                self.update_table()
        else:
            QMessageBox.warning(self.main_window, 'Input Error', 'Please enter a valid numeric car ID.')

    def populate_car_details(self):
        # Fills in the car details for editing when a car ID is entered
        car_id = self.main_window.carEditCarID.text().strip()
        if car_id.isdigit():
            car_details = self.car_database.get_car_by_id(car_id)
            if car_details:
                self.main_window.carEditRegNumber.setText(car_details[1])  # car registration
                self.main_window.carEditMake.setText(car_details[2])  # car make
                self.main_window.carEditYear.setText(str(car_details[3]))  # car year
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No car found with the provided ID.')

    def update_table(self):
        # Updates the car table with current data from the database
        rows = self.car_database.get_all_cars()
        self.main_window.carTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.carTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.carTable.verticalHeader().setVisible(False)
