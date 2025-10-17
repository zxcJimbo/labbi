name = input('enter your name: ')
age = int(input('enter your age: '))
def describe_person(name, age = 30):
    return f"Меня зовут {name}, Мне {age} лет."

print(describe_person(name, age))
