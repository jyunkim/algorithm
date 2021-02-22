n = int(input())
map = [[0 for i in range(n)] for j in range(n)]

def star(n):
    global map

    if n == 3:
        map[0][:3] = map[2][:3] = [1] * 3
        map[1][:3] = [1, 0, 1]
        return
    star(n//3)  # int/int = float
    a = n // 3
    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1):  # not and -> or 주의
                for k in range(a):
                    map[i * a + k][j * a:(j + 1) * a] = map[k][:a]

star(n)

for i in range(n):
    for j in range(n):
        if map[i][j]:
            print('*', end='')
        else:
            print(' ', end='')
    print()
