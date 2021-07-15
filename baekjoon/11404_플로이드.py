import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 노선이 여러개 일 수 있으므로
    graph[a][b] = min(graph[a][b], c)

# i->j보다 i->k->j 비용이 더 작을 경우 갱신
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] == inf else graph[i][j], end=' ')
    print()
