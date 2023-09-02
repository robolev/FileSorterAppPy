from PySide6 import QtWidgets

import Dialogs.CalendarDialog
from ProgramLogic.FileSorter import FileSorter
import pandas as pd
import UI.FileSortingUI

class DateSelectionDialog(QtWidgets.QDialog):
    def __init__(self, backup_directory, root_directory):
        super(DateSelectionDialog, self).__init__()
        
        self.ui = UI.FileSortingUI.Ui_Dialog()
        
        self.date_list = None
        self.backup_directory = backup_directory
        self.root_directory = root_directory  

        self.copyDateButton = QtWidgets.QPushButton("Copy Files with Special Date")
        self.copyAllButton = QtWidgets.QPushButton("Copy All Files")
        self.textLabel = QtWidgets.QLabel("Do you want to copy files with a special date or copy all files?")
        self.calendar = Dialogs.CalendarDialog.CalenderX()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.textLabel)
        layout.addWidget(self.copyDateButton)
        layout.addWidget(self.copyAllButton)
        layout.addWidget(self.calendar)
        self.setLayout(layout)

        self.copyDateButton.clicked.connect(self.copy_files_with_special_date)
        self.copyAllButton.clicked.connect(lambda: self.call_copy_files())

    def copy_files_with_special_date(self):
        self.print_days_selected()
        print(self.date_list)
        FileSorter.copy_files_matching_dates(self.root_directory, self.backup_directory, self.date_list)
        self.accept()
        
    def print_days_selected(self):
        if self.calendar.from_date and self.calendar.to_date:
            start_date = min(self.calendar.from_date.toPython(), self.calendar.to_date.toPython())
            end_date = max(self.calendar.from_date.toPython(), self.calendar.to_date.toPython())
           
            self.date_list = pd.date_range(start=start_date, end=end_date).to_list()

        else:
            print('No date range is selected')

    def call_copy_files(self):
        FileSorter.copy_files(self.root_directory, self.backup_directory)
        self.ui.lineEdit_3.setText("Copy Complete")
        self.accept()