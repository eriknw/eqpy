import sympy
from ._apimappings import mathtosympy

locals().update(
    (key, val) if callable(val)
    else (key, getattr(sympy, val)) if isinstance(val, str) and hasattr(sympy, val)
    else (key, sympy.S(val))
    for key, val in mathtosympy.items()
)
del sympy
