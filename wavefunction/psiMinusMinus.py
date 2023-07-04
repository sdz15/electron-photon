from scipy.integrate import quad
from util.config import omega, step

from initialdata.psi.psimm import psimm
from initialdata.imag.i_psimm import i_psimm
from initialdata.imag.i_psimp import i_psimp
from initialdata.real.r_psimm import r_psimm
from initialdata.real.r_psimp import r_psimp
from wavefunction.bessel.besselfunction import besselfun
from wavefunction.bessel.besselterm import besselterm

# s_el >= s_ph


def psi_minus_minus(t_ph, s_ph, t_el, s_el):
    x = psimm(s_ph - t_ph, s_el - t_el)

    r_j1 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 1) * (t_el + s_el - sigma) * r_psimm(s_ph - t_ph, sigma)
    i_j1 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 1) * (t_el + s_el - sigma) * i_psimm(s_ph - t_ph, sigma)
    y = -(omega / 2) * (quad(r_j1, s_el - t_el, s_el + t_el)[0] + quad(i_j1, s_el - t_el, s_el + t_el)[0])

    r_j0 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 0) * r_psimp(s_ph - t_ph, sigma)
    i_j0 = lambda sigma: besselfun(besselterm(t_el, s_el, sigma), 0) * i_psimp(s_ph - t_ph, sigma)
    z = -(1j * omega / 2) * (quad(r_j0, s_el - t_el, s_el + t_el)[0] + quad(i_j0, s_el - t_el, s_el + t_el)[0])

    return x + y + z
