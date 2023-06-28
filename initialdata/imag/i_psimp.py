import numpy as np
from initialdata.psi.psimp import psimp


def i_psimp(s_ph, s_el):
    return np.imag(psimp(s_ph, s_el))
