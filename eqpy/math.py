from sympy import (
    acos,
    acosh,
    asin,
    asinh,
    atan,
    atan2,
    atanh,
    ceiling as ceil,
    # `copysign` defined below
    cos,
    cosh,
    deg as degrees,
    E as e,
    erf,
    erfc,
    exp,
    # `expm1` defined below
    Abs as fabs,
    factorial,
    floor,
    Mod as fmod,
    # `frexp` defined below
    # `fsum` defined below
    gamma,
    # `hypot` defined below
    # `isfinite` defined below
    # `isinf` defined below
    # `isnan` defined below
    # `ldexp` defined below
    loggamma as lgamma,
    log,
    # `log10` defined below
    # `log1p` defined below
    # `log2` defined below
    # `modf` defined below
    pi,
    Pow as pow,
    rad as radians,
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
    # `trunc` defined below
)
from sympy import sign as _sign, Add as _Add, oo as _oo, nan as _nan, S as _S


def copysign(x, y):
    """copysign(x, y)

    Return x with the sign of y.
    """
    return fabs(x) * _sign(y)


# update this if implemented in sympy
def expm1(x):
    """expm1(x)

    Return exp(x)-1.
    """
    return exp(x) - 1


def frexp(x):
    """frexp(x)

    Return the mantissa and exponent of x, as pair (m, e).
    m is a float and e is an int, such that x = m * 2.**e.
    If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    """
    if x == 0:
        return (0.0, 0)
    exponent = floor(log2(abs(x))) + 1
    mantissa = x / pow(2, exponent)
    return (mantissa, exponent)


def fsum(iterable):
    """fsum(iterable)

    Return an accurate floating point sum of values in the iterable.
    """
    return reduce(_Add, iterable)


def hypot(x, y):
    """hypot(x, y)

    Return the Euclidean distance, sqrt(x*x + y*y).
    """
    return sqrt(x*x + y*y)


def isfinite(x):
    """isfinite(x) -> bool

    Return True if x is neither an infinity nor a NaN, and False otherwise.
    """
    x = _S(x)
    return x != _oo and x != -_oo and x != _nan


def isinf(x):
    """isinf(x) -> bool

    Check if float x is infinite (positive or negative).
    """
    x = _S(x)
    return x == _oo or x == -_oo


def isnan(x):
    """isnan(x) -> bool

    Check if float x is not a number (NaN).
    """
    x = _S(x)
    return x == _nan


def ldexp(x, i):
    """ldexp(x, i)

    Return x * (2**i).
    """
    return x * pow(2, i)


def log10(x):
    """log10(x)

    Return the base 10 logarithm of x.
    """
    return log(x) / log(10)


# update this if implemented in sympy
def log1p(x):
    """log1p(x)

    Return the natural logarithm of 1+x (base e).
    """
    return log(1 + x)


def log2(x):
    """log2(x)

    Return the base 2 logarithm of x.
    """
    return log(x) / log(2)


def modf(x):
    """modf(x)

    Return the fractional and integer parts of x.  Both results carry the sign
    of x.
    """
    signx = _sign(x)
    absx = fabs(x)
    return (signx * fmod(absx, 1), signx * floor(absx))


def trunc(x):
    """trunc(x:Real) -> Integral

    Truncates x to the nearest Integral toward 0.
    """
    return _sign(x) * floor(fabs(x))
