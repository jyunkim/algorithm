x = int(input())
i = 0
index = 0

while index < x:
    i += 1
    index += i

if i % 2 == 0:
    a = i - (index - x)
    b = 1 + (index - x)
else:
    a = 1 + (index - x)
    b = i - (index - x)

print(f'{a}/{b}')
