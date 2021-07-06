n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

# 완전 탐색
# for i in range(n):
#     total = 0
#     for j in range(i, n):
#         total += nums[j]
#         if total == m:
#             answer += 1
#             break
#         elif total > m:
#             break

# 투 포인터
i = 0
total = 0
for j in range(n):
    total += nums[j]
    while total > m:
        total -= nums[i]
        i += 1
    if total == m:
        answer += 1

print(answer)
