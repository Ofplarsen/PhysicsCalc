import sys
import mpmath

sys.modules['sympy.mpmath'] = mpmath
from sympy import *

class RectilinearMotion:

    @staticmethod
    def solve_method(**kwargs):
        print(RectilinearMotion.v1(kwargs))
        print(RectilinearMotion.v2(kwargs))
        print(RectilinearMotion.v3(kwargs))
        print(RectilinearMotion.v4(kwargs))

    @staticmethod
    def svt(kwargs):
        eq = "x = v * t"
        return RectilinearMotion.solver(eq, kwargs)


    @staticmethod
    def v1(kwargs):
        eq = "v = v0 + a * t"
        return RectilinearMotion.solver(eq, kwargs)

    @staticmethod
    def v2(kwargs):
        eq = "2 * x = v0 * t + v * t"
        return RectilinearMotion.solver(eq, kwargs)

    @staticmethod
    def v3(kwargs):
        eq = "x = v0 * t + 1/2 * a * t**2"
        return RectilinearMotion.solver(eq, kwargs)

    @staticmethod
    def v4(kwargs):
        eq = "v**2 - v0**2 = 2 * a * x"
        return RectilinearMotion.solver(eq, kwargs)


    @staticmethod
    def solver(equation, kwargs):
        sympy_eq = sympify("Eq(" + equation.replace("=", ",") + ")")
        sympy_eq = sympy_eq.subs(kwargs)
        return solve(sympy_eq, dict=true)
