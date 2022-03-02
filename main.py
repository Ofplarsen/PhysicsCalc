import mpmath
import sympy

from topics import rotational_movement, throw, rotational_movement2, rectilinear_motion

if __name__ == '__main__':
    ans =throw.solve_method(y=0.6, v0x=2.4, ay=9.81, i = 0)
    print(ans)
