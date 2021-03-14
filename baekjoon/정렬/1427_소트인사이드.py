# str -> list (공백 x)
# list('asdf')
# arr[:] = 'asdf'
arr = list(map(int, input()))
arr.sort(reverse=True)

for a in arr:
    print(a, end='')
