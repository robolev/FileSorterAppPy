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

            all_files, all_dirs = self.collect_files_and_dirs(root_directory)

            print("All Files:", all_files)
            print("All Directories:", all_dirs)

            self.move_files_to_matching_dirs(root_directory, all_files, all_dirs)

            self.ui.lineEdit.setText("Sorting completed.")

    def collect_files_and_dirs(self, root_directory):
        all_files = [os.path.join(root, file) for root, dirs, files in os.walk(root_directory) for file in files]
        all_dirs = [os.path.join(root, dir) for root, dirs, files in os.walk(root_directory) for dir in dirs]
        return all_files, all_dirs

    def move_files_to_matching_dirs(self, root_directory, all_files, all_dirs):
        for file_path in all_files:
            file_name, _ = os.path.splitext(os.path.basename(file_path))
            file_name = file_name.split('_')[0]  
            found_matching_dir = False

            for dir_path in all_dirs:
                dir_name = os.path.basename(dir_path)
                dir_name = dir_name.split('_')[0]  
                if file_name == dir_name:
                    new_file_path = os.path.join(dir_path, os.path.basename(file_path))
                    os.rename(file_path, new_file_path)
                    found_matching_dir = True
                    break

            if not found_matching_dir:
                new_dir_path = os.path.join(root_directory, file_name)
                os.makedirs(new_dir_path, exist_ok=True)
                new_file_path = os.path.join(new_dir_path, os.path.basename(file_path))
                os.rename(file_path, new_file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())