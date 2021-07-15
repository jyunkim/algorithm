import sys
input = sys.stdin.readline

n = int(input())
scores = [0 if i == 0 else int(input()) for i in range(n + 1)]
total = [[0] * 2 for _ in range(n + 1)]

# 초기값(1부터 시작)
# [i][0]: i-1에서 올라왔을 경우
# [i][1]: i-2에서 올라왔을 경우
total[1][0] = scores[1]
total[1][1] = scores[1]

# n = 1일 때 에러
# total[0][0] = scores[0]
# total[0][0] = scores[1]
# total[1][0] = scores[1] + scores[0]
# total[1][1] = scores[1]

for i in range(2, n + 1):
    # 점화식
    total[i][0] = total[i - 1][1] + scores[i] # 연속 세칸이 될 수 없으므로
    total[i][1] = max(total[i - 2][0], total[i - 2][1]) + scores[i]

print(max(total[-1][0], total[-1][1]))
