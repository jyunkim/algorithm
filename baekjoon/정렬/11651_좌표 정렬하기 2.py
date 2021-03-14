import sys

n = int(sys.stdin.readline())
coords = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
coords.sort(key=lambda coord: (coord[1], coord[0]))  # 정렬 기준 우선순위

for x, y in coords:
    print(x, y)

# for i in range(n):
#     coords[i][0], coords[i][1] = coords[i][1], coords[i][0]

# coords.sort()
# for x, y in coords:
#     print(y, x)
