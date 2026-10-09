import numpy as np

a = np.array([[4, 2], [1, 3]])
values, vectors = np.linalg.eig(a)
print("Eigenvalues:")
print(values)
print("Eigenvectors:")
print(vectors)
