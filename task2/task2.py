print("input filename for the circle file")
with open(input(), "r") as file1:
  x_center, y_center = map(int, file1.readline().split())
  radius = int(file1.readline())

print("input filename for the points file")
points = []
with open(input(), "r") as file2:
  for line in file2:
    x, y = map(int, line.split())
    points.append((x, y)) 

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

for point in points:
    if distance(point, (x_center, y_center)) < radius:
        print(1)
    elif distance(point,(x_center, y_center)) == radius:
        print(0)
    else:
        print(2)