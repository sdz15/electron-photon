import numpy as np
from initialdata.psi.psipm import psipm


def i_psipm(s_ph, s_el):
    return np.imag(psipm(s_ph, s_el))
