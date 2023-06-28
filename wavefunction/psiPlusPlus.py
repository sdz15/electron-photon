from scipy.integrate import quad
from util.config import omega, i, step

from initialdata.psi.psipp import psipp
from initialdata.imag.i_psipm import i_psipm
from initialdata.imag.i_psipp import i_psipp
from initialdata.real.r_psipm import r_psipm
from initialdata.real.r_psipp import r_psipp
from wavefunction.bessel.besselfunction import besselfun
from wavefunction.bessel.besselterm import besselterm

# s_el >= s_ph


def psi_plus_plus(t_ph, s_ph, t_el, s_el):
    x = psipp(s_ph + t_ph, s_el + t_el)

    r_j1 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 1) * (t_el - s_el + sigma) * r_psipp(s_ph + t_ph, sigma)
    i_j1 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 1) * (t_el + s_el - sigma) * i_psipp(s_ph + t_ph, sigma)
    y = -(omega / 2) * (quad(r_j1, s_el - t_el, s_el + t_el)[0] + quad(i_j1, s_el - t_el, s_el + t_el)[0])

    r_j0 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 0) * r_psipm(s_ph + t_ph, sigma)
    i_j0 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 0) * i_psipm(s_ph + t_ph, sigma)
    z = -(i * omega / 2) * (quad(r_j0, s_el - t_el, s_el + t_el)[0] + quad(i_j0, s_el - t_el, s_el + t_el)[0])

    return x + y + z
