m = int(input())
n = int(input())
check = True
sum = 0

for i in range(m, n + 1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        sum += i
        if check:
            least = i
            check = False

if sum == 0:
    print(-1)
else:
    print(sum)
    print(least)
