# https://stepik.org/lesson/372102/step/1?unit=359656

# Генераторы списков | List comprehension | Вложенные генераторы
# Мы имеем список, элементами которого являются кортежи. У кортежей так же есть своя индексация. 
# Теперь при помощи генератора списка будем доставать нужные нам значения:
a = [
    ("Sidorov", 1995),
    ("Lukov", 2002),
    ("Petrov", 1991),
    ("Gorbachev", 1984),
    ("Kostin", 2000),
]
print(a[4][0])    # Kostin
surnames = [elem[0] for elem in a] # Получим только фамилии
years = [elem[1] for elem in a] # Получим только год рождения
print(surnames)   # ['Sidorov', 'Lukov', 'Petrov', 'Gorbachev', 'Kostin']
print('-'*20)     
print(years)      # [1995, 2002, 1991, 1984, 2000]

# Но что, если нам нужно отфильтровать значения и взять только определенные данные. 
# Тоже можем такое реализовать при помощи генератора списка. 
# - Давайте возьмём только те фамилии, которые начинаются с буквы E
# - только  тех людей, чей год рождения больше, чем 2000
# - только первые буквы с каждой фамилии, год рождения которых больше 2000

a = [
    ("Sidorov", 1995),
    ("Lukov", 2002),
    ("Petrov", 1991),
    ("Gorbachev", 1984),
    ("Kostin", 2000),
    ("Isaev", 2005),
    ("Eliseev", 1999),
    ("Kozlov", 2004),
    ("Bukov", 1995),
    ("Gavrilov", 1980),
    ("Efremov", 2006),
]
name_start_e = [elem[0] for elem in a if elem[0].startswith("E")]
print(name_start_e)   # ['Eliseev', 'Efremov']
more_2000 = [elem[0] for elem in a if elem[1]>2000]
print(more_2000)      # ['Lukov', 'Isaev', 'Kozlov', 'Efremov']
first_letter = [elem[0][0] for elem in a if elem[1]>2000]
print(first_letter)   # ['L', 'I', 'K', 'E']

# А теперь попробуем при помощи генератора обработать данные, которые хранятся в словаре. 
# Пусть у нас будет такой вложенный словарь:

a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
keys = [elem for elem in a]
print(keys)   
# ['Sidorov', 'Lukov', 'Petrov', 'Gorbachev', 'Kostin', 'Isaev', 'Eliseev', 'Kozlov', 'Bukov']
print('-'*30)
values = [a[elem] for elem in a]
print(values)   
# [{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'}, 
#  {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'}, 
#  {'age': 1991, 'hobby': 'chess', 'car': 'BMW'}, {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'}, 
#  {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'}, {'age': 2005, 'hobby': 'music', 'car': 'BMW'}, 
#  {'age': 1999, 'hobby': 'chess', 'car': 'Audi'}, {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'}, 
#  {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'}]


# В итоге, мы получили список из ключей (в нашем случае фамилий) и список словарей. 
# Поскольку мы получаем словарь, то мы можем по двойной индексации обратиться к какому-либо значению 
# вложенного словаря. Например, получим список, состоящий из
# - машин владельцев
# - хобби владельцев
# - машин, владельцы которых родились раньше 2000
# из кортежей (имя владельца, машина), где год рождения меньше 2000
# из кортежей (имя владельца, машина), где год рождения меньше 2000 и хобби футбол
a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
cars = [a[elem]['car'] for elem in a]
print(cars)
print('-'*30)  
# ['BMW', 'Opel', 'BMW', 'BMW', 'Audi', 'BMW', 'Audi', 'Opel', 'Audi']
hobbies = [a[elem]['hobby'] for elem in a]
print(hobbies)
# ['soccer', 'basketball', 'chess', 'tennis', 'swimming', 'music', 'chess', 'soccer', 'basketball']
print('-'*30)
cars_lt_2000 = [a[elem]['car'] for elem in a if a[elem]['age'] < 2000]
print(cars_lt_2000)
# ['BMW', 'BMW', 'BMW', 'Audi', 'Audi']
print('-'*30)
name_with_car = [(elem, a[elem]['car']) for elem in a 
                        if a[elem]['age'] < 2000]
