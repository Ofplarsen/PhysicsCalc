import mpmath

from topics import throw

if __name__ == '__main__':
    ans = throw.solve_method(x=2.1, i=mpmath.radians(60), v0=6.4, ay=-9.81)
