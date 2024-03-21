# https://stepik.org/lesson/545393/step/1?unit=538968

# Генератор словаря необходим для быстрого и удобного создания словаря с наполненными значениями
# Общий вид генератора словарей:
# { ключ: значение for переменная in последовательность}

a = {i: i**2 for i in range(1, 11)}
print(a)

# Без генератора этот код имел бы следующий вид:
a = {}
for i in range(1, 11):
    a[i] = i**2
print(a)

# Внутри генератора словарей можно обходить любую коллекцию, поддерживающую итерацию. 
# Для примера возьмём в качестве последовательности список, состоящий из строк:

a = {word:len(word) for word in ['hi', 'hello', 'www']}
print(a)
# {'hi': 2, 'hello': 5, 'www': 3}

# При помощи генератора можно обходить и уже существующие словари. 
# В словаре data сделаем так, чтобы заглавными были только первые буквы каждого слова, 
# а значения преобразуем из строк в целые числа:

data = {
    'Джефф Безос': '177',
    'ИлоН МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГеЙтС': '124',
}
new_data = {key.title(): int(value) for key, value in data.items()}
print(new_data)
# {'Джефф Безос': 177, 'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}

# Без генератора мы должны были бы сделать следующим образом:
new_data = {}
for key, value in data.items():
    new_data[key.title()] = int(value)
print(new_data)


# Если нам надо обращаться не по индексу в списке, а по id пользователя? 
# Для этого надо сделать следующий генератор:

from pprint import pprint
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234'],
    [51, 'qwerty', '1234']
]
new_users = {user[0]: user for user in users}
pprint(new_users)
print('*' * 15)
pprint(new_users[3])
pprint(new_users[51])

# Без генератора мы должны были бы сделать следующим образом:
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [72, 'qwerty', '1234']
]
new_users = {}
for i in users:
    new_users[i[0]] = i

print(new_users)