print(name_with_car)
# [('Sidorov', 'BMW'), ('Petrov', 'BMW'), ('Gorbachev', 'BMW'), 
#  ('Eliseev', 'Audi'), ('Bukov', 'Audi')]
print('-'*30)
less_2000_and_soccer = [(elem, a[elem]['car']) for elem in a 
         if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer'] 
print(less_2000_and_soccer)
# [('Sidorov', 'BMW')]

# Разберём ещё один пример. У нас имеется строка, состоящая из различных символов, 
# в которые входят буквы и цифры. Мы можем при помощи генератора списка сформировать два списка: 
# - в одном будут хранится только цифры, 
# - в другом - только буквы
s = 'gfdogjdf45i398gry74y543hgkgreiuYIUGd'
str_digits = [i for i in s if i.isdigit()]
print(str_digits) # ['4', '5', '3', '9', '8', '7', '4', '5', '4', '3']
print('-'*30)

int_digits = [int(i) for i in str_digits if i.isdigit()]
print(int_digits) # [4, 5, 3, 9, 8, 7, 4, 5, 4, 3]

print('-'*30)
letters = [i for i in s if i.isalpha()]
print(letters)   
# ['g', 'f', 'd', 'o', 'g', 'j', 'd', 'f', 'i', 'g', 'r', 'y', 'y', 'h',
# 'g', 'k', 'g', 'r', 'e', 'i', 'u', 'Y', 'I', 'U', 'G', 'd']

# Рассмотрим ещё один пример. На предыдущем занятии мы составляли двумерный список m x n 
# и заполняли его нулями при помощи генератора. 
# А теперь напишем вложенный генератор и для заполнения используем случайные числа с помощью модуля рандом:
from random import randint
n = 5
m = 3
a = [[randint(1,6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)

# [2, 1, 4]
# [1, 1, 3]
# [3, 1, 6]
# [5, 3, 4]
# [1, 4, 3]

# Принцип работы похож на тот, по которому работают вложенные циклы.
# Сделаем квадратную таблицу и в список b будем вносить лишь элементы главной диагонали, 
# а в список c только элементы со строки с индексом 2, а в список d только элементы столбца с индексом 3.

# ! from random import randint
n = 5
m = 5
a = [[randint(1,6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)
# [3, 4, 6, 1, 1]
# [4, 1, 6, 4, 6]
# [3, 1, 4, 5, 6]
# [4, 6, 1, 2, 1]
# [3, 4, 5, 3, 3]    
b = [a[i][j] for i in range(n) for j in range(m) if i==j]
print('main diagon', b) # main diagon [3, 1, 4, 2, 3]

с = [a[2][j] for j in range(m)]
print('2 row', с)    # 2 row [3, 1, 4, 5, 6]

d =[a[i][3] for i in range(n)]
print('3 column', d) # 3 column [1, 4, 5, 2, 3]

# Теперь рассмотрим, как при помощи вложенных генераторов можно составить таблицу умножения.
n = 5
m = 5
a = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
for i in a:
    print(i)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]

# Также вы можете спокойно обходить элементы матрицы внутри генератора списка по значениям, 
# для этого достаточно во внутреннем цикле обращаться к итерируемой переменной внешнего цикла

from random import randint
n = 3
m = 4
matrix = [[randint(1,10) for j in range(m)] for i in range(n)]
for current_row in matrix:
    print(current_row)
# [10, 8, 5, 5]
# [2, 10, 5, 9]
# [2, 9, 10, 5]
    
print('-'*30)

squares = [num**2 for row in matrix for num in row]
print(squares)
# [100, 64, 25, 25, 4, 100, 25, 81, 4, 81, 100, 25]

