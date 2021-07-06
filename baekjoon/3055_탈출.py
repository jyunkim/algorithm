# BFS - 최단 거리
from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))

s = deque()
w = deque()
s_graph = [[0] * n for _ in range(m)]
dm = [1, -1, 0, 0]
dn = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'S':
            s.append((i, j))
            s_graph[i][j] = 1
        elif graph[i][j] == '*':
            w.append((i, j))

done = False
while s and not done:
    # 현재 시점 +1만 이동
    cur_len = len(w)
    for _ in range(cur_len):
        wm, wn = w.popleft()
        for i in range(4):
            new_wm = wm + dm[i]
            new_wn = wn + dn[i]
            if new_wm < 0 or new_wn < 0 or new_wm >= m or new_wn >= n:
                continue
            if graph[new_wm][new_wn] == 'D' or graph[new_wm][new_wn] == 'X' or graph[new_wm][new_wn] == '*':
                continue
            graph[new_wm][new_wn] = '*'
            w.append((new_wm, new_wn))
    
    cur_len = len(s)
    for _ in range(cur_len):
        sm, sn = s.popleft()
        for i in range(4):
            new_sm = sm + dm[i]
            new_sn = sn + dn[i]
            if new_sm < 0 or new_sn < 0 or new_sm >= m or new_sn >= n:
                continue
            if graph[new_sm][new_sn] == '*' or graph[new_sm][new_sn] == 'X' or s_graph[new_sm][new_sn] != 0:
                continue
            if graph[new_sm][new_sn] == 'D':
                print(s_graph[sm][sn])
                done = True
                break
            else:
                s_graph[new_sm][new_sn] = s_graph[sm][sn] + 1
                s.append((new_sm, new_sn))
        if done:
            break
    
if not done:
    print("KAKTUS")
