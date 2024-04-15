import sys
from PyQt5 import QtWidgets, uic
import sqlite3

class MyApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        uic.loadUi('ui/home.ui', self)
        
        self.carTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.customerTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        self.car_addRadio.toggled.connect(self.handleCarAddRadioToggle)

        # Connect the buttons
        self.addCarButton.clicked.connect(self.addCar)

        # Connect the buttons to the functions
        self.carsMenu.clicked.connect(self.displayCarsPage)
        self.customersMenu.clicked.connect(self.displayCustomersPage)

        # Initialize the database
        self.initDB()

    def displayCarsPage(self):
        # Set the current index of pages_stack to 0 (car_page)
        self.pages_stack.setCurrentIndex(0)
        self.page_name_label.setText("Cars Page")

    def displayCustomersPage(self):
        # Set the current index of pages_stack to 1 (customer_page)
        self.pages_stack.setCurrentIndex(1)
        self.page_name_label.setText("Customers Page")

    def handleCarAddRadioToggle(self, checked):
        if checked:  # If the radio button is checked, show the second page (index 1)
            self.car_action_stack.setCurrentIndex(1)
        else:  # Optional: if you want to reset to the first page when unchecked
            self.car_action_stack.setCurrentIndex(0)

    def initDB(self):
        self.connection = sqlite3.connect("cars.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS cars")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cars (
                                id INTEGER PRIMARY KEY,
                                car_brand TEXT,
                                car_year TEXT,
                                car_plate TEXT,
                                car_color TEXT)""")
        self.connection.commit()

    def addCar(self):
        # Get data from LineEdits
        carBrand = self.brandInput.text()
        carYear = self.yearInput.text()
        carPlate = self.plateInput.text()
        carColor = self.colorInput.text()

        # Insert data into the database
        self.cursor.execute("INSERT INTO cars (car_brand, car_year, car_plate, car_color) VALUES (?, ?, ?, ?)",
                            (carBrand, carYear, carPlate, carColor))
        self.connection.commit()

        # Clear LineEdits
        self.brandInput.clear()
        self.yearInput.clear()
        self.plateInput.clear()
        self.colorInput.clear()

        # Update the table
        self.updateTable()

    def updateTable(self):
        self.cursor.execute("SELECT * FROM cars")
        rows = self.cursor.fetchall()

        self.carTable.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, column_data in enumerate(row_data):
                self.carTable.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(column_data)))
        self.carTable.verticalHeader().setVisible(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MyApplication()
    mainWin.show()
    sys.exit(app.exec_())
