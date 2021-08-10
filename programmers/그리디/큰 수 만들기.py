def solution(number, k):
    arr = []
    count = 0 # 제거한 수 개수
    for n in number:
        # 다음에 오는 수가 더 크면 제거
        while arr and arr[-1] < n and count < k:
            arr.pop()
            count += 1
        arr.append(n)
    
    # k를 다 못 채웠으면 뒷 부분부터 제거
    while len(number) - k != len(arr):
        arr.pop()
    return ''.join(arr)
