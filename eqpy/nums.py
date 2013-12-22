import sys
import types
import sympy
from eqpy._utils import isdunder


constants = ['Catalan', 'E', 'EulerGamma', 'GoldenRatio', 'I', 'nan',
             'oo', 'pi', 'zoo']


class NumsModule(types.ModuleType):
    __call__ = staticmethod(sympy.sympify)

    def __init__(self, self_module):
        super(NumsModule, self).__init__(self_module.__name__)
        self.__dict__['__path__'] = []
        self.__dict__['_self_module_'] = self_module
        for attr in ['__builtins__', '__doc__', '__file__', '__package__']:
            self.__dict__[attr] = getattr(self_module, attr, None)
        for attr in constants:
            self.__dict__[attr] = getattr(sympy, attr)

    def __setattr__(self, name, val):
        if isdunder(name):
            self.__dict__[name] = val
        else:
            self.__dict__[name] = sympy.sympify(val)


self = sys.modules[__name__]
sys.modules[__name__] = NumsModule(self)
