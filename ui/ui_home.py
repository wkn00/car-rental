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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
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
"\n"
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
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QScrollBar:vertical {"
                        "\n"
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
"    \n"
"	color: rgb(0, 10, 52);\n"
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
"	color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QRadioButton{\n"
"	background-color: rgb(95, 165, 247);\n"
"	border-radius: 8px;\n"
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
"	border-color: rgb(95, 165, 247);\n"
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
        self.carsMenu.setGeometry(QRect(30, 170, 150, 45))
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
        self.carsMenu.setIconSize(QSize(30, 30))
        self.customersMenu = QRadioButton(self.icon_widget)
        self.customersMenu.setObjectName(u"customersMenu")
        self.customersMenu.setGeometry(QRect(30, 240, 150, 45))
        self.customersMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.customersMenu.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/customer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.customersMenu.setIcon(icon1)
        self.customersMenu.setIconSize(QSize(30, 30))
        self.rentalMenu = QRadioButton(self.icon_widget)
        self.rentalMenu.setObjectName(u"rentalMenu")
        self.rentalMenu.setGeometry(QRect(30, 310, 150, 45))
        self.rentalMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assignment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rentalMenu.setIcon(icon2)
        self.rentalMenu.setIconSize(QSize(22, 22))
        self.searchMenu = QRadioButton(self.icon_widget)
        self.searchMenu.setObjectName(u"searchMenu")
        self.searchMenu.setGeometry(QRect(30, 380, 150, 45))
        self.searchMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchMenu.setIcon(icon3)
        self.searchMenu.setIconSize(QSize(25, 25))
        self.settingsMenu = QRadioButton(self.icon_widget)
        self.settingsMenu.setObjectName(u"settingsMenu")
        self.settingsMenu.setGeometry(QRect(30, 450, 150, 45))
        self.settingsMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsMenu.setIcon(icon4)
        self.settingsMenu.setIconSize(QSize(25, 25))
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
        self.pages_stack.setGeometry(QRect(0, 120, 931, 681))
        self.pages_stack.setStyleSheet(u"")
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.cars_page.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QStackedWidget{\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}")
        self.frame_8 = QFrame(self.cars_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(-10, 0, 931, 681))
        self.frame_8.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.carTable = QTableWidget(self.frame_8)
        if (self.carTable.columnCount() < 4):
            self.carTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.carTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.carTable.setObjectName(u"carTable")
        self.carTable.setGeometry(QRect(20, 10, 641, 651))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.carTable.setFont(font1)
        self.carTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"color: rgb(0, 10, 52);\n"
" }\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(232, 232, 232);\n"
"	\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 10, 52);\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"color: rgb(0, 10, 52);\n"
"	font: 9pt \"Segoe UI\";\n"
"\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"  background: gray;\n"
"	font: 9pt \"Segoe UI\";\n"
"\n"
"color: rgb(0, 10, 52);\n"
"  padding: 7px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
"color: rgb(0, 10, 52);\n"
" }")
        self.carTable.horizontalHeader().setDefaultSectionSize(155)
        self.carTable.horizontalHeader().setStretchLastSection(True)
        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(670, 10, 241, 651))
        self.frame_5.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 7px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.car_action_stack = QStackedWidget(self.frame_5)
        self.car_action_stack.setObjectName(u"car_action_stack")
        self.car_action_stack.setGeometry(QRect(20, 180, 193, 451))
        self.car_empty = QWidget()
        self.car_empty.setObjectName(u"car_empty")
        self.car_action_stack.addWidget(self.car_empty)
        self.add_car = QWidget()
        self.add_car.setObjectName(u"add_car")
        self.frame_3 = QFrame(self.add_car)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 10, 191, 311))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.carRegNumber = QLineEdit(self.frame_3)
        self.carRegNumber.setObjectName(u"carRegNumber")
        self.carRegNumber.setMaxLength(7)

        self.verticalLayout.addWidget(self.carRegNumber)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.carMake = QLineEdit(self.frame_3)
        self.carMake.setObjectName(u"carMake")

        self.verticalLayout.addWidget(self.carMake)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.carYear = QLineEdit(self.frame_3)
        self.carYear.setObjectName(u"carYear")
        self.carYear.setMaxLength(4)

        self.verticalLayout.addWidget(self.carYear)

        self.carAddButton = QPushButton(self.frame_3)
        self.carAddButton.setObjectName(u"carAddButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carAddButton.sizePolicy().hasHeightForWidth())
        self.carAddButton.setSizePolicy(sizePolicy)
        self.carAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.carAddButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(0, 162, 38);\n"
"	border: 1px solid rgb(0, 162, 38);\n"
"}")

        self.verticalLayout.addWidget(self.carAddButton)

        self.car_action_stack.addWidget(self.add_car)
        self.edit_car = QWidget()
        self.edit_car.setObjectName(u"edit_car")
        self.edit_car.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}")
        self.frame_6 = QFrame(self.edit_car)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 10, 191, 391))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 10, 52);\n"
