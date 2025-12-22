""" ## Numpy library ## """

# NumPy : Numerical Python
# ndarray: N-dimensional array

## differences between python list and numpy arrays

# Parameters and importing:  for python list not required , but for Numpy arrays installation and importing is required

# Types of elements: heterogenous for python list and homogenous for numpy arrays

# Dimension of elements: no restrictions for python list, but for numpy arrays dimensions has to be same.

# Memory allocation : Non-contiguous for python list , contiguous for numpy arrays.

# Size : Python list requires more space, while numpy arrays requires less memory.

# performance : Python list is slower than numpy arrays in the case of performance.

# Element wise operation: For python list element wise operation is not possible but for numpy arrays it is possible.

# Functionality: Python lists cannot handle arithmetic operations, but numpy arrays can handle as well as it has a lot of inbuilt functions.



import numpy as np

a = np.array(42)
b = np.array([[[1,2,3],[4,5,6]], [[1,2,3], [4,5,6]]])

print(a, a.ndim, '\n')
print(b, b.ndim, '\n')


""" ## Pandas Library ## """

#Normal file handling getting max score value from a csv file

f = open("scores.csv", "r")
scores = f.readlines()[1:]
max = 0
for r in scores:
    fields = r.split(",")
    if(int(fields[8]) > max):
        max = int(fields[8])
print(max)

import pandas as pd

scores = pd.read_csv("scores.csv")
print(scores["Total"].max())
print(scores.shape) # number of columns and rows
print(scores.count()) # number of rows in each column
print(scores["Total"].mean()) # mean value of the column
print(scores["Total"].sum()) # total value of the column
print(scores["Total"].sort_values(ascending=False)) # sort values of the column, ascending=True default value














































