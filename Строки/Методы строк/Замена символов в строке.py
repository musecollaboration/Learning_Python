# 4.  Замена символов

# ? .replace()
# Заменяет символы в строке.
# Удаляет символы в строке.
# * Можно указать сколько замен - удалений нужно сделать
s = 'hello world'
print(s.replace('o', '+'))    # hell+ w+rld
print(s.replace('l', ''))     # heo word
print(s.replace('l', '', 2))  # * heo world
print(s.replace(' ', ''))     # helloworld


# ? .ljust()
# Принимает один обязательный параметр width - ширину строки и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел) .
# Возвращает новую строку, в которой исходная строка дополнена справа символами fillchar до указанной длины width. Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений.
d = 'qwerty'
print(d.ljust(10))        # qwerty____
print(d.ljust(10, '-'))   # qwerty----
print(d.ljust(10, '&'))   # qwerty&&&&
print(d.ljust(5, '!'))    # qwerty

# **В параметр fillchar можно передать только строку, состоящую из одного символа. Если передать пустую строку или более одного символа, произойдет ошибка.


# ? .rjust()
# Возвращает новую строку, в которой исходная строка S дополнена слева символами fillchar до указанной длины width.
# Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений.
d = 'qwerty'
print(d.rjust(10))       # ____qwerty
print(d.rjust(10, '-'))  # ----qwerty
print(d.rjust(10, '&'))  # &&&&qwerty
print(d.rjust(5, '!'))   # qwerty


# ? .center()
# Метод .center принимает один обязательный параметр width - ширину строки и один необязательный параметр fillchar - знак заполнителя (по умолчанию пробел)
d = 'qwerty'
print(d.center(10))        # __qwerty__
print(d.center(12, '$'))   # $$$qwerty$$$
print(d.center(13, '+'))   # ++++qwerty+++  **
print(d.center(5, '$'))    # qwerty

# В параметр fillchar также можно передать только строку, состоящую из одного символа.
#  **В случаях, когда количество необходимых для дополнения символов нечетно, слева будет на один символ fillchar больше чем справа


#  ? .zfill()
# Метод .zfill возвращает новую строку, в которой исходная строка S дополнена нулями слева так, чтобы длина новой строки стала равна width
d = '123'
print(d.zfill(5))          # 00123
print(d.zfill(6))          # 000123
print(d.zfill(2))          # 123
print(d.zfill(3))          # 123
print('0.123'.zfill(6))    # 00.123
