n = int(input())

for j in range(n):
    score = 0
    i = 0
    quiz = input()
    for q in quiz:
        if q == 'O':
            i += 1
            score += i
        else:
            i = 0
    print(score)
