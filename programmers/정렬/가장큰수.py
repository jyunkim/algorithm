# 자릿수 별 정렬 => 문자열 변환 후 정렬
def solution(numbers):
    # 3, 30, 34 -> 30, 3, 34
    arr = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    # '00' -> '0'
    return str(int(''.join(arr)))