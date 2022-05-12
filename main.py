import Formulas.Formulas

import mpmath
import sympy
from omath import Solver as omath


def solve_method(theme, **kwargs):
    equations = []
    for enum in theme:
        equations.append(omath.get_sub_equation(enum.value, kwargs))

    return sympy.solve(equations)


def solve(theme, **kwargs):
    return solve_method(theme, **kwargs)


if __name__ == '__main__':
    print(solve(Formulas.Formulas._Block_incline_friction, ))
