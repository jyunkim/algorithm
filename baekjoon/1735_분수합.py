import math

a, b = map(int, input().split())
c, d = map(int, input().split())

x = (a * d) + (c * b)
y = b * d
g = math.gcd(x, y)
print(x // g, y // g)
