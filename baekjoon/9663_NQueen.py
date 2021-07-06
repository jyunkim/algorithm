# 파이썬으로 할 경우 시간 초과
n = int(input())
board = [[-1] * n for _ in range(n)]
answer = 0

def check(i, j):
    # 퀸을 놓을 수 있는지 검사
    # 좌우
    for jj in range(n):
        if board[i][jj] != -1:
            return False
    # 상
    for ii in range(0, i):
        if board[ii][j] != -1:
            return False
    # 대각
    a = i
    b = j
    while a >= 0 and b < n:
        if board[a][b] != -1:
            return False
        a -= 1
        b += 1
    a = i
    b = j
    while a >= 0 and b >= 0:
        if board[a][b] != -1:
            return False
        a -= 1
        b -= 1
    return True

def dfs(line):
    # 종료 조건
    if line == n:
        global answer
        answer += 1
        return

    for j in range(n):
        if not check(line, j):
            continue
        board[line][j] = line
        dfs(line + 1)
        board[line][j] = -1

dfs(0)
print(answer)
