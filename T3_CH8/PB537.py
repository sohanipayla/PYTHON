import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 1. Distance from origin
    def distance_from_origin(self):
        return round(math.sqrt(self.x**2 + self.y**2), 2)
    # 2. Translate the point
    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
    # 3. Reflect about x-axis
    def reflect_x(self):
        return Point(self.x, -self.y)
    # 4. Distance between two points
    def distance(self, other):
        return round(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2), 2)
    def __str__(self):
        return f"({self.x},{self.y})"
p1 = Point(1, 2)
print("Point:", p1)
print("Distance from origin:", p1.distance_from_origin())
p2 = p1.translate(1, 1)
print("After translation by (1,1):", p2)
p3 = p2.reflect_x()
print("After reflection on x-axis:", p3)
p4 = Point(3, 4)
print("Distance between", p3, "and", p4, "=", p3.distance(p4))