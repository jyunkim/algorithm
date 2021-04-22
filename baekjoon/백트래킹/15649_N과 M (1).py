from itertools import permutations

n, m = map(int, input().split())
# ns = [i+1 for i in range(n)]
per = permutations(range(1, n+1), m)

for i in per:
    for j in i:
        print(j, end=' ')
    print()

# ns = map(str, range(1, N+1))
# print('\n'.join(list(map(' '.join, permutations(ns, m)))))