class Point:
    # all classes need to have an init method
    def __init__(self, x, y):
        """
        Init method that initializes the point with x and y
        :param x: x coordinate value
        :param y: Y coordinate value
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        How to print this point?
        :return:
        """
        return f"<x={self.x}, y={self.y}>"

    def __repr__(self):
        """
        How to print if in a list
        :return:
        """
        return self.__str__()

    def distance_orig(self):
        """
        Return the distance from origin of the point instance
        :return:
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        How to compare 2 points? We define it here!
        :param other:
        :return:
        """
        my_size = self.distance_orig()
        their_size = other.distance()
        return my_size > their_size

a = Point(2,3)   # instantly by calling the name of the class and parameters in brackets

print(a.x)
print(a.y)

b = Point(7, 9)
print(b.x, b.y)

# name of the class with uppercase but all the instances with lower case
# dif between the instance and the class: a class with specific values to enter to initialize it vs the ability to
# the class is the template that allows be to create any point
# an instance is the coordinate of a point

# add 5 random points into a list
import random

points = [] # Initialize an empty list to store the points
for i in range(5): # Generate 5 random points and add them to the list
    x = random.randint(0,100)
    y = random.randint(0,100)
    points.append(Point(x, y))

for point in points:
    print(point)

print(points)   #
# similar way
# for _ in range(5):
#    points.append(Points(random.randint(0,100), random.randint(0,100)))
