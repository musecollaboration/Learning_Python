# https://stepik.org/lesson/296961/step/15?auth=login&unit=278689

n = input()
a = []
f = True

for i in n:
    if i in '([{':
        a.append(i)
    elif i in ')]}':
        if not a:
            f = False
            break

        lasti = a.pop()
        if lasti == '(' and i == ')':
            continue
        elif lasti == '[' and i == ']':
            continue
        elif lasti == '{' and i == '}':
            continue
        f = False
        break


if f and len(a) == 0:
    print('YES')
else:
    print('NO')
