from __future__ import print_function
import cmath
import math
import random
import numpy
import sympy
from eqpy._apimappings import (
    mathtosympy,
    cmathtosympy,
    numpytosympy,
    sympymappings,
    cbrt,
    copysign,
    divide,
    divmod,
    exp2,
    expm1,
    floor_divide,
    frexp,
    fsum,
    hypot,
    isclose,
    isfinite,
    isfinite_complex,
    isinf,
    isinf_complex,
    isnan,
    isnan_complex,
    isqrt,
    ldexp,
    log10,
    log1p,
    log2,
    logaddexp,
    logaddexp2,
    modf,
    negative,
    polar,
    positive,
    prod,
    reciprocal,
    rect,
    signbit,
    square,
    subtract,
)
from eqpy._utils import isnear

# This file is a little ugly and sloppy, but it works well enough

# domains used during tests
domains = {
    cbrt: "nan[-inf:inf]",
    copysign: ("[-inf:inf]", "nonzero[-inf:inf]"),
    divide: ("float(-inf:inf)", "nonzero float(-inf:inf)"),
    divmod: ("[-inf:inf]", "nonzero[-inf:inf]"),
    exp2: "[-inf:smallinf]",
    expm1: "[-inf:smallinf]",
    floor_divide: ("float(-inf:inf)", "int(0:inf)"),
    # fmod: ('(-inf:inf)', '(-inf:inf)'),
    frexp: "(-inf:inf)",
    fsum: "iterable(-inf:inf)",
    hypot: ("[-inf:inf]", "[-inf:inf]"),
    isclose: ("[-inf:inf]", "[-inf:inf]"),
    isfinite: "nan[-inf:inf]",
    isfinite_complex: "any",
    isinf: "nan[-inf:inf]",
    isinf_complex: "any",
    isnan: "nan[-inf:inf]",
    isnan_complex: "any",
    isqrt: "int[0:inf)",
    ldexp: ("[-inf:inf]", "int(-smallinf:smallinf)"),
    log10: "(0:inf]",
    log1p: "(-1:inf]",
    log2: "(0:inf]",
    logaddexp: ("(-inf:smallinf)", "(-inf:smallinf)"),
    logaddexp2: ("(-inf:smallinf)", "(-inf:smallinf)"),
    modf: "(-inf:inf)",
    negative: "[-inf:inf]",
    polar: "complex nonzero",
    positive: "any",
    prod: "iterable[-inf:inf]",
    reciprocal: "nonzero[-1:1]",
    rect: ("(-inf:inf)", "(-inf:inf)"),
    signbit: "[-inf:inf]",
    square: "[-inf:inf]",
    subtract: ("(-inf:inf)", "(-inf:inf)"),
    "Abs": "[-inf:inf]",
    "Add": ("(-inf:inf)", "(-inf:inf)"),
    "And": ("bool", "bool"),
    "Equality": ("[-inf:inf]", "[-inf:inf]"),
    "GreaterThan": ("(-inf:inf)", "(-inf:inf)"),
    "Heaviside": ("[-inf:inf]", "[-inf:inf]"),
    "Integer": "(-inf:inf)",
    "LessThan": ("[-inf:inf]", "[-inf:inf]"),
    "Max": ("[-inf:inf]", "[-inf:inf]"),
    "Min": ("[-inf:inf]", "[-inf:inf]"),
    "Mod": ("(-inf:inf)", "[1:inf)"),
    "Mul": ("nonzero(-inf:inf)", "[-inf:inf]"),
    "Ne": ("[-inf:inf]", "[-inf:inf]"),
    "Not": "[-inf:inf]",
    "Or": ("bool", "bool"),
    "Pow": ("[-smallinf:smallinf]", "int[0:inf)"),
    "StrictGreaterThan": ("(-inf:inf)", "(-inf:inf)"),
    "StrictLessThan": ("(-inf:inf)", "(-inf:inf)"),
    "Xor": ("[-inf:inf]", "[-inf:inf]"),
    "acos": "[-1:1]",
    "acosh": "[1:inf]",
    "arg": "nonzero complex",
    "asin": "[-1:1]",
    "asinh": "[-inf:inf]",
    "atan": "[-inf:inf]",
    "atan2": ("nonzero(-inf:inf)", "nonzero(-inf:inf)"),
    "atanh": "(-1:1)",
    "binomial": ("int[0:smallinf)", "int[0:smallinf)"),
    "ceiling": "(-inf:inf)",
    "conjugate": "complex",
    "cos": "(-inf:inf)",
    "cosh": "(-smallinf:smallinf)",
    "deg": "[-inf:inf]",
    "erf": "[-inf:inf]",
    "erfc": "[-inf:inf]",
    "exp": "[-inf:smallinf]",
    "factorial": "int[0:smallinf)",
    "ff": ("int[0:smallinf)", "int[0:smallinf)"),
    "floor": "(-inf:inf)",
    "gamma": "(0:smallinf]",
    "gcd": ("int(-smallinf:smallinf)", "int(-smallinf:smallinf)"),
    "im": "complex",
    "lcm": ("int(-smallinf:smallinf)", "int(-smallinf:smallinf)"),
    "log": "(0:inf]",
    "loggamma": "(0:inf]",
    "rad": "[-inf:inf]",
    "re": "complex",
    "sign": "[-inf:inf]",
    "sin": "(-inf:inf)",
    "sinh": "[-smallinf:smallinf]",
    "sqrt": "[0:inf]",
    "tan": "(-inf:inf)",
    "tanh": "[-inf:inf]",
}

constants = [
    "E",
    "EulerGamma",
    "nan",
    "oo",
    "pi",
    sympy.S("2 * pi"),
    sympy.S("nan*I"),
    sympy.S("oo*I"),
]

