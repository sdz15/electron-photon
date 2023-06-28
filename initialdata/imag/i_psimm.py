import numpy as np
from initialdata.psi.psimm import psimm


def i_psimm(s_ph, s_el):
    return np.imag(psimm(s_ph, s_el))
