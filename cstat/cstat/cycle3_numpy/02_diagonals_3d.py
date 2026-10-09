import numpy as np

arr = np.arange(24).reshape(2, 3, 4)
print("Original array:")
print(arr)
print("Diagonals of each 2D layer:")
print(np.diagonal(arr, axis1=1, axis2=2))
