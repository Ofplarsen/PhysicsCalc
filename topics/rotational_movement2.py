import sympy

from omath import Solver as omath
from Formulas.Formulas import _Rot_movement2 as rot

def solve_method(**kwargs):
    equations = [omath.get_sub_equation(rot.f1.value,kwargs), omath.get_sub_equation(rot.f2.value,kwargs)
        , omath.get_sub_equation(rot.f3.value,kwargs), omath.get_sub_equation(rot.f4.value,kwargs),
        omath.get_sub_equation(rot.tq.value,kwargs), omath.get_sub_equation(rot.acm.value,kwargs),
                 omath.get_sub_equation(rot.vcm.value,kwargs)]

    print(omath.solver(rot.f1.value, kwargs))
    print(omath.solver(rot.f2.value, kwargs))
    print(omath.solver(rot.f3.value, kwargs))
    print(omath.solver(rot.f4.value, kwargs))
    print(omath.solver(rot.tq.value, kwargs))
    print(omath.solver(rot.acm.value, kwargs))
    print(omath.solver(rot.vcm.value, kwargs))
    ans = sympy.solve(equations)
    print(ans)

