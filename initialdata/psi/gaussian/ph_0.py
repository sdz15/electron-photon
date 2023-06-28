from numpy import sin, cos, exp, pi
from util.config import sigma_ph, k_ph, mu_ph, i


def ph_0(s_ph):
    return (2 * pi * sigma_ph ** 2) ** (-0.25) * exp(
        -1 * (s_ph - mu_ph) ** 2 / (4 * sigma_ph ** 2)) * (
            cos(k_ph * s_ph) + i * sin(k_ph * s_ph))
