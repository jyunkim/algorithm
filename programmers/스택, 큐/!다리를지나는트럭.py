from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    count = 0
    bridge = [0] * bridge_length
    while queue:
        count += 1
        bridge.pop(0)
        bridge.append(0)
        if sum(bridge) + queue[0] <= weight:
            bridge[-1] = queue.popleft()
    return count + bridge_length
