n = int(input())
k = 0

while n >= 0:
    if n % 5 == 0:
        k += n // 5
        print(k)
        break
    n -= 3
    k += 1
# while 조건문이 false가 될 때 실행
# break로 loop이 종료될 때는 실행되지 않음
else:
    print(-1)

# for-else
# for문이 끝까지 돌았을 때 else 실행
# break로 loop이 종료될 때는 실행되지 않음