def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1], reverse=True)
    # 가장 먼저 나가는 차량의 진출 시점에 카메라를 설치한 후
    # 해당 카메라와 만날 수 있는 차량들을 제거한다.
    while routes:
        camera = routes.pop()[1]
        # 제거 시 리스트의 복사본을 이용하여 index 문제 없이 제거
        for route in routes[:]:
            if route[0] <= camera and route[1] >= camera:
                routes.remove(route)
        answer += 1
    return answer
