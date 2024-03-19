# Подсчет количества объектов

# Логика
s = 'asdfbhmfvaadsdc'
d = {}
d['a'] = 1
print(d)
if 'a' in d:
    d['a'] += 1
else:
    d['a'] = 1
print(d)
if 'b' in d:
    d['b'] += 1
else:
    d['b'] = 1
print(d)


# Без применения метода .get()
s = 'asdfb@#$hmfvaadsdc'
d = {}
for i in s:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
for i, j in sorted(d.items()):
    print(i, j)


# C применением метода .get()
s = 'asdfb@#$hmfvaadsdc'
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
for i, j in sorted(d.items()):
    print(i, j)


