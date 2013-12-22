import cmath
import eqpy
import sympy

from eqpy.cmath import (
    acos, acosh, asin, asinh, atan, atanh, cos, cosh, e, exp, isfinite, isinf,
    isnan, log, log10, phase, pi, polar, rect, sin, sinh, sqrt, tan, tanh,
)
from eqpy._utils import isnear


def test_alldefined():
    for name in dir(cmath):
        if not name.startswith('_'):
            assert hasattr(eqpy.cmath, name)


def test_isinf():
    assert cmath.isinf(float('inf')) == isinf(float('inf'))
    assert cmath.isinf(-float('inf')) == isinf(-float('inf'))
    assert cmath.isinf(float('nan')) == isinf(float('nan'))
    assert isinf(sympy.oo)
    assert isinf(-sympy.oo)
    assert not isinf(sympy.nan)
    assert cmath.isinf(1.0) == isinf(1.0)
    assert cmath.isinf(0) == isinf(0)
    inf = float('inf')
    nan = float('nan')
    assert cmath.isinf(complex(inf)) == isinf(complex(inf))
    assert cmath.isinf(complex(1, inf)) == isinf(complex(1, inf))
    assert cmath.isinf(complex(1, -inf)) == isinf(complex(1, -inf))
    assert cmath.isinf(complex(inf, 1)) == isinf(complex(inf, 1))
    assert cmath.isinf(complex(inf, inf)) == isinf(complex(inf, inf))
    assert cmath.isinf(complex(1, nan)) == isinf(complex(1, nan))
    assert cmath.isinf(complex(nan, 1)) == isinf(complex(nan, 1))
    assert cmath.isinf(complex(nan, nan)) == isinf(complex(nan, nan))


def test_isfinite():
    assert not isfinite(sympy.oo)
    assert not isfinite(-sympy.oo)
    assert not isfinite(sympy.nan)
    if hasattr(cmath, 'isfinite'):
        assert cmath.isfinite(float('inf')) == isfinite(float('inf'))
        assert cmath.isfinite(-float('inf')) == isfinite(-float('inf'))
        assert cmath.isfinite(float('nan')) == isfinite(float('nan'))
        assert cmath.isfinite(1.0) == isfinite(1.0)
        assert cmath.isfinite(0) == isfinite(0)
        inf = float('inf')
        nan = float('nan')
        assert cmath.isfinite(complex(inf)) == isfinite(complex(inf))
        assert cmath.isfinite(complex(1, inf)) == isfinite(complex(1, inf))
        assert cmath.isfinite(complex(1, -inf)) == isfinite(complex(1, -inf))
        assert cmath.isfinite(complex(inf, 1)) == isfinite(complex(inf, 1))
        assert cmath.isfinite(complex(inf, inf)) == isfinite(complex(inf, inf))
        assert cmath.isfinite(complex(1, nan)) == isfinite(complex(1, nan))
        assert cmath.isfinite(complex(nan, 1)) == isfinite(complex(nan, 1))
        assert cmath.isfinite(complex(nan, nan)) == isfinite(complex(nan, nan))
        assert cmath.isfinite(complex(inf, nan)) == isfinite(complex(inf, nan))
        assert cmath.isfinite(complex(nan, inf)) == isfinite(complex(nan, inf))
        assert cmath.isfinite(complex(1, 2)) == cmath.isfinite(complex(1, 2))
    else:
        assert not isfinite(float('inf'))
        assert not isfinite(-float('inf'))
        assert not isfinite(float('nan'))
        assert isfinite(1.0)
        assert isfinite(0)
        inf = float('inf')
        nan = float('nan')
        assert not isfinite(complex(inf))
        assert not isfinite(complex(1, inf))
        assert not isfinite(complex(1, -inf))
        assert not isfinite(complex(inf, 1))
        assert not isfinite(complex(inf, inf))
        assert not isfinite(complex(1, nan))
        assert not isfinite(complex(nan, 1))
        assert not isfinite(complex(nan, nan))
        assert not isfinite(complex(inf, nan))
        assert not isfinite(complex(nan, inf))
        assert isfinite(complex(1, 2))


def test_isnan():
    assert cmath.isnan(float('inf')) == isnan(float('inf'))
    assert cmath.isnan(-float('inf')) == isnan(-float('inf'))
    assert cmath.isnan(float('nan')) == isnan(float('nan'))
    assert not isnan(sympy.oo)
    assert not isnan(-sympy.oo)
    assert isnan(sympy.nan)
    assert cmath.isnan(1.0) == isnan(1.0)
    assert cmath.isnan(0) == isnan(0)
    inf = float('inf')
    nan = float('nan')
    assert cmath.isnan(complex(inf)) == isnan(complex(inf))
    assert cmath.isnan(complex(1, inf)) == isnan(complex(1, inf))
    assert cmath.isnan(complex(1, -inf)) == isnan(complex(1, -inf))
    assert cmath.isnan(complex(inf, 1)) == isnan(complex(inf, 1))
    assert cmath.isnan(complex(inf, inf)) == isnan(complex(inf, inf))
    assert cmath.isnan(complex(1, nan)) == isnan(complex(1, nan))
    assert cmath.isnan(complex(nan, 1)) == isnan(complex(nan, 1))
    assert cmath.isnan(complex(nan, nan)) == isnan(complex(nan, nan))
    assert cmath.isnan(complex(inf, nan)) == isnan(complex(inf, nan))
    assert cmath.isnan(complex(nan, inf)) == isnan(complex(nan, inf))


def test_log10():
    assert isnear(cmath.log10(0.1), log10(0.1))
    assert isnear(cmath.log10(1), log10(1))
    assert isnear(cmath.log10(123.45), log10(123.45))


def test_phase():
    assert isnear(cmath.phase(complex(0, 1.2)), phase(complex(0, 1.2)))
    assert isnear(cmath.phase(complex(1.2, 0)), phase(complex(1.2, 0)))
    assert isnear(cmath.phase(complex(-3.4, 5.6)), phase(complex(-3.4, 5.6)))
    # XXX sympy is inconsistent with cmath
    # assert isnear(cmath.phase(complex(0, 0)), phase(complex(0, 0)))


def test_polar():
    assert isnear(cmath.polar(complex(0, 1.2)), polar(complex(0, 1.2)))
    assert isnear(cmath.polar(complex(1.2, 0)), polar(complex(1.2, 0)))
    assert isnear(cmath.polar(complex(-3.4, 5.6)), polar(complex(-3.4, 5.6)))
    # XXX sympy is inconsistent with cmath
    # assert isnear(cmath.polar(complex(0, 0)), polar(complex(0, 0)))


def test_rect():
    assert isnear(cmath.rect(0, 1.2), rect(0, 1.2))
    assert isnear(cmath.rect(1.2, 0), rect(1.2, 0))
    assert isnear(cmath.rect(0, 0), rect(0, 0))
    assert isnear(cmath.rect(3.4, 5.6), rect(3.4, 5.6))
