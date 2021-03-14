import sys

n = int(sys.stdin.readline())
users = [sys.stdin.readline().split() for _ in range(n)]
users.sort(key=lambda user: int(user[0]))
# key 설정 안해주면 디폴트로 모든 요소 대상으로 인덱스 순서로 정렬 [(2, 2), (1, 3), (1, 1)] -> [(1, 1), (1, 3), (2, 2)]

for x, y in users:
    print(x, y)
