import os
from collections import namedtuple
import logging
import sys

# Создание именованного кортежа для хранения информации о файлах/каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

class DirectoryScanner:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.file_info_list = []
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='directory_scan.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def scan_directory(self):
        try:
            for root, dirs, files in os.walk(self.directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    name, extension = os.path.splitext(file)
                    extension = extension[1:]  # Удаление точки в расширении
                    parent_dir = os.path.dirname(file_path)
                    file_info = FileInfo(name, extension, False, parent_dir)
                    self.file_info_list.append(file_info)
                    logging.info(f'Обработан файл: {file_path}')

                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    parent_dir = os.path.dirname(dir_path)
                    dir_info = FileInfo(dir_name, '', True, parent_dir)
                    self.file_info_list.append(dir_info)
                    logging.info(f'Обработан каталог: {dir_path}')
        except Exception as e:
            logging.error(f'Произошла ошибка: {str(e)}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Использование: python main.py <путь_к_директории>')
        sys.exit(1)

    directory_path = sys.argv[1]
    scanner = DirectoryScanner(directory_path)
    scanner.scan_directory()

    for file_info in scanner.file_info_list:
        print(file_info)