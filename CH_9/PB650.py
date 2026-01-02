import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_2d = arr.reshape(3, 4)
print("2D Array:")
print(arr_2d)
arr_3d = arr.reshape(2, 3, 2)
print("\n3D Array:")
print(arr_3d)