"border: 0px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(10)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        self.label_10.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_10)

        self.carEditCarID = QLineEdit(self.frame_6)
        self.carEditCarID.setObjectName(u"carEditCarID")

        self.verticalLayout_2.addWidget(self.carEditCarID)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.carEditRegNumber = QLineEdit(self.frame_6)
        self.carEditRegNumber.setObjectName(u"carEditRegNumber")
        self.carEditRegNumber.setMaxLength(7)

        self.verticalLayout_2.addWidget(self.carEditRegNumber)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_7)

        self.carEditMake = QLineEdit(self.frame_6)
        self.carEditMake.setObjectName(u"carEditMake")

        self.verticalLayout_2.addWidget(self.carEditMake)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.carEditYear = QLineEdit(self.frame_6)
        self.carEditYear.setObjectName(u"carEditYear")
        self.carEditYear.setMaxLength(4)

        self.verticalLayout_2.addWidget(self.carEditYear)

        self.carEditButton = QPushButton(self.frame_6)
        self.carEditButton.setObjectName(u"carEditButton")
        sizePolicy.setHeightForWidth(self.carEditButton.sizePolicy().hasHeightForWidth())
        self.carEditButton.setSizePolicy(sizePolicy)
        self.carEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.carEditButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(150, 150, 0);\n"
"	border: 1px solid rgb(153, 153, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.carEditButton)

        self.car_action_stack.addWidget(self.edit_car)
        self.delete_car = QWidget()
        self.delete_car.setObjectName(u"delete_car")
        self.frame_7 = QFrame(self.delete_car)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 30, 191, 161))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_11)

        self.carRemoveCarID = QLineEdit(self.frame_7)
        self.carRemoveCarID.setObjectName(u"carRemoveCarID")

        self.verticalLayout_3.addWidget(self.carRemoveCarID)

        self.carRemoveButton = QPushButton(self.frame_7)
        self.carRemoveButton.setObjectName(u"carRemoveButton")
        sizePolicy.setHeightForWidth(self.carRemoveButton.sizePolicy().hasHeightForWidth())
        self.carRemoveButton.setSizePolicy(sizePolicy)
        self.carRemoveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.carRemoveButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(255, 0, 0);\n"
