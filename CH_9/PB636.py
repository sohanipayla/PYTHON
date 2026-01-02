class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Location:
    def __init__(self, x1, y1, x2, y2):
        self.source = Point(x1, y1)
        self.destination = Point(x2, y2)
    def print_reflection(self):
        ref_x = self.destination.x  # X-axis reflection rule: (x, y) -> (x, -y)
        ref_y = -self.destination.y
        print(f"Destination Point: ({self.destination.x}, {self.destination.y})")
        print(f"Reflection on X-axis: ({ref_x}, {ref_y})")
loc = Location(0, 0, 5, 10)
loc.print_reflection()