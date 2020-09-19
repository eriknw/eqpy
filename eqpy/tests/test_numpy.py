import eqpy
import numpy
import sympy
from eqpy._utils import isnear

from eqpy.numpy import (
    abs,
    absolute,
    add,
    angle,
    arccos,
    arccosh,
    arcsin,
    arcsinh,
    arctan,
    arctan2,
    arctanh,
    ceil,
    conj,
    conjugate,
    copysign,
    cos,
    cosh,
    deg2rad,
    degrees,
    divide,
    e,
    equal,
    euler_gamma,
    exp,
    exp2,
    expm1,
    fabs,
    floor,
    floor_divide,
    fmax,
    fmin,
    fmod,
    frexp,
    greater,
    greater_equal,
    hypot,
    imag,
    inf,
    infty,
    isfinite,
    isinf,
    isnan,
    ldexp,
    less,
    less_equal,
    log,
    log10,
    log1p,
    log2,
    logaddexp,
    logaddexp2,
    logical_and,
    logical_not,
    logical_or,
    logical_xor,
    maximum,
    minimum,
    mod,
    modf,
    multiply,
    nan,
    negative,
    not_equal,
    pi,
    power,
    rad2deg,
    radians,
    real,
    reciprocal,
    remainder,
    sign,
    signbit,
    sin,
    sinh,
    sqrt,
    square,
    subtract,
    tan,
    tanh,
    true_divide,
    trunc,
)


def test_alldefined():
    skipped = [
        "_arg",
        "bitwise_and",
        "bitwise_not",
        "bitwise_or",
        "bitwise_xor",
        "invert",
        "isnat",
        "left_shift",
        "matmul",
        "nextafter",
        "right_shift",
        "rint",
        "spacing",
    ]
    for name, value in sorted(numpy.__dict__.items()):
        if isinstance(value, numpy.ufunc) and name not in skipped:
            assert hasattr(eqpy.numpy, name)


def test_divide():
    assert isnear(numpy.divide(123.0, 456.0), divide(123.0, 456.0))


def test_exp2():
    assert isnear(numpy.exp2(12.3), exp2(12.3))


def test_floor_divide():
    assert isnear(numpy.floor_divide(456.0, 23.0), floor_divide(456.0, 23.0))


def test_logaddexp():
    assert isnear(numpy.logaddexp(7, 8), logaddexp(7, 8))


def test_logaddexp2():
    assert isnear(numpy.logaddexp2(7, 8), logaddexp2(7, 8))


def test_negative():
    assert isnear(numpy.negative(12.3), negative(12.3))
    assert isnear(numpy.negative(-23.4), negative(-23.4))


def test_reciprocal():
    assert isnear(numpy.reciprocal(12.3), reciprocal(12.3))
    assert isnear(numpy.reciprocal(-23.4), reciprocal(-23.4))


def test_signbit():
    assert isnear(numpy.signbit(12.3), signbit(12.3))
    assert isnear(numpy.signbit(-23.4), signbit(-23.4))


def test_square():
    assert isnear(numpy.square(12.3), square(12.3))
    assert isnear(numpy.square(-23.4), square(-23.4))


def test_subtract():
    assert isnear(numpy.subtract(1.2, 3.4), subtract(1.2, 3.4))


def test_true_divide():
    assert isnear(numpy.true_divide(123.0, 456.0), true_divide(123.0, 456.0))
