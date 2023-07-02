import numpy as np
from util.config import sigma_el, sigma_ph, mu_el, mu_ph, num_traj

# Distribution of initial data based on Gaussian

def init_dist():
    return [np.random.normal(mu_ph, sigma_ph, size=(1,num_traj)), np.random.normal(mu_el, sigma_el, size=(1,num_traj))]

# Should try to make this 2D instead of 3D