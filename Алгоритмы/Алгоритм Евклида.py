# https://stepik.org/lesson/296616/step/1?unit=278350

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while b > 0:
    c = a % b
    a = b
    b = c
print(f'Нод={a}')


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(f'Нод={a}')
