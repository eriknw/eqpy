from eqpy._utils import isiterable, isnear, raises, isdunder


def test_isiterable():
    assert isiterable('asdf')
    assert isiterable([1, 2, 3])
    assert isiterable((1, 2, 3))
    assert isiterable(range(10))
    assert isiterable({})
    assert not isiterable(123)


def test_isnear():
    assert isnear(1, 1.000001)
    assert not isnear(1, 1.001)
    assert isnear([1, 2], [1.000001, 2.000001])
    assert not isnear([1, 2], [1.001, 2.000001])


def test_raises():
    assert not raises(None, lambda: None)
    assert raises(ZeroDivisionError, lambda: 1/0)
    assert raises(ZeroDivisionError, lambda: raises(TypeError, lambda: 1/0))


def test_isdunder():
    assert isdunder('__a__')
    assert isdunder('__asdfasdf__')
    assert not isdunder('__')
    assert not isdunder('___')
    assert not isdunder('____')
    assert not isdunder('_____')
    assert not isdunder('__foo___')
    assert not isdunder('___foo__')
    assert not isdunder('foo__')
    assert not isdunder('__foo')
    assert not isdunder('foo')
