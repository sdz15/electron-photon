from numpy import abs
from wavefunction.psiMinusMinus import psi_minus_minus


def psiMM(t_ph, s_ph, t_el, s_el):
    return abs(psi_minus_minus(t_ph, s_ph, t_el, s_el)) ** 2
