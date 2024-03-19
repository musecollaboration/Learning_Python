# ? .startswith()
# Данный метод возвращает True если строка начинается с последовательности символов prefix (префикса) и False в противном случае.
# * При передаче параметра start проверка начнется именно с этой позиции. Если передать значение  end, проверка закончится в этой позиции.
s = 'Мила Кунис'
print(s.startswith('Мила'))        # True
print(s.startswith('М'))           # True
print(s.startswith('Бред'))        # False
print('-----')
print(s.startswith('Мила', 1))     # False
print(s.startswith('ила', 1))      # True
print('-----')
print(s.startswith('ил', 1, 2))    # False
print(s.startswith('ил', 1, 3))    # True


# ? .endswith()
# Данный метод возвращает True если строка S заканчивается последовательностью символов prefix (префикса) и False в противном случае.
s = 'Мила Кунис'

print(s.endswith('Кунис'))        # True
print(s.endswith('с'))            # True
print(s.endswith('Бред'))         # False
print('-----')
print(s.endswith('нис', 10))      # False
print(s.endswith('нис', 7))       # True
print(s.endswith('нис', -3))      # True
print('-----')
print(s.endswith('ис', 8, 9))     # False
print(s.endswith('ис', 8, 10))    # True
