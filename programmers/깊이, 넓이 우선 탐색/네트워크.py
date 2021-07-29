def dfs(computers, visited, n, node):
    visited[node] = True
    for i in range(n):
        # 아직 방문하지 않았거나, 연결되어 있으면 탐색
        if not visited[i] and computers[node][i] == 1:
            dfs(computers, visited, n, i)
    

def solution(n, computers):
    answer = 0
    visited = [False] * n
    # 연결되지 않은 트리 수 = dfs 실행 수(방문하지 않은 노드만 탐색)
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, n, i)
            answer += 1
    return answer
