def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined (Vertical Line)"
    slope = (y2 - y1) / (x2 - x1) # Apply the slope formula
    return slope
print("Enter coordinates for Point 1 (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("\nEnter coordinates for Point 2 (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
result = calculate_slope(x1, y1, x2, y2)
print(f"\nThe slope of the line is: {result}")