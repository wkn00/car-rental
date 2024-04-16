import sys
from ui.ui_home import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.car_interface import CarInterface
from interfaces.customer_interface import CustomerInterface
from interfaces.rental_interface import RentalInterface
from interfaces.search_interface import SearchInterface
from interfaces.settings_interface import SettingsInterface
from data_access.database_manager import check_and_initialize

class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.setupUi(self)  # Setup UI from the generated UI Python file

        # Check and initialize the database to ensure all necessary tables are present
        check_and_initialize()

        # Instantiate interfaces for handling different functionalities within the application
        self.car_interface = CarInterface(self)
        self.customer_interface = CustomerInterface(self)
        self.rental_interface = RentalInterface(self)
        self.search_interface = SearchInterface(self)
        self.settings_interface = SettingsInterface(self)

        self.pages_stack.setCurrentIndex(0)  # Set the default page to be displayed at startup

# The entry point of the application
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the QApplication object
    mainWin = MyApplication()  # Create the main window object
    mainWin.setFixedSize(mainWin.size()) # Prevent resizing of the main window
    mainWin.show()  # Show the main window
    sys.exit(app.exec())  # Execute the application and exit when closed
