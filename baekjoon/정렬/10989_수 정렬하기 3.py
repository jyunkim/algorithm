# pypy: python보다 빠르지만 메모리를 많이 사용
# 주어진 메모리가 매우 적은 문제 -> input 저장 불가
# 입력 숫자는 많지만 범위는 작을 때 -> 카운팅 정렬 이용
import sys

n = int(sys.stdin.readline())
counts = [0] * 10000  # 딕셔너리 key 대신 index로 접근

for _ in range(n):
    i = int(sys.stdin.readline())
    counts[i - 1] += 1

for i in range(len(counts)):
    for _ in range(counts[i]):
        print(i + 1)
