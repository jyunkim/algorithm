n = int(input())
count = 0

for i in range(n):
    word_list = []
    word = input()
    group = True
    for s in word:
        if s not in word_list:
            word_list.append(s)
        else:
            if word_list[-1] != s:
                group = False
                break
    if group:
        count += 1

print(count)
