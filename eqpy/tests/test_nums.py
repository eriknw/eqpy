import eqpy
import sympy
from eqpy._utils import raises


def test_constants():
    assert eqpy.nums.Catalan is sympy.Catalan
    assert eqpy.nums.E is sympy.E
    assert eqpy.nums.EulerGamma is sympy.EulerGamma
    assert eqpy.nums.GoldenRatio is sympy.GoldenRatio
    assert eqpy.nums.I is sympy.I
    assert eqpy.nums.nan is sympy.nan
    assert eqpy.nums.oo is sympy.oo
    assert eqpy.nums.pi is sympy.pi
    assert eqpy.nums.zoo is sympy.zoo


def test_sympify():
    eqpy.nums.x = '1/2'
    assert eqpy.nums.x == sympy.S('1/2')
    assert eqpy.nums('2/3') == sympy.S('2/3')
    assert raises(sympy.SympifyError, lambda: eqpy.nums('1.2.3'))


def test_dunders():
    eqpy.nums.__mydunder__ = '1/2'
    assert eqpy.nums.__mydunder__ == '1/2'
