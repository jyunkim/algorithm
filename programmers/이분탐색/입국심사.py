# 모든 시간을 탐색 - 시간 초과
# 이분 탐색
def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    
    while left <= right:
        # 모든 사람이 심사를 받는데 걸리는 시간
        mid = (left + right) // 2
        # 주어진 시간으로 심사할 수 있는 인원 수
        count = 0
        for time in times:
            count += mid // time
        
        # n명보다 적게 심사할 수 있으면 시간을 늘림
        if count < n:
            left = mid + 1
        # n명보다 많이 심사할 수 있으면 시간을 줄임
        # n명을 심사할 수 있으면 시간을 줄여봄
        else:
            answer = mid
            right = mid - 1
            
    return answer
