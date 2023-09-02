import os
import shutil
from datetime import datetime

from PySide6 import QtWidgets


class FileSorter:
    def __init__(self):
        self.backup_directory = ""
    def collect_files_and_dirs(root_directory):
        all_files = [os.path.join(root, file) for root, dirs, files in os.walk(root_directory) for file in files]
        all_dirs = [os.path.join(root, dir) for root, dirs, files in os.walk(root_directory) for dir in dirs]
        return all_files, all_dirs
    def move_files_to_matching_dirs(root_directory, all_files, all_dirs):
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
    def copy_files(source_directory, destination_directory):
        all_files, _ = FileSorter.collect_files_and_dirs(source_directory)

        for file_path in all_files:
            new_file_path = os.path.join(destination_directory, os.path.basename(file_path))
            shutil.copy(file_path, new_file_path)

    def copy_files_matching_dates(source_directory, destination_directory, date_list):
        all_files, _ = FileSorter.collect_files_and_dirs(source_directory)

        for file_path in all_files:
            creation_timestamp = os.path.getctime(file_path)
            if creation_timestamp is not None:
               creation_date = datetime.fromtimestamp(creation_timestamp).date()
               if any(date.date() == creation_date for date in date_list):
                  new_file_path = os.path.join(destination_directory, os.path.basename(file_path))
                  shutil.copy(file_path, new_file_path)