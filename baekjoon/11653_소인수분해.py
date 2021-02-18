n = int(input())

while True:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            n //= i  # 그냥 나누면 float됨
            break
    if n == 1:
        break
