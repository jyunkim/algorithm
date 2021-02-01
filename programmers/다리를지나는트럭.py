def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = []
    time = []
    truck_weights.reverse()

    while truck_weights:
        if sum(onBridge) + truck_weights[-1] <= weight and len(onBridge) < bridge_length:
            onBridge.append(truck_weights.pop())
            time.append(0)
        
        answer += 1
        for i in range(len(time)):
            time[i] += 1

        if time[0] == bridge_length:
            del onBridge[0]
            del time[0]

    answer += bridge_length

    return answer