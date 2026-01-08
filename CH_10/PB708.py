import numpy as np
# 1. Get dimensions
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
# 2. Build the array 
print(f"Enter {c} values for each row (separated by space):")
data = [input(f"Row {i+1}: ").split() for i in range(r)]
arr = np.array(data, dtype=int)
# 3. Get column indices to swap
c1 = int(input("Index of 1st column: "))
c2 = int(input("Index of 2nd column: "))
print("\nOriginal array:\n", arr)
# 4. THE EASY SWAP
arr[:, [c1, c2]] = arr[:, [c2, c1]]
print("\nAfter swapping:\n", arr)