def solution(numbers):
    answer = ''
    
    if sum(numbers) == 0:
        return "0"

    #for i in range(len(numbers)):
    #    numbers[i] = str(numbers[i])
    numbers = sorted(map(lambda x: str(x), numbers), key = lambda x: x*4)
                    #([str(x) for x in numbers])
    while numbers:
        answer += numbers.pop()
    #answer = ''.join(numbers)
    
    return answer
    #return str(int(answer))