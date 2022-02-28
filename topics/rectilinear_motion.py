import sys
import mpmath
import omath
from Formulas.Formulas import _Rectiliniear_motion as rect

sys.modules['sympy.mpmath'] = mpmath
from sympy import *

class RectilinearMotion:

    @staticmethod
    def solve_method(**kwargs):
        equations = [omath.get_sub_equation(rect.v1.value, kwargs), omath.get_sub_equation(rect.v2.value, kwargs)
            , omath.get_sub_equation(rect.v3.value, kwargs), omath.get_sub_equation(rect.v4.value, kwargs)]

        ans = solve(equations)
        print(ans)

    @staticmethod
    def svt(kwargs):
        return RectilinearMotion.solver(rect.value.svt, kwargs)


    @staticmethod
    def v1(kwargs):
        return RectilinearMotion.solver(rect.value.v1, kwargs)

    @staticmethod
    def v2(kwargs):
        return RectilinearMotion.solver(rect.value.v2, kwargs)

    @staticmethod
    def v3(kwargs):
        return RectilinearMotion.solver(rect.value.v3, kwargs)

    @staticmethod
    def v4(kwargs):
        return RectilinearMotion.solver(rect.value.v4, kwargs)

