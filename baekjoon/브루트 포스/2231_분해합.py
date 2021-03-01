n = int(input())
answer = 0

for i in range(n):
    d_sum = i + sum(map(int, str(i)))  # 각 자리수 합(string도 iterables)
    if d_sum == n:
        answer = i
        break

if answer:
    print(answer)
else:
    print(0)
