import eqpy
import sympy
from eqpy._utils import raises


def test_imports():
    from eqpy.dummies import x1, y1 as why1

    assert x1 is not sympy.Dummy("x1")
    assert why1 is not sympy.Dummy("y1")
    assert eqpy.dummies.x1 is not x1
    assert isinstance(x1, sympy.Dummy)
    assert isinstance(why1, sympy.Dummy)
    from eqpy.dummies import y1

    assert y1 is not why1


def test_attributes():
    x2 = eqpy.dummies.x2
    assert x2 is not sympy.Dummy("x2")
    assert raises(AttributeError, lambda: eqpy.dummies.__dunder_should_fail__)
    assert isinstance(x2, sympy.Dummy)
    ex2 = eqpy.dummies.x2
    assert x2 is not ex2


def test_call():
    x3 = eqpy.dummies("x3")
    assert x3 is not sympy.Dummy("x3")
    assert isinstance(x3, sympy.Dummy)
