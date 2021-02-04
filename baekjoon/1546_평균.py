n = int(input())
score = list(map(int, input().split()))
new_score = list(map(lambda x: x / max(score) * 100, score))
print(sum(new_score) / n)
