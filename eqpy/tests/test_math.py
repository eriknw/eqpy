import math
import eqpy
import sympy

from eqpy.math import (
    acos, acosh, asin, asinh, atan, atan2, atanh, ceil, copysign, cos, cosh,
    degrees, e, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, frexp,
    fsum, gamma, hypot, isfinite, isinf, isnan, ldexp, lgamma, log, log10,
    log1p, log2, modf, pi, pow, radians, sin, sinh, sqrt, tan, tanh, trunc,
)
from eqpy._utils import isnear


def test_alldefined():
    for name in dir(math):
        if not name.startswith('_'):
            assert hasattr(eqpy.math, name)


def test_acos():
    assert isnear(math.acos(0), acos(0))
    assert isnear(math.acos(0.5), acos(0.5))
    assert isnear(math.acos(-0.123), acos(-0.123))


def test_acosh():
    assert isnear(math.acosh(1.0), acosh(1.0))
    assert isnear(math.acosh(10.0), acosh(10.0))


def test_asin():
    assert isnear(math.asin(0), asin(0))
    assert isnear(math.asin(0.5), asin(0.5))
    assert isnear(math.asin(-0.123), asin(-0.123))


def test_asinh():
    assert isnear(math.asinh(1.0), asinh(1.0))
    assert isnear(math.asinh(10.0), asinh(10.0))


def test_atan():
    assert isnear(math.atan(0), atan(0))
    assert isnear(math.atan(-1.0), atan(-1.0))
    assert isnear(math.atan(1000.0), atan(1000.0))


def test_atan2():
    assert isnear(math.atan2(1, 2), atan2(1, 2))
    assert isnear(math.atan2(-3, 4), atan2(-3, 4))
    assert isnear(math.atan2(5, -6), atan2(5, -6))
    assert isnear(math.atan2(-7, -8), atan2(-7, -8))


def test_ceil():
    assert isnear(math.ceil(0.0), ceil(0.0))
    assert isnear(math.ceil(1.1), ceil(1.1))
    assert isnear(math.ceil(1.9), ceil(1.9))
    assert isnear(math.ceil(-1.1), ceil(-1.1))
    assert isnear(math.ceil(-1.9), ceil(-1.9))


def test_copysign():
    assert isnear(math.copysign(-7.2, -87), copysign(-7.2, -87))
    assert isnear(math.copysign(1.1, -3), copysign(1.1, -3))
    assert isnear(math.copysign(-2.2, 4), math.copysign(-2.2, 4))
    assert isnear(math.copysign(3.3, 5), copysign(3.3, 5))


def test_expm1():
    assert isnear(math.expm1(0), expm1(0))
    assert isnear(math.expm1(0.001), expm1(0.001))
    assert isnear(math.expm1(1.001), expm1(1.001))


def test_frexp():
    assert isnear(math.frexp(0), frexp(0))
    assert isnear(math.frexp(1), frexp(1))
    assert isnear(math.frexp(-1), frexp(-1))
    assert isnear(math.frexp(123.45), frexp(123.45))
    assert isnear(math.frexp(-456.78), frexp(-456.78))


def test_fsum():
    assert isnear(math.fsum(range(10)), fsum(range(10)))
    assert isnear(math.fsum(0.3 * x for x in range(10)),
                  fsum(0.3 * x for x in range(10)))
    assert isnear(math.fsum([1]), fsum([1]))


def test_hypot():
    assert isnear(math.hypot(3, 4), hypot(3, 4))


def test_isinf():
    assert math.isinf(float('inf')) == isinf(float('inf'))
    assert math.isinf(-float('inf')) == isinf(-float('inf'))
    assert math.isinf(float('nan')) == isinf(float('nan'))
    assert isinf(sympy.oo)
    assert isinf(-sympy.oo)
    assert not isinf(sympy.nan)
    assert math.isinf(1.0) == isinf(1.0)
    assert math.isinf(0) == isinf(0)


def test_isfinite():
    assert not isfinite(sympy.oo)
    assert not isfinite(-sympy.oo)
    assert not isfinite(sympy.nan)
    if hasattr(math, 'isfinite'):
        assert math.isfinite(float('inf')) == isfinite(float('inf'))
        assert math.isfinite(-float('inf')) == isfinite(-float('inf'))
        assert math.isfinite(float('nan')) == isfinite(float('nan'))
        assert math.isfinite(1.0) == isfinite(1.0)
        assert math.isfinite(0) == isfinite(0)
    else:
        assert not isfinite(float('inf'))
        assert not isfinite(-float('inf'))
        assert not isfinite(float('nan'))
        assert isfinite(1.0)
        assert isfinite(0)


def test_isnan():
    assert math.isnan(float('inf')) == isnan(float('inf'))
    assert math.isnan(-float('inf')) == isnan(-float('inf'))
    assert math.isnan(float('nan')) == isnan(float('nan'))
    assert not isnan(sympy.oo)
    assert not isnan(-sympy.oo)
    assert isnan(sympy.nan)
    assert math.isnan(1.0) == isnan(1.0)
    assert math.isnan(0) == isnan(0)


def test_ldexp():
    assert isnear(math.ldexp(1.2, 3), ldexp(1.2, 3))
    assert isnear(math.ldexp(4.5, -6), ldexp(4.5, -6))
    assert isnear(math.ldexp(-1.2, 3), ldexp(-1.2, 3))


def test_log10():
    assert isnear(math.log10(0.1), log10(0.1))
    assert isnear(math.log10(1), log10(1))
    assert isnear(math.log10(123.45), log10(123.45))


def test_log1p():
    assert isnear(math.log1p(0.1), log1p(0.1))
    assert isnear(math.log1p(1), log1p(1))
    assert isnear(math.log1p(123.45), log1p(123.45))


def test_log2():
    if hasattr(math, 'log2'):
        assert isnear(math.log2(0.1), log2(0.1))
        assert isnear(math.log2(1), log2(1))
        assert isnear(math.log2(123.45), log2(123.45))
    else:
        assert log2(1) == 0
        assert log2(2) == 1
        assert isnear(log2(8), 3)


def test_modf():
    assert isnear(math.modf(0), modf(0))
    assert isnear(math.modf(3), modf(3))
    assert isnear(math.modf(1.2), modf(1.2))
    assert isnear(math.modf(-3.7), modf(-3.7))


def test_trunc():
    assert isnear(math.trunc(1.1), trunc(1.1))
    assert isnear(math.trunc(1.9), trunc(1.9))
    assert isnear(math.trunc(-1.1), trunc(-1.1))
    assert isnear(math.trunc(-1.9), trunc(-1.9))
    assert isnear(math.trunc(0), trunc(0))
    assert isnear(math.trunc(3.0), trunc(3.0))
    assert isnear(math.trunc(-5.0), trunc(-5.0))
