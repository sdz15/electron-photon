import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from math import sqrt
from random import random
from util.config import sigma_el, sigma_ph, t, step

from trajectory.velocity import velocity


for i in range(100):
    rand = random()
    q0 = [sqrt(sigma_ph) * rand, 1-sqrt(sigma_el) * rand]
    time = np.linspace(0, t, step)

    traj = np.transpose(odeint(velocity, q0, time))

    plt.plot(traj[0], time, traj[1], time)

plt.show()
