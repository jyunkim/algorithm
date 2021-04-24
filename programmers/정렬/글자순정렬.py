def sort_by_length(words):
    #words.sort(key = lambda x: len(x), reverse = True)
    #return words

    l = []
    for word in words:
        l.append((len(word), word))
    
    l.sort(reverse = True)
    t=[]
    for x in l:
        t.append(x[1])
    #t = [x[1] for x in l]
    return t

print(sort_by_length(['kim', 'kimseung', 'hwan', 'bumsoo']))