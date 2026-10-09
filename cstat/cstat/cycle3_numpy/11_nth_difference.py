import numpy as np

arr = np.array([1, 4, 9, 16, 25, 36])
n = int(input("Enter order of difference: "))
print("Original array:", arr)
print("Difference:", np.diff(arr, n=n))