modules = {
    "math": math,
    "cmath": cmath,
    "numpy": numpy,
}

skip = {
    "math": {"comb", "erf", "erfc", "expm1", "gamma", "isfinite", "isqrt", "lgamma", "log2", "prod"},
    "cmath": {"isfinite"},
    "numpy": set(),
}
always_skip = {
    "math": set(),
    "cmath": set(),
    "numpy": {"divmod"},
}

inf = float("inf")
nan = float("nan")
integers = list(range(-10, 11)) + [-1001, -101, 101, 1001]
extended_integers = integers + [inf, -inf]
reals = integers + [
    0.0,
    0.01,
    0.5,
    0.99,
    1.0,
    1.01,
    1.57,
    1.58,
    3.14,
    3.15,
    6.28,
    6.29,
    -0.01,
    -0.5,
    -0.99,
    1.0,
    -1.01,
    -1.57,
    -1.58,
    -3.14,
    -3.15,
    -6.28,
    -6.29,
]
extended_reals = reals + [inf, -inf]
complexes = list(complex(x, y) for x in reals for y in reals)
anys = extended_reals + complexes + [nan]
bools = [True, False]
smallinf = 10

randomstate = random.getstate()
random.seed(213)


def shuffle(vals):
    random.shuffle(vals)
    return vals


def get_domain(domain):
    if isinstance(domain, tuple):
        return [shuffle(get_domain(item)[0]) for item in domain]
    if "complex" in domain:
        nums = complexes
        if "nonzero" in domain:
            nums = [x for x in nums if x != 0]
        return [nums]
    if domain == "any":
        return [anys]
    if domain == "bool":
        return [bools]

    excludelower = "(" in domain
    if not excludelower:
        assert "[" in domain
    excludeupper = ")" in domain
    if not excludeupper:
        assert "]" in domain
    lower = domain[domain.index(excludelower and "(" or "[") + 1 : domain.index(":")]
    upper = domain[domain.index(":") + 1 : domain.index(excludeupper and ")" or "]")]

    if "int" in domain:
        nums = "inf" in domain and extended_integers or integers
    else:
        nums = "inf" in domain and extended_reals or reals
    if "smallinf" in lower:
        nums = [x for x in nums if x > smallinf]
        if not excludelower:
            nums.append(-inf)
    elif "inf" in lower and excludelower:
        nums = [x for x in nums if x != -inf]
    else:
        val = "int" in domain and int(lower) or float(lower)
        nums = [x for x in nums if not excludelower and x == val or x > val]
    if "smallinf" in upper:
        nums = [x for x in nums if x < smallinf]
        if not excludeupper:
            nums.append(inf)
    elif "inf" in upper and excludeupper:
        nums = [x for x in nums if x != inf]
    else:
        val = "int" in domain and int(upper) or float(upper)
        nums = [x for x in nums if not excludeupper and x == val or x < val]
    if "float" in domain:
        nums = [float(x) for x in nums]
    if "nonzero" in domain:
        nums = [x for x in nums if x != 0]
    if "nan" in domain:
        nums.append(nan)
    if "iterable" in domain:
        nums = [(x, x, x) for x in nums]
    return [nums]


def test_domains():
    for sympyfunc in sorted(sympymappings, key=lambda x: str(x)):
        if sympyfunc in constants:
            continue
        mappings = sympymappings[sympyfunc]
        try:
            domain = get_domain(domains[sympyfunc])
        except Exception:
            print(sympyfunc, type(sympyfunc))
            raise
        if not callable(sympyfunc):
            sympyfunc = getattr(sympy, sympyfunc)
        for args in zip(*domain):
            try:
                sympyval = sympyfunc(*args)
            except Exception:
                print(sympyfunc, args)
                raise
            for othermodule, othername in mappings.items():
                if othername in always_skip[othermodule]:
                    continue
                otherfunc = getattr(modules[othermodule], othername, None)
                if otherfunc is None and othername not in skip[othermodule]:
                    getattr(modules[othermodule], othername)
                if otherfunc is None:
                    continue
                try:
                    otherval = otherfunc(*args)
                except Exception:
                    print(otherfunc, args)
                    raise

                def check(sympyval, otherval):
                    res1 = isnear(sympyval, otherval)
                    res2 = isinf(sympyval) and isinf(otherval)
                    res3 = isnan(sympyval) and isnan(otherval)
                    res4 = otherval == sympyval
                    res5 = hasattr(sympyval, "n") and isnear(otherval, sympyval.n())
                    if not (res1 or res2 or res3 or res4):
                        print(othermodule, othername, args, sympyval, otherval)
                    assert res1 or res2 or res3 or res4 or res5

                if type(sympyval) is tuple:
                    assert len(sympyval) == len(otherval)
                    for val1, val2 in zip(sympyval, otherval):
                        check(val1, val2)
                else:
                    check(sympyval, otherval)


def test_domains_complete():
    assert len(set(domains).union(constants).symmetric_difference(sympymappings)) == 0


def test_constants():
    for name in constants:
        if isinstance(name, str):
            constant = getattr(sympy, name)
        else:
            constant = name
        for key, val in sympymappings[name].items():
            other = getattr(modules[key], val)
            if name == "nan" or constant is sympy.nan:
                assert not isnear(constant, other)
                assert constant != other
                assert other != constant
                assert isnan(constant)
                assert isnan(other)
            elif name == "oo":
                assert isinf(constant)
                assert isinf(other)
                assert not isfinite(constant)
                assert not isfinite(other)
            elif constant == sympy.S("oo * I"):
                assert isinf_complex(constant)
                assert isinf_complex(other)
                assert not isfinite_complex(constant)
                assert not isfinite_complex(other)
            else:
                assert isnear(constant, other)


random.setstate(randomstate)
