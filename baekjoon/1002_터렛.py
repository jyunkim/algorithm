n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r > r1 + r2 or r < max(r1, r2) - min(r1, r2):
            print(0)
        elif r == r1 + r2 or r == max(r1, r2) - min(r1, r2):
            print(1)
        # if r < r1 + r2로 할 경우 위의 조건들도 포함하기 때문에 else로 뺌
        else:
            print(2) 
