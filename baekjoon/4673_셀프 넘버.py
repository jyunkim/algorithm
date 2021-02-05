def d(n):
    return n + sum(map(int, str(n)))

gen = set([d(i) for i in range(10001)])
for i in range(10001):
    if i not in gen:
        print(i)

# set(range(100))
