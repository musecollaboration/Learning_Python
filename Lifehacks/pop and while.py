n = [1, 2, 3, 4, 5]
while n:
    print(n[-1])
    d = n.pop()


n = [1, 2, 3, 4, 5]
d = n.pop()
while n:
    d = {n.pop(): d}
print(d)
# {1: {2: {3: {4: 5}}}}
