# import math

a, b, v = map(int, input().split())
# print(math.ceil((v - a) / (a - b)) + 1)
h = (v - a) / (a - b) + 1
print(int(h) if int(h) == h else int(h) + 1)

# i = 0
# height = 0
# 시간 초과
# while True:
#     i += 1
#     height += a
#     if height >= v:
#         break
#     height -= b
# print(i)
