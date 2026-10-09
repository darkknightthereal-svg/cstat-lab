import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = np.sin(x)
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
