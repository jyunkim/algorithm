# 1억 = 약 1초 소요
# 탐색 시간 줄이는 방법
# 이분 탐색, 해시
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# O(n^2), n = 100000 -> 약 100초
# for i in b:
#     if i in a:
#         print(1)
#     else:
#         print(0)

# 이분 탐색
a.sort()

for i in b:
    # index 반환
    # list에 없을 경우, 들어가야될 index 반환
    x = bisect_left(a, i)
    if x < len(a) and a[x] == i:
        print(1)
    else:
        print(0)
