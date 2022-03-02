import sympy

from omath import Solver as omath
from Formulas.Formulas import _Electrisity as rot

def solve_method(**kwargs):
    equations = [omath.get_sub_equation(rot.e.value,kwargs), omath.get_sub_equation(rot.v.value,kwargs), omath.get_sub_equation(rot.e2.value,kwargs)
                 , omath.get_sub_equation(rot.f.value,kwargs)]

    ans = sympy.solve(equations)
    print(ans)