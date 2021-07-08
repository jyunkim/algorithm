from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
height = [list(map(int, input().split())) for _ in range(n)]
k_num = 0
height_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'P':
            p_loc = (i, j)
        elif graph[i][j] == 'K':
            k_num += 1
        height_list.append(height[i][j])

# sorted - 모든 iterable 가능
height_list = sorted(set(height_list))
di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(low, high):
    count = 0
    visited = [[False] * n for _ in range(n)]
    dq = deque()
    # P에서 시작
    dq.append(p_loc)
    visited[p_loc[0]][p_loc[1]] = True
    while dq and count < k_num:
        cur_i, cur_j = dq.popleft()
        for i in range(8):
            new_i = cur_i + di[i]
            new_j = cur_j + dj[i]
            # 범위를 벗어난 경우
            if new_i < 0 or new_j < 0 or new_i >= n or new_j >= n:
                continue
            # 이미 방문한 경우
            if visited[new_i][new_j]:
                continue
            # 고도 범위를 벗어난 경우
            if height[new_i][new_j] < height_list[low] or height[new_i][new_j] > height_list[high]:
                continue
            if graph[new_i][new_j] == 'K':
                count += 1
            visited[new_i][new_j] = True
            dq.append((new_i, new_j))
    return count


# 투 포인터
# 피로도를 먼저 설정하고 모든 집을 탐색할 수 있는지 확인
# 모든 집을 탐색할 수 있을 때까지 상한선을 높이고
# 최소 피로도를 찾을 때까지 하한선을 높임
low = 0
high = 0
answer = height_list[-1] - height_list[0]
start_height = height[p_loc[0]][p_loc[1]]
while low < len(height_list) and high < len(height_list):
    # 모든 집을 탐색 가능할 경우(첫번째 지점도 검사)
    if start_height >= height_list[low] and start_height <= height_list[high] and bfs(low, high) == k_num:
        temp = height_list[high] - height_list[low]
        # 최소인 피로도
        answer = min(answer, temp)
        low += 1
    else:
        high += 1

print(answer)
