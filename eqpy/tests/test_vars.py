import eqpy
import sympy
from eqpy._utils import raises


def test_imports():
    from eqpy.vars import x1, y1 as why1
    assert x1 is sympy.Symbol('x1')
    assert why1 is sympy.Symbol('y1')
    assert eqpy.vars.x1 is x1


def test_attributes():
    x2 = eqpy.vars.x2
    assert x2 is sympy.Symbol('x2')
    assert raises(AttributeError, lambda: eqpy.vars.__dunder_should_fail__)


def test_call():
    x3 = eqpy.vars('x3')
    assert x3 is sympy.Symbol('x3')
