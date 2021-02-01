a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = max(a,b,c)
if(a+b > d):
    result = True
else:
    result = False
print("Is it triangle? ", result)