import numpy as np
from math import pi
import matplotlib.pyplot as plt

m = 1.5
g = 9.81

# The expression for the 
def calculate_force(angles, mu_s):
    return (m*g) / (np.sin(angles) + mu_s * np.cos(angles))

angles = np.linspace(0, pi/2, 100)

# List of each corresponding force at each angle with the static coefficient of friction being 0.6
forces = calculate_force(angles, 0.6)
# Finds the min_point (min_theta, min_force).
min_force = min(forces)
min_theta = angles[np.argmin(forces)]
print(f"The minimum point for static coefficient 0.6: ({min_theta}, {min_force}).")

plt.plot(angles, forces, label = "0.6")

# Do the same with the static coefficient of friction being 0.3
forces = calculate_force(angles, 0.3)
min_force = min(forces)
min_theta = angles[np.argmin(forces)]
print(f"The minimum point for static coefficient 0.3: ({min_theta}, {min_force}).")

plt.plot(angles, forces, label = "0.3")
plt.xlabel("Angle")
plt.ylabel("Force")
plt.title("Pushing force required at a given angle")
plt.legend()
plt.show()