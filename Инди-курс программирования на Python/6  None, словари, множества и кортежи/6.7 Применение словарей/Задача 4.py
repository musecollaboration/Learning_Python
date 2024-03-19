# https://stepik.org/lesson/296968/step/6?auth=login&unit=278696

# Анаграмма
# Cтрока S1 называется анаграммой строки S2, 
# если она получается из S2 перестановкой символов.
# Программа получает на вход две строки S1 и S2. 
# Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO

# Sample Input 1:
# abc
# cba

# Sample Output 1:
# YES

# Sample Input 2:
# abb
# bbc

# Sample Output 2:
# NO

S1, S2 = input(), input()
d1, d2 = {}, {}

for i in S1:
    d1[i] = d1.get(i, 0) + 1
for i in S2:
    d2[i] = d2.get(i, 0) + 1

if d1 == d2:
    print('YES')
else:
    print('NO')
