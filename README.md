# Algorithm
## Python
### 시간복잡도
1억 = 약 1초

![time](https://user-images.githubusercontent.com/68456385/124630206-28d27b00-debd-11eb-89c9-f2e72e1e1a2e.PNG)
O(logn) - 1000(2^10) -> 10

출처: https://www.youtube.com/watch?v=m-9pAwq1o3w&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC

### 공간복잡도
- byte = 8bit -> -2^7 ~ 2^7
- int = 4byte = 32bit -> -2^31 ~ 2^31(약 20억)   
-> 범위 벗어날 경우 long 사용!

### 리스트
![2dimarr](https://user-images.githubusercontent.com/68456385/124630211-2a9c3e80-debd-11eb-8cd5-085aa3ad2198.PNG)
![list](https://user-images.githubusercontent.com/68456385/124630213-2b34d500-debd-11eb-9452-039d136c9323.PNG)
출처: https://www.youtube.com/watch?v=m-9pAwq1o3w&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC

### Dynamic Programming
문제를 부분 문제로 나눈 후 점화식을 세움   
초기값 필요   
이전 항들은 최적의 값으로 계산되었다고 생각   
IndexError 주의   
조건문을 줄이기 위해 i를 1부터 시작하거나 계산에 영향을 주지 않는 값 초기화   

**Top-down**   
재귀   
Memoization을 이용하여 재귀 호출을 줄임(가지치기)

**Bottom-up**   
반복문   
초기값부터 n까지 값을 구해나감
