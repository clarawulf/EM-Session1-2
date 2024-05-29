import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

points = [] # Initialize an empty list to store the points
for i in range(5): # Generate 5 random points and add them to the list
    x = random.randint(0,100)
    y = random.randint(0,100)
    points.append(Point(x, y))

for point in points:
    print(point)

print(points)