"	border: 1px solid rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.carRemoveButton)

        self.car_action_stack.addWidget(self.delete_car)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 30, 161, 121))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"    border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"\n"
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
"    background-colo"
                        "r: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton#car_deleteRadio::indicator:checked {\n"
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
        self.car_addRadio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.car_addRadio, 0, 0, 1, 1)

        self.car_editRadio = QRadioButton(self.frame_4)
        self.car_editRadio.setObjectName(u"car_editRadio")
        sizePolicy1.setHeightForWidth(self.car_editRadio.sizePolicy().hasHeightForWidth())
        self.car_editRadio.setSizePolicy(sizePolicy1)
        self.car_editRadio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.car_editRadio, 1, 0, 1, 1)

        self.car_deleteRadio = QRadioButton(self.frame_4)
        self.car_deleteRadio.setObjectName(u"car_deleteRadio")
        sizePolicy1.setHeightForWidth(self.car_deleteRadio.sizePolicy().hasHeightForWidth())
        self.car_deleteRadio.setSizePolicy(sizePolicy1)
        self.car_deleteRadio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.car_deleteRadio, 2, 0, 1, 1)

        self.pages_stack.addWidget(self.cars_page)
        self.customs_page = QWidget()
        self.customs_page.setObjectName(u"customs_page")
        self.customs_page.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QStackedWidget{\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}")
        self.frame_9 = QFrame(self.customs_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(-10, -10, 941, 691))
        self.frame_9.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.customerTable = QTableWidget(self.frame_9)
        if (self.customerTable.columnCount() < 4):
            self.customerTable.setColumnCount(4)
        font3 = QFont()
        font3.setPointSize(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.customerTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.customerTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.customerTable.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.customerTable.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.customerTable.setObjectName(u"customerTable")
        self.customerTable.setGeometry(QRect(20, 20, 641, 651))
        self.customerTable.setFont(font1)
        self.customerTable.setLayoutDirection(Qt.LeftToRight)
        self.customerTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"color: rgb(0, 10, 52);\n"
" }\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(232, 232, 232);\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(0, 10, 52);\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"color: rgb(0, 10, 52);\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"  background: gray;\n"
"color: rgb(0, 10, 52);\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
"color: rgb(0, 10, 52);\n"
" }")
        self.customerTable.horizontalHeader().setDefaultSectionSize(155)
        self.customerTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.customerTable.horizontalHeader().setStretchLastSection(True)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(670, 20, 241, 651))
        self.frame_10.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 7px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.customer_action_stack = QStackedWidget(self.frame_10)
        self.customer_action_stack.setObjectName(u"customer_action_stack")
        self.customer_action_stack.setGeometry(QRect(20, 180, 193, 421))
        self.customer_empty = QWidget()
        self.customer_empty.setObjectName(u"customer_empty")
        self.customer_action_stack.addWidget(self.customer_empty)
        self.add_customer = QWidget()
        self.add_customer.setObjectName(u"add_customer")
        self.frame_11 = QFrame(self.add_customer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 10, 191, 311))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.customerName = QLineEdit(self.frame_11)
        self.customerName.setObjectName(u"customerName")

        self.verticalLayout_5.addWidget(self.customerName)

        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)

        self.customerNumber = QLineEdit(self.frame_11)
        self.customerNumber.setObjectName(u"customerNumber")
        self.customerNumber.setMaxLength(8)

        self.verticalLayout_5.addWidget(self.customerNumber)

        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_5.addWidget(self.label_14)

        self.customerEmail = QLineEdit(self.frame_11)
        self.customerEmail.setObjectName(u"customerEmail")

        self.verticalLayout_5.addWidget(self.customerEmail)

        self.customerAddButton = QPushButton(self.frame_11)
        self.customerAddButton.setObjectName(u"customerAddButton")
        sizePolicy.setHeightForWidth(self.customerAddButton.sizePolicy().hasHeightForWidth())
        self.customerAddButton.setSizePolicy(sizePolicy)
        self.customerAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.customerAddButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(0, 162, 38);\n"
