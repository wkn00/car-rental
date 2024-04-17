from PySide6.QtWidgets import QFileDialog, QMessageBox
from data_access.export_database import ExportDatabase
from data_access.import_database import ImportDatabase

class SettingsInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.export_database = ExportDatabase()
        self.import_database = ImportDatabase()

        # UI Elements setup
        self.main_window.settingsFrame.hide()
        self.main_window.settingsMenu.clicked.connect(self.displaySettingsPage)
        self.main_window.exportButton.clicked.connect(self.showExportButtons)

        # Connect export buttons
        self.main_window.exportJson.clicked.connect(lambda: self.export_data('json'))
        self.main_window.exportXml.clicked.connect(lambda: self.export_data('xml'))
        self.main_window.exportCsv.clicked.connect(lambda: self.export_data('csv'))

        # Connect import button
        self.main_window.importButton.clicked.connect(self.handle_import)

    def displaySettingsPage(self):
        self.main_window.pages_stack.setCurrentIndex(4)
        self.main_window.page_name_label.setText("Car Rental - Settings Page")
        self.main_window.settingsFrame.hide()
        self.main_window.exportButton.show()

    def showExportButtons(self):
        self.main_window.exportButton.hide()
        self.main_window.settingsFrame.show()
        self.main_window.exportJson.show()
        self.main_window.exportXml.show()
        self.main_window.exportCsv.show()

    def handle_import(self):
        file_name, _ = QFileDialog.getOpenFileName(self.main_window, "Open File", "",
                                                   "Data Files (*.json *.csv *.xml)")
        if file_name:
            if file_name.endswith('.json'):
                self.import_database.import_from_json(file_name)
                self.main_window.update_all_tables()  # Update UI tables after import
                QMessageBox.information(self.main_window, "JSON Imported", "JSON file has been successfully imported.")
            elif file_name.endswith('.csv'):
                self.import_database.import_from_csv(file_name)
                self.main_window.update_all_tables()  # Update UI tables after import
                QMessageBox.information(self.main_window, "CSV Imported", "CSV file has been successfully imported.")
            elif file_name.endswith('.xml'):
                self.import_database.import_from_xml(file_name)
                self.main_window.update_all_tables()  # Update UI tables after import
                QMessageBox.information(self.main_window, "XML Imported", "XML file has been successfully imported.")
            else:
                QMessageBox.warning(self.main_window, "Unsupported File", "The selected file format is not supported.")
            self.main_window.updateTable()  # Update UI tables after import

    def export_data(self, format_type):
        file_name, _ = QFileDialog.getSaveFileName(self.main_window, "Save File", "", f"{format_type.upper()} Files (*.{format_type})")
        if file_name:
            data = self.export_database.fetch_data_from_database()
            if format_type == 'json':
                self.export_database.export_data_to_json(data, file_name)
            elif format_type == 'xml':
                self.export_database.export_data_to_xml(data, file_name)
            elif format_type == 'csv':
                self.export_database.export_data_to_csv(data, file_name)
            QMessageBox.information(self.main_window, "Export Success", f"Data successfully exported as {format_type.upper()} to {file_name}")
            print("Data successfully exported to", file_name)