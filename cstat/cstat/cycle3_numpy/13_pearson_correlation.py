import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
corr = np.corrcoef(x, y)
print("Correlation matrix:")
print(corr)
print("Pearson correlation coefficient:", corr[0, 1])
