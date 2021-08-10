# MST
# Kruskal Algorithm

# x, y 연결
def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    parent[y] = x


# x가 속한 집합의 대표 노드(최상위 부모) 반환
def find(x, parent):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x], parent)
        parent[x] = p
        return p
        

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    parent = [i for i in range(n)]
    for edge in costs:
        if find(edge[0], parent) != find(edge[1], parent):
            union(edge[0], edge[1], parent)
            answer += edge[2]
    return answer
