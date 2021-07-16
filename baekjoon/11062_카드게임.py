# 최선의 선택은 모든 선택이 끝났을 때 알 수 있음 -> Top-down 방식
# 그리디로 할 경우 최적값 x
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# l ~ r 구간의 카드에서 얻을 수 있는 최대 점수 반환
def dp(l, r, turn):
    # 종료 조건
    if l > r:
        return 0
    # 메모이제이션
    # 이미 탐색한 경우일 경우
    if score[l][r] != 0:
        return score[l][r]
    # 근우 차례
    # 왼쪽 카드를 선택할 경우와 오른쪽 카드를 선택할 경우 중 큰 점수 선택
    if turn:
        score[l][r] = max(cards[l] + dp(l + 1, r, False), cards[r] + dp(l, r - 1, False))
    # 명우 차례
    # 근우의 점수가 최소가 되도록 선택 - 근우의 다음 선택 중 작은 점수 선택
    else:
        score[l][r] = min(dp(l + 1, r, True), dp(l, r - 1, True))
    return score[l][r]

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    # score[i][j] = i ~ j 구간의 카드에서 얻을 수 있는 최대 점수
    score = [[0] * n for _ in range(n)]
    print(dp(0, n - 1, True))