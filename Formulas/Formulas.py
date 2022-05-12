from enum import Enum

class _Block_incline_friction(Enum):
    y = "N - m*g * cos(i) = 0"
    x = "m * g * sin(i) - f = m * a"
    f = "f = u * N"
    f2 = "f = u * m * g * cos(i)"

class _Rectiliniear_motion(Enum):
    svt = "x = v * t"
    v1 = "v = v0 + a * t"
    v2 = "2 * x = v0 * t + v * t"
    v3 = "x = v0 * t + 1/2 * a * t**2"
    v4 = "v**2 - v0**2 = 2 * a * x"

class _Throw(Enum):
    fx1 = "v0x = cos(i) * v0"
    fx2 = "x = v0x * t"
    fx3 = "x = v0 * cos(i) * t"

    fy1 = "vy = v0 * sin(i) + ay*t"
    fy2 = "y = v0 * sin(i) * t + 1/2 * ay * t**2 "
    fy3 = "y = v0y * t + 1/2 * ay * t**2"

class _Rot_movement(Enum):
    tang_vel = "v = w * r"
    tang_acc_parallel = "tangA = a * r"
    centripetal_acc_1 = "centA = w**2 * r"
    centripetal_acc_2 = "centA = 4 * pi **2 * r * 1/T**2"
    centripetal_acc_3 = "centA = v**2 / r "

class _Vector(Enum):
    sum = "l**2 = x**2 + y**2"

class _Newtons_laws(Enum):
    nwl2 = "F = m*a"

class _Rot_movement2(Enum):
    #o = posisjonsvinkel
    #w = vinkelfart
    #a = vinkelakselerasjon
    f_const = "o = w * t"
    f1 = "w = w0 + a * t"
    f2 = "2 * o * t = w0 + w"
    f3 = "o = w0 * t + 1/2 * a*t**2"
    f4 = "w**2-w0**2 = 2 * a * o"
    tq = "tq = I * acm"
    acm = "acm = a * r"
    vcm = "vcm = w * r"

class _Electrisity(Enum):
    f = "F = k * q1 /r**2 * q2/r**2"
    e = "E = F / q"
    e2 = "E = k*Q/R**2"
    v = "V = k*Q/r"

class _ElPotAndMovEnergy(Enum):
    up1 = "Up1 = k * q1/r1 * q2/r1"
    up2 = "Up2 = k * q1/r2 * q2/r2"
    uk1 = "Uk1 = 1/2*m1*v1**2"
    uk2 = "Uk2 = 1/2*m2*v2**2"
    u1 = "U = Up1 + Uk1"
    u2 = "U = Up2 + Uk2"
    u3 = "Up1 + Uk1 = Up2 + Uk2"

class Formula(Enum):
    rect_motion = _Rectiliniear_motion
    throw = _Throw
    rot_movement = _Rot_movement