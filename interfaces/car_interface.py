from PySide6.QtWidgets import QButtonGroup, QTableWidgetItem, QMessageBox
from data_access.car_database import CarDatabase


class CarInterface:
    def __init__(self, main_window):

        self.main_window = main_window
        self.car_database = CarDatabase()

        self.main_window.carsMenu.toggle()
        self.main_window.updateTable = self.update_table
        self.main_window.car_action_stack.setCurrentIndex(0)

        self.main_window.carsMenu.clicked.connect(self.displayCarsPage)

        #self.main_window.carTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Create the button group
        self.main_window.carRadioGroup = QButtonGroup(self.main_window)
        
        # Add radio buttons to the group
        self.main_window.carRadioGroup.addButton(self.main_window.car_addRadio)
        self.main_window.carRadioGroup.addButton(self.main_window.car_editRadio)
        self.main_window.carRadioGroup.addButton(self.main_window.car_deleteRadio)
        self.main_window.carRadioGroup.buttonToggled.connect(self.handleCarRadioToggle)

        self.main_window.carAddButton.clicked.connect(self.add_car)
        self.main_window.carEditButton.clicked.connect(self.edit_car)
        self.main_window.carEditCarID.editingFinished.connect(self.populate_car_details)
        self.main_window.carRemoveButton.clicked.connect(self.remove_car)

        self.update_table()

    def displayCarsPage(self):
        # Set the current index of pages_stack to 0 (car_page)
        self.main_window.pages_stack.setCurrentIndex(0)
        self.main_window.page_name_label.setText("Car Rental - Cars")

    def handleCarRadioToggle(self, button, checked):
        # This function will be called whenever any radio button's checked state changes
        if checked:
            if button == self.main_window.car_addRadio:
                self.main_window.car_action_stack.setCurrentIndex(1)
                self.main_window.page_name_label.setText("Car Rental - Cars - Add Car")
            elif button == self.main_window.car_editRadio:
                self.main_window.car_action_stack.setCurrentIndex(2)
                self.main_window.page_name_label.setText("Car Rental - Cars - Edit Car")
            elif button == self.main_window.car_deleteRadio:
                self.main_window.car_action_stack.setCurrentIndex(3)
                self.main_window.page_name_label.setText("Car Rental - Cars - Delete Car")
            else:
                self.main_window.car_action_stack.setCurrentIndex(0)


    def add_car(self):
        carRegNumber = self.main_window.carRegNumber.text()
        carMake = self.main_window.carMake.text()
        carYear = self.main_window.carYear.text()

        self.car_database.add_car(carRegNumber, carMake, carYear)

        self.main_window.carRegNumber.clear()
        self.main_window.carMake.clear()
        self.main_window.carYear.clear()

        self.update_table()


    def edit_car(self):
        car_id = self.main_window.carEditCarID.text().strip()
        car_reg = self.main_window.carEditRegNumber.text().strip()
        car_make = self.main_window.carEditMake.text().strip()
        car_year = self.main_window.carEditYear.text().strip()

        if not car_id.isdigit():
            QMessageBox.warning(self.main_window, 'Input Error', 'Car ID must be a numeric value.')
            return

        self.car_database.edit_car(car_id, car_reg, car_make, car_year)
        QMessageBox.information(self.main_window, 'Success', 'Car information updated successfully.')
        self.update_table()


    def populate_car_details(self):
        car_id = self.main_window.carEditCarID.text().strip()
        if car_id.isdigit():
            car_details = self.car_database.get_car_by_id(car_id)
            if car_details:
                self.main_window.carEditRegNumber.setText(car_details[1])  # car_reg
                self.main_window.carEditMake.setText(car_details[2])  # car_make
                self.main_window.carEditYear.setText(str(car_details[3]))  # car_year
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No car found with the provided ID.')
        else:
            QMessageBox.warning(self.main_window, 'Input Error', 'Please enter a valid numeric ID.')

    def remove_car(self):
        car_id = self.main_window.carRemoveCarID.text().strip()
        if car_id.isdigit():
            car_details = self.car_database.get_car_by_id(car_id)
            if car_details:
                confirm_msg = QMessageBox.question(self.main_window, 'Confirm Deletion',
                                                   "Are you sure you want to delete this car?",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if confirm_msg == QMessageBox.Yes:
                    self.car_database.delete_car(car_id)
                    QMessageBox.information(self.main_window, 'Success', 'Car has been deleted successfully.')
                    self.update_table()
            else:
                QMessageBox.warning(self.main_window, 'Not Found', 'No car found with the provided ID.')
        else:
            QMessageBox.warning(self.main_window, 'Input Error', 'Please enter a valid numeric ID.')

        # Clear the input field after processing
        self.main_window.carRemoveCarID.clear()

    def update_table(self):
        rows = self.car_database.get_all_cars()

        self.main_window.carTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.carTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.carTable.verticalHeader().setVisible(False)
