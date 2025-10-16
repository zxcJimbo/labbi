# Задание №1

def format_text(format):
    if format == 'целиком':
        with open(r"C:\Program Files\example.txt", 'r', encoding='utf-8') as file:
            return file.read()
    elif format == 'построчно':
        with open(r"C:\Program Files\example.txt", 'r', encoding='utf-8') as file:
            return file.readlines()
    else:
        return 'Ошибка ввода'
print('Какой формат чтения вы хотите выбрать?','\n' + 'чтение целиком или построчно?')
print(*format_text(input()), sep='')

# Задание №2

def write_text(write):
    if write == 'написать новый текст':
        with open(r"C:\Program Files\example.txt", 'w', encoding='utf-8') as file:
            file.write('\n' + input())
    elif write == 'дописать текст':
        with open(r"C:\Program Files\example.txt", 'a', encoding='utf-8') as file:
            file.write('\n' + input())
    else:
        return 'Ошибка ввода'
    return file
print('Вы хотите написать новый текст или дописать текст?')
print(write_text(input()))

# Задание №3

def format_text(format):
    try:
        if format == 'целиком':
            with open(r"C:\Program Files\example.txt", 'r', encoding='utf-8') as file:
                return file.read()
        elif format == 'построчно':
            with open(r"C:\Program Files\example.txt", 'r', encoding='utf-8') as file:
                return file.readlines()
        else:
            return 'Ошибка ввода'
    except:
        return 'FileNotFoundError'
print('Какой формат чтения вы хотите выбрать?','\n' + 'чтение целиком или построчно?')
print(*format_text(input()), sep='')
