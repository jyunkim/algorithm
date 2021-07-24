# 거리 완전탐색 - 시간 초과
# 이분탐색
def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        # 바위를 n개 제거했을 때 거리의 최소값이 mid인 경우가 있는지 확인
        mid = (left + right) // 2
        cur = 0
        min_dist = distance
        remove = 0
        for rock in rocks:
            dist = rock - cur
            # 거리가 mid보다 작으면 mid가 최소값이 될 수 없으므로 바위 제거
            if dist < mid:
                remove += 1
            else:
                min_dist = min(min_dist, dist)
                cur = rock
        
        # 바위를 n보다 많이 제거했으면 mid가 너무 큰 것
        if remove > n:
            right = mid - 1
        # 바위를 n보다 적게 제거했으면 mid가 너무 작은 것
        # 바위를 n개 제거했으면 mid를 늘려봄
        else:
            answer = mid
            left = mid + 1
            
    return answer
