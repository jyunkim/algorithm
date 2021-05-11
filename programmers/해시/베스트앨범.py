def solution(genres, plays):
    answer = []
    plays_per_genres = {}
    each_plays = {}
    
    for i in range(len(genres)):
        plays_per_genres[genres[i]] = plays_per_genres.get(genres[i], 0) + plays[i]
        each_plays[genres[i]] = each_plays.get(genres[i], []) + [(i, plays[i])]
    plays_per_genres = sorted(plays_per_genres.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in plays_per_genres:
        if len(each_plays[genre]) == 1:
            answer.append(each_plays[genre][0][0])
        else:
            each_play = sorted(each_plays[genre], key=lambda x: (-x[1], x[0]))
            answer.append(each_play[0][0])
            answer.append(each_play[1][0])
    return answer