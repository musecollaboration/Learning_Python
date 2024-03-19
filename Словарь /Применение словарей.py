# Подсчет количества объектов
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
