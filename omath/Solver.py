from sympy import *


def solver(equation, kwargs):
    sympy_eq = get_equation(equation)

    sympy_eq = sympy_eq.subs(kwargs)
    return solve(sympy_eq, dict=true)


def get_equation(equation):
    return sympify("Eq(" + equation.replace("=", ",") + ")")

def get_sub_equation(equation, kwargs):
    sympy_eq = get_equation(equation)

    return sympy_eq.subs(kwargs)