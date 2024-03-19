# https://stepik.org/lesson/296967/step/4?auth=login&unit=278695
n = int(input())

database = {}
for i in range(n):
    login = input()
    if login in database:
        database[login] += 1
        database[f"{login}{database[login]}"] = 0
        print(f"{login}{database[login]}")
    else:
        database[login] = 0
        print(f'OK')
print(database)
