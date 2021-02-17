n = int(input())
numbers = list(map(int, input().split()))
count = 0

for number in numbers:
    if number == 1:
        continue
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        count += 1

print(count)
