import numpy as np
from initialdata.psi.psipm import psipm


def r_psipm(s_ph, s_el):
    return np.real(psipm(s_ph, s_el))
