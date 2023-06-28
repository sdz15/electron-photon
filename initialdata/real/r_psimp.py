import numpy as np
from initialdata.psi.psimp import psimp


def r_psimp(s_ph, s_el):
    return np.real(psimp(s_ph, s_el))
