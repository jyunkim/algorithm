n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    score = a[1:]
    avg = sum(score) / a[0]
    over = list(filter(lambda x: x > avg, score))
    ratio = len(over) / a[0] * 100
    print(f'{ratio:.3f}%')
