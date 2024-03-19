# https://stepik.org/lesson/296616/step/6?unit=278350

a, b = map(int, input().split())
while a != b:
    if a == 0 or b == 0:
        break
    else:
        c = a % b
        a, b = b, c

print(a)
