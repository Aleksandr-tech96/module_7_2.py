from pprint import pprint
# Создаём функцию custom_write (file_name, strings)
# которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
# Получение номера байта начала строки используем метод tell() перед записью
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(i, position)] = string
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
# Вывод на консоль:
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)