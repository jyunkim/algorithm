import sys

temp = sys.maxsize

def dfs(current, target, words, visited, depth):
    global temp
    
    # target에 도달했으면 현재 깊이를 현재까지의 답과 비교하여 더 작으면 갱신
    if current == target:
        temp = min(temp, depth)
        return
    
    # 탐색
    for i in range(len(words)):
        # 이미 탐색한 단어는 스킵
        if visited[i]:
            continue
        # 다른 알파벳 수
        count = 0
        for j in range(len(current)):
            if count > 1:
                break
            if current[j] != words[i][j]:
                count += 1
        # 한 개의 알파벳만 다를 경우 탐색
        if count == 1:
            # 방문 처리
            visited[i] = True
            # 깊이를 1 증가시키며 다음 단어 탐색
            dfs(words[i], target, words, visited, depth + 1)
            visited[i] = False


def solution(begin, target, words):
    visited = [False] * len(words)
    # target이 words에 있으면 탐색
    if target in words:
        dfs(begin, target, words, visited, 0)
        answer = temp
    # target이 words에 없는 경우
    else:
        answer = 0
    return answer
