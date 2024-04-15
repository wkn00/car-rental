import sys
from ui.ui_home import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.car_interface import CarInterface
from interfaces.customer_interface import CustomerInterface
from interfaces.rental_interface import RentalInterface
from interfaces.search_interface import SearchInterface

class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.setupUi(self)

        self.car_interface = CarInterface(self)
        self.customer_interface = CustomerInterface(self)
        self.rental_interface = RentalInterface(self)
        self.search_interface = SearchInterface(self)

        self.pages_stack.setCurrentIndex(0)  # Default page
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyApplication()
    mainWin.setFixedSize(mainWin.size()) # Disable resizing
    mainWin.show()
    sys.exit(app.exec())
