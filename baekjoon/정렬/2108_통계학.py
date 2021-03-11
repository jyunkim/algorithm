# input보다 sys가 훨 빠름
import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(n)]

s = round(sum(nums) / len(nums))

nums.sort()
j = nums[len(nums) // 2]

# dictinary 생성 -> zip 이용
d = {}
for num in nums:
    if num not in d:
        d[num] = 0
    else:
        d[num] += 1
cs = [k for k, v in d.items() if v == max(d.values())]
if len(cs) == 1:
    c = cs[0]
else:
    c = cs[1]
# max(d, key=d.get) -> value값이 가장 큰 key값
# collections의 Counter 사용가능

r = max(nums) - min(nums)

print(s)
print(j)
print(c)
print(r)
