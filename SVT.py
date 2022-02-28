import sys
import mpmath
import sympy

sys.modules['sympy.mpmath'] = mpmath
from sympy import *


def test(formula, **kwargs):
    expr = sympy.sympify(formula)
    return expr.evalf(subs=kwargs)

def solve(formula):
    return 0

def svt(formula):
    expr = sympy.sympify(formula)
    return expr.evalf(subs=kwargs)