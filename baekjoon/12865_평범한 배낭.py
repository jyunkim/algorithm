# 그리디
# 가치가 높은 순서로 넣으면 2개 넣을걸 1개 넣어서 전체 가치가 작을 수 있음

# 완전 탐색
# 시간 초과

# DP
# dp[i]: ikg일 때 물건의 최대 가치
# 1 ~ i-1번째를 이용하여 dp[i]를 구할 수 있는가?
# dp[i][j]도 가능

# Knapsack Problem
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# Index가 다 1부터 시작하므로 물건의 index도 1부터 시작
jewls = [(0, 0) if i == 0 else tuple(map(int, input().split())) for i in range(n + 1)]

# 행: 물건, 열: 배낭 무게
# 0번째 행, 0번째 열은 0으로 초기화
total = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if jewls[i][0] > j:
            total[i][j] = total[i - 1][j]
        else:
            # 현재 물건을 넣지 않을 때 최대 가치
            # 현재 물건을 넣었을 때 최대 가치 -> 전체 무게 중 현재 물건의 무게를 뺀 것의 최대 가치 + 현재 물건의 가치
            total[i][j] = max(total[i - 1][j], total[i - 1][j - jewls[i][0]] + jewls[i][1])

print(total[-1][-1])
