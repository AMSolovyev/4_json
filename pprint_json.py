import json
import os
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except json.decoder.JSONDecodeError:
        return None


def prettify_json(parsed_json):
    return json.dumps(parsed_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файлу")
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit('Такого файла не существует')

    data_from_json = load_data(file_path)
    print(prettify_json(data_from_json))
