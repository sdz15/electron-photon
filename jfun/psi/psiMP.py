from numpy import abs
from wavefunction.psiMinusPlus import psi_minus_plus


def psiMP(t_ph, s_ph, t_el, s_el):
    return abs(psi_minus_plus(t_ph, s_ph, t_el, s_el)) ** 2
