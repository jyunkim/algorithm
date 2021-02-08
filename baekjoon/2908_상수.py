a, b = map(list, input().split())
a.reverse()  # 원래 배열 변화
b.reverse()
c = int(''.join(a))
d = int(''.join(b))

if c > d:
    print(c)
else:
    print(d)
