import itertools

answer = 0
a = ['1', '1', '0']
for i in range(1, len(a) + 1):
    b = set(itertools.permutations(a, i))
    d = []
    for c in b:
        if c[0] == '0':
            continue
        d.append(int(''.join(c)))
    for n in d:
        if n < 10:
            if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
                answer -= 1
                continue
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                answer -= 1
                break
    answer += len(d)
print(answer)