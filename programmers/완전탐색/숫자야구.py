import itertools

def solution(baseball):
    a = [str(i) for i in range(1,10)]
    b = list(itertools.permutations(a,3))
    answer=[]
    for c in b:
        answer.append(''.join(c))

    for i in baseball:
        for j in answer[:]:
            strike = 0
            ball = 0
            for n in range(3):
                if str(i[0])[n] == j[n]:
                    strike += 1
                elif str(i[0])[n] != j[n] and str(i[0])[n] in j:
                    ball += 1
            if strike != i[1] or ball != i[2]:
                answer.remove(j)
        
    return len(answer)