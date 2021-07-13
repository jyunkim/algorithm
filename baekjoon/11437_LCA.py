import sys
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕음
# 런타임 에러를 피하기 위해 제한 설정
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)] # 인접 리스트
depth = [0] * (n + 1) # 각 노드의 깊이
visited = [False] * (n + 1) # 방문 여부
parent = [0] * (n + 1) # 부모 노드

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 깊이 구하기
def dfs(cur, cur_depth):
    visited[cur] = True
    depth[cur] = cur_depth
    for node in graph[cur]:
        if not visited[node]:
            parent[node] = cur
            dfs(node, cur_depth + 1)

# a와 b의 최소 공통 조상 반환
def lca(a, b):
    # 깊이가 다르면 같게 맞춰줌
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 부모가 같을 때까지 -> 둘 중 하나가 lca일 경우 찾지 못함
    # while parent[a] != parent[b]:
    #     a = parent[a]
    #     b = parent[b]
    # return parent[a]
    # 서로 같아질 때 까지
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
