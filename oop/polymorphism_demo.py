import math
class Shape:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        return "Result of area for generic shape"
    
class Rectangle(Shape):

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius** 2