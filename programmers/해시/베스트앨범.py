def solution(genres, plays):
    answer = []
    dic = {}
    play = {}

    for i in range(len(genres)):
        play[genres[i]] = play.get(genres[i], []) + [(plays[i], i)]
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            continue
        dic[genres[i]] = plays[i]
        #dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
    
    lst = list(dic.items())
    lst.sort(key = lambda x: x[1], reverse = True)
    #lst = sorted(dic.items(), key = lambda x: x[1], reverse = True)

    for a,b in lst:
        if len(play[a]) == 1:
            answer.append(play[a][0][1])
        c = sorted(play[a], key = lambda x: (-x[0], x[1]))
        answer.append(c[0][1])
        answer.append(c[1][1])
    
    return answer