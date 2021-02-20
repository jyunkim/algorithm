x_points = []
y_points = []

for i in range(3):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

for i in range(3):
    if x_points.count(x_points[i]) == 1:
        x = x_points[i]
    if y_points.count(y_points[i]) == 1:
        y = y_points[i]
        
print(x, y)
