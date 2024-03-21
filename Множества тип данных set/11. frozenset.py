# https://stepik.org/lesson/843175/step/1?unit=846877


# ! Операции над frozenset
# ? Все операции, которые можно применять над обычным множеством set, можно использовать и над frozenset()
# https://stepik.org/lesson/843175/step/4?unit=846877


# ? Тип данных frozenset()

# frozenset представляет собой такое же множество как и тип данных set
# * Единственным и главным отличием - frozenset является неизменяемым объектом

# ? Создание пустого неизменяемого множества
# Чтобы создать пустое неизменяемое множество необходимо воспользоваться функцией frozenset() , не передав в нее ничего. Либо передав в функцию пустую последовательность: пустой словарь, пустой список, пустой кортеж и т.д.

froz = frozenset()
print(froz)              # frozenset()

empty = frozenset([])
print(empty)             # frozenset()

print(frozenset(''))     # frozenset()
print(frozenset({}))     # frozenset()


print('-'*15)

# ? Создание frozenset на основании другой коллекции
# Мы можем создать frozenset на основании любой другой итерируемой коллекции, а именно  на основании:
# строки
# списка
# кортежа
# множества
# словаря

fr_abra = frozenset('abracadabra')
print(fr_abra)
# frozenset({'d', 'r', 'a', 'c', 'b'})

fr_nums = frozenset([2, 1, 2, 4, 5, 2, 1])
print(fr_nums)
# frozenset({1, 2, 4, 5})

lang = {'eng': 'Английский', 'ru': 'Русский'}

print(frozenset(lang))
# frozenset({'eng', 'ru'})

my_set = {1, 2, 2, 3}
print(frozenset(my_set))
# frozenset({1, 2, 3})
