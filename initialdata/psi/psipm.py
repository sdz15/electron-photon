from util.config import theta_ph, theta_el
from initialdata.psi.gaussian.el_0 import el_0
from initialdata.psi.gaussian.ph_0 import ph_0
from numpy import sin, cos


def psipm(s_ph, s_el):
    return sin(theta_ph/2)*ph_0(s_ph)*cos(theta_el/2)*el_0(s_el)
