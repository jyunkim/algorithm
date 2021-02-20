n = int(input())

if n < 100:
    print(n)
else:
    count = 99
    for i in range(100, n + 1):
        first = i % 10
        second = i // 10 % 10
        third = i // 100
        if second - first == third - second:
            count += 1
    print(count)
