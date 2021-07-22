import heapq as hq

def solution(jobs):
    answer = 0
    length = len(jobs)
    time = 0
    while jobs:
        heap = []
        # 현재 실행할 수 있는 작업들 힙에 푸쉬(소요 시간이 작은 것 우선)
        for job in jobs:
            if job[0] <= time:
                hq.heappush(heap, [job[1], job[0]])
        # 실행할 수 있는 작업이 있으면
        if heap:
            job = hq.heappop(heap)
            time += job[0]
            answer += (time - job[1])
            jobs.remove([job[1], job[0]])
        # 실행할 수 있는 작업이 없으면
        else:
            time += 1
    return answer // length
