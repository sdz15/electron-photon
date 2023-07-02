from numpy import sin, cos, exp, pi
from util.config import sigma_el, k_el, mu_el, i


def el_0(s_el):
    return (2 * pi * sigma_el ** 2) ** (-0.25) * exp(
        -((s_el - mu_el) ** 2) / (4 * sigma_el ** 2)) * (
            cos(k_el * s_el) + i * sin(k_el * s_el))
