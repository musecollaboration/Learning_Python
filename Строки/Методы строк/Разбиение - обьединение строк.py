# Разбиение - обьединение строк

# ? .split()
# Разбивает строку по указаным символам и формирует список
text = "Python is best"
print(text.split())      # ['Python', 'is', 'best']

text = "Ivanov Ivan Ivaovich"
print(text.split('n'))   # ['Iva', 'ov Iva', ' Ivaovich']

text = "43,54,674,1434"
print(text.split(','))   # ['43', '54', '674', '1434']


# ? ' '.join.()
# Обьединяет в строку по указаным символам
text = ['43', '54', '674', '1434']
print('='.join(text))        # 43=54=674=1434

t = "Ivanov Ivan Ivaovich"
print(','.join(t.split()))   # Ivanov,Ivan,Ivaovich


# ? .partition()
# Разбивает строку по указанному разделителю и возвращает кортеж из трех элементов: строка до разделителя, сам разделитель и строка после разделителя.
# *Если разделитель не найден, то возвращается кортеж так же состоящий из трех элементов в котором первый элемент – это исходная строка, а два других элемента – это пустые строки.
text = "Python is best"

print(text.partition('is '))   # ('Python ', 'is ', 'best')
print(text.partition('not '))  # * ('Python is best', '', '')

s = "Python is best, isn't it"

print(s.partition('is'))       # ('Python ', 'is', " best, isn't it")


# ? .rpartition()
# Разбивает строку по последнему встреченному разделителю sep и возвращает кортеж, который состоит из трех элементов: строки до разделителя, самого разделителя и строки после разделителя.
# *Если разделитель в строке отсутствует, то кортеж будет состоять из: двух пустых строк и исходной строки
text = "Python is best"

print(text.rpartition('is '))   # ('Python ', 'is ', 'best')
print(text.rpartition('not '))  # * ('', '', 'Python is best')

s = "Python is best, isn't it"

print(s.rpartition('is'))       # ('Python is best, ', 'is', "n't it")
