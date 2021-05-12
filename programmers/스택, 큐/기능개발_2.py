def solution(progresses, speeds):
    answer = []
    count = 0
    day = 1
    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer
