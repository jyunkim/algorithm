h, m = map(int, input().split())

if h == 0:
    if m < 45:
        h = 23
        m += 15
    else:
        m -= 45
else:
    if m < 45:
        h -= 1
        m += 15
    else:
        m -= 45

print(h, m)
