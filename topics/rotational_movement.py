import sympy

from omath import Solver as omath
from Formulas.Formulas import _Throw as throw

def solve_method(**kwargs):
    equations = [omath.get_sub_equation(throw.fx1.value,kwargs), omath.get_sub_equation(throw.fx2.value,kwargs)
                     , omath.get_sub_equation(throw.fx3.value,kwargs), omath.get_sub_equation(throw.fy1.value,kwargs), omath.get_sub_equation(throw.fy2.value,kwargs),
                     omath.get_sub_equation(throw.fy3.value,kwargs)]
    ###
    #print(fx1(kwargs))
    #print(fx2(kwargs))
    #print(fx3(kwargs))
    #print(fy2(kwargs))
    #print(fy1(kwargs))
    ###
    ans = sympy.solve(equations)
    print(ans)

def fx1(kwargs):
    return omath.solver(throw.fx1.value, kwargs)

def fx2(kwargs):
    return omath.solver(throw.fx2.value, kwargs)

def fx3(kwargs):
    return omath.solver(throw.fx3.value, kwargs)

def fy1(kwargs):
    return omath.solver(throw.fy1.value, kwargs)

def fy2(kwargs):
    return omath.solver(throw.fy2.value, kwargs)
