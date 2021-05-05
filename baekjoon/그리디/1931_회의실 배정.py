n = int(input())
confs = [tuple(map(int, input().split())) for _ in range(n)]
confs.sort(key=lambda x: (x[1], x[0]))
count = 1

end = confs[0][1]
for i in range(1, n):
    if confs[i][0] >= end:
        count += 1
        end = confs[i][1]

print(count)
