# ? Регистр строк

# ? .upper()
a = 'hello'.upper()
print(a)
# HELLO


# ? .lower()
a = 'HeLLO'.lower()
print(a)
# hello


# ? .title()
# каждое слово исходной строки начинается с буквы в верхнем регистре, а все остальные буквы в нижнем
s = 'hello world'
print(s.title())
# Hello World


# ? .capitalize()
# первый символ находится в верхнем регистре, а все остальные в нижнем
s = 'hello world'
print(s.capitalize())
# Hello world


# ? .swapcase()
# все заглавные буквы преобразованы в строчные, строчные – в заглавные
s = 'hellO wOrld!123'
print(s.swapcase())
# HELLo WoRLD!123
