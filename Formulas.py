import enum


class Formula(enum.Enum):
    svt = "x = v * t"
    v1 = "v = v0 + a * t"
    v2 = "2 * x = v0 * t + v * t"
    v3 = "x = v0 * t + 1/2 * a * t**2"
    v4 = "v**2 - v0**2 = 2 * a * x"