# PriorityQueue: thread-safety class(lock 제공)
# heapq: thread-safe x, 일반 list 사용, 속도 빠름
import sys
import heapq

inf = sys.maxsize
v, e = map(int, input().split())
start = int(input())
heap = []
# 노드 번호가 1번부터 시작하므로
graph = [[] for _ in range(v + 1)]
weights = [inf] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    # (가중치, 목적지)
    graph[a].append((w, b))

# 다익스트라 알고리즘
def dijkstra(start):
    weights[start] = 0
    # 튜플을 넣을 경우 첫번째 요소 기준
    heapq.heappush(heap, (0, start))
    while heap:
        weight, cur = heapq.heappop(heap)
        # 이미 탐색한 노드인데 가중치가 더 크면 스킵
        if weight > weights[cur]:
            continue
        # 갈 수 있는 노드 중
        for next_weight, dest in graph[cur]:
            # 시작부터 목적지 노드까지 가중치 합
            next_weight += weight
            # 현재까지의 최소값보다 작으면 갱신
            if next_weight < weights[dest]:
                weights[dest] = next_weight
                heapq.heappush(heap, (next_weight, dest))

dijkstra(start)

for i in range(1, v + 1):
    print("INF" if weights[i] == inf else weights[i])
