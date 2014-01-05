import cmath
import math
import numpy
import sympy
from eqpy._apimappings import (
    mathtosympy, cmathtosympy, numpytosympy, sympymappings, copysign, divide,
    exp2, expm1, floor_divide, frexp, fsum, hypot, isfinite, isfinite_complex,
    isinf, isinf_complex, isnan, isnan_complex, ldexp, log10, log1p, log2,
    logaddexp, logaddexp2, modf, negative, polar, reciprocal, rect, signbit,
    square, subtract)
from eqpy._utils import isnear

# domains used during tests
domains = {
    copysign: ('[-inf:inf]', '[-inf:inf]'),
    divide: ('any', 'any'),
    exp2: '[-inf:smallinf]',
    expm1: '[-inf:smallinf]',
    floor_divide: ('(-inf:inf)', '(-inf:inf)'),
    frexp: '(-inf:inf)',
    fsum: 'iterable(-inf:inf)',
    hypot: ('[-inf:inf]', '[-inf:inf]'),
    isfinite: 'nan[-inf:inf]',
    isfinite_complex: 'any',
    isinf: 'nan[-inf:inf]',
    isinf_complex: 'any',
    isnan: 'nan[-inf:inf]',
    isnan_complex: 'any',
    ldexp: ('[-inf:inf]', 'int(-smallinf:smallinf)'),
    log10: '(0:inf]',
    log1p: '(-1:inf]',
    log2: '(0:inf]',
    logaddexp: ('[-inf:smallinf]', '[-inf:smallinf]'),
    logaddexp2: ('[-inf:smallinf]', '[-inf:smallinf]'),
    modf: '(-inf:inf)',
    negative: '[-inf:inf]',
    polar: 'complex',
    reciprocal: '[-inf:inf]',
    rect: ('[-inf:inf]', '(-inf:inf)'),
    signbit: '[-inf:inf]',
    square: '[-inf:inf]',
    subtract: ('any', 'any'),
    'Abs': '[-inf:inf]',
    'Add': ('any', 'any'),
    'And': ('any', 'any'),
    'Equality': ('any', 'any'),
    'GreaterThan': ('any', 'any'),
    'Integer': '(-inf:inf)',
    'LessThan': ('[-inf:inf]', '[-inf:inf]'),
    'Max': ('[-inf:inf]', '[-inf:inf]'),
    'Min': ('[-inf:inf]', '[-inf:inf]'),
    'Mod': ('(-inf:inf)', '(-inf:inf)'),
    'Mul': ('any', 'any'),
    'Ne': ('any', 'any'),
    'Not': 'any',
    'Or': ('any', 'any'),
    'Pow': ('[-inf:inf]', '[-inf:inf]'),
    'StrictGreaterThan': ('any', 'any'),
    'StrictLessThan': ('any', 'any'),
    'Xor': ('any', 'any'),
    'acos': '[-1:1]',
    'acosh': '[1:inf]',
    'arg': 'complex',
    'asin': '[-1:1]',
    'asinh': '[-inf:inf]',
    'atan': '[-inf:inf]',
    'atan2': ('[-inf:inf]', '[-inf:inf]'),
    'atanh': '[1:1]',
    'ceiling': '(-inf:inf)',
    'conjugate': 'complex',
    'cos': '(-inf:inf)',
    'cosh': '(-smallinf:smallinf)',
    'deg': '[-inf:inf]',
    'erf': '[-inf:inf]',
    'erfc': '[-inf:inf]',
    'exp': '[-inf:smallinf]',
    'factorial': 'int[0:smallinf)',
    'floor': '(-inf:inf)',
    'gamma': '(0:smallinf]',
    'im': 'complex',
    'log': '(0:inf]',
    'loggamma': '(0:inf]',
    'rad': '[-inf:inf]',
    're': 'complex',
    'sign': '[-inf:inf]',
    'sin': '(-inf:inf)',
    'sinh': '[-inf:inf]',
    'sqrt': '[0:inf]',
    'tan': '(-inf:inf)',
    'tanh': '[-inf:inf]',
}

constants = [
    'E',
    'EulerGamma',
    'nan',
    'oo',
    'pi',
]

modules = {
    'math': math,
    'cmath': cmath,
    'numpy': numpy,
}


def test_domains_complete():
    assert len(set(domains).union(
        constants).symmetric_difference(sympymappings)) == 0


def test_constants():
    for name in constants:
        constant = getattr(sympy, name)
        for key, val in sympymappings[name].items():
            other = getattr(modules[key], val)
            if name == 'nan':
                assert not isnear(constant, other)
                assert constant != other
                assert other != constant
                assert isnan(constant)
                assert isnan(other)
            elif name == 'oo':
                assert isinf(constant)
                assert isinf(other)
                assert not isfinite(constant)
                assert not isfinite(other)
            else:
                assert isnear(constant, other)
