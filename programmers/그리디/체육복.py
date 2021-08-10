def solution(n, lost, reserve):
    # 교집합 빼기
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n
    
    for lost_id in new_lost:
        if lost_id - 1 in new_reserve:
            new_reserve.remove(lost_id - 1)
        elif lost_id + 1 in new_reserve:
            new_reserve.remove(lost_id + 1)
        else:
            answer -= 1
    return answer
