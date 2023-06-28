from numpy import abs
from wavefunction.psiPlusPlus import psi_plus_plus


def psiPP(t_ph, s_ph, t_el, s_el):
    return abs(psi_plus_plus(t_ph, s_ph, t_el, s_el)) ** 2
