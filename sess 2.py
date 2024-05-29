import random


class Point:
    # all classes need to have an init method
    def _init_(self, x, y):
        """
        Init method that initializes the point with X and Y
        :param x: coordinate value
        :param y: coordinate value
        """
        self.x = x
        self.y = y

    def _str_(self):
        # when you print you see the id of the object, so this function changes that so it prints the points
        """
        How to print this point?
        :return:
        """
        return f"<{self.x},{self.y}>"

    def _repr_(self):
        # when you print you see the id of the object, so this function changes that so it prints the points
        """
        How to print this point?
        :return:
        """
        return self._str_()

    def distance_orig(self):
        """
        Return the distance from origin of the point instance
        :return:
        """
        return(self.x*2 + self.y2)*0.5

    def _gt_(self, other):
        """
        How to compare 2 points? we define it here
        :param other: the other point we are comparing against
        :return:
        """
        my_size = self.distance_orig()
        their_size = other.distance_orig()
        return my_size > their_size


a = Point(2,3)  # instantiate by calling the name of the class and parameters in brackets
print(a.x)
print(a.y)

b = Point(7,9)
print(b.x, b.y)

import random
points = []
for _ in range(5):
    points.append(Point(random.randint(0, 100), random.randint(0,100)))

for point in points:
    print(point) # here it iterates and calls point _str__

print(points) # here it iterates and calls point _repr__

a = Point(3,4) # we expect 5 as the distance to origin
b = Point(12, 5) # we expect 13 as the distance to origin

print(a.distance_orig(), b.distance_orig())
print(a > b)