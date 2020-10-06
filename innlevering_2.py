import numpy as np
from math import pi
import matplotlib.pyplot as plt

m = 1.5
g = 9.81

def func(x, mu_s):
    return (m*g) / (np.sin(x) + mu_s * np.cos(x))

thetas = np.linspace(0, pi/2, 100)
frictions = np.linspace(0, 1, 100)
forces = func(thetas, 0.6)

forces = func(thetas, frictions)

plt.plot(thetas, frictions, forces)
plt.xlabel("Theta")
plt.ylabel("Force")
plt.show()