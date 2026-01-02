import numpy as np
arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
# Case 1: Sort by 2nd Row 
idx1 = arr[1].argsort()
case1 = arr[:, idx1]
# Case 2: Sort by 2nd Column
idx2 = arr[:, 1].argsort()
case2 = arr[idx2] 
print("Case 1 (Row wise):\n", case1)
print("\nCase 2 (Column wise):\n", case2)