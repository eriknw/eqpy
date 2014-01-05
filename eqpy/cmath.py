import sympy
from ._apimappings import cmathtosympy

locals().update((key, val) if callable(val) else (key, getattr(sympy, val))
                for key, val in cmathtosympy.items())
del sympy
