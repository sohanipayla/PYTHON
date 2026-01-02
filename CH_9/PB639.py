import math
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Apply the distance formula
    return distance
print("Enter coordinates for Point 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("\nEnter coordinates for Point 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
result = calculate_distance(x1, y1, x2, y2)
print(f"\nThe distance between the points is: {result:.2f}")