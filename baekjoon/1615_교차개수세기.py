# Count index tree
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
# A 기준으로 오름차순 정렬
edges.sort()

num = 1
temp = 0
while num <= n:
    num *= 2
    temp += 1

tree = [0] * (num * 2)

# edge 하나씩 추가하면서 트리 갱신
def update(i):
    index = i + num - 1
    tree[index] += 1
    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] + tree[index * 2 + 1]

# 구간합 - 개수 count
def query(l, r):
    count = 0
    l += (num - 1)
    r += (num - 1)
    while l <= r:
        if l % 2 == 1:
            count += tree[l]
            l += 1
        if r % 2 == 0:
            count += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return count

answer = 0
for edge in edges:
    # 이전 edge들 중에서 B가 더 큰 edge 개수 구하기 - 현재까지 갱신된 트리의 구간합 이용
    answer += query(edge[1] + 1, n)
    # 트리 갱신 - 현재 B 정점값 + 1
    update(edge[1])

print(answer)
