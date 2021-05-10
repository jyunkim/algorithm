def solution(phone_book):
    n = len(phone_book)
    # string 배열 정렬
    # 문자열 첫번째 요소부터 하나씩 비교
    phone_book.sort()
    for i in range(n-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
