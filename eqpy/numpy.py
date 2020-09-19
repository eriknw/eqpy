import sympy
from ._apimappings import numpytosympy

locals().update(
    (key, val) if callable(val) else (key, getattr(sympy, val)) for key, val in numpytosympy.items()
)
del sympy
