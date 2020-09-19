import sympy
from ._apimappings import cmathtosympy

locals().update(
    (key, val)
    if callable(val)
    else (key, getattr(sympy, val))
    if isinstance(val, str) and hasattr(sympy, val)
    else (key, sympy.S(val))
    for key, val in cmathtosympy.items()
)
del sympy