"	border: 1px solid rgb(0, 162, 38);\n"
"}")

        self.verticalLayout_5.addWidget(self.customerAddButton)

        self.customer_action_stack.addWidget(self.add_customer)
        self.edit_customer = QWidget()
        self.edit_customer.setObjectName(u"edit_customer")
        self.frame_12 = QFrame(self.edit_customer)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 10, 191, 391))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"  border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_16)

        self.customerEditCustomerID = QLineEdit(self.frame_12)
        self.customerEditCustomerID.setObjectName(u"customerEditCustomerID")

        self.verticalLayout_6.addWidget(self.customerEditCustomerID)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_17)

        self.customerEditName = QLineEdit(self.frame_12)
        self.customerEditName.setObjectName(u"customerEditName")

        self.verticalLayout_6.addWidget(self.customerEditName)

        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_18)

        self.customerEditNumber = QLineEdit(self.frame_12)
        self.customerEditNumber.setObjectName(u"customerEditNumber")
        self.customerEditNumber.setMaxLength(8)

        self.verticalLayout_6.addWidget(self.customerEditNumber)

        self.label_19 = QLabel(self.frame_12)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_6.addWidget(self.label_19)

        self.customerEditEmail = QLineEdit(self.frame_12)
        self.customerEditEmail.setObjectName(u"customerEditEmail")

        self.verticalLayout_6.addWidget(self.customerEditEmail)

        self.customerEditButton = QPushButton(self.frame_12)
        self.customerEditButton.setObjectName(u"customerEditButton")
        sizePolicy.setHeightForWidth(self.customerEditButton.sizePolicy().hasHeightForWidth())
        self.customerEditButton.setSizePolicy(sizePolicy)
        self.customerEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.customerEditButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(153, 153, 0);\n"
"	border: 1px solid rgb(153, 153, 0);\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.customerEditButton)

        self.customer_action_stack.addWidget(self.edit_customer)
        self.delete_customer = QWidget()
        self.delete_customer.setObjectName(u"delete_customer")
        self.frame_13 = QFrame(self.delete_customer)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 30, 191, 161))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"color: rgb(0, 10, 52);")

        self.verticalLayout_7.addWidget(self.label_21)

        self.customerRemoveCustomerID = QLineEdit(self.frame_13)
        self.customerRemoveCustomerID.setObjectName(u"customerRemoveCustomerID")

        self.verticalLayout_7.addWidget(self.customerRemoveCustomerID)

        self.customerRemoveButton = QPushButton(self.frame_13)
        self.customerRemoveButton.setObjectName(u"customerRemoveButton")
        sizePolicy.setHeightForWidth(self.customerRemoveButton.sizePolicy().hasHeightForWidth())
        self.customerRemoveButton.setSizePolicy(sizePolicy)
        self.customerRemoveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.customerRemoveButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(255, 0, 0);\n"
