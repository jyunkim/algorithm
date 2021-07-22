import heapq as hq

def solution(operations):
    heap = []
    for operation in operations:
        oper = operation.split()
        if oper[0] == 'I':
            hq.heappush(heap, int(oper[1]))
        elif oper[0] == 'D' and heap:
            if oper[1] == '1':
                # 최댓값 삭제
                heap = hq.nsmallest(len(heap) - 1, heap)
            else:
                hq.heappop(heap)
                
    if not heap:
        return [0, 0]
    return [max(heap), heap[0]]
