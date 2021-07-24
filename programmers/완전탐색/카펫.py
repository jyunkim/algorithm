# 내가 풀려고 하지 마라!
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for y in range(3, total):
        if total % y == 0:
            x = total / y
            if (x + y - 2) * 2 == brown:
                answer.extend([x, y])
                break
    return answer
