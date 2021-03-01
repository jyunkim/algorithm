n = int(input())
arr = [tuple(map(int, input().split())) for i in range(n)]

for person in arr:
    count = 1
    for other in arr:
        if person[0] < other[0] and person[1] < other[1]:
            count += 1
    print(count, end=' ')
