import sys
input = sys.stdin.readline

# 최적화
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
# 양 끝일 때 조건문 안써도 되도록 1개씩 늘려줌
total = [[0] * (i + 2) for i in range(1, n + 1)]

# 초기값
total[0][1] = triangle[0][0]

answer = 0
for i in range(1, n):
    for j in range(1, len(total[i]) - 1):
        # 점화식
        total[i][j] = max(total[i - 1][j - 1], total[i - 1][j]) + triangle[i][j - 1]
        answer = max(answer, total[i][j])

print(answer)

# n = int(input())
# triangle = [list(map(int, input().split())) for _ in range(n)]
# total = [[0] * i for i in range(1, n + 1)]
# total[0][0] = triangle[0][0]

# for i in range(1, n):
#     for j in range(len(total[i])):
#         if j == 0:
#             total[i][j] = total[i - 1][j] + triangle[i][j]
#         elif j == len(total[i]) - 1:
#             total[i][j] = total[i - 1][j - 1] + triangle[i][j]
#         else:
#             total[i][j] = max(total[i - 1][j - 1], total[i - 1][j]) + triangle[i][j]

# answer = 0
# for j in range(len(total[n - 1])):
#     answer = max(answer, total[n - 1][j])

# print(answer)
