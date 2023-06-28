import numpy as np
from initialdata.psi.psimm import psimm


def r_psimm(s_ph, s_el):
    return np.real(psimm(s_ph, s_el))
