import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.einsum('ij,jk->ik', a, b)
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Result:")
print(result)
