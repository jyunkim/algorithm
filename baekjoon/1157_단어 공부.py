s = input().upper()
unique_words = list(set(s))
count_list = [s.count(word) for word in unique_words]

if count_list.count(max(count_list)) > 1:  # 최댓값이 여러개 일 때
    print('?')
else:
    print(unique_words[count_list.index(max(count_list))])
