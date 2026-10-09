import numpy as np

n = int(input("Enter number of terms: "))
phi = (1 + np.sqrt(5)) / 2
psi = (1 - np.sqrt(5)) / 2
series = [int(round((phi ** i - psi ** i) / np.sqrt(5))) for i in range(n)]
print("Fibonacci series:")
print(series)
