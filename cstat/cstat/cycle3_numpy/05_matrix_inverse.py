import numpy as np

m = np.array([[4, 7], [2, 6]])
print("Original matrix:")
print(m)
if np.linalg.det(m) != 0:
    print("Inverse matrix:")
    print(np.linalg.inv(m))
else:
    print("Matrix is not invertible")
