def solution(arrangement):
    answer = 0
    stack = []
    
    for a in arrangement:
        if a == "(":
            stack.append(a)
            top = 1
        else:
            stack.pop()
            if top == 1:
                answer += len(stack)
            else:
                answer += 1
            top = 0
    
    return answer