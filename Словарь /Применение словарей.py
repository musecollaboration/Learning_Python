# https://www.youtube.com/watch?v=dZ474oWml9k&ab_channel=egoroff_channel
# https://stepik.org/lesson/296968/step/2?auth=login&unit=278696

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


# Разряженный список
# без словаря
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(i, letters[i])


# Разряженный список
# со словарем
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)


# Установление связи между обьектами
# переводчикб словарь
words = {}
while True:
    s = input()
    if s in words:
        print(f'Слово {s} переводится как {words[s]}')
    else:
        print('Введите перевод слова')
        words[s] = input()
