x, y = map(int, input().split())
first_z = (y * 100) // x
# first_z = int(y / x * 100) -> 틀림

# 완전 탐색 - 시간 초과
# def solve(x, y, z):
#     if z == 100 or z == 99:
#         return -1

#     count = 0
#     while True:
#         count += 1
#         x += 1
#         y += 1
#         z = int(y / x * 100)
#         if z != first_z:
#             return count

# 이분 탐색
def solve(x, y, z):
    if z == 100 or z == 99:
        return -1

    first = 0
    last = 1000000000
    while first <= last:
        mid = (first + last) // 2
        z = ((y + mid) * 100) // (x + mid)
        z2 = ((y + mid + 1) * 100) // (x + mid + 1)
        if z == first_z and z != z2:
            return mid + 1
        elif z > first_z:
            last = mid - 1
        else:
            first = mid + 1
    return -1

print(solve(x, y, first_z))
