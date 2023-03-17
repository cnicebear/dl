import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y2 = x ** 2
plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')
plt.plot(x, y)
# plt.xlim((-2, 2))
plt.ylim((-2, 2))
plt.xlabel("x")
plt.ylabel("Y")
plt.show()