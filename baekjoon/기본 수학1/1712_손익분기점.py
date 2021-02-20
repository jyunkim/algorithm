a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    # 손익분기점: a + b * x = c * x
    # x = a / (c - b)
    print(int(a / (c - b)) + 1)
