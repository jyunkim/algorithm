from math import ceil

def solution(progresses, speeds):
    answer = []
    # + for문 -> *
    while progresses:
        count = 0
        day = ceil((100 - progresses[0]) / speeds[0])
        while progresses and progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        answer.append(count)
    return answer
