a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in a:
    s = s.replace(i, ' ')
    
print(len(s))
