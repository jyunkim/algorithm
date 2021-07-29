def dfs(tickets, arr, visited, index):
    for i in range(len(tickets)):
        # 방문하지 않았고, 갈 수 있는 공항이면 방문
        if not visited[i] and tickets[index][1] == tickets[i][0]:
            visited[i] = True
            arr.append(tickets[i][0])
            
            # 모두 방문했으면 종료
            if len(arr) == len(tickets):
                arr.append(tickets[i][1])
                return
            
            # 다음 공항에서 다시 탐색
            dfs(tickets, arr, visited, i)
            visited[i] = False
    
    # 다 방문하지 못했고, 더 이상 갈 수 있는 공항이 없는 경우 경로 원상복구
    if len(arr) != len(tickets) + 1:
        arr.pop()


def solution(tickets):
    # 가능한 경로가 여러 개일 경우 사전식 순서가 앞인 경로 선택
    tickets.sort()
    
    for i in range(len(tickets)):
        # ICN에서 출발
        if tickets[i][0] == "ICN":
            answer = []
            visited = [False] * len(tickets)
            
            answer.append(tickets[i][0])
            visited[i] = True
            dfs(tickets, answer, visited, i)
            
            # 모두 방문 가능하면 종료
            if len(answer) == len(tickets) + 1:
                break
                
    return answer
