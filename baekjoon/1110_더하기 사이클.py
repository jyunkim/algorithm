first = int(input())
n = first
count = 0

while True:
    temp1 = (n // 10) + (n % 10)
    temp2 = (n % 10) * 10 + (temp1 % 10)
    count += 1
    if first == temp2:
        break
    n = temp2

print(count)