# https://www.youtube.com/watch?v=dZ474oWml9k&ab_channel=egoroff_channel
# https://stepik.org/lesson/296968/step/2?auth=login&unit=278696

# Подсчет количества объектов

# Логика
s = 'asdfbhmfvaadsdc'
d = {}
d['a'] = 1
print(d)
if 'a' in d:
    d['a'] += 1
else:
    d['a'] = 1
print(d)
if 'b' in d:
    d['b'] += 1
else:
    d['b'] = 1
print(d)


# Без применения метода .get()
s = 'asdfb@#$hmfvaadsdc'
d = {}
for i in s:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
for i, j in sorted(d.items()):
    print(i, j)


# C применением метода .get()
s = 'asdfb@#$hmfvaadsdc'
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
for i, j in sorted(d.items()):
    print(i, j)


# Разряженный список
# без словаря
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(i, letters[i])


# Разряженный список
# со словарем
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)


# Установление связи между обьектами
# переводчик словарь
words = {}
while True:
    s = input()
    if s in words:
        print(f'Слово {s} переводится как {words[s]}')
    else:
        print('Введите перевод слова')
        words[s] = input()


# Хранение данных об объекте
# СПОСОБ 1 Получение значений внутри вложенного словаря
contacts = {
    'John Kennedy': {
        'birthday': '29 may 1917', 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    'Arnold Schwarzenegger': {
        'birthday': '30 july 1947', 'city': 'Gradec',
        'phone': 555 - 555 - 555, 'children': 5
    },
    'Donald John Trump': {
        'birthday': '14 july 1946', 'city': 'New York',
        'phone': 777 - 777 - 777, 'children': 4
    }
}

person = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']

for i in person:
    birthday = contacts[i]['birthday']
    city = contacts[i]['city']
    phone = contacts[i]['phone']
    children = contacts[i]['children']
    print(i, children, phone)

# СПОСОБ 2
contacts = {
    'John Kennedy': {
        'birthday': '29 may 1917', 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    'Arnold Schwarzenegger': {
        'birthday': '30 july 1947', 'city': 'Gradec',
        'phone': 555 - 555 - 555, 'children': 5
    },
    'Donald John Trump': {
        'birthday': '14 july 1946', 'city': 'New York',
        'phone': 777 - 777 - 777, 'children': 4
    }
}

person = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']

for i in person:
    print(i)
    for j in contacts[i]:
        print(j, contacts[i][j])
