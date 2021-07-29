# 가지를 뻗는 문제 - DFS
answer = 0

def dfs(numbers, target, result, index):
    global answer
    if index == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(numbers, target, result + numbers[index], index + 1)
    dfs(numbers, target, result - numbers[index], index + 1)

    
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer
