import builtins
import sympy
from sympy import (Abs, Add, arg, cos, exp, floor, I, im, log, Mod, Mul, oo,
                   nan, prod, Pow, Rational, re, real_root, S, sign, sin, sqrt, StrictLessThan)
from functools import reduce


# math
def copysign(x, y):
    """copysign(x, y)

    Return x with the sign of y.
    """
    return Abs(x) * sign(y)


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
    mantissa = x / Pow(2, exponent)
    return (mantissa, exponent)


def fsum(iterable):
    """fsum(iterable)

    Return an accurate floating point sum of values in the iterable.
    """
    return reduce(Add, iterable)


def hypot(x, y):
    """hypot(x, y)

    Return the Euclidean distance, sqrt(x*x + y*y).
    """
    return sqrt(x*x + y*y)


def isfinite(x):
    """isfinite(x) -> bool

    Return True if x is neither an infinity nor a NaN, and False otherwise.
    """
    x = S(x)
    return x != oo and x != -oo and x != nan


def isinf(x):
    """isinf(x) -> bool

    Check if float x is infinite (positive or negative).
    """
    x = S(x)
    if x == oo or x == -oo:
        return True
    elif callable(getattr(x, 'n', None)):
        val = x.n()
        return val == oo or val == -oo
    return False


def isnan(x):
    """isnan(x) -> bool

    Check if float x is not a number (NaN).
    """
    x = S(x)
    return x == nan


def isqrt(x):
    return floor(sqrt(x))


def ldexp(x, i):
    """ldexp(x, i)

    Return x * (2**i).
    """
    return x * Pow(2, i)


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
    signx = sign(x)
    absx = Abs(x)
    return (signx * Mod(absx, 1), signx * floor(absx))


def prod(iterables, start=1):
    return sympy.prod(iterables, start=start)


# cmath
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    a = S(a)
    b = S(b)
    if a == b:
        return True
    if isinf_complex(Abs(a)) or isinf_complex(Abs(b)):
        return False
    diff = Abs(a - b)
    return diff <= rel_tol * Abs(a) or diff <= rel_tol * Abs(b) or diff <= abs_tol


def isfinite_complex(x):
    """isfinite(z) -> bool
    Return True if both the real and imag parts of z are finite, else False.
    """
    x = S(x)
    return isfinite(re(x)) and isfinite(im(x))


def isinf_complex(x):
    """isinf(z) -> bool
    Checks if the real or imaginary part of z is infinite.
    """
    x = S(x)
    return isinf(re(x)) or isinf(im(x))


def isnan_complex(x):
    """isnan(z) -> bool
    Checks if the real or imaginary part of z not a number (NaN)
    """
    x = S(x)
    return x == nan


def polar(z):
    """polar(z) -> r: float, phi: float

    Convert a complex from rectangular coordinates to polar coordinates. r is
    the distance from 0 and phi the phase angle.
    """
    return (Abs(z), arg(z))


def rect(r, phi):
    """rect(r, phi) -> z: complex

    Convert from polar coordinates to rectangular coordinates.
    """
    return r * cos(phi) + I * r * sin(phi)


# numpy
def cbrt(x):
    return real_root(x, 3)


def divide(x1, x2):
    """divide(x1, x2)

    Divide arguments.
    """
    return Rational(x1, x2)


def divmod(x, y):
    return builtins.divmod(S(x), S(y))


def exp2(x):
    """exp2(x)

    Calculate `2**x`.
    """
    return Pow(2, x)


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
    return Mul(-1, x)


def positive(x):
    return +S(x)


def reciprocal(x):
    """reciprocal(x)

    Return the reciprocal of the argument.  Calculates ``1/x``.
    """
    return Rational(1, x)


def signbit(x):
    """signbit(x)

    Returns True if signbit is set (less than zero).
    """
    return StrictLessThan(x, 0)


def square(x):
    """square(x)

    Return the square of the input, x * x.
    """
    return Pow(x, 2)


def subtract(x1, x2):
    """subtract(x1, x2[, out])

    Subtract arguments, x1 - x2.
    """
    return x1 + Mul(-1, x2)


# mappings
mathtosympy = {
    'acos': 'acos',
    'acosh': 'acosh',
    'asin': 'asin',
    'asinh': 'asinh',
    'atan': 'atan',
    'atan2': 'atan2',
    'atanh': 'atanh',
    'ceil': 'ceiling',
    'comb': 'binomial',
    'copysign': copysign,
    'cos': 'cos',
    'cosh': 'cosh',
    'degrees': 'deg',
    'dist': hypot,
    'e': 'E',
    'erf': 'erf',
    'erfc': 'erfc',
    'exp': 'exp',
    'expm1': expm1,
    'fabs': 'Abs',
    'factorial': 'factorial',
    'floor': 'floor',
    # 'fmod': fmod,  # SKIPPED: not consistent; depends on architecture
    'frexp': frexp,
    'fsum': fsum,
    'gamma': 'gamma',
    'gcd': 'gcd',
    'hypot': hypot,
    'inf': 'oo',
    'isclose': isclose,
    'isfinite': isfinite,
    'isinf': isinf,
    'isnan': isnan,
    'isqrt': isqrt,
    'ldexp': ldexp,
    'lgamma': 'loggamma',
    'log': 'log',
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'modf': modf,
    'nan': nan,
    'perm': 'ff',
    'pi': 'pi',
    'pow': 'Pow',
    'prod': prod,
    'radians': 'rad',
    # 'remainder': remainder,  # what a stupid function!
    'sin': 'sin',
    'sinh': 'sinh',
    'sqrt': 'sqrt',
    'tan': 'tan',
    'tanh': 'tanh',
    'tau': S('2 * pi'),
    'trunc': 'Integer',
}

cmathtosympy = {
    'acos': 'acos',
    'acosh': 'acosh',
    'asin': 'asin',
    'asinh': 'asinh',
    'atan': 'atan',
    'atanh': 'atanh',
    'cos': 'cos',
    'cosh': 'cosh',
    'e': 'E',
    'exp': 'exp',
    'isclose': isclose,
    'isfinite': isfinite_complex,
    'isinf': isinf_complex,
    'isnan': isnan_complex,
    'log': 'log',
    'log10': log10,
    'inf': 'oo',
    'infj': S('oo*I'),
    'nan': 'nan',
    'nanj': S('nan*I'),  # currently just `nan`
    'phase': 'arg',
    'pi': 'pi',
    'polar': polar,
    'rect': rect,
    'sin': 'sin',
    'sinh': 'sinh',
    'sqrt': 'sqrt',
    'tan': 'tan',
    'tanh': 'tanh',
    'tau': S('2 * pi'),
}

numpytosympy = {
    'abs': 'Abs',
    'absolute': 'Abs',
    'add': 'Add',
    'angle': 'arg',  # not a ufunc
    'arccos': 'acos',
    'arccosh': 'acosh',
    'arcsin': 'asin',
    'arcsinh': 'asinh',
    'arctan': 'atan',
    'arctan2': 'atan2',
    'arctanh': 'atanh',
    # `bitwise_{and,not,or,xor}` SKIPPED
    'cbrt': cbrt,
    'ceil': 'ceiling',
    'conj': 'conjugate',
    'conjugate': 'conjugate',
    'copysign': copysign,
    'cos': 'cos',
    'cosh': 'cosh',
    'deg2rad': 'rad',
    'degrees': 'deg',
    'divide': divide,
    'divmod': divmod,
    'e': 'E',
    'equal': 'Equality',
    'euler_gamma': 'EulerGamma',
    'exp': 'exp',
    'exp2': exp2,
    'expm1': expm1,
    'fabs': 'Abs',
    'float_power': 'Pow',
    'floor': 'floor',
    'floor_divide': floor_divide,
    'fmax': 'Max',
    'fmin': 'Min',
    'fmod': 'Mod',
    'frexp': frexp,
    'gcd': 'gcd',
    'greater': 'StrictGreaterThan',
    'greater_equal': 'GreaterThan',
    'heaviside': 'Heaviside',
    'hypot': hypot,
    'imag': 'im',
    'inf': 'oo',
    'infty': 'oo',
    # `invert` SKIPPED
    'isfinite': isfinite_complex,
    'isinf': isinf_complex,
    'isnan': isnan_complex,
    # `isnat` SKIPPED
    'lcm': 'lcm',
    'ldexp': ldexp,
    # `left_shift` SKIPPED
    'less': 'StrictLessThan',
    'less_equal': 'LessThan',
    'log': 'log',
    'log10': log10,
    'log1p': log1p,
    'log2': log2,
    'logaddexp': logaddexp,
    'logaddexp2': logaddexp2,
    'logical_and': 'And',
    'logical_not': 'Not',
    'logical_or': 'Or',
    'logical_xor': 'Xor',
    # `matmul` SKIPPED
    'maximum': 'Max',
    'minimum': 'Min',
    'mod': 'Mod',
    'modf': modf,
    'multiply': 'Mul',
    'nan': 'nan',
    'negative': negative,
    # `nextafter` SKIPPED
    'not_equal': 'Ne',
    'pi': 'pi',
    'positive': positive,
    'power': 'Pow',
    'rad2deg': 'deg',
    'radians': 'rad',
    'real': 're',  # not a ufunc
    'reciprocal': reciprocal,
    'remainder': 'Mod',
    # `right_shift` SKIPPED
    # `rint` SKIPPED (for now) XXX
    'sign': 'sign',
    'signbit': signbit,
    'sin': 'sin',
    'sinh': 'sinh',
    # `spacing` SKIPPED
    'sqrt': 'sqrt',
    'square': square,
    'subtract': subtract,
    'tan': 'tan',
    'tanh': 'tanh',
    'true_divide': divide,
    'trunc': 'Integer',
}

sympymappings = {}
for othername, otherdict in [('math', mathtosympy), ('cmath', cmathtosympy),
                             ('numpy', numpytosympy)]:
    for otherval, sympyval in otherdict.items():
        if sympyval not in sympymappings:
            sympymappings[sympyval] = {}
        sympymappings[sympyval][othername] = otherval
del othername, otherdict, otherval, sympyval
