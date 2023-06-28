from numpy import abs
from wavefunction.psiPlusMinus import psi_plus_minus


def psiPM(t_ph, s_ph, t_el, s_el):
    return abs(psi_plus_minus(t_ph, s_ph, t_el, s_el)) ** 2
