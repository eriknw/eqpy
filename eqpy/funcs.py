import sympy
import types

d = {}

# add Functions from top-level `sympy` module
for name, value in sympy.__dict__.items():
    if isinstance(value, sympy.FunctionClass):
        d[name] = value

# add more functions from `sympy.functions`
for name, value in sympy.functions.__dict__.items():
    if name in d:
        continue
    if isinstance(value, (sympy.FunctionClass, types.FunctionType)):
        d[name] = value

# add additional functions from `sympy`
for name in ['rad', 'deg']:
    d[name] = getattr(sympy, name)

del name
del sympy
del types
del value
locals().update(d)
del d
