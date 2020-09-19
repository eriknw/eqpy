import cmath
from ._compatibility import zip


def isiterable(x):
    try:
        iter(x)
        return True
    except TypeError:
        return False


def raises(err, lamda):
    try:
        lamda()
        return False
    except err:
        return True


def isnear(a, b, rtol=1e-05, atol=1e-08):
    if isiterable(a) and isiterable(b):
        return all(isnear(x, y, rtol=rtol, atol=atol) for x, y in zip(a, b))
    try:
        return bool(abs(a - b) < atol + rtol*abs(b))
    except TypeError:
        return a == b


def isdunder(name):
    return (len(name) > 4 and name.startswith('__') and name.endswith('__')
            and name[2] != '_' and name[-3] != '_')
