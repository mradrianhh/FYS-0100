import numpy as np
from math import pi
import matplotlib.pyplot as plt

m = 1.5
g = 9.81

def func(x, mu_s):
    return (m*g) / (np.sin(x) + mu_s * np.cos(x))

thetas = np.linspace(0, pi/2, 100)

plt.plot(thetas, func(thetas, 0.6), label = "0.6")
plt.plot(thetas, func(thetas, 0.3), label = "0.3")
plt.xlabel("Theta")
plt.ylabel("Force")
plt.legend()
plt.show()