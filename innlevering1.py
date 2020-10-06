"""
Innlevering 1 | Oppgave 5

Kjør programmet ved kommandoen:
    python oppg_5.py


Kastet er vertikalt, dvs at ballen kun vil bevege seg langs vertikalaksen(y-aksen).
Setter positiv retning oppover.

Ser bort fra luftmotstand, da er den eneste kraften som virker på ballen i luften vekten, W = mg.
Summen av kreftene er ikke lik 0, så -W = ma <=> -mg = ma <=> a = -g, hvor g = 9.81 m/s^2.

Ut fra bevegelseslikningene, så får vi at
y = y0 + v0*t + 1/2*a*t^2, hvor vi setter nullpunktet i utgangshøyden, altså er y0 = 0, og substituerer -g inn for a. Dette gir
y = v0*t - 1/2*g*t^2

For å finne tiden ballen bruker fra den blir kastet til den lander igjen, så kan vi finne løsningene
for y = 0.

Vi ser at
v0*t = 1/2*g*t^2
som gir løsningene 
    - t = 0
    - t = 2v0/g
Vi er ute etter den siste løsningen, når ballen treffer bakken etter å ha vært i luften.

Vi vet at apex-punktet(det høyeste punktet) på kurven til et kast når vi ser bort fra luftmotstand
er høyden ved t_slutt/2.
"""
import numpy as np
import matplotlib.pylab as plt

g = 9.81

def calculate_time_of_impact(v0, a=-g, y0 = 0):
    """
    For a vertical toss, given the initial velocity v0 and the acceleration, a, 
    calculate at which time the ball hits the ground after being airborne.
    Note that positive direction is upwards.

    v0 - initial velocity given in meter(s) per second.
    y0 - initial height given in meter(s).
    a - acceleration given in meter(s) per second per second.

    Returns the latest time at which the position is 0 meters in second(s), aka
    the time of impact after being airborne.
    """
    t_1 = (-v0 + (v0**2-2*a*y0)**0.5)/a
    t_2 = (-v0 - (v0**2-2*a*y0)**0.5)/a
    return t_1 if t_1 == t_2 else max(t_1, t_2)


def calculate_height(v0, t, a=-g, y0 = 0):
    """
    For a vertical toss, given the initial velocity v0, initial height y0
    and the acceleration, a, of the object, calculate the height at time t.
    Note that positive direction is upwards.

    v0 - initial velocity given in meter(s) per second.
    y0 - initial height given in meter(s). 
    a - acceleration given in meter(s) per second per second.
    t - time given in second(s). 

    Returns the height at time t in meter(s).
    """
    return y0 + v0*t + 1/2*a*t**2

def calculate_max_height(v0_y, a_y=-g, y0 = 0):
    """
    Calculates the max-height of a given the initial vertical velocity v0_y, the vertical acceleration, a_y
    and the initial height, y0 by recognizing that when disregarding air-resistance, the time of the apex of the jump
    is half the time of the impact, or halfway between the time of toss and the time of impact.

    v0_y - initial vertical velocity given in meter(s) per second.
    a_y - initial vertical acceleration given in meter(s) per second per second.
    y0 - initial height given in meter(s).
    """
    t_apex = calculate_time_of_impact(v0_y, a_y, y0)/2
    return calculate_height(v0_y, t_apex, a_y, y0)

def solve_a():
    print("a)\n")

    print(calculate_max_height(5))

def solve_b():
    print("\nb)\n")

    print(calculate_max_height(10))

def solve_c():
    print("\nc)\n")

    v0_start = 0
    v0_slutt = 20
    v0_steg = 0.1

    v0_arr = np.arange(v0_start, v0_slutt, v0_steg)

    # Utfordringen her er at du kan ikke bare gi v0_arr som et argument til
    # 'calculate_max_height' fordi den ikke er av datatypen 'int'.
    # Derfor må du bruke list-comprehension til å danne et nytt 'numpy.ndarray' fra
    # max-høyden til hver enkelt verdi i v0-arr, ellers får du en 'ValueError'.
    y_max = np.array([calculate_max_height(v0) for v0 in v0_arr])


    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.scatter(v0_arr, y_max)
    plt.xlabel("Initial velocity (m/s)", fontsize=16)
    plt.ylabel("Max height (m)", fontsize=16)
    plt.show()

if __name__ == "__main__":
    solve_a()
    solve_b()
    solve_c()
