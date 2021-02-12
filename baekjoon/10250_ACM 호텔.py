import math

k = int(input())
for i in range(k):
    h, w, n = map(int, input().split())
    b = math.ceil(n / h)
    a = n % h
    if a == 0:
        a = h
    print(f'{a}{b}' if b >= 10 else f'{a}0{b}')
