# https://stepik.org/lesson/296963/step/8?auth=login&unit=278691

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break

print(*a)
