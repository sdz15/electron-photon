from jfun.psi.psiMM import psiMM
from jfun.psi.psiMP import psiMP
from jfun.psi.psiPM import psiPM
from jfun.psi.psiPP import psiPP
from jfun.j10 import j10
from jfun.j01 import j01
from jfun.j00 import j00


def velocity(s,t):
    t_ph = t
    t_el = t
    s_ph = s[0]
    s_el = s[1]
    pMM = psiMM(t_ph, s_ph, t_el, s_el)
    pMP = psiMP(t_ph, s_ph, t_el, s_el)
    pPM = psiPM(t_ph, s_ph, t_el, s_el)
    pPP = psiPP(t_ph, s_ph, t_el, s_el)

    Q = [0, 0]
    j_00 = j00(pMM, pMP, pPM, pPP)
    if j_00 > 1e-14:
        j_10 = j10(pMM, pMP, pPM, pPP)
        j_01 = j01(pMM, pMP, pPM, pPP)
        Q = [j_01, j_10] / j_00

    return Q
