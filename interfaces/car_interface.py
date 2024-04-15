from PySide6.QtWidgets import QButtonGroup, QHeaderView, QTableWidgetItem
from services.car_service import CarService

class CarInterface:
    def __init__(self, main_window):

        self.main_window = main_window
        self.car_service = CarService()

        self.main_window.carsMenu.toggle()
        self.main_window.updateTable = self.update_table
        self.main_window.car_action_stack.setCurrentIndex(0)

        self.main_window.carsMenu.clicked.connect(self.displayCarsPage)

        # Set the stretch mode for the horizontal header of the carTable
        self.main_window.carTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Create the button group
        self.main_window.carRadioGroup = QButtonGroup(self.main_window)
        
        # Add radio buttons to the group
        self.main_window.carRadioGroup.addButton(self.main_window.car_addRadio)
        self.main_window.carRadioGroup.addButton(self.main_window.car_editRadio)
        self.main_window.carRadioGroup.addButton(self.main_window.car_deleteRadio)
        self.main_window.carRadioGroup.buttonToggled.connect(self.handleCarRadioToggle)

        self.main_window.carAddButton.clicked.connect(self.add_car)

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
        car_RegistrationNumber = self.main_window.registrationNumber.text()
        car_Make = self.main_window.make.text()
        car_Year = self.main_window.year.text()
        car_Color = self.main_window.color.text()

        self.car_service.add_new_car(car_RegistrationNumber, car_Make, car_Year, car_Color)

        self.main_window.registrationNumber.clear()
        self.main_window.make.clear()
        self.main_window.year.clear()
        self.main_window.color.clear()

        self.update_table()

    def update_table(self):
        rows = self.car_service.get_all_cars()

        self.main_window.carTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.main_window.carTable.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
        self.main_window.carTable.verticalHeader().setVisible(False)
