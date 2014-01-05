import sympy
from ._apimappings import mathtosympy

locals().update((key, val) if callable(val) else (key, getattr(sympy, val))
                for key, val in mathtosympy.items())
del sympy
