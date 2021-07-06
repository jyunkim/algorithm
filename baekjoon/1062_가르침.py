# 완전 탐색(브루트 포스) -> 시간 초과
# 백트래킹(DFS), 가지치기, DP 이용
from itertools import combinations

n, k = map(int, input().split())
words = [set(input()[4:-4]).difference({'a', 'c', 'i', 'n', 't'}) for i in range(n)]
letters = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 0

if k < 5:
    print(0)
else:
    for case in list(combinations(letters, k - 5)):
        count = 0
        for word in words:
            if not word.difference(case): # 인자는 set이 아니어도 됨
                count += 1
        answer = max(answer, count)
    print(answer)
