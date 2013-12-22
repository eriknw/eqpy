from sympy import (
    Abs as abs,
    Abs as absolute,
    Add as add,
    arg as angle,  # not a ufunc
    acos as arccos,
    acosh as arccosh,
    asin as arcsin,
    asinh as arcsinh,
    atan as arctan,
    atan2 as arctan2,
    atanh as arctanh,
    # `bitwise_{and,not,or,xor}` SKIPPED
    ceiling as ceil,
    conjugate as conj,
    conjugate,
    # `copysign` defined below
    cos,
    cosh,
    rad as deg2rad,
    deg as degrees,
    # `divide` defined below
    E as e,
    Equality as equal,
    EulerGamma as euler_gamma,
    exp,
    # `exp2` defined below
    # `expm1` defined below
    Abs as fabs,
    floor,
    # `floor_divide` defined below
    Max as fmax,
    Min as fmin,
    Mod as fmod,
    # `frexp` defined below
    StrictGreaterThan as greater,
    GreaterThan as greater_equal,
    # `hypot` defined below
    im as imag,  # not a ufunc
    oo as inf,
    oo as infty,
    # `invert` SKIPPED
    # `isfinite` defined below
    # `isinf` defined below
    # `isnan` defined below
    # `ldexp` defined below
    # `left_shift` SKIPPED
    StrictLessThan as less,
    LessThan as less_equal,
    log,
    # `log10` defined below
    # `log1p` defined below
    # `log2` defined below
    # `logaddexp` defined below
    # `logaddexp2` defined below
    And as logical_and,
    Not as logical_not,
    Or as logical_or,
    Xor as logical_xor,
    Max as maximum,
    Min as minimum,
    Mod as mod,
    # `modf` defined below
    Mul as multiply,
    nan,
    # `negative` defined below
    # `nextafter` SKIPPED
    Ne as not_equal,
    pi,
    Pow as power,
    deg as rad2deg,
    rad as radians,
    re as real,  # not a ufunc
    # `reciprocal` defined below
    Mod as remainder,
    # `right_shift` SKIPPED
    # `rint` SKIPPED (for now) XXX
    sign,
    # `signbit` defined below
    sin,
    sinh,
    # `spacing` SKIPPED
    sqrt,
    # `square` defined below
    # `subtract` defined below
    tan,
    tanh,
    # `true_divide` defined below
    # `trunc` defined below
)
from eqpy.math import (
    copysign,
    expm1,
    # trunc as fix,  # not a ufunc
    frexp,
    hypot,
    ldexp,
    log10,
    log1p,
    log2,
    modf,
    trunc,
)
from eqpy.cmath import (
    isfinite,
    isinf,
    isnan,
)
from sympy import Rational as _Rational


def divide(x1, x2):
    """divide(x1, x2)

    Divide arguments.
    """
    return _Rational(x1, x2)


def exp2(x):
    """exp2(x)

    Calculate `2**x`.
    """
    return power(2, x)


def floor_divide(x1, x2):
    """floor_divide(x1, x2)

    Return the largest integer smaller or equal to the division of the inputs.
    """
    return floor(divide(x1, x2))


def logaddexp(x1, x2):
    """logaddexp(x1, x2)

    Logarithm of the sum of exponentiations of the inputs.
    """
    return log(exp(x1) + exp(x2))


def logaddexp2(x1, x2):
    """logaddexp2(x1, x2)

    Logarithm of the sum of exponentiations of the inputs in base-2.
    """
    return log2(exp2(x1) + exp2(x2))


def negative(x):
    """negative(x)

    Same as -x.
    """
    return multiply(-1, x)


def reciprocal(x):
    """reciprocal(x)

    Return the reciprocal of the argument.  Calculates ``1/x``.
    """
    return _Rational(1, x)


def signbit(x):
    """signbit(x)

    Returns True if signbit is set (less than zero).
    """
    return less(x, 0)


def square(x):
    """square(x)

    Return the square of the input, x * x.
    """
    return power(x, 2)


def subtract(x1, x2):
    """subtract(x1, x2[, out])

    Subtract arguments, x1 - x2.
    """
    return x1 + multiply(-1, x2)


true_divide = divide
