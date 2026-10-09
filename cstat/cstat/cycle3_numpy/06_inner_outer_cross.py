import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Inner product:", np.inner(a, b))
print("Outer product:")
print(np.outer(a, b))
print("Cross product:", np.cross(a, b))
