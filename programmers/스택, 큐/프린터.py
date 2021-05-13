from collections import deque

def solution(priorities, location):
    # 리스트에 index 같이 저장
    # i_list = [(p, i) for i, p in enumerate(priorities)]
    count = 0
    queue = deque(priorities)
    while location >= 0:
        m = max(queue)
        tmp = queue.popleft()
        if tmp == m:
            count += 1
            location -= 1
        elif tmp != m and location == 0:
            queue.append(tmp)
            location = len(queue) - 1
        else:
            queue.append(tmp)
            location -= 1
    return count
