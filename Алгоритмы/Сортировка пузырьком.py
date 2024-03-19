# https://stepik.org/lesson/296963/step/6?auth=login&unit=278691

n = int(input())
m = list(map(int, input().split()))
c = 0
for run in range(n - 1):
    for i in range(n - 1 - run):
        if m[i] > m[i + 1]:
            c += 1
            m[i], m[i + 1] = m[i + 1], m[i]

print(*m)
print(c)
