import numpy as np
# 1. Array create karna
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print("Original Array:")
print(sampleArray)
# 2. Max from Axis 0 (Column-wise max)
max_axis0 = np.amax(sampleArray, axis=0)
print("\nMax from axis 0 (Columns):")
print(max_axis0)
# 3. Min from Axis 1 (Row-wise min)
min_axis1 = np.amin(sampleArray, axis=1)
print("\nMin from axis 1 (Rows):")
print(min_axis1)