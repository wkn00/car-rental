# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 798)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 1px solid #E0E0E0;\n"
"    gridline-color: #E0E0E0;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #E7F3FF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F5F5F5;\n"
"    padding: 4px;\n"
"    border: 1px solid #E0E0E0;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(95, 165, 247);\n"
"    color: rgb(0, 10, 52);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003d7a;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #a0a0a0;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QSpinBox {\n"
"    padding: 5px;\n"
"    margin: 2px;\n"
"    background-color: white;\n"
"    border: 1px solid #cccccc;\n"
"}\n"
"\n"
"QLineEdit:focus, QComboBox:focus, QSpinBox:focus {\n"
""
                        "    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #F5F5F5;\n"
"    width: 10px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #BEBEBE;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* Adjust the sidebar styles according to your widget type, here assuming it's a QFrame */\n"
"QFrame#Sidebar {\n"
"    background-color: #2D3E50;\n"
"}\n"
"\n"
"QLabel#SidebarLabel {\n"
"    color: #F5F5F5;\n"
"}\n"
"\n"
"/* You can also add styles for QMenuBar, QStatusBar, QDialog, etc. */\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icon_widget = QWidget(self.centralwidget)
        self.icon_widget.setObjectName(u"icon_widget")
        self.icon_widget.setGeometry(QRect(0, 0, 211, 801))
        self.icon_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QRadioButton{\n"
"	background-color: rgb(95, 165, 247);\n"
"	border-radius: 9px;\n"
"	border: 2px solid black;\n"
"	padding: 3px;\n"
"	color: rgb(0, 10, 52);\n"
"	font: 600 12pt \"Segoe UI Variable Display Semib\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"	background-color: rgb(0, 10, 52);\n"
"	color: rgb(95, 165, 247);\n"
"	border-color: rgb(95, 165, 247);\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: rgb(0, 10, 52);\n"
"    color: rgb(95, 165, 247);\n"
"}")
        self.logo = QLabel(self.icon_widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(60, 20, 80, 80))
        self.logo.setMinimumSize(QSize(80, 80))
        self.logo.setMaximumSize(QSize(80, 80))
        self.logo.setPixmap(QPixmap(u":/icons/car-logo-small.png"))
        self.logo.setScaledContents(True)
        self.carsMenu = QRadioButton(self.icon_widget)
        self.carsMenu.setObjectName(u"carsMenu")
        self.carsMenu.setGeometry(QRect(50, 160, 171, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display Semib"])
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.carsMenu.setFont(font)
        self.carsMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/car3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.carsMenu.setIcon(icon)
        self.carsMenu.setIconSize(QSize(32, 32))
        self.customersMenu = QRadioButton(self.icon_widget)
        self.customersMenu.setObjectName(u"customersMenu")
        self.customersMenu.setGeometry(QRect(50, 220, 171, 41))
        self.customersMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/customer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.customersMenu.setIcon(icon1)
        self.customersMenu.setIconSize(QSize(33, 33))
        self.assignMenu = QRadioButton(self.icon_widget)
        self.assignMenu.setObjectName(u"assignMenu")
        self.assignMenu.setGeometry(QRect(50, 280, 171, 41))
        self.assignMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assignment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.assignMenu.setIcon(icon2)
        self.assignMenu.setIconSize(QSize(25, 25))
        self.searchMenu = QRadioButton(self.icon_widget)
        self.searchMenu.setObjectName(u"searchMenu")
        self.searchMenu.setGeometry(QRect(50, 340, 171, 41))
        self.searchMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchMenu.setIcon(icon3)
        self.searchMenu.setIconSize(QSize(28, 28))
        self.settingsMenu = QRadioButton(self.icon_widget)
        self.settingsMenu.setObjectName(u"settingsMenu")
        self.settingsMenu.setGeometry(QRect(50, 400, 171, 41))
        self.settingsMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsMenu.setIcon(icon4)
        self.settingsMenu.setIconSize(QSize(28, 28))
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(210, 0, 921, 801))
        self.main_menu.setStyleSheet(u"")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(0, 0, 921, 121))
        self.header_widget.setStyleSheet(u"background-color: rgb(0, 10, 52);")
        self.verticalLayout_4 = QVBoxLayout(self.header_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.page_name_label = QLabel(self.header_widget)
        self.page_name_label.setObjectName(u"page_name_label")
        self.page_name_label.setStyleSheet(u"color: rgb(95, 165, 247);\n"
"font: 600 20pt \"Segoe UI Variable Small Semibol\";\n"
"border: 2px solid rgb(95, 165, 247);\n"
"padding:15px;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.page_name_label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.page_name_label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pages_stack = QStackedWidget(self.main_menu)
        self.pages_stack.setObjectName(u"pages_stack")
        self.pages_stack.setGeometry(QRect(30, 140, 881, 641))
        self.pages_stack.setStyleSheet(u"")
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.cars_page.setStyleSheet(u"")
        self.carTable = QTableWidget(self.cars_page)
        if (self.carTable.columnCount() < 5):
            self.carTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setPointSize(7)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.carTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.carTable.setObjectName(u"carTable")
        self.carTable.setGeometry(QRect(0, 10, 631, 621))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.carTable.setFont(font2)
        self.carTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
" }")
        self.frame_5 = QFrame(self.cars_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(640, 10, 221, 621))
        self.frame_5.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 7px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.car_action_stack = QStackedWidget(self.frame_5)
        self.car_action_stack.setObjectName(u"car_action_stack")
        self.car_action_stack.setGeometry(QRect(20, 180, 193, 421))
        self.car_empty = QWidget()
        self.car_empty.setObjectName(u"car_empty")
        self.car_action_stack.addWidget(self.car_empty)
        self.add_car = QWidget()
        self.add_car.setObjectName(u"add_car")
        self.frame_3 = QFrame(self.add_car)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 10, 191, 411))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.RegistrationNumber = QLineEdit(self.frame_3)
        self.RegistrationNumber.setObjectName(u"RegistrationNumber")

        self.verticalLayout.addWidget(self.RegistrationNumber)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.Make = QLineEdit(self.frame_3)
        self.Make.setObjectName(u"Make")

        self.verticalLayout.addWidget(self.Make)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.Year = QLineEdit(self.frame_3)
        self.Year.setObjectName(u"Year")

        self.verticalLayout.addWidget(self.Year)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.Color = QLineEdit(self.frame_3)
        self.Color.setObjectName(u"Color")

        self.verticalLayout.addWidget(self.Color)

        self.addCarButton = QPushButton(self.frame_3)
        self.addCarButton.setObjectName(u"addCarButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCarButton.sizePolicy().hasHeightForWidth())
        self.addCarButton.setSizePolicy(sizePolicy)
        self.addCarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addCarButton.setStyleSheet(u"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:22px;")

        self.verticalLayout.addWidget(self.addCarButton)

        self.car_action_stack.addWidget(self.add_car)
        self.edit_car = QWidget()
        self.edit_car.setObjectName(u"edit_car")
        self.frame_6 = QFrame(self.edit_car)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 10, 191, 411))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(10)
        font3.setWeight(QFont.DemiBold)
        font3.setItalic(False)
        self.label_10.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_10)

        self.carID_new = QLineEdit(self.frame_6)
        self.carID_new.setObjectName(u"carID_new")

        self.verticalLayout_2.addWidget(self.carID_new)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3)

        self.RegistrationNumber_new = QLineEdit(self.frame_6)
        self.RegistrationNumber_new.setObjectName(u"RegistrationNumber_new")

        self.verticalLayout_2.addWidget(self.RegistrationNumber_new)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_7)

        self.Make_new = QLineEdit(self.frame_6)
        self.Make_new.setObjectName(u"Make_new")

        self.verticalLayout_2.addWidget(self.Make_new)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.Year_new = QLineEdit(self.frame_6)
        self.Year_new.setObjectName(u"Year_new")

        self.verticalLayout_2.addWidget(self.Year_new)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.color_new = QLineEdit(self.frame_6)
        self.color_new.setObjectName(u"color_new")

        self.verticalLayout_2.addWidget(self.color_new)

        self.saveEdit_button = QPushButton(self.frame_6)
        self.saveEdit_button.setObjectName(u"saveEdit_button")
        sizePolicy.setHeightForWidth(self.saveEdit_button.sizePolicy().hasHeightForWidth())
        self.saveEdit_button.setSizePolicy(sizePolicy)
        self.saveEdit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveEdit_button.setStyleSheet(u"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;")

        self.verticalLayout_2.addWidget(self.saveEdit_button)

        self.car_action_stack.addWidget(self.edit_car)
        self.delete_car = QWidget()
        self.delete_car.setObjectName(u"delete_car")
        self.frame_7 = QFrame(self.delete_car)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 30, 191, 161))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_11)

        self.carID_delete = QLineEdit(self.frame_7)
        self.carID_delete.setObjectName(u"carID_delete")

        self.verticalLayout_3.addWidget(self.carID_delete)

        self.deleteCar_button = QPushButton(self.frame_7)
        self.deleteCar_button.setObjectName(u"deleteCar_button")
        sizePolicy.setHeightForWidth(self.deleteCar_button.sizePolicy().hasHeightForWidth())
        self.deleteCar_button.setSizePolicy(sizePolicy)
        self.deleteCar_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteCar_button.setStyleSheet(u"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;")

        self.verticalLayout_3.addWidget(self.deleteCar_button)

        self.car_action_stack.addWidget(self.delete_car)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 30, 161, 121))
        self.frame_4.setStyleSheet(u"QRadioButton {\n"
"	font: 600 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QRadioButton#car_addRadio::indicator {\n"
"    border: 2px solid #004d00; /* Dark green border */\n"
"    background-color: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton#car_addRadio::indicator:checked {\n"
"    background-color: #00e600; /* Bright green for \"on\" state */\n"
"}\n"
"\n"
"QRadioButton#car_editRadio::indicator {\n"
"    border: 2px solid #666600; /* Dark yellow border */\n"
"    background-color: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton#car_editRadio::indicator:checked {\n"
"    background-color: #ffff00; /* Bright yellow for \"on\" state */\n"
"}\n"
"\n"
"QRadioButton#car_deleteRadio::indicator {\n"
"    border: 2px solid #660000; /* Dark red border */\n"
"    background-color: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton#car_deleteRadio::"
                        "indicator:checked {\n"
"    background-color: #ff0000; /* Bright red for \"on\" state */\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.car_addRadio = QRadioButton(self.frame_4)
        self.car_addRadio.setObjectName(u"car_addRadio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.car_addRadio.sizePolicy().hasHeightForWidth())
        self.car_addRadio.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.car_addRadio, 0, 0, 1, 1)

        self.car_editRadio = QRadioButton(self.frame_4)
        self.car_editRadio.setObjectName(u"car_editRadio")
        sizePolicy1.setHeightForWidth(self.car_editRadio.sizePolicy().hasHeightForWidth())
        self.car_editRadio.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.car_editRadio, 1, 0, 1, 1)

        self.car_deleteRadio = QRadioButton(self.frame_4)
        self.car_deleteRadio.setObjectName(u"car_deleteRadio")
        sizePolicy1.setHeightForWidth(self.car_deleteRadio.sizePolicy().hasHeightForWidth())
        self.car_deleteRadio.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.car_deleteRadio, 2, 0, 1, 1)

        self.pages_stack.addWidget(self.cars_page)
        self.customs_page = QWidget()
        self.customs_page.setObjectName(u"customs_page")
        self.frame_2 = QFrame(self.customs_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(690, 60, 120, 441))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.customerTable = QTableWidget(self.customs_page)
        if (self.customerTable.columnCount() < 4):
            self.customerTable.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.customerTable.setObjectName(u"customerTable")
        self.customerTable.setGeometry(QRect(50, 50, 601, 451))
        self.pages_stack.addWidget(self.customs_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.assignments = QTableWidget(self.page)
        if (self.assignments.columnCount() < 4):
            self.assignments.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.assignments.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.assignments.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.assignments.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.assignments.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.assignments.setObjectName(u"assignments")
        self.assignments.setGeometry(QRect(40, 30, 571, 491))
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(649, 39, 141, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 110, 91, 21))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 170, 113, 22))
        self.pages_stack.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_stack.setCurrentIndex(0)
        self.car_action_stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.carsMenu.setText(QCoreApplication.translate("MainWindow", u"Cars", None))
        self.customersMenu.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.assignMenu.setText(QCoreApplication.translate("MainWindow", u"Assign", None))
        self.searchMenu.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.settingsMenu.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.page_name_label.setText(QCoreApplication.translate("MainWindow", u"Car Rental", None))
        ___qtablewidgetitem = self.carTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CarID", None));
        ___qtablewidgetitem1 = self.carTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"RegistrationNumber", None));
        ___qtablewidgetitem2 = self.carTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Make", None));
        ___qtablewidgetitem3 = self.carTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Year", None));
        ___qtablewidgetitem4 = self.carTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">RegistrationNumber</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Make</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.addCarButton.setText(QCoreApplication.translate("MainWindow", u"Add Car", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">CarID</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">New RegistrationNumber</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">New Make</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"New Year", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"New Color", None))
        self.saveEdit_button.setText(QCoreApplication.translate("MainWindow", u"Edit Car", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">CarID</span></p></body></html>", None))
        self.deleteCar_button.setText(QCoreApplication.translate("MainWindow", u"Remove Car", None))
        self.car_addRadio.setText(QCoreApplication.translate("MainWindow", u"Add Car", None))
        self.car_editRadio.setText(QCoreApplication.translate("MainWindow", u"Edit Car", None))
        self.car_deleteRadio.setText(QCoreApplication.translate("MainWindow", u"Delete Car", None))
        ___qtablewidgetitem5 = self.customerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"customer_id", None));
        ___qtablewidgetitem6 = self.customerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"customer_firstname", None));
        ___qtablewidgetitem7 = self.customerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"customer_lastname", None));
        ___qtablewidgetitem8 = self.customerTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"customer_number", None));
        ___qtablewidgetitem9 = self.assignments.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Assignment_id", None));
        ___qtablewidgetitem10 = self.assignments.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"car_id", None));
        ___qtablewidgetitem11 = self.assignments.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"customer_id", None));
        ___qtablewidgetitem12 = self.assignments.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"assignment_date", None));
    # retranslateUi

