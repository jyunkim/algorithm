from itertools import product

n, m = map(int, input().split())
prd = product(range(1, n+1), repeat=m)
for i in prd:
    print(*i)  # iterable 공백으로 분리해서 출력
    # print(*i, sep = '\n')
    # print(' '.join(map(str, i)))