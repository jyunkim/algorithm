n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = [0] * m
used = [False] * n

def recur(x):
    # 종료 조건
    if x == m:
        for a in answer:
            print(a, end=' ')
        print()
        return
    last = 0
    for i in range(n):
        # 백트래킹
        # 전에 쓰인 숫자는 사용 x
        if not used[i] and last != nums[i]:
            answer[x] = nums[i]
            last = nums[i]
            used[i] = True
            recur(x + 1)
            used[i] = False

recur(0)
