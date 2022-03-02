import mpmath
import sympy

from topics import rotational_movement, throw, rotational_movement2, rectilinear_motion, El_mag_Energy

if __name__ == '__main__':
    ans =El_mag_Energy.solve_method(q1=1.6*10**(-19), q2=1.6*10**(-19), r1=10**(-10), r2=2*10**(-10), v1=3*10**6, k=8.99*10**9, m1=9.11*10**(-31), m2=9.11*10**(-31))
    print(ans)
