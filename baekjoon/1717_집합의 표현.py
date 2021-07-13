# Union-Find
n, m = map(int, input().split())
# 자신이 가리키고 있는 수를 표현
parent = [i for i in range(n + 1)]

# 자신의 최상위 부모를 찾음
def get_parent(x):
    # 종료 조건
    if parent[x] == x:
        return x
    p = get_parent(parent[x])
    # 최상위 부모를 가리키게 해서 시간 단축
    parent[x] = p
    return p

# 자신의 최상위 부모가 가리키게 함
def union(x, y):
    x = get_parent(x)
    y = get_parent(y)
    if x != y:
        parent[x] = y

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    elif a == 1:
        # 최상위 부모가 같을 경우
        if find(b) == find(c):
            print("yes")
        else:
            print("no")
