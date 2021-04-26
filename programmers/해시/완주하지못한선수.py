# completion에 있는 요소를 participant에서 remove => O(n^2)
# 해시 사용 => O(n) average

def solution(participant, completion):
    part = to_dict(participant)
    comp = to_dict(completion)
    for k, v in part.items():
        if v != comp.get(k):
            return k


def to_dict(arr):
    dic = {}
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    return dic
