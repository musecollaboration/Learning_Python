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
print(surnames)
print('-'*20)     # 
print(years)

