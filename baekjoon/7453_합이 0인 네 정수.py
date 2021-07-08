# 완전 탐색 - 4000^4 -> 시간 초과
# 1. 정렬 -> 이분 탐색 / 투 포인터
# 2. 해시
# 최악의 경우 4000^4이므로 int가 아닌 long 사용

n = int(input())
a = []; b = []; c = []; d = []
for _ in range(n):
    nums = input().split()
    a.append(int(nums[0]))
    b.append(int(nums[1]))
    c.append(int(nums[2]))
    d.append(int(nums[3]))

ab = []; cd = []
for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])
        cd.append(c[i] + d[j])

answer = 0

# # 투 포인터 - 가장 빠름

# ab.sort()
# cd.sort()

# count = 0
# j = n * n - 1
# for i in range(n * n):
#     # 같은 값이면 이전 count 더함
#     if i > 0 and ab[i] == ab[i-1]:
#         answer += count
#         continue
#     # index를 조작할 땐 범위 벗어나는 것 염두
#     while j > 0 and ab[i] + cd[j] > 0:
#         j -= 1
#     count = 0
#     while j >= 0 and ab[i] + cd[j] == 0:
#         count += 1
#         j -= 1
#     answer += count


# 해시
# from collections import Counter

# cd_dict = Counter(cd)
# for num in ab:
#     answer += cd_dict[-num]

# 해시 직접 구현이 속도는 더 빠름
cd_dict = {}
for i in cd:
    if cd_dict.get(i):
        cd_dict[i] += 1
    else:
        cd_dict[i] = 1

for num in ab:
    if cd_dict.get(-num):
        answer += cd_dict[-num]

print(answer)
