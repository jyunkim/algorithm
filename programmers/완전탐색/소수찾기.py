from itertools import permutations

def isPrime(x):
    if x < 2:
        return False
    
    sqrt = int(x ** 0.5)
    for i in range(2, sqrt + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    arr = []
    for i in range(len(numbers)):
        arr.extend(list(map(lambda x: int(''.join(x)), permutations(numbers, i + 1))))
    
    arr = set(arr)
    for n in arr:
        if isPrime(n):
            answer += 1
    return answer
