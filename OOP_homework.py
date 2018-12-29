# create a class that accepts coordinates and returns the slop and distance of the line
import math


class Line:
    """
    Class: creates a line object
    Input: 2 coordinates
    Description: includes a rise and run (absolute change in height, absolute change in horizontal distance)
    Methods: return the overall distance, and return the overall slope
    """

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.rise = abs(self.coor2[1] - self.coor1[1])
        self.run = abs(self.coor2[0] - self.coor1[0])

    def distance(self):
        return (self.rise ** 2 + self.run ** 2) ** (1 / 2)

    # y = mx + b
    # rise over run
    def slope(self):
        return self.rise / self.run


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


class Cylinder:
    """
    Creates a Cylinder class. 
    Inputs: height and radius
    Methods: returns a volume and returns the overall surface area
    """

    pi = 3.14  # using this because it's what the solutions use

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    # V = pi * r^2 * h
    def volume(self):
        return self.pi * self.radius ** 2 * self.height

    # A = 2 * pi * r * h + 2 * pi * r^2
    def surface_area(self):
        return self.pi * self.radius * self.height * 2 + 2 * self.pi * self.radius ** 2


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
