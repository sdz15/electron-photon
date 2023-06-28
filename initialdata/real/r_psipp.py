import numpy as np
from initialdata.psi.psipp import psipp


def r_psipp(s_ph, s_el):
    return np.real(psipp(s_ph, s_el))
