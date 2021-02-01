from bisect import *

def solution(budgets, M):
    budgets.sort()
    x = max(budgets)

    if sum(budgets) <= M:
        answer = x
    else:
        while sum(budgets) > M:
            x -= 1
            for i in range(bisect(budgets, x), len(budgets)):
                budgets[i] = x
        answer = x
    return answer