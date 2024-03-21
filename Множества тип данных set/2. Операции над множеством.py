
# ! К элементам множества нельзя обращаться по индексу, это приведет к ошибке

# ! reversed() нельзя использовать для множества, так как множество представляет собой неупорядоченную коллекцию. При попытке вызывать функцию reversed()  вы получите ошибку\


# ? .len()
# Нахождение длины множества
a = {1, 2, 3}
print(f'Длина a = {len(a)}')   # Длина a = 3

b = set()
print(f'Длина b = {len(b)}')   # Длина b = 0

c = set([1, 1, 2, 2, 1, 2, 1])
print(f'Длина c = {len(c)}')   # Длина c = 2


# ? Оператор in
# Позволяет проверить имеется ли элемент в множестве или нет. Если данный элемент присутствует, то результат будет  True, в обратном случае – False.
a = {1, 2, 3}
print(2 in a)       # True
print(5 in a)       # False
print(4 not in a)   # True
print(1 not in a)   # False


# ? min(), max()
# Позволяют найти минимальный и максимальный элемент множества
a = {1, 2, 3}
print(min(a), max(a))      # 1 3

b = set([11, 19, 22, 2, 13, 22, 10])
print(min(b), max(b))     # 2 22
# Можно использовать только если множество состоит из однотипных элементов, которые можно сравнить между собой (целиком из чисел или целиком из строк). Если бы наше множество было бы таким
a = {1, 2, 'hi', 4, 5}
# То получили бы ошибку


# ? sum
# Суммирование элементов множества
a = {2, 4, 5, 7, 8, 9}
print(sum(a))              # 35
# Если в множестве будут присутствовать не числа, то получим ошибку


# ? sorted
# Можно отсортировать множество, если в нем содержатся однородные элементы
my_set = {8, 4, 7, 5, 2, 3, 6}
sorted_list = sorted(my_set)
print(sorted_list)             # [2, 3, 4, 5, 6, 7, 8]
# * Результат работы функции sorted() всегда является список

# Убывающий отортированный список
print(sorted(my_set, reverse=True))
# [8, 7, 6, 5, 4, 3, 2]
