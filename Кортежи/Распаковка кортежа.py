# У нас есть кортеж с четырьмя элементами
t = ('Allison Hill', 334053, 'M', '1635644202')

# Распаковываем значения кортежа в переменные
name, salary, gender, passport = t

# Теперь переменные содержат соответствующие значения из кортежа
print(name)      # Allison Hill
print(salary)    # 334053
print(gender)    # M
print(passport)  # 1635644202

print('-' * 10)
# Количество переменных должно соответствовать количеству элементов в кортеже. 
# Если элементов больше или меньше, чем переменных, Python выдаст ошибку. 
# Если вам нужно распаковать только некоторые элементы,
# вы можете использовать:
# символ _ для игнорирования ненужных элементов 
# или * для сбора оставшихся элементов в список. 
# Вот пример:

# Распаковываем только первый и последний элементы
name, *_, passport = t
print(name)      # Allison Hill
print(passport)  # 1635644202

# Использование * для сбора оставшихся элементов:
# *middle собирает все элементы между первым и последним в список.
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(first)   # Выведет 1
print(middle)  # Выведет [2, 3, 4]
print(last)    # Выведет 5

# Использование _ для игнорирования некоторых элементов:
# _ используется для игнорирования всех элементов, кроме первого и последнего. 
t = (1, 2, 3, 4, 5)
first, _, _, _, last = t
print(first)  # Выведет 1
print(last)   # Выведет 5

# Это полезно, когда вам нужны только определенные данные из кортежа.

s = ('Allison Hill', 334053, 'M', '1635644202')
name, salary, gender, passport = s
d = {
    'name': name,
    'salary': salary,
    'gender': gender,
    'passport': passport
}
print(d)
# {'name': 'Allison Hill', 'salary': 334053, 'gender': 'M', 'passport': '1635644202'}
# PS D:\My_folder\Python> 
