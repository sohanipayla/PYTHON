from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        return self.length * self.breadth
    # Operator Overloading for '>'
    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
r1 = Rectangle(10, 5)
r2 = Rectangle(5, 5) 
c = Circle(7)
print(f"Rectangle 1 Area: {r1.calculate_area()}")
print(f"Rectangle 2 Area: {r2.calculate_area()}")
# Checking '>' overload
if r1 > r2:
    print("Rectangle 1 is larger than Rectangle 2")
# MRO of Circle
print(f"MRO of Circle: {Circle.mro()}")