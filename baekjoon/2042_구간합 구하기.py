# 구간 합
# 데이터 개수: N, 데이터 변경 횟수: M, 구간 합 계산 횟수: K
# 시간복잡도 - O(M), O(KM)
# Index tree
# 시간복잡도 - O(MlogN), O(KlogN)
# 구간 최대, 최소, 중앙값 등에도 사용 가능
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 필요한 리프노드 수 구하기
num = 1
temp = 0
while num < n:
    num *= 2
    temp += 1

# 1 ~ num-1 -> 부모 노드, num ~ num*2-1 -> 리프 노드
tree = [0] * (num * 2)

# 리프 노드 채우기
for i in range(n):
    tree[i + num] = int(input())

# 부모 노드 채우기
for i in range(num - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

# 수가 변경될 경우 갱신
def update(i, value):
    index = i + num - 1
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] + tree[index * 2 + 1]

# 구간합 반환
def query(l, r):
    answer = 0
    l += (num - 1)
    r += (num - 1)
    # l이 왼쪽 노드(짝수)면 부모로 이동, 오른쪽 노드(홀수)면 현재 값을 더하고 다음 오른쪽 노드의 부모로 이동
    # r이 오른쪽 노드(홀수)면 부모로 이동, 왼쪽 노드(짝수)면 현재 값을 더하고 이전 왼쪽 노드의 부모로 이동
    while l <= r:
        if l % 2 == 1:
            answer += tree[l]
            l += 1
        if r % 2 == 0:
            answer += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return answer

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        print(query(b, c))
