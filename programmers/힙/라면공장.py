from heapq import *

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    j = 0
    while k > stock:
        for i in range(j, len(dates)):
            if stock >= dates[i]:
                heappush(heap, -supplies[i])
            else:
                j = i
                break
        stock += -heappop(heap)
        answer += 1
    return answer