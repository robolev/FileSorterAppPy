from PySide6 import QtWidgets

from FileSorter import FileSorter


class DateSelectionDialog(QtWidgets.QDialog):
    def __init__(self, backup_directory, root_directory):
        super(DateSelectionDialog, self).__init__()

        self.backup_directory = backup_directory
        self.root_directory = root_directory

        self.copyDateButton = QtWidgets.QPushButton("Copy Files with Special Date")
        self.copyAllButton = QtWidgets.QPushButton("Copy All Files")
        self.textLabel = QtWidgets.QLabel("Do you want to copy files with a special date or copy all files?")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.textLabel)
        layout.addWidget(self.copyDateButton)
        layout.addWidget(self.copyAllButton)
        self.setLayout(layout)

        self.copyDateButton.clicked.connect(self.copy_files_with_special_date)
        self.copyAllButton.clicked.connect(FileSorter.copy_files(self.root_directory,self.backup_directory))

    def copy_files_with_special_date(self):
        self.copy_files(self.root_directory, self.backup_directory)
        self.accept()