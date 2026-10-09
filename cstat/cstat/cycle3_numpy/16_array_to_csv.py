import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
filename = "output.csv"
np.savetxt(filename, arr, delimiter=",", fmt="%d")
print("Array saved to", filename)
