import os
import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication
import FileSortingUI

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.thread_pool = QtCore.QThreadPool.globalInstance()

        self.ui = FileSortingUI.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.sort_files)

    def sort_files(self):
        root_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Root Directory")

        if root_directory:
            self.ui.lineEdit.setText("Sorting files...")

            entries = os.listdir(root_directory)

            all_files = [os.path.join(root, file) for root, dirs, files in os.walk(root_directory) for file in files]
            all_dirs = [os.path.join(root, dir) for root, dirs, files in os.walk(root_directory) for dir in dirs]

            print("All Files:", all_files)
            print("All Directories:", all_dirs)

            for file_path in all_files:
                file_name, _ = os.path.splitext(os.path.basename(file_path))
                for dir_path in all_dirs:
                    dir_name = os.path.basename(dir_path)
                    if file_name == dir_name:
                        new_file_path = os.path.join(dir_path, os.path.basename(file_path))
                        os.rename(file_path, new_file_path)
                        break

            self.ui.lineEdit.setText("Sorting completed.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())