import numpy as np

a = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
q, r = np.linalg.qr(a)
print("Original matrix:")
print(a)
print("Q matrix:")
print(q)
print("R matrix:")
print(r)
