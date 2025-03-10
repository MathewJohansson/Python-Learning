# Numeric Python

import numpy as np

# Note: NumPy arrays can only contain one data type

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print type of np_baseball
print(type(np_baseball))



# Vector Arithmetic

np.array([True, 1, 2]) + np.array([3, 4, False])
# Produces:
np.array([4, 3, 0]) + np.array([0, 2, 2]) 

# Index of sub-array (height_in not defined)
# np_height_in = np.array(height_in)
# print(np_height_in[100:111])
# Prints indexes 100-110



# 2D NumPy Arrays

np_2d = np.array([[1.75, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
np_2d

np_2d.shape

np_2d[0][2] 

# For both rows, second and third cols of both
np_2d[:, 1:3]

# Second row, all cols 
np_2d[1, :]

# Find mean of array np_city, all rows and first col
np.mean(np_city[:, 0])

# Other functions include 
np.median(np_city[:, 0])
np.corrcoef(np_city[:, 0], np_city[:, 0]) # check for correlation
np-std(np_city[:, 0]) # standard deviation

# Random distributions to create heights and weights
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

# Paste two variables together as two cols
np_city = np.column.stack((height, weight))