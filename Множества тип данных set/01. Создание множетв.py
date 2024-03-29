
# ? Множество (тип данных set) – это неупорядоченная коллекция уникальных элементов. Здесь стоит подчеркнуть слово уникальных, потому что тип данных set не допустит, чтобы в одной коллекции хранились повторяющиеся элементы.

# ? Способы создания множества
a = {1, 2, 3}
print(a)           # {1, 2, 3}
print(type(a))     # <class 'set'>

b = {1, 2, 1, 2, 3, 1, 1, 4}
print(b)           # {1, 2, 3, 4}
print(type(b))     # <class 'set'>
# Полученных множествах находятся уникальные элементы в одном экземпляре и нету ни одного повторяющего значения

# Также важно отметить, что множество является неупорядоченной коллекцией, то есть в предыдущем случае мы могли бы получить что-то из следующего: {1, 4, 3, 2} , {4, 3, 2, 1} или {4, 2, 1, 3}


# ? При помощи функции set() мы можем преобразовать другую коллекцию (список, строку и т.д.) в множество
a = set('abcdeabc')
b = set([1, 2, 3, 2, 3, 1, 3])
c = set(range(5))
print(a)            # {'a', 'b', 'c', 'e', 'd'}
print(b)            # {1, 2, 3}
print(c)            # {0, 1, 2, 3, 4}


# ? Создание пустого множества
# Чтобы создать пустое множество необходимо воспользоваться функцией set() без указания аргументов. Стоит отметить, что нельзя создать множество с помощью пустых фигурных скобок {}, т.к. при помощи пустых фигурных скобок создается словарь.
a = set()
print(a)          # set()
print(type(a))    # <class 'set'>

print('-'*15)

b = {}
print(b)         # {}
print(type(b))   # <class 'dict'>
# Словари и множества оба записываются в фигурных скобках, это создает небольшую путаницу. Не забывайте, что словари содержат пары ключ-значения, которые всегда записываются через двоеточие. Именно по наличию знака : в выводе объекта можно понять, что перед вами словарь. Также вы всегда можете проверить тип объекта.


# ! Ограничение на элементы множества
# * Множество может состоять только из неизменяемых объектов.
# * К примеру, множество можно сделать из списка чисел, но вот из вложенного списка уже нельзя, поскольку элементами такого списка являются списки, которые сами по себе являются изменяемыми объектами.
a = [1, 2, 3, 4, 3, 2, 3, 1, 3, 4, 2, 2, 2]
a = list(set(a))

print(a)              # [1, 2, 3, 4]

b = [[1, 2, 3, 4],
     [3, 2, 3, 1],
     [3, 4, 2, 2]]
b = set(b)
print(b)              # Ошибка
# * При попытке создать множество, содержащее изменяемый объект, возникнет ошибка

# * К неизменяемым объектам, напоминаю, относятся:
# строки
# числа int и float
# кортежи
# frozenset (изучаем далее)
# Все эти значения могут являться элементами множества