"	border: 1px solid rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.customerRemoveButton)

        self.customer_action_stack.addWidget(self.delete_customer)
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(30, 30, 161, 121))
        self.frame_14.setStyleSheet(u"QRadioButton {\n"
"	font: 600 10pt \"Segoe UI Semibold\";\n"
"   color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QRadioButton#customer_addRadio::indicator {\n"
"    border: 2px solid #004d00; /* Dark green border */\n"
"    background-color: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton#customer_addRadio::indicator:checked {\n"
"    background-color: #00e600; /* Bright green for \"on\" state */\n"
"}\n"
"\n"
"QRadioButton#customer_editRadio::indicator {\n"
"    border: 2px solid #666600; /* Dark yellow border */\n"
"    background-color: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton#customer_editRadio::indicator:checked {\n"
"    background-color: #ffff00; /* Bright yellow for \"on\" state */\n"
"}\n"
"\n"
"QRadioButton#customer_deleteRadio::indicator {\n"
"    border: 2px solid #660000; /* Dark red border */\n"
"    background-color: white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-rad"
                        "ius: 7px;\n"
"}\n"
"\n"
"QRadioButton#customer_deleteRadio::indicator:checked {\n"
"    background-color: #ff0000; /* Bright red for \"on\" state */\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.customer_addRadio = QRadioButton(self.frame_14)
        self.customer_addRadio.setObjectName(u"customer_addRadio")
        sizePolicy1.setHeightForWidth(self.customer_addRadio.sizePolicy().hasHeightForWidth())
        self.customer_addRadio.setSizePolicy(sizePolicy1)
        self.customer_addRadio.setCursor(QCursor(Qt.PointingHandCursor))
        self.customer_addRadio.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.customer_addRadio, 0, 0, 1, 1)

        self.customer_editRadio = QRadioButton(self.frame_14)
        self.customer_editRadio.setObjectName(u"customer_editRadio")
        sizePolicy1.setHeightForWidth(self.customer_editRadio.sizePolicy().hasHeightForWidth())
        self.customer_editRadio.setSizePolicy(sizePolicy1)
        self.customer_editRadio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.customer_editRadio, 1, 0, 1, 1)

        self.customer_deleteRadio = QRadioButton(self.frame_14)
        self.customer_deleteRadio.setObjectName(u"customer_deleteRadio")
        sizePolicy1.setHeightForWidth(self.customer_deleteRadio.sizePolicy().hasHeightForWidth())
        self.customer_deleteRadio.setSizePolicy(sizePolicy1)
        self.customer_deleteRadio.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.customer_deleteRadio, 2, 0, 1, 1)

        self.pages_stack.addWidget(self.customs_page)
        self.rentals_page = QWidget()
        self.rentals_page.setObjectName(u"rentals_page")
        self.rentals_page.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QStackedWidget{\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
" border: 1px solid rgb(157, 157, 157) ; /* Dark green border */\n"
"\n"
"}")
        self.frame_15 = QFrame(self.rentals_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(-10, -10, 941, 691))
        self.frame_15.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.rentalTable = QTableWidget(self.frame_15)
        if (self.rentalTable.columnCount() < 4):
            self.rentalTable.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.rentalTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self.rentalTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self.rentalTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        self.rentalTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.rentalTable.setObjectName(u"rentalTable")
        self.rentalTable.setGeometry(QRect(20, 20, 641, 651))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rentalTable.sizePolicy().hasHeightForWidth())
        self.rentalTable.setSizePolicy(sizePolicy2)
        self.rentalTable.setFont(font1)
        self.rentalTable.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.rentalTable.setAutoFillBackground(False)
        self.rentalTable.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"color: rgb(0, 10, 52);\n"
" }\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(232, 232, 232);\n"
"	font: 9pt \"Segoe UI\";\n"
"\n"
"	color: rgb(0, 10, 52);\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"color: rgb(0, 10, 52);\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"  background: gray;\n"
"color: rgb(0, 10, 52);\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
"color: rgb(0, 10, 52);\n"
" }")
        self.rentalTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.rentalTable.setShowGrid(True)
        self.rentalTable.setSortingEnabled(False)
        self.rentalTable.horizontalHeader().setCascadingSectionResizes(False)
        self.rentalTable.horizontalHeader().setDefaultSectionSize(150)
        self.rentalTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.rentalTable.horizontalHeader().setStretchLastSection(True)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(670, 20, 241, 651))
        self.frame_16.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius: 7px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(30, 70, 181, 221))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_22 = QLabel(self.frame_17)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_8.addWidget(self.label_22)

        self.rentalCarID = QLineEdit(self.frame_17)
        self.rentalCarID.setObjectName(u"rentalCarID")

        self.verticalLayout_8.addWidget(self.rentalCarID)

        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_8.addWidget(self.label_23)

        self.rentalCustomerID = QLineEdit(self.frame_17)
        self.rentalCustomerID.setObjectName(u"rentalCustomerID")

        self.verticalLayout_8.addWidget(self.rentalCustomerID)

        self.rentalStartButton = QPushButton(self.frame_17)
        self.rentalStartButton.setObjectName(u"rentalStartButton")
        sizePolicy.setHeightForWidth(self.rentalStartButton.sizePolicy().hasHeightForWidth())
        self.rentalStartButton.setSizePolicy(sizePolicy)
        self.rentalStartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.rentalStartButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(0, 162, 38);\n"
