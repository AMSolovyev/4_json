import json
import os
import sys

DEFAULT_FILE_NAME = 'alco_shops.json'


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(parsed_json):
    return json.dumps(parsed_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска!'
              '  Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
        work_file = DEFAULT_FILE_NAME
    else:
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))
            work_file = sys.argv[1]

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)

    data_from_json = load_data(work_file)
    print(pretty_print_json(data_from_json))
