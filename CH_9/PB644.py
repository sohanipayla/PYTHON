import numpy as np
data = np.arange(100, 200, 10)
res = data.reshape(5, 2) #Reshape into 5 rows and 2 columns
print(res)