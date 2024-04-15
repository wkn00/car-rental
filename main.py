import sys
from ui.ui_home import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.car_interface import CarInterface
from interfaces.customer_interface import CustomerInterface

class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.setupUi(self)
        self.car_interface = CarInterface(self)
        self.car_customer = CustomerInterface(self)

        self.pages_stack.setCurrentIndex(0)  # Default page
        
    def closeEvent(self, event):
        # Close database connection if it's open
        if hasattr(self, 'car_interface'):
            self.car_interface.car_service.database_access.close()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyApplication()
    mainWin.show()
    sys.exit(app.exec())
