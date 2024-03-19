# https://stepik.org/lesson/296956/step/6?unit=278684

a = int(input())
i = 0
while True:
    if a == 1:
        break
    elif a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
    i += 1

print(i)
