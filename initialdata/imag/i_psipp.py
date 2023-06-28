import numpy as np
from initialdata.psi.psipp import psipp


def i_psipp(s_ph, s_el):
    return np.imag(psipp(s_ph, s_el))
