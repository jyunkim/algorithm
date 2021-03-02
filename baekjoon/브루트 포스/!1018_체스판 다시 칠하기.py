m, n = map(int, input().split())
board = []
counts = []

for i in range(m):
    board.append(input())

for a in range(m - 7):
    for b in range(n - 7):
        cnt1 = 0
        cnt2 = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if board[i][j] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        counts.append(min(cnt1, cnt2))

print(min(counts))
