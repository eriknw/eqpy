import sys
import types
import sympy
from eqpy._utils import isdunder


class DummiesModule(types.ModuleType):
    __call__ = staticmethod(sympy.Dummy)

    def __init__(self, self_module):
        super(DummiesModule, self).__init__(self_module.__name__)
        self.__path__ = []
        self._self_module_ = self_module
        for attr in ["__builtins__", "__doc__", "__file__", "__package__"]:
            setattr(self, attr, getattr(self_module, attr, None))

    def __getattr__(self, name):
        if isdunder(name):
            raise AttributeError
        return sympy.Dummy(name)


self = sys.modules[__name__]
sys.modules[__name__] = DummiesModule(self)
