import sympy

from omath import Solver as omath
from Formulas.Formulas import _Rot_movement as rot

def solve_method(**kwargs):
    equations = [omath.get_sub_equation(rot.tang_acc_parallel.value,kwargs), omath.get_sub_equation(rot.tang_vel.value,kwargs), omath.get_sub_equation(rot.centripetal_acc_1.value,kwargs)
                 , omath.get_sub_equation(rot.centripetal_acc_2.value,kwargs)]

    ans = sympy.solve(equations)
    print(ans)