"	border: 1px solid rgb(0, 162, 38);\n"
"}")

        self.verticalLayout_8.addWidget(self.rentalStartButton)

        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 111, 41))
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(30, 380, 181, 161))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_24 = QLabel(self.frame_18)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_9.addWidget(self.label_24)

        self.rentalRentalID = QLineEdit(self.frame_18)
        self.rentalRentalID.setObjectName(u"rentalRentalID")

        self.verticalLayout_9.addWidget(self.rentalRentalID)

        self.rentalEndButton = QPushButton(self.frame_18)
        self.rentalEndButton.setObjectName(u"rentalEndButton")
        sizePolicy.setHeightForWidth(self.rentalEndButton.sizePolicy().hasHeightForWidth())
        self.rentalEndButton.setSizePolicy(sizePolicy)
        self.rentalEndButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.rentalEndButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(255, 0, 0);\n"
"	border: 1px solid rgb(255, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.rentalEndButton)

        self.label_27 = QLabel(self.frame_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 320, 111, 41))
        self.pages_stack.addWidget(self.rentals_page)
        self.search_page = QWidget()
        self.search_page.setObjectName(u"search_page")
        self.frame_19 = QFrame(self.search_page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(-10, -10, 941, 691))
        self.frame_19.setStyleSheet(u"background-color: rgb(212, 212, 212);\n"
" border: 1px solid rgb(157, 157, 157) ; ")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(670, 20, 241, 651))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(20, 70, 201, 161))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_25 = QLabel(self.frame_21)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u" border: 0px solid rgb(157, 157, 157) ; \n"
"")

        self.verticalLayout_10.addWidget(self.label_25)

        self.searchCar = QLineEdit(self.frame_21)
        self.searchCar.setObjectName(u"searchCar")
        self.searchCar.setMaxLength(7)

        self.verticalLayout_10.addWidget(self.searchCar)

        self.searchCarButton = QPushButton(self.frame_21)
        self.searchCarButton.setObjectName(u"searchCarButton")
        sizePolicy.setHeightForWidth(self.searchCarButton.sizePolicy().hasHeightForWidth())
        self.searchCarButton.setSizePolicy(sizePolicy)
        self.searchCarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchCarButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:14px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(95, 165, 247);\n"
"	border: 1px solid rgb(95, 165, 247);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/search (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchCarButton.setIcon(icon5)
        self.searchCarButton.setIconSize(QSize(22, 22))

        self.verticalLayout_10.addWidget(self.searchCarButton)

        self.label_29 = QLabel(self.frame_20)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 111, 41))
        self.label_29.setStyleSheet(u"\n"
"font: 600 11pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; \n"
"")
        self.label_31 = QLabel(self.frame_20)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 320, 131, 41))
        self.label_31.setStyleSheet(u"\n"
"font: 600 11pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; \n"
"")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(20, 380, 201, 161))
        self.frame_22.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_22)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_28 = QLabel(self.frame_22)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u" border: 0px solid rgb(157, 157, 157) ; \n"
"")

        self.verticalLayout_11.addWidget(self.label_28)

        self.searchCustomer = QLineEdit(self.frame_22)
        self.searchCustomer.setObjectName(u"searchCustomer")
        self.searchCustomer.setMaxLength(8)

        self.verticalLayout_11.addWidget(self.searchCustomer)

        self.searchCustomerButton = QPushButton(self.frame_22)
        self.searchCustomerButton.setObjectName(u"searchCustomerButton")
        sizePolicy.setHeightForWidth(self.searchCustomerButton.sizePolicy().hasHeightForWidth())
        self.searchCustomerButton.setSizePolicy(sizePolicy)
        self.searchCustomerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchCustomerButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(95, 165, 247);\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"margin-top:14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(95, 165, 247);\n"
"	border: 1px solid rgb(95, 165, 247);\n"
"}")
        self.searchCustomerButton.setIcon(icon5)
        self.searchCustomerButton.setIconSize(QSize(22, 22))

        self.verticalLayout_11.addWidget(self.searchCustomerButton)

        self.carsList = QListWidget(self.frame_19)
        self.carsList.setObjectName(u"carsList")
        self.carsList.setGeometry(QRect(90, 100, 491, 151))
        self.carsList.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius: 9px;\n"
