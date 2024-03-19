
# ? .isalfa()
# Проверяет состоит ли строка целиком из букв
# * Пробел не буква!
s1 = 'hello world'
s2 = 'helloworld'
print(s1.isalpha())    # * False
print(s2.isalpha())    # True


# ? .isdigit()
# Проверяет состоит ли строка целиком из цифр
# * Пробел не цифра!
# * Полезно делать проверку перед преобразованием в число
s1 = '1234'
s2 = '12 34'
print(s1.isdigit())   # True
print(s2.isdigit())   # * False
