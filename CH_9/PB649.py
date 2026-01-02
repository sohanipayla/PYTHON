import numpy as np
# 1. Create the NumPy array with Fahrenheit values
f_values = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Values in Fahrenheit degrees:")
print(f_values)
# 2. Convert Fahrenheit to Celsius using the formula
# C = 5*F/9 - 5*32/9
c_values = (5 * f_values / 9) - (5 * 32 / 9)
print("\nValues in Centigrade degrees:")
print(c_values)
# 3. Sort the Celsius array
sorted_c = np.sort(c_values)
print("\nSorted Celsius values:")
print(sorted_c)
# 4. Find the position (index) of 0.0
position = np.where(sorted_c == 0.0)
print("\nPosition of 0.0 index:")
print(position)