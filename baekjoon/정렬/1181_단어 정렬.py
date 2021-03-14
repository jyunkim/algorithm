n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))
words.sort(key=lambda word: (len(word), word))

for word in words:
    print(word)
