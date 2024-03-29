# Удаление символов слева и справа

# ? .strip()
# Возвращает копию строки, удаляя как начальные, так и конечные символы (в зависимости от переданного строкового аргумента).
# Метод удаляет символы как слева, так и справа в зависимости от аргумента chars .
# *Если аргумент chars не передан, то по умолчанию удаляться пробелы и символы переноса на новую строку \n
q = '  hello  '
print(q)                                 # __hello__
print(q.strip())                         # hello
print('\n\n\n_USB_\n\n\n\n'.strip())     # * _USB_ удалил все переносы
print('123_USB_123'.strip('123'))        # _USB_

# *Символы в параметре chars рассматриваются не как последовательность, а как набор символов, которые необходимо удалить
print('321232321_USB_31121312'.strip('123'))  # _USB_

# Используется при обработке файлов для удаления пробельных символов и символов переноса


# ? .rstrip()
# Возвращает копию строки, в которой справа удалены указанные символы (по умолчанию удаляются пробельные символы)
q = '   hello   '
print(q)                                       # ___hello___
print(q.rstrip())                              # ___hello
# пробел **оставил 3 переноса слева, 4 справа удалил
# пробел
# пробел
print('\n\n\n_USB_\n\n\n\n'.rstrip())          # _USB_ **
print('123_USB_123'.rstrip('123'))             # 123_USB_
print('321232321_USB_31121312'.rstrip('123'))  # 321232321_USB_


# ? .lstrip()
# Возвращает копию строки, в которой слева удалены указанные символы (по умолчанию удаляются пробельные символы)
q = '   hello   '
print(q)                                       # ___hello___
print(q.lstrip())                              # hello___
print('\n\n\n_USB_\n\n\n\n'.lstrip())          # _USB_
# пробел **3 переноса слева удалил, оставил 4 переноса справа
# пробел
# пробел
# пробел
print('123_USB_123'.lstrip('123'))             # _USB_123
print('321232321_USB_31121312'.lstrip('123'))  # _USB_31121312
