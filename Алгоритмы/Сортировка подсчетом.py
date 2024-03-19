# https://stepik.org/lesson/296962/step/1?auth=login&unit=278690

# https://stepik.org/lesson/296962/step/3?auth=login&unit=278690

n = int(input())
a = list(map(int, input().split()))
count = [0] * 201

for i in a:
    count[i + 100] += 1

for i in range(201):
    if count[i] > 0:
        print((str(i - 100) + ' ') * count[i], end='')