"font: 9pt \"Segoe UI\";")
        self.customerList = QListWidget(self.frame_19)
        self.customerList.setObjectName(u"customerList")
        self.customerList.setGeometry(QRect(90, 400, 511, 171))
        self.customerList.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"border-radius: 9px;\n"
"font: 10pt \"Segoe UI\";\n"
"color:rgb(0, 10, 52);")
        self.customerList.setLineWidth(1)
        self.customerList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customerList.setAlternatingRowColors(False)
        self.pages_stack.addWidget(self.search_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.frame_23 = QFrame(self.settings_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(-10, -10, 941, 691))
        self.frame_23.setStyleSheet(u"background-color: rgb(212, 212, 212);\n"
" border: 1px solid rgb(157, 157, 157) ; ")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(170, 220, 521, 211))
        self.frame_24.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"border-radius: 15px;\n"
"border:0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0, 10, 52);\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"background-color: rgb(212, 212, 212);\n"
"border: 1px solid rgb(0, 10, 52)\n"
"}\n"
"\n"
"QPushButton{\n"
"margin:5px;\n"
"padding:5px;\n"
"border-radius: 15px;\n"
"background-color: rgb(0, 10, 52);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"	color: rgb(95, 165, 247);\n"
"	border: 1px solid rgb(0, 10, 52);\n"
"}\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_32 = QLabel(self.frame_25)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"\n"
"font: 600 22pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; \n"
"")

        self.verticalLayout_12.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.importButton = QPushButton(self.frame_25)
        self.importButton.setObjectName(u"importButton")
        sizePolicy.setHeightForWidth(self.importButton.sizePolicy().hasHeightForWidth())
        self.importButton.setSizePolicy(sizePolicy)
        self.importButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.importButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importButton.setIcon(icon6)
        self.importButton.setIconSize(QSize(45, 45))

        self.verticalLayout_12.addWidget(self.importButton)


        self.horizontalLayout_2.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame{\n"
"font: 600 10pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
"background-color: rgb(212, 212, 212);\n"
"border: 1px solid rgb(0, 10, 52)\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"margin:5px;\n"
"padding:5px;\n"
"border-radius: 15px;\n"
"background-color: rgb(0, 10, 52);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(212, 212, 212);\n"
"	border: 1px solid rgb(0, 10, 52);\n"
"}\n"
"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_33 = QLabel(self.frame_26)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"\n"
"font: 600 22pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 10, 52);\n"
" border: 0px solid rgb(157, 157, 157) ; \n"
"")

        self.verticalLayout_13.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.exportButton = QPushButton(self.frame_26)
        self.exportButton.setObjectName(u"exportButton")
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportButton.setIcon(icon7)
        self.exportButton.setIconSize(QSize(45, 45))

        self.verticalLayout_13.addWidget(self.exportButton)

        self.settingsFrame = QFrame(self.frame_26)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setStyleSheet(u"border:0px;\n"
"")
        self.settingsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.settingsFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.exportJson = QPushButton(self.settingsFrame)
        self.exportJson.setObjectName(u"exportJson")
        sizePolicy.setHeightForWidth(self.exportJson.sizePolicy().hasHeightForWidth())
        self.exportJson.setSizePolicy(sizePolicy)
        self.exportJson.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportJson.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(139, 92, 225);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(212, 212, 212);\n"
"	border: 1px solid rgb(139, 92, 225);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/json.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportJson.setIcon(icon8)
        self.exportJson.setIconSize(QSize(45, 45))
        self.exportJson.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.exportJson)

        self.exportXml = QPushButton(self.settingsFrame)
        self.exportXml.setObjectName(u"exportXml")
        sizePolicy.setHeightForWidth(self.exportXml.sizePolicy().hasHeightForWidth())
        self.exportXml.setSizePolicy(sizePolicy)
        self.exportXml.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportXml.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(242, 156, 31);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(212, 212, 212);\n"
