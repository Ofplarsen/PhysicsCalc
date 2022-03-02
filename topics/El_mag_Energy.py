import sympy

from omath import Solver as omath
from Formulas.Formulas import _ElPotAndMovEnergy as pm

def solve_method(**kwargs):
    equations = [omath.get_sub_equation(pm.u1.value,kwargs), omath.get_sub_equation(pm.u2.value,kwargs), omath.get_sub_equation(pm.u3.value,kwargs)
                 , omath.get_sub_equation(pm.uk1.value,kwargs), omath.get_sub_equation(pm.uk2.value,kwargs), omath.get_sub_equation(pm.up1.value,kwargs),
                 omath.get_sub_equation(pm.up2.value,kwargs)]

    ans = sympy.solve(equations)
    print(ans)