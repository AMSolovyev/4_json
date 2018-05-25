import json
import os
import sys

DEFAULT_FILE_NAME = 'alco_shops.json'
DEFAULT_FILE_ENCODING = 'utf-8'
DEFAULT_INDENT = 4

def load_from_json(filepath, file_encoding):
        with open(filepath, 'r', encoding=file_encoding) as file_handler:
            return json.load(file_handler)

def printer_json(data):
    return json.dumps(data, indent=DEFAULT_INDENT, ensure_ascii=False)

if __name__== '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска!  Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
        work_file = DEFAULT_FILE_NAME
    else:
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))
            work_file = sys.argv[1]

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)

    data_from_json = load_from_json(work_file, DEFAULT_FILE_ENCODING)
    print(printer_json(data_from_json))