"	border: 1px solid rgb(242, 156, 31);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/xml.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportXml.setIcon(icon9)
        self.exportXml.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.exportXml)

        self.exportCsv = QPushButton(self.settingsFrame)
        self.exportCsv.setObjectName(u"exportCsv")
        sizePolicy.setHeightForWidth(self.exportCsv.sizePolicy().hasHeightForWidth())
        self.exportCsv.setSizePolicy(sizePolicy)
        self.exportCsv.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportCsv.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(31, 179, 91);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(212, 212, 212);\n"
"	border: 1px solid  rgb(31, 179, 91);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/csv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportCsv.setIcon(icon10)
        self.exportCsv.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.exportCsv)


        self.verticalLayout_13.addWidget(self.settingsFrame)


        self.horizontalLayout_2.addWidget(self.frame_26)

        self.pages_stack.addWidget(self.settings_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_stack.setCurrentIndex(4)
        self.car_action_stack.setCurrentIndex(3)
        self.customer_action_stack.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.carsMenu.setText(QCoreApplication.translate("MainWindow", u"Cars", None))
        self.customersMenu.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.rentalMenu.setText(QCoreApplication.translate("MainWindow", u"Rentals", None))
        self.searchMenu.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.settingsMenu.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.page_name_label.setText(QCoreApplication.translate("MainWindow", u"Car Rental - Cars Page", None))
        ___qtablewidgetitem = self.carTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"car_id", None));
        ___qtablewidgetitem1 = self.carTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"car_reg", None));
        ___qtablewidgetitem2 = self.carTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"car_make", None));
        ___qtablewidgetitem3 = self.carTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"car_year", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RegistrationNumber", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Make", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.carAddButton.setText(QCoreApplication.translate("MainWindow", u"Add Car", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Car ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"New Registration Nulmber", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"New Make", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"New Year", None))
        self.carEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit Car", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Car ID", None))
        self.carRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Car", None))
        self.car_addRadio.setText(QCoreApplication.translate("MainWindow", u"Add Car", None))
        self.car_editRadio.setText(QCoreApplication.translate("MainWindow", u"Edit Car", None))
        self.car_deleteRadio.setText(QCoreApplication.translate("MainWindow", u"Delete Car", None))
        ___qtablewidgetitem4 = self.customerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"customer_id", None));
        ___qtablewidgetitem5 = self.customerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"customer_name", None));
        ___qtablewidgetitem6 = self.customerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"customer_number", None));
        ___qtablewidgetitem7 = self.customerTable.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"customer_email", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.customerAddButton.setText(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"New Name", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"New Contact Number", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"New Email", None))
        self.customerEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit Customer", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.customerRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Customer", None))
        self.customer_addRadio.setText(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.customer_editRadio.setText(QCoreApplication.translate("MainWindow", u"Edit Customer", None))
        self.customer_deleteRadio.setText(QCoreApplication.translate("MainWindow", u"Delete Customer", None))
        ___qtablewidgetitem8 = self.rentalTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Rental_ID", None));
        ___qtablewidgetitem9 = self.rentalTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Car_ID", None));
        ___qtablewidgetitem10 = self.rentalTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Customer_ID", None));
        ___qtablewidgetitem11 = self.rentalTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"StartDate", None));
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Car ID", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.rentalStartButton.setText(QCoreApplication.translate("MainWindow", u"Assign Car", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Start Rental", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Rental ID", None))
        self.rentalEndButton.setText(QCoreApplication.translate("MainWindow", u"Unassign Car", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"End Rental", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Car Registeration Number", None))
        self.searchCar.setInputMask("")
        self.searchCarButton.setText(QCoreApplication.translate("MainWindow", u"Search Car", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Search Car", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Search Customer", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Customer Mobile Number", None))
        self.searchCustomerButton.setText(QCoreApplication.translate("MainWindow", u"Search Customer", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.importButton.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"EXPORT", None))
        self.exportButton.setText("")
        self.exportJson.setText("")
        self.exportXml.setText("")
        self.exportCsv.setText("")
    # retranslateUi

