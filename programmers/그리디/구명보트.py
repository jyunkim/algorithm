# 투 포인터
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    done = [False] * len(people) # 탈출한 사람 체크
    
    while left < right:
        # 인덱스를 조작할 땐 인덱스 벗어나는 것 생각
        while right >= 0 and people[left] + people[right] > limit:
            right -= 1
        if left < right:
            answer += 1
            done[left] = True
            done[right] = True
            left += 1
            right -= 1
    
    # 남은 사람 계산
    for check in done:
        if not check:
            answer += 1
    return answer
