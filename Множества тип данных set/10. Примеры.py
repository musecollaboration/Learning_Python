
# ? Добавляются уникальные слова в множество
text = input()
a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    text = input()

print(a)          # вывод множества
print(len(a))     # колличество уникальных слов
