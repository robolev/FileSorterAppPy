from PySide6 import QtWidgets, QtCore
import FileSortingUI
from DateSelectionDialog import DateSelectionDialog
from FileSorter import FileSorter

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.thread_pool = QtCore.QThreadPool.globalInstance()

        self.ui = FileSortingUI.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.sort_files)
        self.ui.pushButton_2.clicked.connect(self.set_backup_directory)
        self.ui.pushButton_3.clicked.connect(self.open_date_selection_dialog)

        self.file_sorter = FileSorter()
        self.backup_directory = ""

    def sort_files(self):
        root_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Root Directory")

        if root_directory:
            self.ui.lineEdit.setText("Sorting files...")

            all_files, all_dirs = FileSorter.collect_files_and_dirs(root_directory)

            print("All Files:", all_files)
            print("All Directories:", all_dirs)

            FileSorter.move_files_to_matching_dirs(root_directory, all_files, all_dirs)

            self.ui.lineEdit.setText("Sorting completed.")

    def set_backup_directory(self):
        self.backup_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Backup Directory")
        self.ui.lineEdit_2.setText("Directory Setting complete")

    def open_date_selection_dialog(self):
        if not self.backup_directory:
            self.ui.lineEdit_2.setText("Please set the backup directory first.")
            return

        root_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Root Directory for Copying")

        if root_directory:
            date_selection_dialog = DateSelectionDialog(self.backup_directory, root_directory)
            date_selection_dialog.exec()
