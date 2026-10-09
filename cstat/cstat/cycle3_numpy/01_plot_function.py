import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = x ** 2 + 2 * x + 1
plt.plot(x, y)
plt.title("y = x^2 + 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
