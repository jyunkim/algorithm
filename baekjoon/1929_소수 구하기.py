# 에라토스테네스의 체
m, n = map(int, input().split())
primes = [False, False] + [True] * (n-1)

for i in range(2, len(primes)):
    if primes[i]:
        for j in range(2 * i, len(primes), i):
            primes[j] = False

for i in range(m, n + 1):
    if primes[i]:
        print(i)
